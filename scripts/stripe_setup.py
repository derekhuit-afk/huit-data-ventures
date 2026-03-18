#!/usr/bin/env python3
"""
Huit Data Ventures - Stripe Product Setup
Run: python3 stripe_setup.py sk_live_YOUR_KEY_HERE
Creates all 25 DaaS products + price IDs and inserts into Supabase
"""

import sys, subprocess, json

SUPABASE_URL = "https://vvkdnzqgtajeouxlliuk.supabase.co"
SUPABASE_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InZ2a2RuenFndGFqZW91eGxsaXVrIiwicm9sZSI6InNlcnZpY2Vfcm9sZSIsImlhdCI6MTc3MTAwOTE4NiwiZXhwIjoyMDg2NTg1MTg2fQ.Q61WGhT0KHUbrVc3FiRzQN-vhmy53dEqaad4w4c_Z9o"

PRODUCTS = [
    # Phase 1 — Revenue NOW
    {"slug": "lenderpulse",   "name": "LenderPulse",   "tagline": "Mortgage Lender Risk Intelligence Feed",    "price_cents": 350000, "phase": 1},
    {"slug": "flightrisk",    "name": "FlightRisk",    "tagline": "HR Attrition Signal Intelligence",          "price_cents": 400000, "phase": 1},
    {"slug": "zonescore",     "name": "ZoneScore",     "tagline": "Insurance Zip-Code Risk Scores",            "price_cents": 300000, "phase": 1},
    {"slug": "licensewatch",  "name": "LicenseWatch",  "tagline": "NMLS License Lapse & Reinstatement Monitor","price_cents": 250000, "phase": 1},
    {"slug": "exposureiq",    "name": "ExposureIQ",    "tagline": "Legal Exposure Intelligence — FinServ",     "price_cents": 450000, "phase": 1},
    # Phase 2
    {"slug": "origintrace",   "name": "OriginTrace",   "tagline": "CRE Loan Origination Trend Reports",       "price_cents": 250000, "phase": 2},
    {"slug": "fairlend",      "name": "FairLend",      "tagline": "HMDA Disparate Impact Dashboard",           "price_cents": 350000, "phase": 2},
    {"slug": "advisortrack",  "name": "AdvisorTrack",  "tagline": "Financial Advisor Movement Intelligence",   "price_cents": 400000, "phase": 2},
    {"slug": "leasesignal",   "name": "LeaseSignal",   "tagline": "Commercial Lease Expiration Intelligence",  "price_cents": 300000, "phase": 2},
    {"slug": "depositiq",     "name": "DepositIQ",     "tagline": "Regional Banking Deposit Concentration",    "price_cents": 350000, "phase": 2},
    {"slug": "caprateiq",     "name": "CapRateIQ",     "tagline": "CRE Cap Rate & Stress Test Data Feed",     "price_cents": 400000, "phase": 2},
    {"slug": "carriershift",  "name": "CarrierShift",  "tagline": "P&C Carrier Appetite Intelligence",         "price_cents": 300000, "phase": 2},
    {"slug": "esgflag",       "name": "ESGFlag",       "tagline": "ESG Compliance Exposure Feed — CRE",        "price_cents": 450000, "phase": 2},
    # Phase 3
    {"slug": "exodusmap",     "name": "ExodusMap",     "tagline": "Talent Exodus Map — Financial Services",    "price_cents": 400000, "phase": 3},
    {"slug": "claimbench",    "name": "ClaimBench",    "tagline": "Workers Comp Claim Frequency Heatmap",      "price_cents": 350000, "phase": 3},
    {"slug": "leasecomps",    "name": "LeaseComps",    "tagline": "Lease Comps Intelligence for Legal",        "price_cents": 500000, "phase": 3},
    {"slug": "servicerrisk",  "name": "ServicerRisk",  "tagline": "Mortgage Servicer Performance Intelligence","price_cents": 450000, "phase": 3},
    {"slug": "headcountiq",   "name": "HeadcountIQ",   "tagline": "Corporate Headcount Signal Feed",           "price_cents": 400000, "phase": 3},
    {"slug": "regaction",     "name": "RegAction",     "tagline": "Regulatory Action Monitor — Insurance",     "price_cents": 350000, "phase": 3},
    {"slug": "distressmap",   "name": "DistressMap",   "tagline": "CRE Distress Signal Feed",                  "price_cents": 500000, "phase": 3},
    # Phase 4
    {"slug": "auditready",    "name": "AuditReady",    "tagline": "Fair Lending Audit Prep Data Room",         "price_cents": 500000, "phase": 4},
    {"slug": "insuretarget",  "name": "InsureTarget",  "tagline": "Insurance M&A Target Identification Feed",  "price_cents": 500000, "phase": 4},
    {"slug": "contractbench", "name": "ContractBench", "tagline": "Employment Contract Benchmark Intelligence", "price_cents": 400000, "phase": 4},
    {"slug": "deedguard",     "name": "DeedGuard",     "tagline": "Title & Deed Fraud Intelligence Feed",      "price_cents": 450000, "phase": 4},
    {"slug": "compliancerisk","name": "ComplianceRisk","tagline": "Multi-State Employer Compliance Intelligence","price_cents": 450000, "phase": 4},
]

def stripe_request(method, endpoint, key, data=None):
    cmd = ["curl", "-s", "-X", method,
           f"https://api.stripe.com/v1/{endpoint}",
           "-u", f"{key}:"]
    if data:
        for k, v in data.items():
            cmd += ["-d", f"{k}={v}"]
    r = subprocess.run(cmd, capture_output=True, text=True)
    return json.loads(r.stdout)

def supabase_insert(table, data):
    body = json.dumps(data)
    r = subprocess.run([
        "curl", "-s", "-X", "POST",
        f"{SUPABASE_URL}/rest/v1/{table}",
        "-H", f"apikey: {SUPABASE_KEY}",
        "-H", f"Authorization: Bearer {SUPABASE_KEY}",
        "-H", "Content-Type: application/json",
        "-H", "Prefer: return=representation",
        "-d", body
    ], capture_output=True, text=True)
    return r.stdout

def run(stripe_key):
    print(f"\n🚀 Huit Data Ventures — Stripe Setup")
    print(f"   Creating 25 products × 2 prices (monthly + annual) = 50 price IDs\n")

    results = []
    
    for p in PRODUCTS:
        print(f"\n{'📦' if p['phase'] == 1 else '⏳'} [{p['phase']}] {p['name']} (${p['price_cents']//100}/mo)")
        
        # Create Stripe product
        product = stripe_request("POST", "products", stripe_key, {
            "name": f"{p['name']} — Huit Data Ventures",
            "description": p["tagline"],
            "metadata[slug]": p["slug"],
            "metadata[phase]": str(p["phase"]),
            "metadata[portfolio]": "huit-data-ventures",
        })
        
        if "id" not in product:
            print(f"  ❌ Product creation failed: {product.get('error', {}).get('message', 'unknown')}")
            continue
        
        prod_id = product["id"]
        print(f"  ✅ Product: {prod_id}")
        
        # Monthly price
        monthly = stripe_request("POST", "prices", stripe_key, {
            "product": prod_id,
            "unit_amount": str(p["price_cents"]),
            "currency": "usd",
            "recurring[interval]": "month",
            "nickname": f"{p['name']} Monthly",
            "metadata[slug]": p["slug"],
            "metadata[interval]": "month",
        })
        
        monthly_price_id = monthly.get("id", "ERROR")
        print(f"  ✅ Monthly: {monthly_price_id} (${p['price_cents']//100}/mo)")
        
        # Annual price (15% discount)
        annual_amount = int(p["price_cents"] * 12 * 0.85)
        annual = stripe_request("POST", "prices", stripe_key, {
            "product": prod_id,
            "unit_amount": str(annual_amount),
            "currency": "usd",
            "recurring[interval]": "year",
            "nickname": f"{p['name']} Annual (15% off)",
            "metadata[slug]": p["slug"],
            "metadata[interval]": "year",
        })
        
        annual_price_id = annual.get("id", "ERROR")
        print(f"  ✅ Annual:  {annual_price_id} (${annual_amount//100}/yr)")
        
        result = {
            "slug": p["slug"],
            "name": p["name"],
            "phase": p["phase"],
            "price_monthly_cents": p["price_cents"],
            "stripe_product_id": prod_id,
            "stripe_price_id_monthly": monthly_price_id,
            "stripe_price_id_annual": annual_price_id,
        }
        results.append(result)
        
        # Insert monthly price into Supabase stripe_prices table
        supabase_insert("stripe_prices", {
            "vertical": "daas",
            "tier": p["slug"].upper(),
            "interval": "month",
            "stripe_price_id": monthly_price_id,
            "stripe_product_id": prod_id,
            "amount_cents": p["price_cents"],
        })
        
        # Insert annual price
        supabase_insert("stripe_prices", {
            "vertical": "daas",
            "tier": p["slug"].upper(),
            "interval": "year",
            "stripe_price_id": annual_price_id,
            "stripe_product_id": prod_id,
            "amount_cents": annual_amount,
        })
        
        # Insert into stripe_products table
        supabase_insert("stripe_products", {
            "id": prod_id,
            "name": p["name"],
            "tier": "COMMAND",
            "vertical": "daas" if False else "mortgage",  # use mortgage as closest enum
            "description": p["tagline"],
            "active": True,
        })

    # Output summary
    print("\n" + "="*60)
    print("STRIPE SETUP COMPLETE")
    print("="*60)
    print("\nENV VARS FOR VERCEL (copy into each project):\n")
    
    phase1 = [r for r in results if r["phase"] == 1]
    for r in phase1:
        print(f"# {r['name']}")
        print(f"STRIPE_PRICE_ID={r['stripe_price_id_monthly']}")
        print(f"STRIPE_PRODUCT_ID={r['stripe_product_id']}")
        print()
    
    # Save full manifest
    with open("stripe_manifest.json", "w") as f:
        json.dump(results, f, indent=2)
    print("📄 Full manifest saved to stripe_manifest.json")
    
    return results

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python3 stripe_setup.py sk_live_YOUR_KEY_HERE")
        sys.exit(1)
    run(sys.argv[1])
