# Huit Data Ventures — Scripts

## Stripe Setup

```bash
python3 huit_stripe_setup.py sk_live_YOUR_KEY_HERE
```

Creates all 25 DaaS products, 50 price IDs (monthly + annual),
inserts into Supabase, and outputs Vercel env vars.

### Output
- Console: all price IDs + copy-paste Vercel env vars
- File: `stripe_manifest.json` — full product registry

### Requirements
- Python 3.8+
- curl
- Your Stripe secret key (sk_live_... or sk_test_...)
