# Incident Response Playbook 

A practical **Incident Response (IR) toolkit** containing:
- Standard **incident response playbooks**
- Evidence collection + incident documentation **templates**
- A Python **Incident Report Generator** for fast, consistent reporting

This repository is designed to reflect real SOC/IR workflows using the standard IR lifecycle:

**Preparation → Detection & Analysis → Containment → Eradication → Recovery → Lessons Learned**

---

##  What’s Included

###  Playbooks
These playbooks provide step-by-step response procedures:

- **Phishing Response** → `playbooks/phishing_response.md`
- **Ransomware Response** → `playbooks/ransomware_response.md`
- **Business Email Compromise (BEC)** → `playbooks/business_email_compromise.md`

---

###  Templates
Use these templates to standardize response documentation:

- **Incident Report Template** → `templates/incident_report_template.md`
- **Evidence Collection Checklist** → `templates/evidence_collection_checklist.md`

---

###  Automation Tooling (Python)
This toolkit includes a lightweight script for automatically generating incident reports in Markdown format:

- **Incident Report Generator** → `scripts/incident_report_generator.py`

Output reports are saved to:
- `reports/`

---

##  Repository Structure

```bash
incident-response-playbook/
│── README.md
│── playbooks/
│   ├── phishing_response.md
│   ├── ransomware_response.md
│   └── business_email_compromise.md
│── templates/
│   ├── incident_report_template.md
│   └── evidence_collection_checklist.md
│── scripts/
│   └── incident_report_generator.py
│── reports/
│   └── _incident_report.md
│── sample-logs/
│   └── (optional training logs)
