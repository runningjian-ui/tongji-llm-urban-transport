# Lab 1: 本地部署大模型

> **时间**：2 学时
> **对应讲次**：第 2 讲 - LLM 内部机理
> **难度**：⭐⭐☆☆☆
> **目标**：在本地部署一个开源 LLM，并通过 API 与程序对话

---

## 一、实验目标

完成本实验后，你应能够：

1. ✅ 在本地环境部署一个开源 LLM（Qwen2.5-7B）
2. ✅ 通过命令行与 LLM 对话
3. ✅ 启动 LLM 的 API Server，通过 Python 客户端调用
4. ✅ 对比本地部署 vs API 调用的优劣
5. ✅ 完成一份实验报告，附 AI 使用披露

---

## 二、实验环境

### 硬件要求

| 部署方式 | 最低配置 | 推荐配置 |
|---|---|---|
| Ollama 部署 | 8GB RAM | 16GB RAM + M1/M2 Mac |
| vLLM 部署 | 16GB GPU 显存 | 24GB GPU 显存（A5000/A100） |
| 仅 API 调用 | 任意 | 任意 |

### 软件要求

- macOS 12+ / Ubuntu 20.04+ / Windows 11 WSL2
- Python 3.10+
- 磁盘空间 ≥ 10GB

---

## 三、实验步骤

### Step 1: 安装 Ollama（推荐路径）

```bash
# macOS
brew install ollama
# 或直接下载：https://ollama.com/download

# Linux
curl -fsSL https://ollama.com/install.sh | sh
```

**验证安装**：

```bash
ollama --version
# 应输出：ollama version 0.x.x
```

### Step 2: 拉取 Qwen2.5-7B 模型

```bash
# 拉取模型（约 4.7GB）
ollama pull qwen2.5:7b

# 查看已下载的模型
ollama list
```

**说明**：
- `qwen2.5:7b` 是 7B 参数版本
- 如机器性能不够，可用 `qwen2.5:1.5b`（1.5B 参数）
- 如机器性能充足，可用 `qwen2.5:14b` 或更大

### Step 3: 命令行对话测试

```bash
# 启动对话
ollama run qwen2.5:7b

# 试试这些问题：
# > 你好，请介绍下同济大学
# > Transformer 的核心思想是什么？
# > 用 Python 写一个快速排序
# > 上海市有哪些交通枢纽？
```

**退出对话**：`/bye`

### Step 4: 启动 API Server

Ollama 自动暴露 OpenAI 兼容 API：

```bash
# 启动 server（默认在 11434 端口）
ollama serve

# 另开终端，测试 API
curl http://localhost:11434/v1/models
```

### Step 5: 通过 Python 客户端调用

复制 [`starter/chat_with_llm.py`](starter/chat_with_llm.py) 并运行：

```bash
cd starter
pip install -r requirements.txt
python chat_with_llm.py
```

**预期输出**：

```
✅ 连接到本地 Ollama (http://localhost:11434)
✅ 加载模型：qwen2.5:7b

📝 问题：Transformer 的核心思想是什么？
🤖 回答：Transformer 的核心思想是...

📝 问题：同济大学在哪座城市？
🤖 回答：同济大学位于中国上海市...

📊 统计：
   - 总 token 数：342
   - 平均响应时间：1.2s
   - 模型：qwen2.5:7b
```

### Step 6: 交通领域测试

修改 `chat_with_llm.py`，让它回答 5 个交通领域问题：

1. 解释什么是"信号配时"
2. 上海外滩附近有几个地铁站？
3. 列出 3 种常见的交通需求预测方法
4. 解释 ITS 是什么
5. 简述 RAG 在交通领域的应用

记录每个回答，并标注"答对 / 答错 / 编造"。

### Step 7（进阶）: 用 vLLM 部署

如果你的机器有 GPU（≥16GB 显存），可以试 vLLM：

```bash
pip install vllm

# 启动 vLLM server
vllm serve Qwen/Qwen2.5-7B-Instruct --port 8000
```

vLLM 比 Ollama 快 5-10 倍，但需要 GPU。

---

## 四、提交物

### 4.1 提交方式

1. Fork 本仓库
2. 在 `labs/lab1-deploy-llm/submission/{your-name}/` 下提交：
   - `chat_with_llm.py`（你修改的版本）
   - `experiment_report.md`（实验报告）
   - `ai-disclosure.md`（AI 使用披露）
3. 提交 Pull Request

### 4.2 实验报告模板

见 [`starter/experiment_report_template.md`](starter/experiment_report_template.md)

报告应包含：

1. **环境信息**：操作系统、Python 版本、模型版本
2. **部署方式**：Ollama / vLLM / API 调用
3. **5 个交通问题的回答 + 评价**（答对/答错/编造）
4. **本地 vs API 对比**（成本、速度、隐私）
5. **遇到的问题与解决方案**
6. **思考题**：Grounded LLM vs 普通 LLM 在交通中的差异

### 4.3 评分标准（20 分）

| 维度 | 分值 | 评分点 |
|---|---|---|
| 部署成功 | 5 | 能本地跑通 Qwen2.5-7B |
| 代码质量 | 5 | Python 代码可运行、有注释 |
| 报告完整 | 5 | 覆盖模板所有部分 |
| 思考深度 | 3 | 有自己的分析、不只是复述 |
| AI 披露 | 2 | `.ai-disclosure.md` 详尽 |

---

## 五、AI 协作指南

### ✅ 允许
- 让 GPT-4 帮你 debug 报错
- 让 LLM 解释 Ollama 文档
- 用 Copilot 写 boilerplate

### ❌ 禁止
- 让 AI 帮你"测试结果"（必须自己测）
- 让 AI 帮你写交通问题的"答对/答错"判断（必须自己判断）
- 让 AI 帮你"生成实验报告"（必须自己写）

### 📋 必披露
- 用 AI 写的代码段
- 用 AI 解释的概念
- 用 AI 调试的过程

---

## 六、常见问题（FAQ）

### Q1: Ollama 下载太慢怎么办？
A: 配置代理或使用国内镜像：
```bash
# 临时设置（Linux/macOS）
export OLLAMA_HOST=https://mirror.ollama.cn
ollama pull qwen2.5:7b
```

### Q2: 模型推理很慢？
A: 检查是否使用了纯 CPU 推理。Ollama 在 Apple Silicon 上会自动用 GPU。如在 Linux 上用 NVIDIA GPU，需安装 CUDA。

### Q3: 端口被占用？
A: 换端口启动：
```bash
OLLAMA_HOST=0.0.0.0:11435 ollama serve
```

### Q4: 显存不够？
A: 用更小的模型（qwen2.5:1.5b）或开启量化：
```bash
ollama pull qwen2.5:7b-q4_0  # 4-bit 量化版本
```

### Q5: 想用 OpenAI API 而不是本地？
A: 把 `starter/chat_with_llm.py` 中的 `base_url` 改为 `https://api.openai.com/v1`，并设置 `OPENAI_API_KEY` 环境变量。

---

## 七、参考资料

- [Ollama 官方文档](https://github.com/ollama/ollama)
- [Qwen2.5 技术报告](https://qwenlm.github.io/blog/qwen2.5/)
- [vLLM 官方文档](https://docs.vllm.ai/)
- [OpenAI API 兼容](https://platform.openai.com/docs/api-reference)

---

## 八、思考题

1. **本地部署 vs API 调用**：在交通治理场景中，哪个更合适？为什么？
2. **模型选择**：对于交通问答任务，1.5B 和 7B 模型效果差距大吗？你怎么看这个 tradeoff？
3. **Grounded 思考**：本地部署的 LLM 如何做到"扎根交通数据"？

---

> 🚀 **下一步**：完成本 Lab 后，你将能熟练调用 LLM，可以开始 Lab 2（搭建 RAG 系统）。
