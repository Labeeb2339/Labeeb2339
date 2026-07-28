<img
  align="right"
  src="./assets/espeon-loop.gif"
  alt="Animated pixel-art Espeon"
  width="185"
/>

# Muhammad Labeeb Aryan

Form 3 student in Sarawak, Malaysia.

I build inspectable systems across AI inference and quantization, fine-tuning
reliability, RAG, secure software, and RTL/digital design. I care about measured
evidence, reproducible tests, and clear limits.

[LinkedIn](https://www.linkedin.com/in/muhammad-labeeb-aryan-bin-mohd-lokman-369211300/)
&nbsp;&middot;&nbsp;
[Repositories](https://github.com/Labeeb2339?tab=repositories)

<br clear="right" />

## Flagship work

| Project | Focus | Evidence |
| --- | --- | --- |
| **[CliffQuant](https://github.com/Labeeb2339/cliffquant)** ([model](https://huggingface.co/labeebaryan/Qwen3.5-0.8B-Base-CliffQuant-W4A16-G128)) | Quantization and inference | Exact minimax FP16 scale selection for multi-environment W4A16 quantization. On frozen Qwen3.5-0.8B held-out windows, the validated checkpoint lowered macro NLL by 0.0548 versus uniform AbsMax. |
| **[RecurQuant](https://github.com/Labeeb2339/recurquant)** | Recurrent-state quantization | A physically packed INT8/INT4 policy used 2,564,096 resident bytes and reduced macro excess NLL by 72.75% versus uniform INT4 on a frozen 500-task MBPP confirmation. |
| **[SFTGuard](https://github.com/Labeeb2339/sftguard)** | Fine-tuning reliability | Fail-closed dataset, mask-evidence, and paired regression gates; the sealed synthetic suite found all 270 required fault signals with 0/30 clean-control false positives. |
| **[CyberRAG](https://github.com/Labeeb2339/cyber-rag)** | RAG and evaluation | Local threat-intelligence retrieval with hybrid search, ATT&CK grounding, citations, and a fixed 15-question paired evaluation harness. |
| **[Edge AI RTL Lab](https://github.com/Labeeb2339/edge-ai-rtl-lab)** | RTL and digital design | A signed INT8 SystemVerilog compute core checked across 369 deterministic transactions against a bit-exact Python model and Yosys synthesis. |
| **[StrataMoE Lab](https://github.com/Labeeb2339/stratamoe-lab)** | AI systems research | A deterministic GPU/RAM/NVMe placement harness with provenance-bearing traces, including an honest captured benchmark where the preregistered policy missed its traffic gate. |

More builds:
[ScamShield AI](https://github.com/Labeeb2339/scamshield-ai-case-study),
[DataTrust Gate](https://github.com/Labeeb2339/data-trust-gate),
[Shark Habitat Prototype](https://github.com/Labeeb2339/shark-habitat-prototype),
[Local Evidence MCP](https://github.com/Labeeb2339/local-evidence-mcp), and
[CustodianMesh AI](https://github.com/Labeeb2339/custodian-mesh-ai).

## How I work

`scope the claim -> build -> test -> publish the evidence -> name the limits`

These are student-built prototypes and small research evaluations, not
production deployments or silicon results.

**Working with:** Python, PyTorch, LLM quantization, FastAPI, TypeScript,
Dart/Flutter, RAG evaluation, MCP, SystemVerilog, Yosys, and GitHub Actions.

I welcome technical feedback, mentorship, job shadowing, student programmes,
and small supervised collaborations.

<sub>
The LABEEB + Espeon contribution pattern is intentional contribution art, not
a record of development activity. Sprite source and attribution are documented
in <a href="./assets/README.md">assets/README.md</a>.
</sub>
