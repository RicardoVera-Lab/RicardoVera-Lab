# Evidence & limits — SIPER-AGRO synthetic case

**Source of the example:** A user-supplied private G10F synthetic-case ZIP (`SYNTHETIC_CONTROLLED`), with six XLSX source workbooks, a relationship contract, a result JSON, preflight results and a public-style anonymized report. The original ZIP explicitly designated itself private; it has **not** been uploaded to this repository. This case reconstructs only seven non-sensitive arithmetic comparisons from the synthetic fixture.

**Case recorded:** 2026-11-12. Case period: 2026-02-01 inclusive through 2026-03-01 exclusive. Ingestion preflight state `CALCULATED`, issue count 0, company data synthetic, economic authority `NONE`; 41 domain decisions open and commercial release `HOLD` in the source fixture. Document coverage counts (6/6, 5/5, 5/5, 4/4) refer to linked input rows **within the synthetic fixture**, not to sector validation.

**Public reconstruction:** `data/synthetic_transactions.csv` is a deliberately reduced, human-readable teaching fixture derived from the numerical values and explicit relation IDs of that synthetic case. The Python code in `src/reproduce.py` is new stand-alone arithmetic, using `decimal.Decimal` and the standard library. It is not private production code and does not exercise full XLSX ingestion, security or report generation. Running `python -m unittest discover -s tests -v` tests its arithmetic and negative controls only.

**Windows W7 evidence:** The owner posted a `WINDOWS_PASS_CANDIDATE` console result for the W7 integration with app-manifest, package-manifest and Windows gate marked PASS. The W7-native log folder was not attached to this public case, and no third-party or live-client homologation has been conducted here. The newer executive interpretation is a **documentary management reading**, not a replacement for the historical enterprise risk model.

**No claims of:** real acopio customers, production deployment, predictive risk calibration, IRO/KRI recomputation from G10F, profit/loss quantification, fraud detection, certified audit, official accounting, security certification or guaranteed business outcomes. These require additional evidence and approvals.

**Privacy boundary:** No private ZIP, company source files, encrypted backup, token, installation script, manifest, raw local file path or internal algorithm is included. All public figures represent synthetic values.
