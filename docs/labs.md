# Recitation Lab

> 4 次上机实验，助教带实操。每人提交代码 + 报告。

## 实验安排

| Lab | 时间 | 主题 | 工具 | 时长 |
|---|---|---|---|---|
| Lab 1 | W4（第 4 讲后） | 本地部署 LLM | vLLM / Ollama + Qwen2.5-7B | 2h |
| Lab 2 | W6（第 5 讲后） | 搭建 RAG 系统 | LangChain + Chroma | 2h |
| Lab 3 | W11（第 7 讲后） | 多智能体仿真 | CrewAI | 2h |
| Lab 4 | W8（第 9 讲后） | 端到端 AD demo | CARLA | 2h |

## 实验目录

每个 Lab 包含：

```
labX-name/
├── README.md          # 实验手册
├── starter/           # 起始代码（学生 fork）
├── solution/          # 参考答案（助教私有）
└── rubric.md          # 评分标准
```

## 实验手册模板

每个 Lab README 包含：

1. **实验目标**：3-5 条
2. **环境准备**：依赖、安装步骤
3. **任务描述**：分 step，每步 10-30 分钟
4. **提示与坑**：常见错误
5. **提交要求**：代码 + 报告
6. **评分标准**：rubric
7. **AI 协作指南**：哪些可以用 AI

## 运行示例

Lab 1 示例（部署 LLM）：

```bash
# 1. 安装 Ollama
curl -fsSL https://ollama.com/install.sh | sh

# 2. 拉取模型
ollama pull qwen2.5:7b

# 3. 测试对话
ollama run qwen2.5:7b "你好，请介绍下同济大学"

# 4. 启动 API server
ollama serve
# 访问 http://localhost:11434
```

完整实验手册见 [labs/lab1-deploy-llm](../labs/lab1-deploy-llm/README.md)。
