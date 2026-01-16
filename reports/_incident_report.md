# Incident Report (Sample)

## 1. Incident Summary
- **Incident ID:** IR-2026-001
- **Date/Time Detected:** 2026-01-15 20:35
- **Reported By:** Helpdesk
- **Incident Type:** Phishing
- **Severity:** High
- **Status:** Contained

## 2. Scope & Impact
- **Affected Systems/Assets:** Microsoft 365 user mailbox
- **Affected Users:** 1 (targeted user)
- **Business Impact:** Credential exposure risk, attempted account takeover
- **Data Exposure Risk:** Suspected (credentials entered on fake login page)

## 3. Timeline of Events
| Time | Event |
|---|---|
| 20:35 | User reported suspicious email asking to “verify password” |
| 20:40 | SOC validated phishing URL and identified lookalike domain |
| 20:45 | Account sessions revoked + password reset enforced |
| 20:50 | Similar emails searched and removed from mailboxes |

## 4. Indicators of Compromise (IOCs)
- **Domains/URLs:** login-verification-example[.]com
- **IP Addresses:** N/A
- **File Hashes:** N/A

## 5. Actions Taken
- **Containment:** Blocked sender + removed emails + revoked sessions
- **Eradication:** Blocked domain at DNS/web filter
- **Recovery:** MFA enforced, monitored sign-ins for 72 hours

## 6. Root Cause Analysis
- **Root cause:** User interacted with a spoofed login page
- **Contributing factors:** Social engineering + lookalike domain

## 7. Lessons Learned / Recommendations
- Strengthen phishing training for staff
- Expand email filtering rules
- Enforce MFA for all users
