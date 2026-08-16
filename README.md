# Hi, I'm Labeeb

<img
  align="right"
  src="./assets/espeon-loop.gif"
  alt="Animated pixel-art Espeon"
  width="170"
/>

I'm a student in Sarawak, Malaysia. I like cybersecurity, local AI, and
digital hardware. Most of my projects start because I want to understand
how something works — so I build it from first principles, benchmark it
against the real thing, and write down what the result does *not* prove.

[LinkedIn](https://www.linkedin.com/in/muhammad-labeeb-aryan-bin-mohd-lokman-369211300/)
&nbsp;&middot;&nbsp;
[All repositories](https://github.com/Labeeb2339?tab=repositories)

<br clear="right" />

## Projects I'd show first

- **[RecurQuant](https://github.com/Labeeb2339/recurquant)** — Qwen3.5
  recurrent-state quantization with packed-state measurements and a frozen
  500-task held-out fidelity result.
- **[From-scratch ML systems](https://github.com/Labeeb2339/pico-kernels)** —
  Triton/CUDA kernels built from first principles, benchmarked against cuBLAS
  and torch:
  - fp8 GEMM **2.14×** cuBLAS fp16 @4096² · FlashAttention fwd+bwd **3.7–6.9×**
    · grouped-query attention **34–38×** · GPTQ 4-bit **+0.013 ppl** (RTN +0.088)
  - [PicoDiffusion](https://github.com/Labeeb2339/pico-diffusion) — DDPM/DDIM
    from scratch; CIFAR-10 FID **53.23 → 39.44** (class-conditioned); a
    DPM-Solver++ failure case and a latent-diffusion bug-fix, both documented.
  - [PicoLM](https://github.com/Labeeb2339/picolm) — a GPT from scratch: RoPE,
    RMSNorm, flash attention, BPE, and a from-scratch HellaSwag harness.
  - [PicoEngine](https://github.com/Labeeb2339/pico-engine) — a from-scratch
    GGUF inference engine (GGML dequant + LLaMA forward + BPE) that runs
    Qwen2.5-0.5B, dequantized bit-exact and benchmarked against llama.cpp.
- **[ScamShield](https://github.com/Labeeb2339/scamshield-case-study)** — a
  Flutter prototype for the Young Innovators Challenge 2026 that explains
  Malaysian scam-risk signals.
- **[CyberRAG](https://github.com/Labeeb2339/cyber-rag)** — local cybersecurity
  retrieval: hybrid search + cross-encoder rerank (MRR **+18%**), full IR
  metrics, MITRE ATT&CK grounding.
- **[PortCVE](https://github.com/Labeeb2339/PortCVE)** — a Windows CLI for
  finding listening ports, their owners, exposure changes, and possible CVE
  matches.
- **[INT8 dot-product RTL](https://github.com/Labeeb2339/int8-dot-product-rtl)** —
  a signed-INT8 SystemVerilog compute core with a Python reference model and CI.

Some experiments worked. Some failed. I keep the useful failure cases with
their measurements instead of turning every result into a success story.

## Right now

I'm working through quantization (GPTQ, W4A16, recurrent-state), RAG
evaluation, and diffusion samplers, and learning Windows/.NET and SystemVerilog
along the way. Everything above is tested and benchmarked against a reference;
if I can't show how a number was produced, it doesn't go here.
