# InferNEON evidence kit (2026-11-13, updated 2026-11-22)

Evidence for the Moeify / InferNEON work: language models on a Raspberry Pi Compute Module 4 and a 2017 office PC with no operating
system, and the Lambda Engine that builds each model's engine from its published files.

**Start with [`START_HERE.html`](START_HERE.html)** (open it in a browser). It walks through the
claims, the measurements behind each one, and where every number comes from.

| File | Contents |
|---|---|
| `START_HERE.html` | The presentation page |
| `FACT_SHEET.txt`, `EVALUATION_NOTES.txt`, `README.txt` | Plain-text summary, evaluation notes and kit guide |
| `claims.csv` | Every claim with its status (measured on the board, measured off-board, secondary record, not yet measured) and its sources |
| `sources/` | The source excerpts (S01–S22) the claims cite, with `SOURCE_INDEX.csv` |
| `data/` | The measured data behind the figures |
| `data/2026-11-16`, `2026-11-20`, `2026-11-22`, `2026-11-23` | Later board records, the Lambda Engine's verification and a llama.cpp reference run, each folder with its own README |
| `figures/` | Figures as PNG and SVG; `reproduce_figures.py` regenerates them from `data/` |
| `SHA256SUMS` | Checksums of every file above |

## Verify the files

```sh
sha256sum -c SHA256SUMS
```

Every file listed must report `OK`. The kit was checked before release against the original
records it was excerpted from. That check is not an independent audit.
