# Business Email Compromise (BEC) Incident Response Playbook

## Objective
Respond quickly to email takeover and prevent fraud, data leakage, and unauthorized transfers.

---

## 1. Identification
### Common Indicators
- Unusual email forwarding rules created
- Login from suspicious location/device
- Unauthorized password reset attempts
- Vendor requests for payment details changes

---

## 2. Containment
- Immediately reset the compromised account password
- Revoke active sessions and tokens
- Enable/force MFA
- Disable suspicious inbox rules and forwarding

---

## 3. Investigation
- Review authentication logs (successful/failed logins)
- Identify IPs, location, device fingerprints
- Search for:
  - forwarding rules
  - sent messages
  - deleted emails

---

## 4. Financial Protection
- Verify if any fraudulent payments occurred
- Contact bank/payment provider immediately if funds were transferred
- Notify finance department to pause payments if necessary

---

## 5. Recovery
- Confirm account security controls:
  - MFA enabled
  - trusted devices reviewed
  - recovery email/phone verified

---

## 6. Lessons Learned
- Strengthen MFA enforcement
- Security awareness training (finance + exec teams)
- Email protections (DMARC/SPF/DKIM)
- Monitor for rule creation alerts
