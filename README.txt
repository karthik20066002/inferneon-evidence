Research evidence kit — snapshot 2026-11-13, updated 2026-11-22

Open START_HERE.html (a standalone page: no network needed) to present or read the evidence.
FACT_SHEET.txt is the plain-text version. Read EVALUATION_NOTES.txt before quoting numbers.

Contents:
- claims.csv: every result, its status (measured on the CM4, on the ThinkCentre, on two boards, on the laptop, secondary, not yet measured),
  source IDs and its limits. The page and fact sheet are generated from this table.
- data/: sanitized numeric observations, including data/cm4_generation_runs.csv (all CM4 generation runs cited).
- sources/: sanitized project records S01–S21, SOURCE_INDEX.csv and public references.
- figures/: standalone PNG and SVG figures; reproduce_figures.py regenerates them from data/ only.
- SHA256SUMS: hashes of every file in this folder. Check with: sha256sum -c SHA256SUMS

What changed since 2026-11-04: sources S12–S17 and claims C12–C19 add the longer CM4 answers of the 27B model,
two further models running on the CM4 (Gemma 3 1B and Gemma 3n E4B) with reference-text checks, an NVMe boot,
and laptop conformance checks for LFM3-1.7B.

What changed since 2026-11-13: data/2026-11-16, 2026-11-20 and 2026-11-22 add board records, and
sources S18–S21 and claims C20–C26 summarise them: Attis on a 2017 ThinkCentre office PC with no operating system, one
model served by the ThinkCentre and the CM4 together, the Lambda Engine's verification against reference code,
and LFM3-1.7B measured on the CM4 (C18) and served with identical answers on both machines from one container.

Only this SHAREABLE folder is intended for disclosure. The private provenance mapping is not included. The archive
contains no research implementation, method documents, training configuration, model weights, private
correspondence, credentials or contacts. Limitations are marked on every claim.

This is an AI-assisted evidence-organizing artifact, not an EV application. EV's instructions permit AI only for
proofreading and prohibit PDF attachments; check the live form before attaching anything. Write the application in
your own words.
