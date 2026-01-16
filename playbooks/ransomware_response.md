# Ransomware Incident Response Playbook

## Objective
Contain ransomware activity, prevent spread, preserve evidence, restore business services safely, and reduce repeat exposure.

---

## 1. Identification / Detection
### Common Indicators
- Files encrypted / extensions changed
- Ransom note dropped on endpoints
- Unusual CPU/disk spikes
- Sudden inability to access shared drives
- EDR alerts showing suspicious process behavior

### Key Questions
- When did encryption begin?
- Which systems are affected?
- Is the ransomware still actively spreading?
- What business functions are impacted?

---

## 2. Containment (Immediate Actions)
### Isolation
- Disconnect infected endpoints from network (Wi-Fi + Ethernet)
- Disable SMB/file share access temporarily (if needed)
- Block suspicious IPs/domains in firewall/DNS

### Access Control
- Disable compromised accounts
- Reset privileged credentials (Admin accounts)
- Rotate service account passwords if compromised

---

## 3. Evidence Preservation
Collect evidence BEFORE wiping systems:
- Ransom note file(s)
- File hashes of suspicious binaries
- EDR telemetry
- Authentication logs
- Network traffic logs
- Timeline of events

---

## 4. Eradication
- Remove persistence mechanisms
- Delete malicious binaries (after evidence collection)
- Patch exploited vulnerabilities (VPN, RDP, email, OS, apps)
- Run full endpoint scans and confirm clean state

---

## 5. Recovery
- Restore from backups (only after verifying backups are not infected)
- Prioritize critical systems first
- Validate restored systems using:
  - vulnerability scanning
  - EDR monitoring
  - IOC scanning

---

## 6. Communications
- Internal notification (IT, leadership, legal)
- External notification if required (customers/vendors/regulators)
- Law enforcement engagement if needed

---

## 7. Lessons Learned / Improvements
- Improve backup strategy (offline + immutable)
- Implement network segmentation
- Enforce MFA everywhere
- Monitor privileged account usage
- Tighten email filtering and endpoint controls
