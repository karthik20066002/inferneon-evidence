Records added 2026-11-20.

Board records, 2026-11-16 (later) to 2026-11-18 (all "Measured on the board"):

  thinkcentre-long-prompt-1-reference-engine.json   Attis on the ThinkCentre, a 3076-token prompt
  thinkcentre-long-prompt-2-compiled-engine.json    the same prompt on the compiled engine: same text
  thinkcentre-long-prompt-3-parallel-attention.json the compiled engine with attention heads on 4
                                                    cores: same text, 972 s against 1189 s
  thinkcentre-attis-dual-channel-memory.json        ThinkCentre with a second memory module
                                                    (dual-channel): same text, 0.344 s/token decode
                                                    (before: 0.515)
  two-board-link-settings-sweep.json                ThinkCentre + CM4: link window and retransmit
                                                    settings, with link counters
  two-board-row-parallel-splits.json                row-parallel work splits between the boards
  two-board-row-parallel-gigabit.json               row parallel with both ports at gigabit
  two-board-row-parallel-gigabit-switch.json        row parallel through a gigabit switch
  thinkcentre-native-network-driver.json            the firmware's own network driver in place of
                                                    the UEFI one: per-frame send 1.55 us against
                                                    36.7 us
  thinkcentre-integrated-gpu-first-light.json       first command executed by the integrated GPU
                                                    under the firmware (a value written and read back)

The Lambda Engine's model verification ("Measured off-board", on a laptop). The Lambda Engine
reads a model's published configuration and is checked against the Hugging Face transformers
library (f32):

  lambda-engine-tier1-real-weights.csv  20 published checkpoints on their real weights: every
                                        layer's hidden states and the output scores within 1e-4
                                        relative, the same next token at every position; and
                                        Gemma 3 4B's vision tower alone (image features)
  lambda-engine-tier2-tiny-models.csv   46 architecture families and 3 vision-language paths on
                                        small random models built from the published
                                        configurations (within 5e-5 relative)
  lambda-engine-smolvla.csv             SmolVLA (vision-language-action) against LeRobot's own
                                        code, on a small random policy and on the published
                                        policy's real weights

Errors are the largest absolute difference divided by the reference's largest value.
