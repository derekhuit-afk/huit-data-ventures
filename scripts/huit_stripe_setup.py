#!/usr/bin/env python3
"""
╔══════════════════════════════════════════════════════════════════╗
║          HUIT DATA VENTURES — STRIPE SETUP SCRIPT               ║
║          Creates all 25 DaaS products + 50 price IDs            ║
║          Inserts everything into Supabase stripe_prices table    ║
╚══════════════════════════════════════════════════════════════════╝

USAGE:
  python3 huit_stripe_setup.py sk_live_YOUR_KEY_HERE

WHAT THIS DOES:
  1. Creates 25 Stripe Products (one per DaaS company)
  2. Creates 50 Price IDs (monthly + annual 15% discount per product)
  3. Inserts all price IDs into Supabase stripe_prices table
  4. Outputs a stripe_manifest.json with everything
  5. Prints copy-paste ENV VARS for all Vercel deployments

REQUIREMENTS:
  - Python 3.8+
  - curl (already on your system)
  - Your Stripe secret key (sk_live_... or sk_test_... for testing)

RUN TIME: ~2-3 minutes
"""

import sys
import subprocess
import json
import os
from datetime import datetime

# ── Supabase Config ──────────────────────────────────────────────
SUPABASE_URL = "https://vvkdnzqgtajeouxlliuk.supabase.co"
SUPABASE_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InZ2a2RuenFndGFqZW91eGxsaXVrIiwicm9sZSI6InNlcnZpY2Vfcm9sZSIsImlhdCI6MTc3MTAwOTE4NiwiZXhwIjoyMDg2NTg1MTg2fQ.Q61WGhT0KHUbrVc3FiRzQN-vhmy53dEqaad4w4c_Z9o"

# ── All 25 DaaS Products ─────────────────────────────────────────
PRODUCTS = [
    # ── PHASE 1 — Build + Revenue NOW (Days 15–25) ──────────────
    {
        "slug":        "lenderpulse",
        "name":        "LenderPulse",
        "tagline":     "Mortgage Lender Risk Intelligence Feed",
        "description": "7 years of HMDA data transformed into lender performance scores — denial rates, approval trends, and LTV risk by geography.",
        "price_cents": 350000,   # $3,500/mo
        "phase":       1,
        "industry":    "Insurance & Underwriting",
        "subdomain":   "lenderpulse.data.huit.ai",
        "repo":        "lenderpulse",
    },
    {
        "slug":        "flightrisk",
        "name":        "FlightRisk",
        "tagline":     "HR Attrition Signal Intelligence",
        "description": "Real-time departure signals for financial services professionals. Powered by APEX TLS Engine with 86% predictive accuracy.",
        "price_cents": 400000,   # $4,000/mo
        "phase":       1,
        "industry":    "HR & Workforce Intelligence",
        "subdomain":   "flightrisk.data.huit.ai",
        "repo":        "flightrisk",
    },
    {
        "slug":        "zonescore",
        "name":        "ZoneScore",
        "tagline":     "Insurance Zip-Code Risk Scores",
        "description": "Neighborhood-level underwriting risk scores derived from HMDA denial concentration and census overlays.",
        "price_cents": 300000,   # $3,000/mo
        "phase":       1,
        "industry":    "Insurance & Underwriting",
        "subdomain":   "zonescore.data.huit.ai",
        "repo":        "zonescore",
    },
    {
        "slug":        "licensewatch",
        "name":        "LicenseWatch",
        "tagline":     "NMLS License Lapse & Reinstatement Monitor",
        "description": "Real-time alerts when loan officers lose, suspend, or reinstate NMLS licenses across all 50 states.",
        "price_cents": 250000,   # $2,500/mo
        "phase":       1,
        "industry":    "Legal & Compliance",
        "subdomain":   "licensewatch.data.huit.ai",
        "repo":        "licensewatch",
    },
    {
        "slug":        "exposureiq",
        "name":        "ExposureIQ",
        "tagline":     "Legal Exposure Intelligence — Financial Services",
        "description": "Monthly enforcement action reports, CFPB patterns, and regulatory exposure scores for compliance and legal teams.",
        "price_cents": 450000,   # $4,500/mo
        "phase":       1,
        "industry":    "Legal & Compliance",
        "subdomain":   "exposureiq.data.huit.ai",
        "repo":        "exposureiq",
    },

    # ── PHASE 2 — Deploy Days 30–45 ─────────────────────────────
    {
        "slug":        "origintrace",
        "name":        "OriginTrace",
        "tagline":     "CRE Loan Origination Trend Reports",
        "description": "HMDA commercial origination records and census tract overlays — who's lending, where, at what LTV.",
        "price_cents": 250000,
        "phase":       2,
        "industry":    "Commercial Real Estate",
        "subdomain":   "origintrace.data.huit.ai",
        "repo":        "origintrace",
    },
    {
        "slug":        "fairlend",
        "name":        "FairLend",
        "tagline":     "HMDA Disparate Impact Dashboard",
        "description": "Compliance dashboard showing denial rate disparities by race and income — built for CRA and fair lending exam prep.",
        "price_cents": 350000,
        "phase":       2,
        "industry":    "Legal & Compliance",
        "subdomain":   "fairlend.data.huit.ai",
        "repo":        "fairlend",
    },
    {
        "slug":        "advisortrack",
        "name":        "AdvisorTrack",
        "tagline":     "Financial Advisor Movement Intelligence",
        "description": "FINRA BrokerCheck API-powered feed flagging advisor departures, new registrations, and firm-level headcount shifts.",
        "price_cents": 400000,
        "phase":       2,
        "industry":    "HR & Workforce Intelligence",
        "subdomain":   "advisortrack.data.huit.ai",
        "repo":        "advisortrack",
    },
    {
        "slug":        "leasesignal",
        "name":        "LeaseSignal",
        "tagline":     "Commercial Lease Expiration Intelligence",
        "description": "Monthly feed of upcoming CRE lease expirations by market — tenant, square footage, and expiration date.",
        "price_cents": 300000,
        "phase":       2,
        "industry":    "Commercial Real Estate",
        "subdomain":   "leasesignal.data.huit.ai",
        "repo":        "leasesignal",
    },
    {
        "slug":        "depositiq",
        "name":        "DepositIQ",
        "tagline":     "Regional Banking Deposit Concentration Feed",
        "description": "Parsed deposit concentration and loan-to-deposit ratio trends by bank and geography from FDIC Call Reports.",
        "price_cents": 350000,
        "phase":       2,
        "industry":    "Insurance & Underwriting",
        "subdomain":   "depositiq.data.huit.ai",
        "repo":        "depositiq",
    },
    {
        "slug":        "caprateiq",
        "name":        "CapRateIQ",
        "tagline":     "CRE Cap Rate & Stress Test Data Feed",
        "description": "Monthly cap rate benchmarks by asset class and MSA with stress test modeling at 50/100/200bps rate shifts.",
        "price_cents": 400000,
        "phase":       2,
        "industry":    "Commercial Real Estate",
        "subdomain":   "caprateiq.data.huit.ai",
        "repo":        "caprateiq",
    },
    {
        "slug":        "carriershift",
        "name":        "CarrierShift",
        "tagline":     "P&C Carrier Appetite Intelligence",
        "description": "Monthly carrier appetite shifts by state and line — which carriers are pulling back, expanding, or re-rating.",
        "price_cents": 300000,
        "phase":       2,
        "industry":    "Insurance & Underwriting",
        "subdomain":   "carriershift.data.huit.ai",
        "repo":        "carriershift",
    },
    {
        "slug":        "esgflag",
        "name":        "ESGFlag",
        "tagline":     "ESG Compliance Exposure Feed — Real Estate",
        "description": "Monthly portfolio-level ESG risk flags for CRE owners and lenders from EPA, HUD, and climate disclosure sources.",
        "price_cents": 450000,
        "phase":       2,
        "industry":    "Legal & Compliance",
        "subdomain":   "esgflag.data.huit.ai",
        "repo":        "esgflag",
    },

    # ── PHASE 3 — Deploy Days 45–60 ─────────────────────────────
    {
        "slug":        "exodusmap",
        "name":        "ExodusMap",
        "tagline":     "Talent Exodus Map — Financial Services by Firm",
        "description": "Quarterly exodus index showing which firms are losing top producers and where they are going.",
        "price_cents": 400000,
        "phase":       3,
        "industry":    "HR & Workforce Intelligence",
        "subdomain":   "exodusmap.data.huit.ai",
        "repo":        "exodusmap",
    },
    {
        "slug":        "claimbench",
        "name":        "ClaimBench",
        "tagline":     "Workers Comp Claim Frequency Heatmap",
        "description": "Claim frequency and loss ratio benchmarks by NAICS code and state from NCCI, BLS, and OSHA data.",
        "price_cents": 350000,
        "phase":       3,
        "industry":    "Insurance & Underwriting",
        "subdomain":   "claimbench.data.huit.ai",
        "repo":        "claimbench",
    },
    {
        "slug":        "leasecomps",
        "name":        "LeaseComps",
        "tagline":     "Lease Comps Intelligence for Legal Discovery",
        "description": "Comparable lease data packaged for litigation support — expert witness prep and landlord/tenant disputes.",
        "price_cents": 500000,
        "phase":       3,
        "industry":    "Legal & Compliance",
        "subdomain":   "leasecomps.data.huit.ai",
        "repo":        "leasecomps",
    },
    {
        "slug":        "servicerrisk",
        "name":        "ServicerRisk",
        "tagline":     "Mortgage Servicer Performance Intelligence",
        "description": "Servicer risk scores from CFPB complaint data, HMDA servicing transfers, and Ginnie/Fannie servicer reports.",
        "price_cents": 450000,
        "phase":       3,
        "industry":    "Insurance & Underwriting",
        "subdomain":   "servicerrisk.data.huit.ai",
        "repo":        "servicerrisk",
    },
    {
        "slug":        "headcountiq",
        "name":        "HeadcountIQ",
        "tagline":     "Corporate Headcount Signal Feed",
        "description": "Monthly headcount velocity by company from SEC 10-K/10-Q filings and layoff tracking sources.",
        "price_cents": 400000,
        "phase":       3,
        "industry":    "HR & Workforce Intelligence",
        "subdomain":   "headcountiq.data.huit.ai",
        "repo":        "headcountiq",
    },
    {
        "slug":        "regaction",
        "name":        "RegAction",
        "tagline":     "Regulatory Action Monitor — State Insurance Depts",
        "description": "Unified regulatory action feed from all 50 state DOIs — cease and desist, license suspensions, market conduct exams.",
        "price_cents": 350000,
        "phase":       3,
        "industry":    "Insurance & Underwriting",
        "subdomain":   "regaction.data.huit.ai",
        "repo":        "regaction",
    },
    {
        "slug":        "distressmap",
        "name":        "DistressMap",
        "tagline":     "CRE Distress Signal Feed",
        "description": "Weekly distressed property and loan signals by market from CMBS watchlists, NOD filings, and FDIC problem loans.",
        "price_cents": 500000,
        "phase":       3,
        "industry":    "Commercial Real Estate",
        "subdomain":   "distressmap.data.huit.ai",
        "repo":        "distressmap",
    },

    # ── PHASE 4 — Deploy Day 60 ──────────────────────────────────
    {
        "slug":        "auditready",
        "name":        "AuditReady",
        "tagline":     "Fair Lending Audit Prep Data Room",
        "description": "Pre-packaged audit-ready data room with peer comparisons, disparity analysis, and remediation documentation.",
        "price_cents": 500000,
        "phase":       4,
        "industry":    "Legal & Compliance",
        "subdomain":   "auditready.data.huit.ai",
        "repo":        "auditready",
    },
    {
        "slug":        "insuretarget",
        "name":        "InsureTarget",
        "tagline":     "Insurance M&A Target Identification Feed",
        "description": "Scored acquisition targets — carriers, MGAs, and agencies scored by financial health and market position.",
        "price_cents": 500000,
        "phase":       4,
        "industry":    "Insurance & Underwriting",
        "subdomain":   "insuretarget.data.huit.ai",
        "repo":        "insuretarget",
    },
    {
        "slug":        "contractbench",
        "name":        "ContractBench",
        "tagline":     "Employment Contract Benchmark Intelligence",
        "description": "Compensation and contract benchmark data for financial services roles from NLRB, SEC, and union contract filings.",
        "price_cents": 400000,
        "phase":       4,
        "industry":    "HR & Workforce Intelligence",
        "subdomain":   "contractbench.data.huit.ai",
        "repo":        "contractbench",
    },
    {
        "slug":        "deedguard",
        "name":        "DeedGuard",
        "tagline":     "Title & Deed Fraud Intelligence Feed",
        "description": "Fraud signal scores by geography from county recorder data, FinCEN GTO reports, and wire fraud complaint patterns.",
        "price_cents": 450000,
        "phase":       4,
        "industry":    "Insurance & Underwriting",
        "subdomain":   "deedguard.data.huit.ai",
        "repo":        "deedguard",
    },
    {
        "slug":        "compliancerisk",
        "name":        "ComplianceRisk",
        "tagline":     "Multi-State Employer Compliance Intelligence",
        "description": "Employer compliance risk scores from DOL wage/hour enforcement, EEOC filings, OSHA violations, and state AG actions.",
        "price_cents": 450000,
        "phase":       4,
        "industry":    "HR & Workforce Intelligence",
        "subdomain":   "compliancerisk.data.huit.ai",
        "repo":        "compliancerisk",
    },
]


# ── Helpers ──────────────────────────────────────────────────────

def stripe(method, endpoint, key, params=None):
    """Make a Stripe API request via curl."""
    cmd = ["curl", "-s", "-X", method,
           f"https://api.stripe.com/v1/{endpoint}",
           "-u", f"{key}:"]
    if params:
        for k, v in params.items():
            cmd += ["-d", f"{k}={v}"]
    r = subprocess.run(cmd, capture_output=True, text=True, timeout=30)
    return json.loads(r.stdout)


def supabase_upsert(table, data):
    """Insert a row into Supabase (ignore conflicts)."""
    body = json.dumps(data)
    r = subprocess.run([
        "curl", "-s", "-X", "POST",
        f"{SUPABASE_URL}/rest/v1/{table}",
        "-H", f"apikey: {SUPABASE_KEY}",
        "-H", f"Authorization: Bearer {SUPABASE_KEY}",
        "-H", "Content-Type: application/json",
        "-H", "Prefer: resolution=merge-duplicates",
        "-d", body
    ], capture_output=True, text=True, timeout=15)
    return r.stdout


def validate_key(key):
    """Confirm the Stripe key is valid before running."""
    result = stripe("GET", "account", key)
    if "id" in result:
        mode = "LIVE" if key.startswith("sk_live") else "TEST"
        print(f"  ✅ Stripe key valid — Account: {result.get('display_name', result['id'])} [{mode} MODE]")
        return True
    else:
        print(f"  ❌ Invalid Stripe key: {result.get('error', {}).get('message', 'unknown error')}")
        return False


def annual_price(monthly_cents):
    """Annual price = 12 months × 85% (15% discount)."""
    return int(monthly_cents * 12 * 0.85)


# ── Main ─────────────────────────────────────────────────────────

def run(stripe_key):
    print()
    print("╔══════════════════════════════════════════════════════════╗")
    print("║       HUIT DATA VENTURES — STRIPE PRODUCT SETUP         ║")
    print("╚══════════════════════════════════════════════════════════╝")
    print(f"  Started: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"  Products: {len(PRODUCTS)}")
    print(f"  Price IDs: {len(PRODUCTS) * 2} (monthly + annual per product)")
    print()

    # Validate key
    print("── Validating Stripe key ───────────────────────────────────")
    if not validate_key(stripe_key):
        sys.exit(1)
    print()

    results      = []
    errors       = []
    phase1_envs  = {}

    for i, p in enumerate(PRODUCTS, 1):
        phase_icon = "🟢" if p["phase"] == 1 else "🟠" if p["phase"] == 2 else "🟡" if p["phase"] == 3 else "🟣"
        print(f"── [{i:02d}/25] {phase_icon} {p['name']} · ${p['price_cents']//100:,}/mo · Phase {p['phase']} ──")

        # ── 1. Create Stripe Product ─────────────────────────────
        product_resp = stripe("POST", "products", stripe_key, {
            "name":                       f"{p['name']} — Huit Data Ventures",
            "description":                p["description"],
            "metadata[slug]":             p["slug"],
            "metadata[phase]":            str(p["phase"]),
            "metadata[industry]":         p["industry"],
            "metadata[subdomain]":        p["subdomain"],
            "metadata[portfolio]":        "huit-data-ventures",
            "metadata[repo]":             p["repo"],
        })

        if "id" not in product_resp:
            err = product_resp.get("error", {}).get("message", "unknown")
            print(f"  ❌ Product failed: {err}")
            errors.append({"slug": p["slug"], "step": "product", "error": err})
            continue

        prod_id = product_resp["id"]
        print(f"  ✅ Product:  {prod_id}")

        # ── 2. Monthly Price ────────────────────────────────────
        monthly_resp = stripe("POST", "prices", stripe_key, {
            "product":                    prod_id,
            "unit_amount":                str(p["price_cents"]),
            "currency":                   "usd",
            "recurring[interval]":        "month",
            "nickname":                   f"{p['name']} — Monthly",
            "metadata[slug]":             p["slug"],
            "metadata[interval]":         "month",
            "metadata[portfolio]":        "huit-data-ventures",
        })

        if "id" not in monthly_resp:
            err = monthly_resp.get("error", {}).get("message", "unknown")
            print(f"  ❌ Monthly price failed: {err}")
            errors.append({"slug": p["slug"], "step": "monthly_price", "error": err})
            continue

        monthly_id  = monthly_resp["id"]
        monthly_amt = p["price_cents"]
        print(f"  ✅ Monthly:  {monthly_id}  (${monthly_amt//100:,}/mo)")

        # ── 3. Annual Price (15% off) ───────────────────────────
        annual_amt  = annual_price(p["price_cents"])
        annual_resp = stripe("POST", "prices", stripe_key, {
            "product":                    prod_id,
            "unit_amount":                str(annual_amt),
            "currency":                   "usd",
            "recurring[interval]":        "year",
            "nickname":                   f"{p['name']} — Annual (15% off)",
            "metadata[slug]":             p["slug"],
            "metadata[interval]":         "year",
            "metadata[portfolio]":        "huit-data-ventures",
            "metadata[discount]":         "15pct",
        })

        if "id" not in annual_resp:
            err = annual_resp.get("error", {}).get("message", "unknown")
            print(f"  ❌ Annual price failed: {err}")
            errors.append({"slug": p["slug"], "step": "annual_price", "error": err})
            annual_id = "ERROR"
        else:
            annual_id = annual_resp["id"]
            print(f"  ✅ Annual:   {annual_id}  (${annual_amt//100:,}/yr — 15% off)")

        # ── 4. Insert into Supabase stripe_prices ───────────────
        supabase_upsert("stripe_prices", {
            "vertical":        "daas",
            "tier":            p["slug"],
            "interval":        "month",
            "stripe_price_id": monthly_id,
            "stripe_product_id": prod_id,
            "amount_cents":    monthly_amt,
        })
        supabase_upsert("stripe_prices", {
            "vertical":        "daas",
            "tier":            p["slug"],
            "interval":        "year",
            "stripe_price_id": annual_id,
            "stripe_product_id": prod_id,
            "amount_cents":    annual_amt,
        })
        print(f"  ✅ Supabase: stripe_prices updated")

        # ── 5. Store result ─────────────────────────────────────
        result = {
            "slug":                   p["slug"],
            "name":                   p["name"],
            "phase":                  p["phase"],
            "industry":               p["industry"],
            "subdomain":              p["subdomain"],
            "repo":                   p["repo"],
            "price_monthly_cents":    monthly_amt,
            "price_annual_cents":     annual_amt,
            "stripe_product_id":      prod_id,
            "stripe_price_id_monthly": monthly_id,
            "stripe_price_id_annual": annual_id,
            "vercel_env_vars": {
                "STRIPE_PRICE_ID":         monthly_id,
                "STRIPE_PRICE_ID_ANNUAL":  annual_id,
                "NEXT_PUBLIC_PRODUCT_SLUG": p["slug"],
                "NEXT_PUBLIC_PRODUCT_NAME": p["name"],
                "NEXT_PUBLIC_SUBDOMAIN":   p["subdomain"],
                "NEXT_PUBLIC_PRICE_CENTS": str(monthly_amt),
            }
        }
        results.append(result)

        if p["phase"] == 1:
            phase1_envs[p["slug"]] = result

        print()

    # ── Output ───────────────────────────────────────────────────
    print("═" * 62)
    print("  STRIPE SETUP COMPLETE")
    print("═" * 62)
    print(f"  ✅ Products created:   {len(results)}")
    print(f"  ✅ Price IDs created:  {len(results) * 2}")
    print(f"  ❌ Errors:             {len(errors)}")
    print()

    # Print Phase 1 Vercel env vars
    print("── PHASE 1 — VERCEL ENVIRONMENT VARIABLES ──────────────────")
    print("   Copy these into each project's Vercel → Settings → Env Vars")
    print()
    for slug, r in phase1_envs.items():
        print(f"  ┌─ {r['name']} ({r['subdomain']}) ─{'─'*max(0, 40-len(r['name']))}┐")
        for k, v in r["vercel_env_vars"].items():
            print(f"  │  {k}={v}")
        print(f"  └{'─'*58}┘")
        print()

    # Also print the shared vars needed for ALL projects
    print("── SHARED ENV VARS (same for all 25 projects) ──────────────")
    print("  NEXT_PUBLIC_SUPABASE_URL=https://vvkdnzqgtajeouxlliuk.supabase.co")
    print("  SUPABASE_SERVICE_ROLE_KEY=<your_supabase_service_role_key>")
    print("  STRIPE_SECRET_KEY=<your_stripe_secret_key>")
    print("  STRIPE_WEBHOOK_SECRET=<from_stripe_dashboard_webhooks>")
    print("  NEXT_PUBLIC_STRIPE_PUBLISHABLE_KEY=<pk_live_or_pk_test_...>")
    print("  JWT_SECRET=<random_32+_char_string>")
    print()

    # Revenue summary
    total_mrr   = sum(r["price_monthly_cents"] for r in results) / 100
    phase1_mrr  = sum(r["price_monthly_cents"] for r in results if r["phase"] == 1) / 100
    print("── REVENUE SUMMARY ─────────────────────────────────────────")
    print(f"  Phase 1 MRR potential:  ${phase1_mrr:,.0f}/mo (5 products × 1 subscriber)")
    print(f"  Full portfolio MRR:     ${total_mrr:,.0f}/mo (25 products × 1 subscriber)")
    print(f"  Full portfolio ARR:     ${total_mrr*12:,.0f}/yr")
    print()

    # Save manifest
    manifest = {
        "generated_at":   datetime.now().isoformat(),
        "total_products": len(results),
        "total_price_ids": len(results) * 2,
        "errors":         errors,
        "products":       results,
    }
    manifest_path = os.path.join(os.path.dirname(__file__), "stripe_manifest.json")
    with open(manifest_path, "w") as f:
        json.dump(manifest, f, indent=2)
    print(f"  📄 Full manifest saved → stripe_manifest.json")
    print(f"     Contains all product IDs, price IDs, and env vars")
    print()
    print("  🔗 Next step: Vercel → New Project → Import each GitHub repo")
    print("     Repos: github.com/derekhuit-afk/[product-slug]")
    print()

    if errors:
        print("── ERRORS ──────────────────────────────────────────────────")
        for e in errors:
            print(f"  ❌ {e['slug']} / {e['step']}: {e['error']}")
        print()

    return results


# ── Entry Point ──────────────────────────────────────────────────
if __name__ == "__main__":
    if len(sys.argv) < 2:
        print(__doc__)
        print("ERROR: No Stripe key provided.")
        print("Usage: python3 huit_stripe_setup.py sk_live_YOUR_KEY_HERE")
        sys.exit(1)

    key = sys.argv[1].strip()
    if not (key.startswith("sk_live_") or key.startswith("sk_test_")):
        print(f"ERROR: Key must start with sk_live_ or sk_test_")
        print(f"       Got: {key[:12]}...")
        sys.exit(1)

    run(key)
