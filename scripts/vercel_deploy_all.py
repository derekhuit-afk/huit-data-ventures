#!/usr/bin/env python3
"""
╔══════════════════════════════════════════════════════════════════╗
║      HUIT DATA VENTURES — VERCEL MASS DEPLOYMENT SCRIPT         ║
║      Deploys all 26 products to Vercel via API                  ║
╚══════════════════════════════════════════════════════════════════╝

USAGE:
  python3 vercel_deploy_all.py YOUR_VERCEL_TOKEN

HOW TO GET YOUR VERCEL TOKEN:
  vercel.com → Account Settings → Tokens → Create Token

WHAT THIS DOES:
  1. Creates 26 Vercel projects linked to GitHub repos
  2. Sets environment variables for each project
  3. Triggers first deployment for each project
  4. Outputs the live URLs for all 26 products

REQUIREMENTS: Python 3.8+ · curl

RUN TIME: ~5–10 minutes
"""
import sys, subprocess, json, time

GITHUB_OWNER = "derekhuit-afk"
SUPABASE_URL = "https://vvkdnzqgtajeouxlliuk.supabase.co"
SUPABASE_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InZ2a2RuenFndGFqZW91eGxsaXVrIiwicm9sZSI6InNlcnZpY2Vfcm9sZSIsImlhdCI6MTc3MTAwOTE4NiwiZXhwIjoyMDg2NTg1MTg2fQ.Q61WGhT0KHUbrVc3FiRzQN-vhmy53dEqaad4w4c_Z9o"

PRODUCTS = [
    {"slug":"huit-data-ventures","name":"Huit Data Ventures","price":0,"subdomain":"data.huit.ai","phase":0},
    {"slug":"lenderpulse","name":"LenderPulse","price":350000,"subdomain":"lenderpulse.data.huit.ai","phase":1},
    {"slug":"flightrisk","name":"FlightRisk","price":400000,"subdomain":"flightrisk.data.huit.ai","phase":1},
    {"slug":"zonescore","name":"ZoneScore","price":300000,"subdomain":"zonescore.data.huit.ai","phase":1},
    {"slug":"licensewatch","name":"LicenseWatch","price":250000,"subdomain":"licensewatch.data.huit.ai","phase":1},
    {"slug":"exposureiq","name":"ExposureIQ","price":450000,"subdomain":"exposureiq.data.huit.ai","phase":1},
    {"slug":"origintrace","name":"OriginTrace","price":250000,"subdomain":"origintrace.data.huit.ai","phase":2},
    {"slug":"fairlend","name":"FairLend","price":350000,"subdomain":"fairlend.data.huit.ai","phase":2},
    {"slug":"advisortrack","name":"AdvisorTrack","price":400000,"subdomain":"advisortrack.data.huit.ai","phase":2},
    {"slug":"leasesignal","name":"LeaseSignal","price":300000,"subdomain":"leasesignal.data.huit.ai","phase":2},
    {"slug":"depositiq","name":"DepositIQ","price":350000,"subdomain":"depositiq.data.huit.ai","phase":2},
    {"slug":"caprateiq","name":"CapRateIQ","price":400000,"subdomain":"caprateiq.data.huit.ai","phase":2},
    {"slug":"carriershift","name":"CarrierShift","price":300000,"subdomain":"carriershift.data.huit.ai","phase":2},
    {"slug":"esgflag","name":"ESGFlag","price":450000,"subdomain":"esgflag.data.huit.ai","phase":2},
    {"slug":"exodusmap","name":"ExodusMap","price":400000,"subdomain":"exodusmap.data.huit.ai","phase":3},
    {"slug":"claimbench","name":"ClaimBench","price":350000,"subdomain":"claimbench.data.huit.ai","phase":3},
    {"slug":"leasecomps","name":"LeaseComps","price":500000,"subdomain":"leasecomps.data.huit.ai","phase":3},
    {"slug":"servicerrisk","name":"ServicerRisk","price":450000,"subdomain":"servicerrisk.data.huit.ai","phase":3},
    {"slug":"headcountiq","name":"HeadcountIQ","price":400000,"subdomain":"headcountiq.data.huit.ai","phase":3},
    {"slug":"regaction","name":"RegAction","price":350000,"subdomain":"regaction.data.huit.ai","phase":3},
    {"slug":"distressmap","name":"DistressMap","price":500000,"subdomain":"distressmap.data.huit.ai","phase":3},
    {"slug":"auditready","name":"AuditReady","price":500000,"subdomain":"auditready.data.huit.ai","phase":4},
    {"slug":"insuretarget","name":"InsureTarget","price":500000,"subdomain":"insuretarget.data.huit.ai","phase":4},
    {"slug":"contractbench","name":"ContractBench","price":400000,"subdomain":"contractbench.data.huit.ai","phase":4},
    {"slug":"deedguard","name":"DeedGuard","price":450000,"subdomain":"deedguard.data.huit.ai","phase":4},
    {"slug":"compliancerisk","name":"ComplianceRisk","price":450000,"subdomain":"compliancerisk.data.huit.ai","phase":4},
]

def vercel(method, endpoint, token, data=None):
    cmd = ["curl", "-s", "-X", method,
           f"https://api.vercel.com{endpoint}",
           "-H", f"Authorization: Bearer {token}",
           "-H", "Content-Type: application/json"]
    if data:
        cmd += ["-d", json.dumps(data)]
    r = subprocess.run(cmd, capture_output=True, text=True, timeout=30)
    try:
        return json.loads(r.stdout)
    except:
        return {"error": r.stdout}

def run(token):
    print("\n╔══════════════════════════════════════════════════════════╗")
    print("║      HUIT DATA VENTURES — VERCEL DEPLOYMENT             ║")
    print("╚══════════════════════════════════════════════════════════╝")

    # Validate token
    user = vercel("GET", "/v2/user", token)
    if "error" in user and user.get("error", {}).get("code") == "forbidden":
        print("\n❌ Invalid Vercel token. Get one at: vercel.com/account/tokens")
        sys.exit(1)
    print(f"\n✅ Vercel token valid — Account: {user.get('user', {}).get('username', 'unknown')}")

    # Get team ID
    teams = vercel("GET", "/v2/teams", token)
    team_id = None
    if teams.get("teams"):
        # Try to find the derekhuit-afk team
        for team in teams["teams"]:
            if "huit" in team.get("slug", "").lower() or "derek" in team.get("slug", "").lower():
                team_id = team["id"]
                print(f"✅ Team found: {team.get('slug')} ({team_id})")
                break
        if not team_id:
            team_id = teams["teams"][0]["id"]
            print(f"✅ Using team: {teams['teams'][0].get('slug')} ({team_id})")

    results = []
    errors = []

    for i, p in enumerate(PRODUCTS, 1):
        phase_icon = "🏛️" if p["phase"]==0 else "🟢" if p["phase"]==1 else "🟠" if p["phase"]==2 else "🟡" if p["phase"]==3 else "🟣"
        print(f"\n── [{i:02d}/26] {phase_icon} {p['name']} ({p['slug']}) ──────────────────────")

        # ── 1. Create Vercel project ──────────────────────────────
        project_data = {
            "name": p["slug"],
            "framework": "nextjs",
            "gitRepository": {
                "type": "github",
                "repo": f"{GITHUB_OWNER}/{p['slug']}",
            },
            "buildCommand": "next build",
            "outputDirectory": ".next",
            "installCommand": "npm install",
        }
        if team_id:
            project_resp = vercel("POST", f"/v10/projects?teamId={team_id}", token, project_data)
        else:
            project_resp = vercel("POST", "/v10/projects", token, project_data)

        if "error" in project_resp and project_resp.get("error", {}).get("code") != "PROJECT_ALREADY_EXISTS":
            err = project_resp.get("error", {}).get("message", str(project_resp))
            print(f"  ❌ Project creation failed: {err}")
            errors.append({"slug": p["slug"], "error": err})
            continue

        project_id = project_resp.get("id") or project_resp.get("project", {}).get("id")
        if not project_id:
            # Project already exists - get it
            if team_id:
                existing = vercel("GET", f"/v10/projects/{p['slug']}?teamId={team_id}", token)
            else:
                existing = vercel("GET", f"/v10/projects/{p['slug']}", token)
            project_id = existing.get("id")
            print(f"  ⚠️  Project exists — using: {project_id}")
        else:
            print(f"  ✅ Project created: {project_id}")

        # ── 2. Set environment variables ──────────────────────────
        env_vars = [
            {"key": "NEXT_PUBLIC_SUPABASE_URL", "value": SUPABASE_URL, "type": "plain", "target": ["production","preview"]},
            {"key": "SUPABASE_SERVICE_ROLE_KEY", "value": SUPABASE_KEY, "type": "encrypted", "target": ["production"]},
            {"key": "NEXT_PUBLIC_PRODUCT_SLUG", "value": p["slug"], "type": "plain", "target": ["production","preview"]},
            {"key": "NEXT_PUBLIC_PRODUCT_NAME", "value": p["name"], "type": "plain", "target": ["production","preview"]},
            {"key": "NEXT_PUBLIC_SUBDOMAIN", "value": p["subdomain"], "type": "plain", "target": ["production","preview"]},
            {"key": "NEXT_PUBLIC_PRICE_CENTS", "value": str(p["price"]), "type": "plain", "target": ["production","preview"]},
            {"key": "JWT_SECRET", "value": f"huit-data-ventures-{p['slug']}-jwt-secret-2026-production-key", "type": "encrypted", "target": ["production"]},
        ]

        env_endpoint = f"/v10/projects/{project_id}/env" + (f"?teamId={team_id}" if team_id else "")
        env_resp = vercel("POST", env_endpoint, token, env_vars)
        env_ok = not ("error" in env_resp and "code" in env_resp.get("error", {}))
        print(f"  {'✅' if env_ok else '⚠️'} Env vars set ({len(env_vars)} variables)")

        # ── 3. Add custom domain ──────────────────────────────────
        if p["phase"] > 0:  # skip for parent hub (different domain)
            domain_data = {"name": p["subdomain"]}
            domain_endpoint = f"/v10/projects/{project_id}/domains" + (f"?teamId={team_id}" if team_id else "")
            domain_resp = vercel("POST", domain_endpoint, token, domain_data)
            domain_ok = "name" in domain_resp or domain_resp.get("error", {}).get("code") == "DOMAIN_ALREADY_EXISTS"
            print(f"  {'✅' if domain_ok else '⚠️'} Domain: {p['subdomain']}")

        # ── 4. Trigger deployment ─────────────────────────────────
        deploy_data = {
            "name": p["slug"],
            "gitSource": {
                "type": "github",
                "repoId": f"{GITHUB_OWNER}/{p['slug']}",
                "ref": "main",
            },
            "target": "production",
        }
        deploy_endpoint = "/v13/deployments" + (f"?teamId={team_id}" if team_id else "")
        deploy_resp = vercel("POST", deploy_endpoint, token, deploy_data)
        deploy_url = deploy_resp.get("url", "")
        deploy_id = deploy_resp.get("id", "")
        if deploy_url:
            print(f"  ✅ Deployment triggered: https://{deploy_url}")
        else:
            print(f"  ⚠️  Deployment: {deploy_resp.get('error', {}).get('message', 'check Vercel dashboard')}")

        results.append({
            "slug": p["slug"],
            "name": p["name"],
            "phase": p["phase"],
            "project_id": project_id,
            "subdomain": p["subdomain"],
            "vercel_url": f"https://{deploy_url}" if deploy_url else f"https://{p['slug']}.vercel.app",
            "custom_url": f"https://{p['subdomain']}",
        })

        # Brief pause to avoid rate limiting
        time.sleep(0.5)

    # ── Output summary ────────────────────────────────────────────
    print("\n" + "═"*62)
    print("  DEPLOYMENT SUMMARY")
    print("═"*62)
    print(f"  ✅ Projects deployed: {len(results)}")
    print(f"  ❌ Errors:            {len(errors)}")
    print()
    print("── LIVE URLS ────────────────────────────────────────────────")
    for r in results:
        phase = f"[P{r['phase']}]" if r['phase'] > 0 else "[HUB]"
        print(f"  {phase} {r['name']:<18} {r['custom_url']}")

    print()
    print("── REMAINING MANUAL STEPS ───────────────────────────────────")
    print("  1. DNS: Add *.data.huit.ai CNAME → cname.vercel-dns.com")
    print("     (One record covers all 25 subdomains)")
    print()
    print("  2. Stripe: Run scripts/huit_stripe_setup.py to get price IDs")
    print("     Then add to each Vercel project:")
    print("     STRIPE_SECRET_KEY, STRIPE_PRICE_ID, STRIPE_WEBHOOK_SECRET")
    print("     NEXT_PUBLIC_STRIPE_PUBLISHABLE_KEY")
    print()
    print("  3. Stripe Webhooks: Register per product at stripe.com/webhooks")
    print("     Endpoint: https://[product].data.huit.ai/api/stripe/webhook")
    print("     Events: checkout.session.completed, customer.subscription.*")
    print()
    print("  4. Resend: Add RESEND_API_KEY to each Vercel project")
    print("     Get key at resend.com — welcome emails are pre-wired")
    print()

    # Save manifest
    manifest = {"deployed_at": __import__('datetime').datetime.now().isoformat(), "products": results, "errors": errors}
    with open("vercel_manifest.json", "w") as f:
        json.dump(manifest, f, indent=2)
    print("  📄 Full manifest → vercel_manifest.json")

    if errors:
        print("\n── ERRORS ──────────────────────────────────────────────────")
        for e in errors:
            print(f"  ❌ {e['slug']}: {e['error']}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print(__doc__)
        print("Usage: python3 vercel_deploy_all.py YOUR_VERCEL_TOKEN")
        sys.exit(1)
    run(sys.argv[1])
