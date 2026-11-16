Board records, 2026-11-16 (all "Measured on the board" unless noted).

Generation runs: 3 fixed prompts x 32 greedy tokens each, streamed; text, time to first
token and median decode seconds per token. A later run passes if its text is identical
and its decode speed is within 3% (or faster).

  cm4-attis-reference.json                  Raspberry Pi CM4, reference firmware
  cm4-attis-platform.json                   CM4, platform firmware (memory-safety layer)
  thinkcentre-attis-reference.json          ThinkCentre M710q, reference firmware
  thinkcentre-attis-platform.json           ThinkCentre, platform firmware
  thinkcentre-attis-platform-verified.json  ThinkCentre, platform firmware after verification fixes
  thinkcentre-attis-kernel-update.json      ThinkCentre, kernel update

Kernel benchmarks on the ThinkCentre (on-board, synthetic weights at the model's layer
shapes; every configuration's output checked bit-identical to the single-thread run):

  thinkcentre-kernel-bench-1-baseline.json
  thinkcentre-kernel-bench-2-prefetch.json
  thinkcentre-kernel-bench-3-packed-layout.json   (kernel not yet used by the generation runs)

  thinkcentre-hardware-memory.json          memory configuration and measured read bandwidth

Added later on 2026-11-16 (all measured on the boards):

  thinkcentre-attis-compiled-engine.json  ThinkCentre, the compiled engine with target parameters
                                          chosen by the board's own sweep: same text, 0.52 s/token
  two-board-layer-split.json              ThinkCentre + CM4 running one model together (layers split
                                          between the boards): same text as one board
  two-board-row-parallel.json             ThinkCentre + CM4 computing every matrix together over raw
                                          Ethernet: known-answer check identical bit for bit; link
                                          round trip and per-exchange times
  cm4-kernel-bench-1-before.json          CM4 kernel benchmark before the load fix
  cm4-kernel-bench-2-after-load-fix.json  CM4 kernel benchmark after it (2.5x, at the memory limit)
