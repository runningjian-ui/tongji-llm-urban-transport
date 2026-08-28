# 第 4 讲 讲义：Prompt 工程与适配技术

> 🎯 **本讲核心**：什么时候用 Prompt、什么时候用 RAG、什么时候微调？
>
> 📅 上课时间：2026/10/16（五）13:30-15:00 · 嘉定 C208
>
> 👨‍🏫 授课：李健

## 一、本讲目标

1. **掌握 Prompt 工程的全部技巧**
2. **理解适配技术的选型决策**
3. **熟悉 LoRA、QLoRA 的工程实践**
4. **对比主流开源/闭源模型**

## 二、本讲内容

### Part 1：Prompt 基础
- Few-shot、CoT、ReAct
- Self-Consistency
- ToT、Step-Back Prompting
- Reflection

### Part 2：适配技术选型
- Prompt vs LoRA vs Full Fine-tuning vs RAG
- 决策框架
- 成本与效果对比

### Part 3：LoRA / QLoRA
- 原理（低秩分解）
- 实践：用 PEFT 库微调 7B 模型
- 交通领域数据准备

### Part 4：模型选型
- 闭源：GPT-4o / Claude / Gemini
- 开源：Qwen / GLM / DeepSeek / Llama
- 交通领域选型建议

## 三、本讲作业

**HW 2：LoRA 微调 7B 交通问答**
- 提交训练代码 + 模型 + 评估
- ⏰ 截止：W6（10/30）
