---
title: 大模型驱动的城市交通治理技术
subtitle: Grounded LLM for Urban Transportation @ Tongji University
---

<div align="center">

# 🚦 大模型驱动的城市交通治理技术

### LLM-Powered Urban Transportation Governance

**同济大学交通学院 · 研究生课程（2026 秋季）**

[![Course](https://img.shields.io/badge/课程-研究生-blue)](#)
[![Lectures](https://img.shields.io/badge/讲次-12-green)](#lectures)
[![Labs](https://img.shields.io/badge/实验-4-orange)](#labs)
[![Projects](https://img.shields.io/badge/项目-10-red)](#projects)
[![License](https://img.shields.io/badge/license-CC--BY--SA--4.0-lightgrey)](#license)

[📚 课程网站](https://runningjian-ui.github.io/tongji-llm-urban-transport) ·
[📖 大纲](syllabus.md) ·
[📋 政策](policy.md) ·
[💬 讨论区](https://github.com/runningjian-ui/tongji-llm-urban-transport/discussions)

</div>

---

## 🎯 课程定位

> **用 Grounded 的方法，构建 AI Native 的城市交通治理系统。**

这门课是国内第一门系统讲"**Grounded LLM for Transportation**"的研究生课程。我们不只教 API 怎么调、Prompt 怎么写——我们关注：

- 🧠 **LLM 内部机理**：Transformer、SFT、RLHF、推理模型怎么工作
- 🛠 **核心技术栈**：RAG、Agent、多智能体、多模态、端到端
- 🚦 **交通场景落地**：信号配时、公交评价、出行规划、应急调度、自动驾驶
- 🌍 **Grounded AI**：每个 LLM 输出都扎根真实数据/知识/反馈
- 🤖 **AI Native 思维**：从系统架构层面重新思考 AI 时代的产品与治理

---

## 📚 12 讲速览

| 讲 | 主题 | 关键技术 |
|---|---|---|
| 1 | 课程导论：Grounded AI for Transportation | AI Native 哲学 / 三波浪潮 |
| 2 | LLM 内部机理 | Transformer / SFT / RLHF / DPO |
| 3 | 推理大模型 | o1 / R1 / Test-Time Compute |
| 4 | Prompt 工程与适配 | Few-shot / LoRA / 模型选型 |
| 5 | RAG：从朴素到 GraphRAG | 向量库 / 知识图谱 / Agentic RAG |
| 6 | Agent 与 Function Calling | ReAct / LangGraph / Harness Engineering |
| 7 | 多智能体系统 | CrewAI / Generative Agents / SUMO |
| 8 | 多模态大模型 | VLM / VLA / 长视频理解 |
| 9 | 端到端自动驾驶与世界模型 | UniAD / FSD V12 / GAIA-1 / CARLA |
| 10 | 交通治理全景图 | 监测/规划/服务/应急/决策 5 层 |
| 11 | 评测：怎么知道 LLM 答得对 | LLM-as-Judge / 交通 Benchmark |
| 12 | AI 治理、安全伦理与未来 | 幻觉 / 隐私 / 算法公平 / 监管 |

**配套**：4 次 Recitation Lab · 8 次作业 · 1 个期末项目 · 2 次专家课

---

## 🌟 课程特色

### 1. AI Native 的课程本身
- 课件用 **Slidev** 写，HTML 部署，全 Git 版本管理
- 课程网站用 **VitePress** 部署到 GitHub Pages
- 作业提交流程 AI 自动化（Issue 模板 + LLM 辅助）
- **Allowed with disclosure** 政策，鼓励"AI 友好"使用

### 2. Grounded AI 原则
- 所有项目必须挂真实交通数据
- 所有 LLM 输出必须能追溯到来源
- 评测环节（第 11 讲）专门设计交通领域 Benchmark

### 3. 国际对标 + 本土实践
- 参考 MIT UAI、UMN、SJTU 等国际一流课程
- 案例覆盖上海/北京/深圳/雄安真实场景
- 与同济交通学院研究优势结合

---

## 🚀 快速开始

### 学生
1. ⭐ Star 本仓库
2. 📖 阅读 [syllabus.md](syllabus.md) 了解大纲
3. 📋 阅读 [policy.md](policy.md) 了解 AI 使用规则
4. 💬 在 [Discussions](https://github.com/runningjian-ui/tongji-llm-urban-transport/discussions) 提问
5. 📁 在对应章节目录下查看课件与作业

### 教师 / 助教
1. Fork 本仓库
2. 在 [Issues](https://github.com/runningjian-ui/tongji-llm-urban-transport/issues) 用模板创建任务
3. 用 [GitHub Projects](https://github.com/runningjian-ui/tongji-llm-urban-transport/projects) 管理进度
4. 接收学生 PR 改进课件/作业

### 校外学习者
- 所有课件与代码以 **CC-BY-SA-4.0** 协议开源
- 数据集遵循各自 license
- 欢迎贡献 PR，但请先阅读 [CONTRIBUTING.md](CONTRIBUTING.md)

---

## 🤝 贡献

欢迎提交 Issue 和 PR 改进：
- 课件错误/补充
- 新增交通领域案例
- 翻译（英文/其他语言）
- Lab 实验优化

详见 [CONTRIBUTING.md](CONTRIBUTING.md)

---

## 📜 引用

如果本课程对你的研究/教学有帮助，请引用：

```bibtex
@course{tongji-llm-urban-transport-2026,
  title  = {大模型驱动的城市交通治理技术},
  author = {李健 and 课程团队},
  year   = {2026},
  url    = {https://github.com/runningjian-ui/tongji-llm-urban-transport}
}
```

---

## 📄 License

本仓库内容采用 [CC-BY-SA-4.0](https://creativecommons.org/licenses/by-sa/4.0/) 协议。
代码部分采用 [MIT](https://opensource.org/licenses/MIT) 协议。

---

<div align="center">

**Instructor**: [李健 @ 同济大学交通学院](https://github.com/runningjian-ui) ·
**Built with**: Slidev · VitePress · GitHub Actions ·
**Last updated**: 2026-08

</div>
