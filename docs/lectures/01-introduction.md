# 第 1 讲 讲义：Grounded AI for Transportation

> 🎯 **本讲核心**：建立"Grounded AI"心智模型，立方法论
>
> 📅 上课时间：2026/9/18（五）13:30-15:00 · 嘉定 C208
>
> 👨‍🏫 授课：李健

## 🎬 课件

- 📊 **在线课件**（reveal.js）：[lecture-01-slides.html](/lecture-01-slides.html) · 按 → 翻页 · 按 F 全屏
- 📝 **Slidev 源文件**：[GitHub 仓库](https://github.com/runningjian-ui/tongji-llm-urban-transport/tree/main/lectures/01-introduction/slides)
- 💻 **演示代码**：[grounded_qa.py](https://github.com/runningjian-ui/tongji-llm-urban-transport/blob/main/lectures/01-introduction/demo/grounded_qa.py)

## 一、本讲目标

完成本讲后，你应能够：

1. **理解 AI 三波浪潮**：Chat → 推理 → Agent
2. **描述 LLM 在交通的 4 类角色**：助手 / 规划器 / 评估器 / 协调器
3. **解释 Grounded AI 三层架构**：数据接地 / 知识接地 / 反馈接地
4. **应用 Allowed with disclosure 政策**

## 二、本讲内容

### Part 1：为什么是现在？（20 分钟）
- AI 三波浪潮
- 范式转移：感知 → 认知 → 行动
- LLM 在交通的 4 类角色

### Part 2：为什么是交通？（15 分钟）
- 城市交通的 4 类老问题
- 过去 20 年 AI 方案回顾
- LLM vs 传统 AI 的差异

### Part 3：Grounded AI（25 分钟）⭐
- 定义与来源（MIT Jinhua Zhao）
- 与幻觉的关系
- **三层架构**：
  - 数据接地（实时数据 API）
  - 知识接地（知识图谱、规范）
  - 反馈接地（人在环）
- 5 个交通领域例子

### Part 4：12 讲地图（10 分钟）
- 全景图
- 5 类能力对应表

### Part 5：课程安排（10 分钟）
- 考核方式
- 关键节点
- **AI 使用政策**

### Part 6：课堂演示（15 分钟）
- 让 LLM 读懂《上海交通运行报告》
- 演示 Grounded vs 不 Grounded 的差异

### Part 7：Q&A + 作业布置（5 分钟）

## 三、关键概念

### Grounded AI（扎根式 AI）
> AI 的输出必须扎根真实世界——数据、知识、上下文、人类反馈。
> — Prof. Jinhua Zhao, MIT

### AI Native
一种设计哲学：从产品/系统诞生的第一天起，AI 就是默认能力，不是后期插件。

### Allowed with disclosure
一种 AI 使用政策：允许使用 GenAI 协助完成作业，但必须如实披露。

## 四、课堂演示说明

**演示主题**：让 LLM 读懂《上海年度交通运行报告》

**演示步骤**：

1. **准备**：下载一份 2024 或 2025 上海交通运行报告 PDF
2. **不 Grounded 版本**：
   - 直接把 PDF 内容贴进 ChatGPT
   - 让它回答"上海外滩早高峰几点最堵"
   - 观察：可能给出看似合理但无法验证的回答
3. **Grounded 版本**：
   - 用 RAG 把 PDF 切片、向量化
   - 接入 LangChain + Chroma
   - 提问时要求 LLM 标注引用源
   - 观察：每个数据点都能追溯到 PDF 原文

**演示代码**：[grounded_qa.py](https://github.com/runningjian-ui/tongji-llm-urban-transport/blob/main/lectures/01-introduction/demo/grounded_qa.py)

## 五、作业 0

> ⏰ **截止日期**：W2 课程结束前（2026/9/25）

**任务**：选定交通子领域，提交问题陈述 + 数据来源（≤500 字）

**提交方式**：

1. Fork [GitHub 仓库](https://github.com/runningjian-ui/tongji-llm-urban-transport)
2. 在 `assignments/hw0-proposal/` 下创建 `{your-name}.md`
3. 提交 Pull Request

**评分（5 分）**：

| 维度 | 分值 |
|---|---|
| 问题清晰度 | 2 |
| 数据可获得性 | 2 |
| Grounded 程度 | 1 |

## 六、推荐阅读

1. **Nie, T., Sun, J., & Ma, W. (2025)**. *Exploring the roles of large language models in reshaping transportation systems: A survey, framework, and roadmap*. AI for Transportation, 1, 100003.
2. **Choi, S. et al. (2025)**. *A gentle introduction and tutorial on deep generative models in transportation research*. TR-C, 176, 105145.
3. **Vaswani et al. (2017)**. *Attention Is All You Need*. NeurIPS.
4. **Park, J. et al. (2023)**. *Generative Agents: Interactive Simulacra of Human Behavior*. UIST.

## 七、下讲预告

**第 2 讲：LLM 内部机理**
- Tokenization（BPE / SentencePiece）
- Transformer 架构
- 训练三阶段：Pre-training → SFT → RLHF / DPO
- 推理机制：Sampling、KV Cache

为什么这讲很重要：不理解 LLM 内部机理，就无法理解第 3 讲"推理模型"的范式突破。


### Part 2：为什么是交通？（15 分钟）
- 城市交通的 4 类老问题
- 过去 20 年 AI 方案回顾
- LLM vs 传统 AI 的差异

### Part 3：Grounded AI（25 分钟）
- 定义与来源（MIT Jinhua Zhao）
- 与幻觉的关系
- **三层架构**：
  - 数据接地（实时数据 API）
  - 知识接地（知识图谱、规范）
  - 反馈接地（人在环）
- 5 个交通领域例子

### Part 4：12 讲地图（10 分钟）
- 全景图（Mermaid）
- 5 类能力对应表

### Part 5：课程安排（10 分钟）
- 考核方式
- 关键节点
- **AI 使用政策**

### Part 6：课堂演示（15 分钟）
- 让 LLM 读懂《上海交通运行报告》
- 演示 Grounded vs 不 Grounded 的差异

### Part 7：Q&A + 作业布置（5 分钟）

## 三、关键概念

### Grounded AI（扎根式 AI）
> AI 的输出必须扎根真实世界——数据、知识、上下文、人类反馈。
> — Prof. Jinhua Zhao, MIT

### AI Native
一种设计哲学：从产品/系统诞生的第一天起，AI 就是默认能力，不是后期插件。

### Allowed with disclosure
一种 AI 使用政策：允许使用 GenAI 协助完成作业，但必须如实披露。

## 四、课堂演示说明

**演示主题**：让 LLM 读懂《上海年度交通运行报告》

**演示步骤**：

1. **准备**：下载一份 2024 或 2025 上海交通运行报告 PDF
2. **不 Grounded 版本**：
   - 直接把 PDF 内容贴进 ChatGPT
   - 让它回答"上海外滩早高峰几点最堵"
   - 观察：可能给出看似合理但无法验证的回答
3. **Grounded 版本**：
   - 用 RAG 把 PDF 切片、向量化
   - 接入 LangChain + Chroma
   - 提问时要求 LLM 标注引用源
   - 观察：每个数据点都能追溯到 PDF 原文

**演示代码**：[demo/grounded_qa.py](demo/grounded_qa.py)（待开发）

## 五、作业 0

详见 [assignments/hw0-proposal/](../../assignments/hw0-proposal/)

**任务**：选定交通子领域，提交问题陈述 + 数据来源（≤500 字）

**截止**：W2 课程结束前

## 六、推荐阅读

1. **Nie, T., Sun, J., & Ma, W. (2025)**. Exploring the roles of LLMs in transportation. *AI for Transportation*, 1, 100003.
2. **Choi, S. et al. (2025)**. A gentle introduction and tutorial on deep generative models in transportation. *TR-C*, 176, 105145.
3. **Vaswani et al. (2017)**. Attention Is All You Need. *NeurIPS*.
4. **Park, J. et al. (2023)**. Generative Agents: Interactive Simulacra of Human Behavior. *UIST*.

## 七、备课提示

- 演示代码需要在课前调试好，避免现场出错
- 准备 1-2 个 Grounded 与不 Grounded 的对比案例
- 政策宣示要在第 1 讲明确，避免后续争议
- 留 5 分钟答疑时间

## 八、下讲预告

**第 2 讲：LLM 内部机理**
- Tokenization（BPE / SentencePiece）
- Transformer 架构
- 训练三阶段：Pre-training → SFT → RLHF / DPO
- 推理机制：Sampling、KV Cache

为什么这讲很重要：不理解 LLM 内部机理，就无法理解第 3 讲"推理模型"的范式突破。
