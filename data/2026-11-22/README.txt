Records added 2026-11-22.

Board record (Measured on the board):

  cm4-lfm3-first-run.json   LFM3-1.7B on the Raspberry Pi CM4, its first board run: three fixed
                            prompts, 32 greedy tokens each; 0.584 s/token decode, first token
                            8.5-10.5 s; model loaded from SD with every byte checked

The Lambda Engine ("Measured off-board", on a laptop):

  lambda-engine-tier1-real-weights.csv  20 published checkpoints on their real weights, matched to
                                        Hugging Face transformers (f32) in every layer within 1e-4
                                        relative, the same next token at every position; and
                                        Gemma 3 4B's vision tower alone
  lambda-engine-tier2-tiny-models.csv   47 architecture families and 3 vision-language paths on
                                        small random models built from the published
                                        configurations (within 5e-5 relative), including
                                        Thinking Machines' Inkling 2 Mini (released 2026-11-20)
  lambda-engine-smolvla.csv             SmolVLA (vision-language-action) against LeRobot's own code
  lambda-engine-generated-engines.csv   engines generated from each model's config.json, weights
                                        packed from its Hugging Face checkpoint, against the
                                        hand-written board engines: every layer at every position
                                        and the logits, bit for bit
  lambda-engine-tokenizers.csv          tokenizers read from each model's published tokenizer.json,
                                        against the Hugging Face tokenizers library

Errors are the largest absolute difference divided by the reference's largest value.
