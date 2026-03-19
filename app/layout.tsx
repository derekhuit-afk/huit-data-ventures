import type { Metadata } from "next";
import "./globals.css";
import AgentWidget from '@/components/AgentWidget';

export const metadata: Metadata = {
  title: "Huit Data Ventures — 25 Enterprise Intelligence Products",
  description: "A portfolio of enterprise-grade DaaS products covering Insurance, Legal, CRE, and HR & Workforce Intelligence.",
};

export default function RootLayout({ children }: { children: React.ReactNode }) {
  return (
    <html lang="en">
      <body style={{ background: "#050810", color: "#E8EAF0", fontFamily: "monospace", margin: 0 }}>
        {children}
            <AgentWidget />
    </body>
    </html>
  );
}
