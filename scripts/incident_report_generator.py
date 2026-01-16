from datetime import datetime
import os

TEMPLATE = """# Incident Report

## 1. Incident Summary
- Incident ID: {incident_id}
- Date/Time Detected: {detected_time}
- Reported By: {reported_by}
- Incident Type: {incident_type}
- Severity: {severity}

## 2. Scope & Impact
- Systems affected: {systems}
- Users affected: {users}
- Business impact: {impact}
- Data exposure risk: {data_risk}

## 3. Timeline
| Time | Event |
|------|-------|
{timeline}

## 4. Indicators of Compromise (IOCs)
- Domains: {domains}
- IP Addresses: {ips}
- File Hashes: {hashes}

## 5. Actions Taken
- Containment: {containment}
- Eradication: {eradication}
- Recovery: {recovery}

## 6. Root Cause Analysis
- Root cause: {root_cause}
- Contributing factors: {contributing_factors}

## 7. Lessons Learned / Recommendations
{recommendations}
"""


def prompt_list(label):
    items = input(f"{label} (comma-separated or leave blank): ").strip()
    return items if items else "N/A"


def main():
    print("=== Incident Report Generator ===")

    incident_id = input("Incident ID (e.g. IR-2026-001): ").strip()
    reported_by = input("Reported by: ").strip()
    incident_type = input("Incident type (Phishing/Ransomware/BEC/etc): ").strip()
    severity = input("Severity (Low/Medium/High/Critical): ").strip()

    systems = prompt_list("Systems affected")
    users = prompt_list("Users affected")
    impact = input("Business impact (short): ").strip() or "N/A"
    data_risk = input("Data exposure risk (short): ").strip() or "N/A"

    print("\nTimeline: enter events. Type 'done' to finish.")
    timeline_rows = []
    while True:
        t = input("Time (e.g. 10:35 AM or 2026-01-14 10:35): ").strip()
        if t.lower() == "done":
            break
        e = input("Event description: ").strip()
        timeline_rows.append(f"| {t} | {e} |")

    timeline = "\n".join(timeline_rows) if timeline_rows else "| N/A | N/A |"

    domains = prompt_list("IOC domains")
    ips = prompt_list("IOC IP addresses")
    hashes = prompt_list("IOC file hashes")

    containment = input("Containment actions: ").strip() or "N/A"
    eradication = input("Eradication actions: ").strip() or "N/A"
    recovery = input("Recovery actions: ").strip() or "N/A"

    root_cause = input("Root cause: ").strip() or "N/A"
    contributing_factors = input("Contributing factors: ").strip() or "N/A"

    recommendations = input("Lessons learned / recommendations: ").strip() or "- N/A"

    detected_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    content = TEMPLATE.format(
        incident_id=incident_id,
        detected_time=detected_time,
        reported_by=reported_by,
        incident_type=incident_type,
        severity=severity,
        systems=systems,
        users=users,
        impact=impact,
        data_risk=data_risk,
        timeline=timeline,
        domains=domains,
        ips=ips,
        hashes=hashes,
        containment=containment,
        eradication=eradication,
        recovery=recovery,
        root_cause=root_cause,
        contributing_factors=contributing_factors,
        recommendations=recommendations
    )

    os.makedirs("reports", exist_ok=True)
    filename = f"reports/{incident_id}_incident_report.md".replace(" ", "_")

    with open(filename, "w", encoding="utf-8") as f:
        f.write(content)

    print(f"\n✅ Report generated: {filename}")


if __name__ == "__main__":
    main()
