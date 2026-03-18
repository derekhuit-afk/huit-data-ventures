export default function Home() {
  return (
    <div style={{ minHeight: "100vh" }}>
      {/* Nav */}
      <nav style={{ borderBottom: "1px solid #1E2235", padding: "20px 48px", display: "flex", justifyContent: "space-between", alignItems: "center" }}>
        <div>
          <div style={{ fontWeight: 900, fontSize: "20px", letterSpacing: "-0.5px" }}>HUIT DATA VENTURES</div>
          <div style={{ fontSize: "10px", color: "#6B7280", letterSpacing: "3px", marginTop: "2px" }}>ENTERPRISE INTELLIGENCE PORTFOLIO</div>
        </div>
        <div style={{ fontSize: "11px", color: "#6B7280" }}>data.huit.ai</div>
      </nav>

      {/* Hero */}
      <div style={{ maxWidth: "1200px", margin: "0 auto", padding: "80px 48px 60px" }}>
        <div style={{ fontSize: "11px", letterSpacing: "4px", color: "#00E5FF", textTransform: "uppercase", marginBottom: "20px" }}>25 Independent DaaS Companies</div>
        <h1 style={{ fontWeight: 900, fontSize: "clamp(32px, 5vw, 60px)", lineHeight: 1.05, letterSpacing: "-2px", marginBottom: "20px", maxWidth: "700px" }}>
          Institutional-Grade Data.<br />Enterprise Pricing.<br />Live Dashboards.
        </h1>
        <p style={{ fontSize: "16px", color: "#9CA3AF", maxWidth: "560px", lineHeight: 1.7, marginBottom: "0" }}>
          Insurance underwriting, legal compliance, commercial real estate, and HR workforce intelligence — packaged as separate, purchasable data products.
        </p>
      </div>

      {/* Stats */}
      <div style={{ borderTop: "1px solid #1E2235", borderBottom: "1px solid #1E2235" }}>
        <div style={{ maxWidth: "1200px", margin: "0 auto", padding: "32px 48px", display: "grid", gridTemplateColumns: "repeat(4, 1fr)", gap: "40px" }}>
          [('25', 'Products'), ('$98K', 'MRR Potential'), ('5', 'Live Now'), ('60 Days', 'Full Rollout')]
          <div><div style={{ fontWeight: 900, fontSize: "32px", color: "#00E5FF" }}>25</div><div style={{ fontSize: "10px", color: "#6B7280", letterSpacing: "2px", textTransform: "uppercase", marginTop: "4px" }}>Products</div></div>
          <div><div style={{ fontWeight: 900, fontSize: "32px" }}>$98K</div><div style={{ fontSize: "10px", color: "#6B7280", letterSpacing: "2px", textTransform: "uppercase", marginTop: "4px" }}>MRR Potential</div></div>
          <div><div style={{ fontWeight: 900, fontSize: "32px", color: "#00FF88" }}>5</div><div style={{ fontSize: "10px", color: "#6B7280", letterSpacing: "2px", textTransform: "uppercase", marginTop: "4px" }}>Live Now</div></div>
          <div><div style={{ fontWeight: 900, fontSize: "32px" }}>60 Days</div><div style={{ fontSize: "10px", color: "#6B7280", letterSpacing: "2px", textTransform: "uppercase", marginTop: "4px" }}>Full Rollout</div></div>
        </div>
      </div>

      {/* Products Grid */}
      <div style={{ maxWidth: "1200px", margin: "0 auto", padding: "60px 48px" }}>
        <div style={{ display: "flex", justifyContent: "space-between", alignItems: "baseline", marginBottom: "32px" }}>
          <div style={{ fontSize: "11px", letterSpacing: "3px", color: "#6B7280", textTransform: "uppercase" }}>All 25 Products</div>
          <div style={{ fontSize: "11px", color: "#6B7280" }}>Phase 1 products are live and purchasable</div>
        </div>
        <div style={{ display: "grid", gridTemplateColumns: "repeat(3, 1fr)", gap: "12px" }}>

        <a href="https://lenderpulse.data.huit.ai" style={{ textDecoration: "none", display: "block", border: "1px solid #00FF8830", padding: "20px 24px", background: "#080C1A", opacity: "1", cursor: "pointer", transition: "all 0.2s" }}>
          <div style={{ display: "flex", justifyContent: "space-between", alignItems: "flex-start" }}>
            <div>
              <div style={{ fontSize: "10px", color: "#6B7280", letterSpacing: "2px", marginBottom: "6px" }}>P1 · Insurance & Underwri</div>
              <div style={{ fontWeight: 900, fontSize: "16px", color: "#E8EAF0", marginBottom: "4px" }}>LenderPulse</div>
              <div style={{ fontSize: "11px", color: "#6B7280" }}>Mortgage Lender Risk Intelligence</div>
            </div>
            <div style={{ textAlign: "right" }}>
              <div style={{ fontWeight: 900, fontSize: "16px", color: "#00FF88" }}>$3,500</div>
              <div style={{ fontSize: "9px", color: "#4B5563", letterSpacing: "1px" }}>PER MONTH</div>
              <div style={{{{ fontSize: '9px', color: '#00E5FF', marginTop: '4px', letterSpacing: '1px' }}}}>LIVE</div>
            </div>
          </div>
        </a>

        <a href="https://flightrisk.data.huit.ai" style={{ textDecoration: "none", display: "block", border: "1px solid #00E5FF30", padding: "20px 24px", background: "#080C1A", opacity: "1", cursor: "pointer", transition: "all 0.2s" }}>
          <div style={{ display: "flex", justifyContent: "space-between", alignItems: "flex-start" }}>
            <div>
              <div style={{ fontSize: "10px", color: "#6B7280", letterSpacing: "2px", marginBottom: "6px" }}>P1 · HR & Workforce Intel</div>
              <div style={{ fontWeight: 900, fontSize: "16px", color: "#E8EAF0", marginBottom: "4px" }}>FlightRisk</div>
              <div style={{ fontSize: "11px", color: "#6B7280" }}>HR Attrition Signal Feed</div>
            </div>
            <div style={{ textAlign: "right" }}>
              <div style={{ fontWeight: 900, fontSize: "16px", color: "#00E5FF" }}>$4,000</div>
              <div style={{ fontSize: "9px", color: "#4B5563", letterSpacing: "1px" }}>PER MONTH</div>
              <div style={{{{ fontSize: '9px', color: '#00E5FF', marginTop: '4px', letterSpacing: '1px' }}}}>LIVE</div>
            </div>
          </div>
        </a>

        <a href="https://zonescore.data.huit.ai" style={{ textDecoration: "none", display: "block", border: "1px solid #FFD70030", padding: "20px 24px", background: "#080C1A", opacity: "1", cursor: "pointer", transition: "all 0.2s" }}>
          <div style={{ display: "flex", justifyContent: "space-between", alignItems: "flex-start" }}>
            <div>
              <div style={{ fontSize: "10px", color: "#6B7280", letterSpacing: "2px", marginBottom: "6px" }}>P1 · Insurance & Underwri</div>
              <div style={{ fontWeight: 900, fontSize: "16px", color: "#E8EAF0", marginBottom: "4px" }}>ZoneScore</div>
              <div style={{ fontSize: "11px", color: "#6B7280" }}>Insurance Zip-Code Risk Scores</div>
            </div>
            <div style={{ textAlign: "right" }}>
              <div style={{ fontWeight: 900, fontSize: "16px", color: "#FFD700" }}>$3,000</div>
              <div style={{ fontSize: "9px", color: "#4B5563", letterSpacing: "1px" }}>PER MONTH</div>
              <div style={{{{ fontSize: '9px', color: '#00E5FF', marginTop: '4px', letterSpacing: '1px' }}}}>LIVE</div>
            </div>
          </div>
        </a>

        <a href="https://licensewatch.data.huit.ai" style={{ textDecoration: "none", display: "block", border: "1px solid #7B61FF30", padding: "20px 24px", background: "#080C1A", opacity: "1", cursor: "pointer", transition: "all 0.2s" }}>
          <div style={{ display: "flex", justifyContent: "space-between", alignItems: "flex-start" }}>
            <div>
              <div style={{ fontSize: "10px", color: "#6B7280", letterSpacing: "2px", marginBottom: "6px" }}>P1 · Legal & Compliance</div>
              <div style={{ fontWeight: 900, fontSize: "16px", color: "#E8EAF0", marginBottom: "4px" }}>LicenseWatch</div>
              <div style={{ fontSize: "11px", color: "#6B7280" }}>NMLS License Monitor</div>
            </div>
            <div style={{ textAlign: "right" }}>
              <div style={{ fontWeight: 900, fontSize: "16px", color: "#7B61FF" }}>$2,500</div>
              <div style={{ fontSize: "9px", color: "#4B5563", letterSpacing: "1px" }}>PER MONTH</div>
              <div style={{{{ fontSize: '9px', color: '#00E5FF', marginTop: '4px', letterSpacing: '1px' }}}}>LIVE</div>
            </div>
          </div>
        </a>

        <a href="https://exposureiq.data.huit.ai" style={{ textDecoration: "none", display: "block", border: "1px solid #FF6B3530", padding: "20px 24px", background: "#080C1A", opacity: "1", cursor: "pointer", transition: "all 0.2s" }}>
          <div style={{ display: "flex", justifyContent: "space-between", alignItems: "flex-start" }}>
            <div>
              <div style={{ fontSize: "10px", color: "#6B7280", letterSpacing: "2px", marginBottom: "6px" }}>P1 · Legal & Compliance</div>
              <div style={{ fontWeight: 900, fontSize: "16px", color: "#E8EAF0", marginBottom: "4px" }}>ExposureIQ</div>
              <div style={{ fontSize: "11px", color: "#6B7280" }}>Legal Exposure Reports</div>
            </div>
            <div style={{ textAlign: "right" }}>
              <div style={{ fontWeight: 900, fontSize: "16px", color: "#FF6B35" }}>$4,500</div>
              <div style={{ fontSize: "9px", color: "#4B5563", letterSpacing: "1px" }}>PER MONTH</div>
              <div style={{{{ fontSize: '9px', color: '#00E5FF', marginTop: '4px', letterSpacing: '1px' }}}}>LIVE</div>
            </div>
          </div>
        </a>

        <a href="#" style={{ textDecoration: "none", display: "block", border: "1px solid #1E2235", padding: "20px 24px", background: "#06080F", opacity: "0.7", cursor: "default", transition: "all 0.2s" }}>
          <div style={{ display: "flex", justifyContent: "space-between", alignItems: "flex-start" }}>
            <div>
              <div style={{ fontSize: "10px", color: "#6B7280", letterSpacing: "2px", marginBottom: "6px" }}>P2 · Commercial Real Esta</div>
              <div style={{ fontWeight: 900, fontSize: "16px", color: "#9CA3AF", marginBottom: "4px" }}>OriginTrace</div>
              <div style={{ fontSize: "11px", color: "#6B7280" }}>CRE Loan Origination Trends</div>
            </div>
            <div style={{ textAlign: "right" }}>
              <div style={{ fontWeight: 900, fontSize: "16px", color: "#4B5563" }}>$2,500</div>
              <div style={{ fontSize: "9px", color: "#4B5563", letterSpacing: "1px" }}>PER MONTH</div>
              <div style={{ fontSize: '9px', color: '#4B5563', marginTop: '4px' }}>Phase 2</div>
            </div>
          </div>
        </a>

        <a href="#" style={{ textDecoration: "none", display: "block", border: "1px solid #1E2235", padding: "20px 24px", background: "#06080F", opacity: "0.7", cursor: "default", transition: "all 0.2s" }}>
          <div style={{ display: "flex", justifyContent: "space-between", alignItems: "flex-start" }}>
            <div>
              <div style={{ fontSize: "10px", color: "#6B7280", letterSpacing: "2px", marginBottom: "6px" }}>P2 · Legal & Compliance</div>
              <div style={{ fontWeight: 900, fontSize: "16px", color: "#9CA3AF", marginBottom: "4px" }}>FairLend</div>
              <div style={{ fontSize: "11px", color: "#6B7280" }}>HMDA Disparate Impact Dashboard</div>
            </div>
            <div style={{ textAlign: "right" }}>
              <div style={{ fontWeight: 900, fontSize: "16px", color: "#4B5563" }}>$3,500</div>
              <div style={{ fontSize: "9px", color: "#4B5563", letterSpacing: "1px" }}>PER MONTH</div>
              <div style={{ fontSize: '9px', color: '#4B5563', marginTop: '4px' }}>Phase 2</div>
            </div>
          </div>
        </a>

        <a href="#" style={{ textDecoration: "none", display: "block", border: "1px solid #1E2235", padding: "20px 24px", background: "#06080F", opacity: "0.7", cursor: "default", transition: "all 0.2s" }}>
          <div style={{ display: "flex", justifyContent: "space-between", alignItems: "flex-start" }}>
            <div>
              <div style={{ fontSize: "10px", color: "#6B7280", letterSpacing: "2px", marginBottom: "6px" }}>P2 · HR & Workforce Intel</div>
              <div style={{ fontWeight: 900, fontSize: "16px", color: "#9CA3AF", marginBottom: "4px" }}>AdvisorTrack</div>
              <div style={{ fontSize: "11px", color: "#6B7280" }}>Financial Advisor Movement</div>
            </div>
            <div style={{ textAlign: "right" }}>
              <div style={{ fontWeight: 900, fontSize: "16px", color: "#4B5563" }}>$4,000</div>
              <div style={{ fontSize: "9px", color: "#4B5563", letterSpacing: "1px" }}>PER MONTH</div>
              <div style={{ fontSize: '9px', color: '#4B5563', marginTop: '4px' }}>Phase 2</div>
            </div>
          </div>
        </a>

        <a href="#" style={{ textDecoration: "none", display: "block", border: "1px solid #1E2235", padding: "20px 24px", background: "#06080F", opacity: "0.7", cursor: "default", transition: "all 0.2s" }}>
          <div style={{ display: "flex", justifyContent: "space-between", alignItems: "flex-start" }}>
            <div>
              <div style={{ fontSize: "10px", color: "#6B7280", letterSpacing: "2px", marginBottom: "6px" }}>P2 · Commercial Real Esta</div>
              <div style={{ fontWeight: 900, fontSize: "16px", color: "#9CA3AF", marginBottom: "4px" }}>LeaseSignal</div>
              <div style={{ fontSize: "11px", color: "#6B7280" }}>Commercial Lease Expiration Intel</div>
            </div>
            <div style={{ textAlign: "right" }}>
              <div style={{ fontWeight: 900, fontSize: "16px", color: "#4B5563" }}>$3,000</div>
              <div style={{ fontSize: "9px", color: "#4B5563", letterSpacing: "1px" }}>PER MONTH</div>
              <div style={{ fontSize: '9px', color: '#4B5563', marginTop: '4px' }}>Phase 2</div>
            </div>
          </div>
        </a>

        <a href="#" style={{ textDecoration: "none", display: "block", border: "1px solid #1E2235", padding: "20px 24px", background: "#06080F", opacity: "0.7", cursor: "default", transition: "all 0.2s" }}>
          <div style={{ display: "flex", justifyContent: "space-between", alignItems: "flex-start" }}>
            <div>
              <div style={{ fontSize: "10px", color: "#6B7280", letterSpacing: "2px", marginBottom: "6px" }}>P2 · Insurance & Underwri</div>
              <div style={{ fontWeight: 900, fontSize: "16px", color: "#9CA3AF", marginBottom: "4px" }}>DepositIQ</div>
              <div style={{ fontSize: "11px", color: "#6B7280" }}>Regional Banking Deposit Feed</div>
            </div>
            <div style={{ textAlign: "right" }}>
              <div style={{ fontWeight: 900, fontSize: "16px", color: "#4B5563" }}>$3,500</div>
              <div style={{ fontSize: "9px", color: "#4B5563", letterSpacing: "1px" }}>PER MONTH</div>
              <div style={{ fontSize: '9px', color: '#4B5563', marginTop: '4px' }}>Phase 2</div>
            </div>
          </div>
        </a>

        <a href="#" style={{ textDecoration: "none", display: "block", border: "1px solid #1E2235", padding: "20px 24px", background: "#06080F", opacity: "0.7", cursor: "default", transition: "all 0.2s" }}>
          <div style={{ display: "flex", justifyContent: "space-between", alignItems: "flex-start" }}>
            <div>
              <div style={{ fontSize: "10px", color: "#6B7280", letterSpacing: "2px", marginBottom: "6px" }}>P2 · Commercial Real Esta</div>
              <div style={{ fontWeight: 900, fontSize: "16px", color: "#9CA3AF", marginBottom: "4px" }}>CapRateIQ</div>
              <div style={{ fontSize: "11px", color: "#6B7280" }}>CRE Cap Rate & Stress Test Feed</div>
            </div>
            <div style={{ textAlign: "right" }}>
              <div style={{ fontWeight: 900, fontSize: "16px", color: "#4B5563" }}>$4,000</div>
              <div style={{ fontSize: "9px", color: "#4B5563", letterSpacing: "1px" }}>PER MONTH</div>
              <div style={{ fontSize: '9px', color: '#4B5563', marginTop: '4px' }}>Phase 2</div>
            </div>
          </div>
        </a>

        <a href="#" style={{ textDecoration: "none", display: "block", border: "1px solid #1E2235", padding: "20px 24px", background: "#06080F", opacity: "0.7", cursor: "default", transition: "all 0.2s" }}>
          <div style={{ display: "flex", justifyContent: "space-between", alignItems: "flex-start" }}>
            <div>
              <div style={{ fontSize: "10px", color: "#6B7280", letterSpacing: "2px", marginBottom: "6px" }}>P2 · Insurance & Underwri</div>
              <div style={{ fontWeight: 900, fontSize: "16px", color: "#9CA3AF", marginBottom: "4px" }}>CarrierShift</div>
              <div style={{ fontSize: "11px", color: "#6B7280" }}>P&C Carrier Appetite Intelligence</div>
            </div>
            <div style={{ textAlign: "right" }}>
              <div style={{ fontWeight: 900, fontSize: "16px", color: "#4B5563" }}>$3,000</div>
              <div style={{ fontSize: "9px", color: "#4B5563", letterSpacing: "1px" }}>PER MONTH</div>
              <div style={{ fontSize: '9px', color: '#4B5563', marginTop: '4px' }}>Phase 2</div>
            </div>
          </div>
        </a>

        <a href="#" style={{ textDecoration: "none", display: "block", border: "1px solid #1E2235", padding: "20px 24px", background: "#06080F", opacity: "0.7", cursor: "default", transition: "all 0.2s" }}>
          <div style={{ display: "flex", justifyContent: "space-between", alignItems: "flex-start" }}>
            <div>
              <div style={{ fontSize: "10px", color: "#6B7280", letterSpacing: "2px", marginBottom: "6px" }}>P2 · Legal & Compliance</div>
              <div style={{ fontWeight: 900, fontSize: "16px", color: "#9CA3AF", marginBottom: "4px" }}>ESGFlag</div>
              <div style={{ fontSize: "11px", color: "#6B7280" }}>ESG Compliance Exposure Feed</div>
            </div>
            <div style={{ textAlign: "right" }}>
              <div style={{ fontWeight: 900, fontSize: "16px", color: "#4B5563" }}>$4,500</div>
              <div style={{ fontSize: "9px", color: "#4B5563", letterSpacing: "1px" }}>PER MONTH</div>
              <div style={{ fontSize: '9px', color: '#4B5563', marginTop: '4px' }}>Phase 2</div>
            </div>
          </div>
        </a>

        <a href="#" style={{ textDecoration: "none", display: "block", border: "1px solid #1E2235", padding: "20px 24px", background: "#06080F", opacity: "0.7", cursor: "default", transition: "all 0.2s" }}>
          <div style={{ display: "flex", justifyContent: "space-between", alignItems: "flex-start" }}>
            <div>
              <div style={{ fontSize: "10px", color: "#6B7280", letterSpacing: "2px", marginBottom: "6px" }}>P3 · HR & Workforce Intel</div>
              <div style={{ fontWeight: 900, fontSize: "16px", color: "#9CA3AF", marginBottom: "4px" }}>ExodusMap</div>
              <div style={{ fontSize: "11px", color: "#6B7280" }}>Talent Exodus Map</div>
            </div>
            <div style={{ textAlign: "right" }}>
              <div style={{ fontWeight: 900, fontSize: "16px", color: "#4B5563" }}>$4,000</div>
              <div style={{ fontSize: "9px", color: "#4B5563", letterSpacing: "1px" }}>PER MONTH</div>
              <div style={{ fontSize: '9px', color: '#4B5563', marginTop: '4px' }}>Phase 3</div>
            </div>
          </div>
        </a>

        <a href="#" style={{ textDecoration: "none", display: "block", border: "1px solid #1E2235", padding: "20px 24px", background: "#06080F", opacity: "0.7", cursor: "default", transition: "all 0.2s" }}>
          <div style={{ display: "flex", justifyContent: "space-between", alignItems: "flex-start" }}>
            <div>
              <div style={{ fontSize: "10px", color: "#6B7280", letterSpacing: "2px", marginBottom: "6px" }}>P3 · Insurance & Underwri</div>
              <div style={{ fontWeight: 900, fontSize: "16px", color: "#9CA3AF", marginBottom: "4px" }}>ClaimBench</div>
              <div style={{ fontSize: "11px", color: "#6B7280" }}>Workers Comp Claim Heatmap</div>
            </div>
            <div style={{ textAlign: "right" }}>
              <div style={{ fontWeight: 900, fontSize: "16px", color: "#4B5563" }}>$3,500</div>
              <div style={{ fontSize: "9px", color: "#4B5563", letterSpacing: "1px" }}>PER MONTH</div>
              <div style={{ fontSize: '9px', color: '#4B5563', marginTop: '4px' }}>Phase 3</div>
            </div>
          </div>
        </a>

        <a href="#" style={{ textDecoration: "none", display: "block", border: "1px solid #1E2235", padding: "20px 24px", background: "#06080F", opacity: "0.7", cursor: "default", transition: "all 0.2s" }}>
          <div style={{ display: "flex", justifyContent: "space-between", alignItems: "flex-start" }}>
            <div>
              <div style={{ fontSize: "10px", color: "#6B7280", letterSpacing: "2px", marginBottom: "6px" }}>P3 · Legal & Compliance</div>
              <div style={{ fontWeight: 900, fontSize: "16px", color: "#9CA3AF", marginBottom: "4px" }}>LeaseComps</div>
              <div style={{ fontSize: "11px", color: "#6B7280" }}>Lease Comps for Legal Discovery</div>
            </div>
            <div style={{ textAlign: "right" }}>
              <div style={{ fontWeight: 900, fontSize: "16px", color: "#4B5563" }}>$5,000</div>
              <div style={{ fontSize: "9px", color: "#4B5563", letterSpacing: "1px" }}>PER MONTH</div>
              <div style={{ fontSize: '9px', color: '#4B5563', marginTop: '4px' }}>Phase 3</div>
            </div>
          </div>
        </a>

        <a href="#" style={{ textDecoration: "none", display: "block", border: "1px solid #1E2235", padding: "20px 24px", background: "#06080F", opacity: "0.7", cursor: "default", transition: "all 0.2s" }}>
          <div style={{ display: "flex", justifyContent: "space-between", alignItems: "flex-start" }}>
            <div>
              <div style={{ fontSize: "10px", color: "#6B7280", letterSpacing: "2px", marginBottom: "6px" }}>P3 · Insurance & Underwri</div>
              <div style={{ fontWeight: 900, fontSize: "16px", color: "#9CA3AF", marginBottom: "4px" }}>ServicerRisk</div>
              <div style={{ fontSize: "11px", color: "#6B7280" }}>Mortgage Servicer Performance</div>
            </div>
            <div style={{ textAlign: "right" }}>
              <div style={{ fontWeight: 900, fontSize: "16px", color: "#4B5563" }}>$4,500</div>
              <div style={{ fontSize: "9px", color: "#4B5563", letterSpacing: "1px" }}>PER MONTH</div>
              <div style={{ fontSize: '9px', color: '#4B5563', marginTop: '4px' }}>Phase 3</div>
            </div>
          </div>
        </a>

        <a href="#" style={{ textDecoration: "none", display: "block", border: "1px solid #1E2235", padding: "20px 24px", background: "#06080F", opacity: "0.7", cursor: "default", transition: "all 0.2s" }}>
          <div style={{ display: "flex", justifyContent: "space-between", alignItems: "flex-start" }}>
            <div>
              <div style={{ fontSize: "10px", color: "#6B7280", letterSpacing: "2px", marginBottom: "6px" }}>P3 · HR & Workforce Intel</div>
              <div style={{ fontWeight: 900, fontSize: "16px", color: "#9CA3AF", marginBottom: "4px" }}>HeadcountIQ</div>
              <div style={{ fontSize: "11px", color: "#6B7280" }}>Corporate Headcount Signal Feed</div>
            </div>
            <div style={{ textAlign: "right" }}>
              <div style={{ fontWeight: 900, fontSize: "16px", color: "#4B5563" }}>$4,000</div>
              <div style={{ fontSize: "9px", color: "#4B5563", letterSpacing: "1px" }}>PER MONTH</div>
              <div style={{ fontSize: '9px', color: '#4B5563', marginTop: '4px' }}>Phase 3</div>
            </div>
          </div>
        </a>

        <a href="#" style={{ textDecoration: "none", display: "block", border: "1px solid #1E2235", padding: "20px 24px", background: "#06080F", opacity: "0.7", cursor: "default", transition: "all 0.2s" }}>
          <div style={{ display: "flex", justifyContent: "space-between", alignItems: "flex-start" }}>
            <div>
              <div style={{ fontSize: "10px", color: "#6B7280", letterSpacing: "2px", marginBottom: "6px" }}>P3 · Insurance & Underwri</div>
              <div style={{ fontWeight: 900, fontSize: "16px", color: "#9CA3AF", marginBottom: "4px" }}>RegAction</div>
              <div style={{ fontSize: "11px", color: "#6B7280" }}>State Insurance Regulatory Monitor</div>
            </div>
            <div style={{ textAlign: "right" }}>
              <div style={{ fontWeight: 900, fontSize: "16px", color: "#4B5563" }}>$3,500</div>
              <div style={{ fontSize: "9px", color: "#4B5563", letterSpacing: "1px" }}>PER MONTH</div>
              <div style={{ fontSize: '9px', color: '#4B5563', marginTop: '4px' }}>Phase 3</div>
            </div>
          </div>
        </a>

        <a href="#" style={{ textDecoration: "none", display: "block", border: "1px solid #1E2235", padding: "20px 24px", background: "#06080F", opacity: "0.7", cursor: "default", transition: "all 0.2s" }}>
          <div style={{ display: "flex", justifyContent: "space-between", alignItems: "flex-start" }}>
            <div>
              <div style={{ fontSize: "10px", color: "#6B7280", letterSpacing: "2px", marginBottom: "6px" }}>P3 · Commercial Real Esta</div>
              <div style={{ fontWeight: 900, fontSize: "16px", color: "#9CA3AF", marginBottom: "4px" }}>DistressMap</div>
              <div style={{ fontSize: "11px", color: "#6B7280" }}>CRE Distress Signal Feed</div>
            </div>
            <div style={{ textAlign: "right" }}>
              <div style={{ fontWeight: 900, fontSize: "16px", color: "#4B5563" }}>$5,000</div>
              <div style={{ fontSize: "9px", color: "#4B5563", letterSpacing: "1px" }}>PER MONTH</div>
              <div style={{ fontSize: '9px', color: '#4B5563', marginTop: '4px' }}>Phase 3</div>
            </div>
          </div>
        </a>

        <a href="#" style={{ textDecoration: "none", display: "block", border: "1px solid #1E2235", padding: "20px 24px", background: "#06080F", opacity: "0.7", cursor: "default", transition: "all 0.2s" }}>
          <div style={{ display: "flex", justifyContent: "space-between", alignItems: "flex-start" }}>
            <div>
              <div style={{ fontSize: "10px", color: "#6B7280", letterSpacing: "2px", marginBottom: "6px" }}>P4 · Legal & Compliance</div>
              <div style={{ fontWeight: 900, fontSize: "16px", color: "#9CA3AF", marginBottom: "4px" }}>AuditReady</div>
              <div style={{ fontSize: "11px", color: "#6B7280" }}>Fair Lending Audit Prep</div>
            </div>
            <div style={{ textAlign: "right" }}>
              <div style={{ fontWeight: 900, fontSize: "16px", color: "#4B5563" }}>$5,000</div>
              <div style={{ fontSize: "9px", color: "#4B5563", letterSpacing: "1px" }}>PER MONTH</div>
              <div style={{ fontSize: '9px', color: '#4B5563', marginTop: '4px' }}>Phase 4</div>
            </div>
          </div>
        </a>

        <a href="#" style={{ textDecoration: "none", display: "block", border: "1px solid #1E2235", padding: "20px 24px", background: "#06080F", opacity: "0.7", cursor: "default", transition: "all 0.2s" }}>
          <div style={{ display: "flex", justifyContent: "space-between", alignItems: "flex-start" }}>
            <div>
              <div style={{ fontSize: "10px", color: "#6B7280", letterSpacing: "2px", marginBottom: "6px" }}>P4 · Insurance & Underwri</div>
              <div style={{ fontWeight: 900, fontSize: "16px", color: "#9CA3AF", marginBottom: "4px" }}>InsureTarget</div>
              <div style={{ fontSize: "11px", color: "#6B7280" }}>Insurance M&A Target Feed</div>
            </div>
            <div style={{ textAlign: "right" }}>
              <div style={{ fontWeight: 900, fontSize: "16px", color: "#4B5563" }}>$5,000</div>
              <div style={{ fontSize: "9px", color: "#4B5563", letterSpacing: "1px" }}>PER MONTH</div>
              <div style={{ fontSize: '9px', color: '#4B5563', marginTop: '4px' }}>Phase 4</div>
            </div>
          </div>
        </a>

        <a href="#" style={{ textDecoration: "none", display: "block", border: "1px solid #1E2235", padding: "20px 24px", background: "#06080F", opacity: "0.7", cursor: "default", transition: "all 0.2s" }}>
          <div style={{ display: "flex", justifyContent: "space-between", alignItems: "flex-start" }}>
            <div>
              <div style={{ fontSize: "10px", color: "#6B7280", letterSpacing: "2px", marginBottom: "6px" }}>P4 · HR & Workforce Intel</div>
              <div style={{ fontWeight: 900, fontSize: "16px", color: "#9CA3AF", marginBottom: "4px" }}>ContractBench</div>
              <div style={{ fontSize: "11px", color: "#6B7280" }}>Employment Contract Benchmarks</div>
            </div>
            <div style={{ textAlign: "right" }}>
              <div style={{ fontWeight: 900, fontSize: "16px", color: "#4B5563" }}>$4,000</div>
              <div style={{ fontSize: "9px", color: "#4B5563", letterSpacing: "1px" }}>PER MONTH</div>
              <div style={{ fontSize: '9px', color: '#4B5563', marginTop: '4px' }}>Phase 4</div>
            </div>
          </div>
        </a>

        <a href="#" style={{ textDecoration: "none", display: "block", border: "1px solid #1E2235", padding: "20px 24px", background: "#06080F", opacity: "0.7", cursor: "default", transition: "all 0.2s" }}>
          <div style={{ display: "flex", justifyContent: "space-between", alignItems: "flex-start" }}>
            <div>
              <div style={{ fontSize: "10px", color: "#6B7280", letterSpacing: "2px", marginBottom: "6px" }}>P4 · Insurance & Underwri</div>
              <div style={{ fontWeight: 900, fontSize: "16px", color: "#9CA3AF", marginBottom: "4px" }}>DeedGuard</div>
              <div style={{ fontSize: "11px", color: "#6B7280" }}>Title & Deed Fraud Intelligence</div>
            </div>
            <div style={{ textAlign: "right" }}>
              <div style={{ fontWeight: 900, fontSize: "16px", color: "#4B5563" }}>$4,500</div>
              <div style={{ fontSize: "9px", color: "#4B5563", letterSpacing: "1px" }}>PER MONTH</div>
              <div style={{ fontSize: '9px', color: '#4B5563', marginTop: '4px' }}>Phase 4</div>
            </div>
          </div>
        </a>

        <a href="#" style={{ textDecoration: "none", display: "block", border: "1px solid #1E2235", padding: "20px 24px", background: "#06080F", opacity: "0.7", cursor: "default", transition: "all 0.2s" }}>
          <div style={{ display: "flex", justifyContent: "space-between", alignItems: "flex-start" }}>
            <div>
              <div style={{ fontSize: "10px", color: "#6B7280", letterSpacing: "2px", marginBottom: "6px" }}>P4 · HR & Workforce Intel</div>
              <div style={{ fontWeight: 900, fontSize: "16px", color: "#9CA3AF", marginBottom: "4px" }}>ComplianceRisk</div>
              <div style={{ fontSize: "11px", color: "#6B7280" }}>Multi-State Employer Compliance</div>
            </div>
            <div style={{ textAlign: "right" }}>
              <div style={{ fontWeight: 900, fontSize: "16px", color: "#4B5563" }}>$4,500</div>
              <div style={{ fontSize: "9px", color: "#4B5563", letterSpacing: "1px" }}>PER MONTH</div>
              <div style={{ fontSize: '9px', color: '#4B5563', marginTop: '4px' }}>Phase 4</div>
            </div>
          </div>
        </a>
        </div>
      </div>

      {/* Footer */}
      <div style={{ borderTop: "1px solid #1E2235", padding: "24px 48px", display: "flex", justifyContent: "space-between", alignItems: "center" }}>
        <div style={{ fontSize: "12px", color: "#4B5563" }}>© 2026 Huit Data Ventures · Powered by Huit.AI</div>
        <div style={{ fontSize: "12px", color: "#4B5563" }}>derek@huit.ai</div>
      </div>
    </div>
  );
}
