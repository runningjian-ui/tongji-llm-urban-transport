# 第 1 讲课堂演示代码

## Grounded QA vs Non-Grounded QA

## 准备

```bash
# 安装依赖
pip install -r requirements.txt

# 设置 API key
export OPENAI_API_KEY=sk-...

# 准备数据（任选其一）
# 1. 真实数据：把《上海交通运行报告》PDF 放到 data/ 目录
# 2. Demo 数据：脚本会自动创建 demo_report.txt
```

## 运行

```bash
python grounded_qa.py
```

## 预期输出

脚本会对比两个版本：

### 🔴 不 Grounded 版本
- LLM 自由回答
- 数据可能编造
- 无来源追溯

### 🟢 Grounded 版本
- LLM 基于 RAG 检索
- 每个数据点带引用编号
- 来源可追溯到 PDF 原文章节

## 关键代码点

1. **文档切分**：`RecursiveCharacterTextSplitter`
2. **向量化**：`OpenAIEmbeddings` + `Chroma`
3. **自定义 Prompt**：强制要求 LLM 标注来源
4. **返回 source_documents**：保留可追溯性

## 课堂讲解建议

1. 先演示不 Grounded 版本：让 LLM 自由回答，观察它可能编造数据
2. 再演示 Grounded 版本：每个数据都带 [1]、[2] 引用
3. 让学生思考：如果你们做交通项目，希望是哪种？
4. 引出"Grounded AI 是这门课的主线条"

## 进阶练习

- 换不同 PDF 测试（不同城市交通报告）
- 尝试不同 Embedding 模型（bge-large-zh、m3e 等）
- 增加 ReRank 步骤（用 bge-reranker）
- 尝试 GraphRAG
