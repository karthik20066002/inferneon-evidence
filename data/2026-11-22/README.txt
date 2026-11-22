Records added 2026-11-22.

Board records (Measured on the board):

  cm4-lfm3-first-run.json   LFM3-1.7B on the Raspberry Pi CM4, its first board run: three fixed
                            prompts, 32 greedy tokens each; 0.584 s/token decode, first token
                            8.5-10.5 s; model loaded from SD with every byte checked
  cm4-lambda-engine-lfm3.json
                            the same three prompts with the Lambda Engine on the CM4: the engine
                            generated from LFM3's config.json, its tokenizer and chat template read
                            from the model's own files in the container; the same 32-token texts
                            and prompt token counts as the board engine, 0.578 s/token
  thinkcentre-lambda-engine-lfm3.json
                            the same container and prompts on the ThinkCentre (x86, booted from a
                            USB stick, no operating system): the same texts as the CM4,
                            0.111 s/token, first token 1.8-2.2 s
  thinkcentre-lambda-engine-lfm3-scalar.json
                            the ThinkCentre's first run with a scalar 8-bit kernel (1.47 s/token),
                            before the vector kernel; same texts

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
  lambda-engine-chat-templates.csv      chat templates read from each model's published files and
                                        rendered on many conversations (tools, tool calls, images,
                                        reasoning), against Hugging Face transformers: every
                                        character, errors included; and a feature corpus

Errors are the largest absolute difference divided by the reference's largest value.
