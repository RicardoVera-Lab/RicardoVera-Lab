# SIPER-AGRO | Verification scope and provenance

This technical note defines **what can be independently verified from the public repository** and keeps the executive narrative separate from claims that require further source records.

## Public-case provenance

- **Nature of the case:** controlled portfolio demonstration using synthetic operational records. It is not a real-customer or paid-consulting engagement.
- **Private reference:** G10F example package with six XLSX input categories, explicit relationship contract, computed results and a restricted report. Private source package and local application are not published.
- **Case record date:** 2026-11-12. Example period: 2026-02-01 inclusive to 2026-03-01 exclusive.
- **Documentary preflight recorded:** `CALCULATED`, 0 reported intake issues; coverage of linked records: 6/6 for inventory, 5/5 for settlements, 5/5 for logistics and 4/4 for price comparisons.
- **Published differences:** stock -2 TN; settlement -500 ARS (plus another 0 ARS comparison); logistics +200 ARS (plus 0 ARS comparison); two price pairs -10 and +5 ARS/TN.

## What is independently reproducible here

The public `data/synthetic_transactions.csv` is a reduced numerical example derived from that controlled case. `src/reproduce.py` independently reconstructs **seven specific comparisons** using explicit relationship IDs, units and `decimal.Decimal`. The nine unit tests cover calculations and negative controls. GitHub Actions runs this public test set across Python 3.10, 3.12 and 3.13.

**Scope boundary:** the public script is not the SIPER-AGRO private ingestion engine, PDF renderer, backup subsystem, application security or domain-risk model. Its successful tests substantiate the published numerical example and its input-checking rules.

## Application validation reported

During local Windows testing, the owner reported a `WINDOWS_PASS_CANDIDATE` result for W7 integration with the application manifest, external manifest and Windows gate marked PASS. The full W7 gate log bundle has not been attached to this public case; the console result is reported as such rather than described as an independent audit or certification.

## Analytical boundaries

A documentary difference identifies a **review question**. It does not by itself measure commercial loss, fraud, liability or a validated causal mechanism. Legacy IRO, 12 KRIs, MCC and PFO-Lite calculations have not been mapped and validated against G10F documentary inputs in this public case. The reference implementation also identified 41 outstanding sector-domain decisions requiring authorized resolution before the broader commercial workflow can be claimed as fully approved.

No private system code, credentials, company identities, client datasets or restricted ZIPs are included. Future customer projects require explicit permission and data governance before any evidence is used publicly.

[Case overview](../README.md) · [Management brief](DECISION_BRIEF_ES.md)
