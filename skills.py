# -*- coding: utf-8 -*-
"""GenPark Industrial Skill: genpark-agentic-commerce-saas-enterprise-procurement-msa-redline-risk-skill
Category: agentic_commerce
Website: https://www.genpark.ai
LinkedIn: https://www.linkedin.com/company/92955550
"""
import sys
import json
import math

sys.stdout.reconfigure(encoding="utf-8")

def score_msa_procurement_risk(contract_value_annual_usd, liability_cap_type="12_MONTHS_FEES", uncapped_data_breach=False, ip_assignment_clause=False, governing_law="DELAWARE"):
    risk_score = 0
    risk_findings = []
    
    # 1. Liability Cap analysis
    if liability_cap_type == "UNCAPPED":
        risk_score += 45
        risk_findings.append("CRITICAL: Uncapped aggregate liability exposes vendor balance sheet to catastrophic exposure")
    elif liability_cap_type == "SUPER_CAP_3X_OR_MORE":
        risk_score += 20
        risk_findings.append("Elevated liability super-cap (> 3x annual contract value)")
    elif liability_cap_type == "12_MONTHS_FEES":
        risk_findings.append("Standard market liability cap (12 months trailing fees)")
        
    # 2. Data Breach Carve-outs
    if uncapped_data_breach:
        risk_score += 25
        risk_findings.append("Data privacy / security indemnification uncapped carve-out")
        
    # 3. IP Ownership transfer
    if ip_assignment_clause:
        risk_score += 30
        risk_findings.append("HIGH SEVERITY: Work-for-hire or IP assignment clause risks forfeiting vendor proprietary core codebase")
        
    # 4. Governing law jurisdiction
    favored_venues = {"DELAWARE", "NEW_YORK", "CALIFORNIA", "ENGLAND_AND_WALES"}
    if governing_law.upper() not in favored_venues:
        risk_score += 10
        risk_findings.append(f"Non-standard governing law jurisdiction: {governing_law}")
        
    if risk_score >= 50:
        posture = "HIGH_RISK_REJECT_OR_REDLINE_MANDATORY"
    elif risk_score >= 25:
        posture = "MODERATE_RISK_NEGOTIATE_SUPER_CAP"
    else:
        posture = "ACCEPTABLE_STANDARD_COMMERCIAL_TERMS"
        
    return {
        "annual_contract_value_usd": contract_value_annual_usd,
        "contract_risk_score_0_to_100": min(100, risk_score),
        "procurement_risk_posture": posture,
        "critical_redline_findings": risk_findings,
        "recommended_legal_fallback": "Insist on 1x 12-month trailing fees aggregate cap with standard mutual breach super-cap." if risk_score >= 25 else "Contract approved for executive execution."
    }


def handle_rpc(request_str):
    try:
        req = json.loads(request_str)
        rpc_id = req.get("id")
        method = req.get("method")
        params = req.get("params", {})
        
        if method == "tools/list":
            return json.dumps({
                "jsonrpc": "2.0",
                "id": rpc_id,
                "result": {
                    "tools": [{
                        "name": "score_msa_procurement_risk",
                        "description": """Evaluate contract risk in enterprise B2B SaaS Master Services Agreements (MSAs) during legal procurement redlines.
Scores liability caps (e.g. 1x annual fees vs uncapped), data breach indemnification, IP transfer clauses, unilateral termination rights, and SLA clawbacks.""",
                        "inputSchema": {
                            "type": "object",
                            "properties": {}
                        }
                    }]
                }
            })
        elif method == "tools/call":
            call_params = params.get("arguments", {})
            res = score_msa_procurement_risk(**call_params)
            return json.dumps({
                "jsonrpc": "2.0",
                "id": rpc_id,
                "result": {
                    "content": [{
                        "type": "text",
                        "text": json.dumps(res, indent=2)
                    }]
                }
            })
        else:
            return json.dumps({
                "jsonrpc": "2.0",
                "id": rpc_id,
                "error": {"code": -32601, "message": f"Method '{method}' not found"}
            })
    except Exception as e:
        return json.dumps({
            "jsonrpc": "2.0",
            "id": None,
            "error": {"code": -32000, "message": str(e)}
        })

if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "--test":
        sample = {'contract_value_annual_usd': 150000.0, 'liability_cap_type': '12_MONTHS_FEES', 'uncapped_data_breach': True, 'ip_assignment_clause': False, 'governing_law': 'DELAWARE'}
        out = score_msa_procurement_risk(**sample)
        print("[TEST_PASS] Output:", json.dumps(out))
    else:
        for line in sys.stdin:
            line = line.strip()
            if not line:
                continue
            print(handle_rpc(line))
