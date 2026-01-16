# Phishing Incident Response Playbook

## Objective
Detect, contain, and remediate phishing attempts to prevent credential theft and account compromise.

---

## 1. Identification
### Indicators
- Suspicious sender domain
- Unexpected attachments or links
- User reports unusual login prompts
- MFA push fatigue alerts

---

## 2. Triage Questions
- Who received the email?
- Was the link clicked/attachment opened?
- Were credentials entered?
- Any suspicious logins after delivery?

---

## 3. Containment
- Block sender domain
- Quarantine similar messages
- Remove email from all inboxes
- Reset compromised credentials + revoke sessions

---

## 4. Eradication
- Block malicious URLs/domains on DNS/Web gateway
- Add IOCs to SIEM/EDR detections

---

## 5. Recovery
- Confirm MFA enabled
- Monitor sign-in logs for 24–72 hours

---

## 6. Lessons Learned
- Improve awareness training
- Strengthen email security controls (SPF/DKIM/DMARC)
