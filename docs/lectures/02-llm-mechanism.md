# 第 2 讲 讲义：LLM 内部机理

> 🎯 **本讲核心**：从 Tokenization 到 RLHF/DPO，真正理解大模型是怎么"思考"的
>
> 📅 上课时间：2026/9/25（五）13:30-15:00 · 嘉定 C208
>
> 👨‍🏫 授课：李健

## 一、本讲目标

1. **理解 Tokenization**：BPE、SentencePiece
2. **掌握 Transformer**：注意力机制、位置编码、KV Cache
3. **熟悉训练三阶段**：Pre-training → SFT → Preference Alignment（RLHF / DPO / GRPO）
4. **理解推理机制**：Sampling、Speculative Decoding

## 二、本讲内容

### Part 1：Tokenization
- 为什么需要 token
- BPE / WordPiece / SentencePiece
- 中文 tokenization 的特殊性

### Part 2：Transformer 架构
- Self-Attention 的直觉
- 位置编码（Sinusoidal / RoPE / ALiBi）
- KV Cache 优化
- 现代架构（Llama、Qwen）

### Part 3：预训练目标
- Next-Token Prediction
- Scale Laws
- 数据规模 vs 算力 vs 模型大小

### Part 4：SFT 与对齐
- Supervised Fine-Tuning
- RLHF（PPO 算法）
- DPO（Direct Preference Optimization）
- GRPO（DeepSeek 方案）

### Part 5：推理机制
- Sampling 策略（Greedy / Top-p / Top-k）
- Speculative Decoding
- KV Cache 复用

## 三、推荐阅读

- **Vaswani et al. (2017)**. *Attention Is All You Need*. NeurIPS.
- **Ouyang et al. (2022)**. *Training language models to follow instructions* (InstructGPT).
- **Rafailov et al. (2023)**. *Direct Preference Optimization*. NeurIPS.

## 四、本讲作业预告

**作业 1**：从 Tokenization 到推理速度，写一篇 1 页分析（可选）。
