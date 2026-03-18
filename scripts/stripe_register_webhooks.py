#!/usr/bin/env python3
"""
HUIT DATA VENTURES — Stripe Webhook Registration
Registers a webhook endpoint for all 25 products simultaneously.

USAGE: python3 stripe_register_webhooks.py sk_live_YOUR_KEY

Creates one webhook per product listening for:
  - checkout.session.completed
  - customer.subscription.created/updated/deleted
  - invoice.payment_succeeded/failed
"""
import sys, subprocess, json

PRODUCTS = [
    "lenderpulse","flightrisk","zonescore","licensewatch","exposureiq",
    "origintrace","fairlend","advisortrack","leasesignal","depositiq",
    "caprateiq","carriershift","esgflag","exodusmap","claimbench",
    "leasecomps","servicerrisk","headcountiq","regaction","distressmap",
    "auditready","insuretarget","contractbench","deedguard","compliancerisk"
]

EVENTS = [
    "checkout.session.completed",
    "customer.subscription.created",
    "customer.subscription.updated",
    "customer.subscription.deleted",
    "invoice.payment_succeeded",
    "invoice.payment_failed",
]

def stripe(method, endpoint, key, params=None):
    cmd = ["curl", "-s", "-X", method,
           f"https://api.stripe.com/v1/{endpoint}",
           "-u", f"{key}:"]
    if params:
        for k, v in params.items():
            if isinstance(v, list):
                for item in v:
                    cmd += ["-d", f"{k}[]={item}"]
            else:
                cmd += ["-d", f"{k}={v}"]
    r = subprocess.run(cmd, capture_output=True, text=True, timeout=30)
    return json.loads(r.stdout)

def run(key):
    print("\n🔗 HUIT DATA VENTURES — Stripe Webhook Registration")
    print(f"   Registering {len(PRODUCTS)} webhook endpoints\n")

    results = []
    for slug in PRODUCTS:
        url = f"https://{slug}.data.huit.ai/api/stripe/webhook"
        resp = stripe("POST", "webhook_endpoints", key, {
            "url": url,
            "enabled_events": EVENTS,
            "description": f"Huit Data Ventures — {slug}",
            "metadata[product]": slug,
            "metadata[portfolio]": "huit-data-ventures",
        })

        if "id" in resp:
            secret = resp.get("secret", "whsec_retrieve_from_dashboard")
            print(f"  ✅ {slug}")
            print(f"     Webhook ID: {resp['id']}")
            print(f"     Secret: {secret}")
            print(f"     → Add to Vercel as STRIPE_WEBHOOK_SECRET")
            print()
            results.append({"slug": slug, "webhook_id": resp["id"], "secret": secret, "url": url})
        else:
            err = resp.get("error", {}).get("message", "unknown")
            print(f"  ❌ {slug}: {err}")

    print("\n── WEBHOOK SECRETS FOR VERCEL ───────────────────────────────")
    print("Add STRIPE_WEBHOOK_SECRET to each Vercel project:")
    for r in results:
        print(f"  {r['slug']}: {r['secret']}")

    with open("webhook_manifest.json", "w") as f:
        json.dump(results, f, indent=2)
    print("\n📄 Full manifest → webhook_manifest.json")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(1)
    run(sys.argv[1])
