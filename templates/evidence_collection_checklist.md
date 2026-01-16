# Evidence Collection Checklist

> Goal: preserve evidence safely, support investigation, and maintain chain of custody.

---

## 1. Chain of Custody
- **Evidence ID:**  
- **Collected by:**  
- **Date/time collected:**  
- **Source system/user:**  
- **Storage location:** (secure drive / case folder)  
- **Hash recorded (if file evidence):**  

---

## 2. Critical Evidence to Collect (by Source)

### Email (Phishing/BEC)
- Full email content + screenshot
- **Email headers** (Message-ID, Received lines)
- Attachment(s) saved separately
- Malicious URL(s) copied exactly

### Identity / Authentication (Azure AD / Okta / Google)
- Successful/failed sign-ins
- MFA events + device/location info
- Password reset logs
- Token/session revocation logs

### Endpoint / EDR (Defender/CrowdStrike/SentinelOne)
- Alert details and process tree
- File execution and command-line arguments
- Quarantine actions taken
- Host isolation events

### Network (Firewall/DNS/Proxy)
- DNS queries to suspicious domains
- Proxy logs for URL visits
- Firewall traffic logs (inbound/outbound)
- Any unusual data transfers

### Servers / Applications
- Windows Event logs / Syslog
- Web server logs (access/error)
- Database access logs (if relevant)

---

## 3. IOC Documentation
Record in a single place:
- Domains/URLs
- IPs
- Hashes (SHA256 preferred)
- Filenames and paths
- User accounts involved

---

## 4. Notes / Reminders
- Collect evidence **before** re-imaging devices
- Do not open suspicious attachments on production machines
- Keep originals unchanged; work on copies when possible
