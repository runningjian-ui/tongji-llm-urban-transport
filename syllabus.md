# 课程大纲：大模型驱动的城市交通治理技术

> **Grounded LLM for Urban Transportation**
> 同济大学交通学院 · 研究生课程 · 2026 春季

---

## 一、课程基本信息

| 项 | 内容 |
|---|---|
| 课程名称 | 大模型驱动的城市交通治理技术 / LLM-Powered Urban Transportation Governance |
| 课程编号 | 待定 |
| 学分 | 2 学分 |
| 学时 | 32 学时（15 次课 × 2 学时 + 实验） |
| 先修要求 | Python 基础 · 概率统计基础 · 交通工程基础 |
| 授课对象 | 交通运输工程、智能交通、交通工程、计算机交叉方向硕士/博士研究生 |

---

## 二、课程目标

完成本课程后，学生应能够：

1. **理解 LLM 工作机理**：掌握 Transformer、SFT、RLHF/DPO 等核心技术概念
2. **掌握 Grounded AI 方法**：能够用 RAG、Agent、多智能体让 LLM 扎根真实交通数据
3. **独立构建交通 LLM 应用**：从 Prompt 到 Fine-tuning 到 Agent 全流程
4. **评测 LLM 系统**：设计交通领域评测方案，理解 LLM-as-Judge 与传统评测差异
5. **批判性思考**：理解 AI Native 范式、Grounded 原则、伦理治理与算法公平

---

## 三、课程结构

```
12 次讲授课 + 2 次专家课 + 1 次项目汇报 = 15 次课
+ 4 次 Recitation Lab（助教带实操）
+ 8 次课后作业
+ 1 个期末小组项目
```

### 时间安排（2026 秋季）

**上课时间**：每周五 · **13:30 - 15:00**（90 分钟）· 2026/9/18 - 2027/1/15
**上课地点**：同济大学嘉定校区 **C208**
**总跨度**：18 周（16 次课 + 国庆、元旦 2 周停课）

> 注：跳过国庆假期（10/2）和元旦假期（1/1）

| 序号 | 日期 | 类型 | 内容 | 备注 |
|---|---|---|---|---|
| 1 | 9/18（五） | 📚 讲授课 | 第 1 讲：导论 + Grounded AI | 立方法论 |
| 2 | 9/25（五） | 📚 讲授课 | 第 2 讲：LLM 内部机理 | + Lab 1 预告 |
| — | 10/2（五） | 🚫 停课 | **国庆假期** | 法定假日 |
| 3 | 10/9（五） | 📚 讲授课 | 第 3 讲：推理大模型 | |
| 4 | 10/16（五） | 📚 讲授课 | 第 4 讲：Prompt + 适配 | + Lab 1（部署 LLM） |
| 5 | 10/23（五） | 📚 讲授课 | 第 5 讲：RAG 进阶 | + Lab 2 |
| 6 | 10/30（五） | 📚 讲授课 | 第 6 讲：Agent | |
| 7 | 11/6（五） | 🎤 **专家课 #1** | RAG / Agent 工程化实战 | 外请讲者 |
| 8 | 11/13（五） | 📚 讲授课 | 第 7 讲：多智能体 | + Lab 3 |
| 9 | 11/20（五） | 📚 讲授课 | 第 8 讲：多模态 VLM | |
| 10 | 11/27（五） | 📚 讲授课 | 第 9 讲：端到端 AD + 世界模型 | + Lab 4 |
| 11 | 12/4（五） | 🎤 **专家课 #2** | 端到端 AD 实战 | 外请讲者 |
| 12 | 12/11（五） | 📚 讲授课 | 第 10 讲：交通治理全景 | |
| 13 | 12/18（五） | 📚 讲授课 | 第 11 讲：评测 | |
| 14 | 12/25（五） | 📚 讲授课 | 第 12 讲：治理 + 前沿 | |
| — | 1/1（五） | 🚫 停课 | **元旦假期** | 法定假日 |
| 15 | 1/8（五） | 🎯 **项目中期汇报** | 各组 10 分钟汇报 + 5 分钟 Q&A | 中期考核 |
| 16 | 1/15（五） | 🎯 **项目终期汇报** | 各组 15 分钟汇报 + 5 分钟 Q&A | **最终考核** |

> 实际安排以教务通知为准。如有调整会在课程仓库发布。

### 课程结构总览

```
12 次讲授课（每周 1 次）
  ↓
2 次专家课（外请讲者，11/6 + 12/4）
  ↓
项目周期
  - W6 (10/23): 项目方向发布
  - W10 (11/27): 项目 proposal 提交
  - W15 (1/8): 项目中期汇报
  - W16 (1/15): 项目终期汇报（最终考核）
```

---

## 四、12 讲详纲

### 第 1 讲｜课程导论：Grounded AI for Transportation
**核心问题**：为什么是现在？为什么是交通？为什么是 Grounded？

- 城市交通治理的"老问题"与 AI 范式转移
- 三波浪潮：Chat → 推理 → Agent
- **Grounded AI 三层**：数据接地 / 知识接地 / 反馈接地
- 12 讲地图 · 考核方式 · 阅读材料 · Recitation 安排
- **政策宣示**：Allowed with disclosure（基于 Choi et al. 2025 教学实践）
- 课堂演示：让 LLM 读懂《上海年度交通运行报告》并交叉验证

**作业 0**：选定一个你关注的交通子领域，提交 1 段"问题陈述 + 数据来源"（≤500 字）

---

### 第 2 讲｜LLM 内部机理【独立成章】
**核心问题**：LLM 到底是怎么"思考"的？

- Tokenization（BPE / SentencePiece）
- Transformer 架构（注意力、位置编码、KV Cache）
- 训练三阶段：Pre-training → SFT → Preference Alignment（RLHF / DPO / GRPO）
- 推理机制：Sampling、Speculative Decoding
- 课堂演示：用 PyTorch 写一个 mini-Transformer，跑 100 步训练
- 论文：Vaswani 2017；Ouyang 2022；Rafailov 2023

---

### 第 3 讲｜推理大模型：让机器"慢慢想"
**核心问题**：o1/R1 为何是范式突破？

- OpenAI o1/o3、DeepSeek R1、Claude Extended Thinking
- Test-Time Compute Scaling、Process Reward Model
- 慢思考 vs 快思考：何时用推理模型
- **交通场景**：复杂路径规划、多目标调度、应急车辆协调
- 课堂演示：4o vs o1 在应急调度题上的推理过程对比

**作业 1**：用 R1 / o1 解一道交通博弈题，对比普通模型输出（1 页分析）

---

### 第 4 讲｜Prompt 工程与适配技术
**核心问题**：什么时候该用 Prompt、什么时候该 Fine-tune、什么时候该 RAG？

- 基础：Few-shot、CoT、ReAct、Self-Consistency
- 进阶：ToT、Step-Back、Reflection
- 适配技术选型：Prompt vs LoRA vs Full Fine-tuning vs RAG
- 主流模型速览：闭源（GPT-4o/Claude/Gemini）vs 开源（Qwen/GLM/DeepSeek）
- 课堂演示：5 个模型对同一份信号报告的摘要对比

**作业 2**：用 LoRA 微调 7B 模型做交通问答（提供数据 + 模板）

---

### 第 5 讲｜RAG：从朴素到 GraphRAG
**核心问题**：如何让 LLM "接外部大脑"？

- 朴素 RAG：Chunking → Embedding → Retrieve → Generate
- 进阶 RAG：ReRank、HyDE、Self-RAG、CRAG
- **GraphRAG**（Microsoft, 2024）：知识图谱 + 社区摘要
- **Agentic RAG**：让 Agent 决定检索策略
- 向量库选型：Milvus、Qdrant、Chroma
- 课堂演示：Neo4j + LLM 搭建"上海交通法规知识问答"

**专家课 #1**：RAG / Agent 工程化实战
**Lab 2**：LangChain + Chroma 搭建 RAG
**作业 3**：用 GraphRAG 构建小型交通知识图谱

---

### 第 6 讲｜Agent 与 Function Calling
**核心问题**：从"对话"到"执行"如何跨越？

- 范式演进：Chain → ReAct → Reflexion → Voyager
- Function Calling / Tool-use 范式
- 主流框架：LangGraph、AutoGen、CrewAI、OpenAI Swarm
- **Harness Engineering**：让 Agent 稳定运行的关键设计
- 课堂演示：5 分钟搭"交通数据分析 Agent"（CSV → 指标 → 报告）
- 案例：OpenClaw / Manus / Devin 思想拆解

**作业 4**：用 LangGraph 构建单车路径规划 Agent

---

### 第 7 讲｜多智能体系统与交通仿真
**核心问题**：为什么一个 Agent 不够？

- 单 Agent 局限 vs 多 Agent 涌现
- 协作模式：流水线 / 群组 / 辩论 / 层级
- 主流框架：CrewAI、AutoGen、MetaGPT、ChatDev
- **前沿论文**：
  - Generative Agents (Stanford, 2023)
  - AgentVerse（动态组网）
  - MetaGPT（软件工程多智能体）
- **交通场景**：
  - 出行者–管理者–运营商三方仿真
  - 应急场景多主体协同
  - 自动驾驶车队协同
- 课堂演示：3 个 Agent 协商出行方案

**Lab 3**：用 CrewAI 搭建应急疏散多智能体仿真
**作业 5**：3 人一组，设计多智能体出行协商场景

---

### 第 8 讲｜多模态大模型：看见、听见、读懂交通
**核心问题**：当 LLM 长出"眼睛"会怎样？

- 视觉-语言模型：CLIP、LLaVA、InternVL 2.5、Qwen2-VL
- 原生多模态：GPT-4o、Gemini 2.0 统一 token 化
- 长视频理解：小时级、跨镜头事件追踪
- **交通场景**：
  - 监控视频事件结构化
  - 道路病害、标志标线
  - 交通事故/施工区识别
  - 交通工程图纸理解
- 课堂演示：30 分钟路口监控 → 自动生成运行报告

**作业 6**：用 Qwen2-VL / InternVL 对 100 张监控截图做事件分类

---

### 第 9 讲｜端到端自动驾驶与世界模型
**核心问题**：模块化范式为何被挑战？世界模型是终极答案吗？

- 范式之争：模块化 vs 端到端
- **前沿产品**：
  - 特斯拉 FSD V12/V13（纯端到端）
  - 华为 ADS 3.0/4.0
  - 百度 Apollo ADFM
  - Wayve AV 2.0 / LINGO（语言可解释）
- **关键论文**：UniAD（CVPR 2023 Best）、VAD、SparseDrive、GenAD
- **世界模型**：
  - Wayve GAIA-1 / LINGO-2
  - DriveDreamer
  - NVIDIA Cosmos
- 课堂演示：传统模块化 vs 端到端决策过程可视化
- 课堂演示：输入"明天早高峰下雨"生成交通仿真视频

**专家课 #2**：端到端 AD 实战
**Lab 4**：CARLA 跑端到端 AD demo

---

### 第 10 讲｜大模型在交通治理中的"全景地图"
**核心问题**：LLM 在交通治理的全景应用图谱是什么？

- **监测层**：运行报告自动生成、异常归因、舆情分析
- **规划层**：信号配时、渠化设计、需求预测、线网优化
- **服务层**：智能客服、个性化出行推荐、无障碍出行
- **应急层**：调度、信息发布、舆情应对
- **决策层**：政策仿真、影响评估
- **一张图总结**：LLM 能做 / 不能做 / 要小心的任务
- 5 个真实落地案例（高德、百度、阿里、海康、滴滴）

**作业 7**：选定交通治理场景，撰写"LLM 解决方案设计书"（3 页）

---

### 第 11 讲｜评测：怎么知道 LLM 答得对【独立成章】
**核心问题**：Grounded 的"度"如何度量？

- 评测范式：人工评测、自动化指标、LLM-as-Judge
- 通用 Benchmark：MMLU、HumanEval、MT-Bench、Chatbot Arena
- **交通领域 Benchmark 设计**（学界空白 = 科研机会）：
  - 法规问答 benchmark
  - 信号策略 benchmark
  - 多智能体出行协商 benchmark
- 评估的"陷阱"：数据污染、评分者偏差、对抗鲁棒性
- 课堂演示：用 LLM-as-Judge 评测 5 个模型的交通问答表现

**作业 8**：为你的项目设计评测方案（指标 + 流程 + 局限）

---

### 第 12 讲｜AI 治理、安全伦理与未来展望 + 项目导引
**核心问题**：怎么让 LLM 真正"用得上、用得久"？

- **风险全景**：幻觉、偏见、隐私、越狱、可解释性
- **治理框架**：欧盟 AI Act、中国《生成式 AI 服务管理暂行办法》
- **交通领域特殊议题**：
  - 自动驾驶 LLM 决策的责任归属
  - 交通数据的隐私与合规
  - 算法公平：弱势群体出行的算法偏见
- **未来 3–5 年**：Agentic AI、世界模型、具身智能、人车路云一体化
- 课程项目选题导引（10 个方向）
- 行业嘉宾对谈

---

## 五、考核方案

| 项 | 占比 | 说明 |
|---|---|---|
| 课堂作业（8 次） | 30% | 每次 5–10 分 |
| Recitation Lab（4 次） | 20% | 提交代码 + 报告 |
| 课程项目 | 40% | 3 人一组，中期+终期答辩 |
| 期末反思（1 页） | 10% | "这门课如何改变了我的研究计划" |

---

## 六、关键政策

### 1. Allowed with disclosure 政策
参考 Choi et al. (2025) 的教学实践，鼓励学生在使用 GenAI 时充分披露：

可用 GenAI 工具（ChatGPT、Claude、Cursor 等）协助完成作业，但：
- **必须**在每次提交中说明：用了什么工具、用在哪一步、产出占比
- 提交 `.ai-disclosure.md` 文件，记录每次会话摘要
- 助教有权对作业进行 AI 使用情况抽查

**参考来源**：Choi, S., Jin, Z., Ham, S. W., Kim, J., & Sun, L. (2025). *A gentle introduction and tutorial on deep generative models in transportation research*. Transportation Research Part C, 176, 105145.

### 2. Grounded AI 原则
Grounded AI 概念由 MIT Jinhua Zhao 团队提出，强调 LLM 输出扎根真实数据：

- 所有项目必须挂真实数据集
- 所有 LLM 输出必须能追溯到来源
- 鼓励使用上海/同济本地数据

**参考来源**：Zhao, J. et al. *Mens, Manus and Machina: How AI Impacts the Future of Work and Learning*. MIT Mobility Initiative.

### 3. 学术诚信
- 抄袭作业 0 分
- 抄袭代码按学校规定处理
- 引用规范：使用 GB/T 7714 格式

### 4. 协作方式
- 课程讨论：GitHub Discussions
- 作业提交：GitHub Pull Request
- 项目看板：GitHub Projects

---

## 七、推荐阅读清单

### 必读
- Vaswani et al. (2017). *Attention Is All You Need*. NeurIPS.
- Ouyang et al. (2022). *Training language models to follow instructions* (InstructGPT).
- Rafailov et al. (2023). *Direct Preference Optimization*. NeurIPS.
- Nie, T., Sun, J., & Ma, W. (2025). *Exploring the roles of large language models in reshaping transportation systems*. AI for Transportation.
- Choi, S. et al. (2025). *A gentle introduction and tutorial on deep generative models in transportation research*. TR-C.
- Hu, E. et al. (2021). *LoRA: Low-Rank Adaptation of Large Language Models*. ICLR.
- Edge, D. et al. (2024). *GraphRAG*. Microsoft Research.
- Yao, S. et al. (2022). *ReAct: Synergizing Reasoning and Acting in Language Models*. ICLR.
- Park, J. et al. (2023). *Generative Agents: Interactive Simulacra of Human Behavior*. UIST.
- Hu, Y. et al. (2023). *UniAD: Planning-oriented Autonomous Driving*. CVPR (Best Paper).

### 选读
- Wei, J. et al. (2022). *Chain-of-Thought Prompting*. NeurIPS.
- Shinn, N. et al. (2023). *Reflexion*. NeurIPS.
- Liu, H. et al. (2024). *Visual Instruction Tuning* (LLaVA). NeurIPS.
- Wayve (2023). *GAIA-1: A Generative World Model for Autonomous Driving*. Tech Report.
- OpenAI (2024). *o1 System Card*.
- DeepSeek (2025). *R1 Tech Report*.

### 行业报告
- 高德地图、百度地图、阿里云、华为、滴滴白皮书
- 中国信通院《AI 大模型应用案例集》
- 麦肯锡《生成式 AI 在交通领域的应用》

---

## 八、与其他课程设计对比

下表比较本课程与几门具有代表性的相关课程在**设计特点**上的异同（直接比较方法论层面）：

| 维度 | 本课 | MIT UAI 课程 | UMN Choi 课程 | SJTU CS4650J |
|---|---|---|---|---|
| Grounded AI 主线 | ✅ | ✅ | ❌ | ❌ |
| LLM 内部机理独立成章 | ✅ | ❌ | 部分 | ✅ |
| Theory→Practice→Project | ✅ | ✅ | ✅ | ✅ |
| 评测独立成章 | ✅ | ❌ | ❌ | ✅ |
| Recitation 实验课 | ✅ | ✅ | ❌ | ❌ |
| 课程仓库完全开源 | ✅ | ✅ | ❌ | ❌ |
| 12 讲覆盖最广前沿 | ✅ | ❌ | ❌ | ❌ |

> **参考课程链接**：
> - MIT UAI Transportation: <https://learn.mit.edu/courses/course-v1:UAI_SOURCE+UAI.MLTL.1>
> - UMN "Generative AI for Transportation Research": <https://www.linkedin.com/pulse/generative-ai-transportation-research-seongjin-choi-rdkkc/>
> - SJTU CS4650J: <https://gc.sjtu.edu.cn/academics/courses/courses-by-number/course-info?id=85958>

**定位**：国内第一门系统讲"**Grounded LLM for Transportation**"的研究生课。

---

## 九、设计灵感来源

本课程在以下研究/教学工作的启发下形成（致谢）：

- **Grounded AI 思想**：Jinhua Zhao 教授团队（MIT Mobility Initiative）提出的"Grounded AI"概念
- **生成式 AI 教学实践**：Seongjin Choi 教授（UMN）"Generative AI for Transportation Research" 课程的"Allowed with disclosure" 政策
- **LLM 系统性教学**：Shuo Wang 教授（SJTU）CS4650J 课程的 LLM 全生命周期结构

具体引用详见每节末尾的"参考来源"。本课程在内容、方法、政策上均参考但不限于以上工作，感谢所有开源贡献者。
