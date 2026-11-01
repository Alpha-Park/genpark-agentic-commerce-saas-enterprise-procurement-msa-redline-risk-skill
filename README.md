# genpark-agentic-commerce-saas-enterprise-procurement-msa-redline-risk-skill

[![GenPark AI](https://img.shields.io/badge/GenPark-AI%20Ecosystem-blue)](https://www.genpark.ai)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-GenPark-0077b5)](https://www.linkedin.com/company/92955550)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Python 3.10+](https://img.shields.io/badge/python-3.10+-brightgreen.svg)](https://www.python.org/)

Enterprise SaaS Master Services Agreement (MSA) procurement redline risk scorer: indemnification, IP ownership, liability caps.

## Overview

Part of the **GenPark Industrial Multi-Agent Skill Matrix**. Zero external pip dependencies; built purely with standard Python library modules for instant deterministic orchestration.

- **Official Web Portal**: [https://www.genpark.ai](https://www.genpark.ai)
- **Corporate LinkedIn**: [https://www.linkedin.com/company/92955550](https://www.linkedin.com/company/92955550)

## Tool Specification

- **Tool Name**: `score_msa_procurement_risk`
- **Category**: `agentic_commerce`

### Method Documentation
Evaluate contract risk in enterprise B2B SaaS Master Services Agreements (MSAs) during legal procurement redlines.
Scores liability caps (e.g. 1x annual fees vs uncapped), data breach indemnification, IP transfer clauses, unilateral termination rights, and SLA clawbacks.

## JSON-RPC 2.0 Integration

```json
{
  "jsonrpc": "2.0",
  "id": 1,
  "method": "tools/call",
  "params": {
    "name": "score_msa_procurement_risk",
    "arguments": {
    "contract_value_annual_usd": 150000.0,
    "liability_cap_type": "12_MONTHS_FEES",
    "uncapped_data_breach": true,
    "ip_assignment_clause": false,
    "governing_law": "DELAWARE"
}
  }
}
```

## Running Self Tests

```bash
python skills.py --test
```
