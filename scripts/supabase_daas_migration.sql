-- ════════════════════════════════════════════════════════════════
-- HUIT DATA VENTURES — Supabase DaaS Schema Migration
-- Run in Supabase SQL Editor: vvkdnzqgtajeouxlliuk.supabase.co
-- ════════════════════════════════════════════════════════════════

-- DaaS subscriptions table (extends existing subscriptions for daas products)
CREATE TABLE IF NOT EXISTS daas_subscriptions (
  id                      UUID DEFAULT gen_random_uuid() PRIMARY KEY,
  stripe_subscription_id  TEXT UNIQUE NOT NULL,
  stripe_customer_id      TEXT NOT NULL,
  customer_email          TEXT NOT NULL,
  product_slug            TEXT NOT NULL,  -- e.g. 'lenderpulse', 'flightrisk'
  status                  TEXT NOT NULL DEFAULT 'active',
  interval                TEXT NOT NULL DEFAULT 'month',
  current_period_start    TIMESTAMPTZ,
  current_period_end      TIMESTAMPTZ,
  cancelled_at            TIMESTAMPTZ,
  created_at              TIMESTAMPTZ DEFAULT NOW(),
  updated_at              TIMESTAMPTZ DEFAULT NOW()
);

-- Index for fast lookups by email + product
CREATE INDEX IF NOT EXISTS idx_daas_subs_email_product 
  ON daas_subscriptions(customer_email, product_slug);

CREATE INDEX IF NOT EXISTS idx_daas_subs_status 
  ON daas_subscriptions(status);

-- DaaS product registry (mirrors our 25-product list)
CREATE TABLE IF NOT EXISTS daas_products (
  id              UUID DEFAULT gen_random_uuid() PRIMARY KEY,
  slug            TEXT UNIQUE NOT NULL,
  name            TEXT NOT NULL,
  tagline         TEXT,
  price_monthly   INTEGER NOT NULL,  -- in cents
  price_annual    INTEGER,           -- in cents (15% off)
  phase           INTEGER NOT NULL,  -- 1-4
  industry        TEXT,
  subdomain       TEXT,
  stripe_product_id TEXT,
  stripe_price_id_monthly TEXT,
  stripe_price_id_annual  TEXT,
  active          BOOLEAN DEFAULT TRUE,
  created_at      TIMESTAMPTZ DEFAULT NOW(),
  updated_at      TIMESTAMPTZ DEFAULT NOW()
);

-- Seed product registry
INSERT INTO daas_products (slug, name, tagline, price_monthly, phase, industry, subdomain) VALUES
  ('lenderpulse',   'LenderPulse',   'Mortgage Lender Risk Intelligence',           350000, 1, 'Insurance & Underwriting',   'lenderpulse.data.huit.ai'),
  ('flightrisk',    'FlightRisk',    'HR Attrition Signal Intelligence',             400000, 1, 'HR & Workforce Intelligence', 'flightrisk.data.huit.ai'),
  ('zonescore',     'ZoneScore',     'Insurance Zip-Code Risk Scores',               300000, 1, 'Insurance & Underwriting',   'zonescore.data.huit.ai'),
  ('licensewatch',  'LicenseWatch',  'NMLS License Lapse & Reinstatement Monitor',  250000, 1, 'Legal & Compliance',          'licensewatch.data.huit.ai'),
  ('exposureiq',    'ExposureIQ',    'Legal Exposure Intelligence',                  450000, 1, 'Legal & Compliance',          'exposureiq.data.huit.ai'),
  ('origintrace',   'OriginTrace',   'CRE Loan Origination Trend Reports',          250000, 2, 'Commercial Real Estate',      'origintrace.data.huit.ai'),
  ('fairlend',      'FairLend',      'HMDA Disparate Impact Dashboard',              350000, 2, 'Legal & Compliance',          'fairlend.data.huit.ai'),
  ('advisortrack',  'AdvisorTrack',  'Financial Advisor Movement Intelligence',     400000, 2, 'HR & Workforce Intelligence', 'advisortrack.data.huit.ai'),
  ('leasesignal',   'LeaseSignal',   'Commercial Lease Expiration Intelligence',    300000, 2, 'Commercial Real Estate',      'leasesignal.data.huit.ai'),
  ('depositiq',     'DepositIQ',     'Regional Banking Deposit Concentration',      350000, 2, 'Insurance & Underwriting',   'depositiq.data.huit.ai'),
  ('caprateiq',     'CapRateIQ',     'CRE Cap Rate & Stress Test Data Feed',        400000, 2, 'Commercial Real Estate',      'caprateiq.data.huit.ai'),
  ('carriershift',  'CarrierShift',  'P&C Carrier Appetite Intelligence',           300000, 2, 'Insurance & Underwriting',   'carriershift.data.huit.ai'),
  ('esgflag',       'ESGFlag',       'ESG Compliance Exposure Feed',                450000, 2, 'Legal & Compliance',          'esgflag.data.huit.ai'),
  ('exodusmap',     'ExodusMap',     'Talent Exodus Map Financial Services',        400000, 3, 'HR & Workforce Intelligence', 'exodusmap.data.huit.ai'),
  ('claimbench',    'ClaimBench',    'Workers Comp Claim Frequency Heatmap',        350000, 3, 'Insurance & Underwriting',   'claimbench.data.huit.ai'),
  ('leasecomps',    'LeaseComps',    'Lease Comps Intelligence for Legal',          500000, 3, 'Legal & Compliance',          'leasecomps.data.huit.ai'),
  ('servicerrisk',  'ServicerRisk',  'Mortgage Servicer Performance Intelligence', 450000, 3, 'Insurance & Underwriting',   'servicerrisk.data.huit.ai'),
  ('headcountiq',   'HeadcountIQ',   'Corporate Headcount Signal Feed',             400000, 3, 'HR & Workforce Intelligence', 'headcountiq.data.huit.ai'),
  ('regaction',     'RegAction',     'Regulatory Action Monitor Insurance',         350000, 3, 'Insurance & Underwriting',   'regaction.data.huit.ai'),
  ('distressmap',   'DistressMap',   'CRE Distress Signal Feed',                    500000, 3, 'Commercial Real Estate',      'distressmap.data.huit.ai'),
  ('auditready',    'AuditReady',    'Fair Lending Audit Prep Data Room',           500000, 4, 'Legal & Compliance',          'auditready.data.huit.ai'),
  ('insuretarget',  'InsureTarget',  'Insurance M&A Target Identification',         500000, 4, 'Insurance & Underwriting',   'insuretarget.data.huit.ai'),
  ('contractbench', 'ContractBench', 'Employment Contract Benchmark Intelligence',  400000, 4, 'HR & Workforce Intelligence', 'contractbench.data.huit.ai'),
  ('deedguard',     'DeedGuard',     'Title & Deed Fraud Intelligence Feed',        450000, 4, 'Insurance & Underwriting',   'deedguard.data.huit.ai'),
  ('compliancerisk','ComplianceRisk','Multi-State Employer Compliance Intelligence', 450000, 4, 'HR & Workforce Intelligence', 'compliancerisk.data.huit.ai')
ON CONFLICT (slug) DO UPDATE SET
  updated_at = NOW();

-- RLS: Only authenticated users with active subscription can read
ALTER TABLE daas_subscriptions ENABLE ROW LEVEL SECURITY;

CREATE POLICY "Users can read own DaaS subscription" 
  ON daas_subscriptions FOR SELECT 
  USING (auth.jwt() ->> 'email' = customer_email);

CREATE POLICY "Service role full access to daas_subscriptions"
  ON daas_subscriptions FOR ALL
  USING (auth.role() = 'service_role');

-- DaaS products are public readable
ALTER TABLE daas_products ENABLE ROW LEVEL SECURITY;

CREATE POLICY "Anyone can read daas products"
  ON daas_products FOR SELECT
  USING (true);

CREATE POLICY "Service role manages daas products"
  ON daas_products FOR ALL
  USING (auth.role() = 'service_role');

-- View: Active DaaS subscriptions with product details
CREATE OR REPLACE VIEW daas_active_subscriptions AS
SELECT 
  ds.id,
  ds.customer_email,
  ds.product_slug,
  dp.name as product_name,
  dp.subdomain,
  dp.price_monthly,
  ds.status,
  ds.interval,
  ds.current_period_end,
  ds.created_at
FROM daas_subscriptions ds
JOIN daas_products dp ON dp.slug = ds.product_slug
WHERE ds.status = 'active';

-- Function: Check if user has active subscription to a product
CREATE OR REPLACE FUNCTION check_daas_access(p_email TEXT, p_slug TEXT)
RETURNS BOOLEAN AS $$
  SELECT EXISTS (
    SELECT 1 FROM daas_subscriptions
    WHERE customer_email = p_email
    AND product_slug = p_slug
    AND status = 'active'
  );
$$ LANGUAGE sql STABLE SECURITY DEFINER;

-- ════════════════════════════════════════════════════════════════
-- Run this in Supabase SQL Editor to complete DaaS schema setup
-- ════════════════════════════════════════════════════════════════
