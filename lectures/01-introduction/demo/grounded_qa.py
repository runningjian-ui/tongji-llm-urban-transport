"""
第 1 讲课堂演示：Grounded QA vs Non-Grounded QA

目标：演示 Grounded LLM（带引用源）和不 Grounded LLM（自由回答）的差异

使用：
- LangChain + Chroma 做 RAG
- OpenAI / DeepSeek / 任何 OpenAI 兼容 API

运行：
    pip install langchain langchain-openai chromadb pypdf
    export OPENAI_API_KEY=sk-...
    python grounded_qa.py
"""

import os
from pathlib import Path
from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings, ChatOpenAI
from langchain_community.vectorstores import Chroma
from langchain.chains import RetrievalQA
from langchain.prompts import PromptTemplate

# ============================================================
# 1. 准备数据
# ============================================================

DATA_DIR = Path("./data")
PDF_PATH = DATA_DIR / "shanghai_traffic_report_2024.pdf"  # 学生需自行准备

# 创建一个 demo PDF（如果没有真实数据）
def create_demo_pdf():
    """如果没有真实 PDF，创建一个简单的 demo 文档"""
    if PDF_PATH.exists():
        return

    DATA_DIR.mkdir(exist_ok=True)

    # 这里只是占位，实际使用请准备真实 PDF
    # 例如：上海市交通委员会发布的《2024 上海交通运行年度报告》
    demo_content = """
    2024 年上海交通运行报告（节选）

    一、早高峰运行情况
    2024 年上海工作日早高峰（7:00-9:00）中心城快速路平均速度为 32.5 km/h，
    较 2023 年下降 2.1%。其中内环高架路早高峰拥堵指数达到 7.2（轻度拥堵）。

    二、晚高峰运行情况
    晚高峰（17:00-19:00）拥堵指数为 6.8，较 2023 年下降 1.5%。
    全市最拥堵路段前三位：
    1. 内环高架路（外滩至共和新路段）
    2. 南北高架路（内江路至中山北路）
    3. 延安高架路（虹桥至外滩）

    三、轨道交通
    2024 年上海轨道交通日均客运量 1100 万人次，较 2023 年增长 8.3%。
    早高峰地铁 1、2、9 号线最为拥挤，平均拥挤度达到 130%。
    """
    (DATA_DIR / "demo_report.txt").write_text(demo_content, encoding="utf-8")
    print(f"⚠️ 未找到 {PDF_PATH}，已生成 demo 文本：{DATA_DIR}/demo_report.txt")
    print("   实际演示请准备真实的《上海交通运行报告》PDF")


# ============================================================
# 2. 构建 RAG 系统（Grounded 版本）
# ============================================================

def build_rag_system():
    """构建基于 RAG 的 Grounded QA 系统"""

    # 加载文档
    if PDF_PATH.exists():
        loader = PyPDFLoader(str(PDF_PATH))
        documents = loader.load()
    else:
        # 退化为文本
        from langchain.schema import Document
        text = (DATA_DIR / "demo_report.txt").read_text(encoding="utf-8")
        documents = [Document(page_content=text, metadata={"source": "demo_report.txt"})]

    # 文本切分
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=50,
        separators=["\n\n", "\n", "。", "；", " ", ""]
    )
    chunks = text_splitter.split_documents(documents)
    print(f"✅ 文档切分完成：{len(chunks)} 个 chunks")

    # 向量化 + 存储
    embeddings = OpenAIEmbeddings(
        model="text-embedding-3-small",
        openai_api_key=os.environ.get("OPENAI_API_KEY")
    )
    vectorstore = Chroma.from_documents(
        documents=chunks,
        embedding=embeddings,
        persist_directory="./chroma_db"
    )
    print(f"✅ 向量化完成，已存储到 ./chroma_db")

    # 自定义 Prompt：要求 LLM 引用来源
    prompt_template = """你是交通领域专家。请基于以下参考资料回答用户问题。

【重要】回答时必须：
1. 每个数据点都要标注来源（如 [1]、[2]）
2. 回答末尾列出所有引用的来源
3. 如果参考资料中没有答案，请明确说"资料中未找到"

参考资料：
{context}

用户问题：{question}

回答格式：
[回答内容，每个数据带来源编号]

引用来源：
[1] [来源 1]
[2] [来源 2]
...

请开始回答："""

    PROMPT = PromptTemplate(
        template=prompt_template,
        input_variables=["context", "question"]
    )

    # 构建 QA 链
    llm = ChatOpenAI(
        model="gpt-4o-mini",
        temperature=0,
        openai_api_key=os.environ.get("OPENAI_API_KEY")
    )

    qa_chain = RetrievalQA.from_chain_type(
        llm=llm,
        chain_type="stuff",
        retriever=vectorstore.as_retriever(search_kwargs={"k": 3}),
        chain_type_kwargs={"prompt": PROMPT},
        return_source_documents=True
    )

    return qa_chain


# ============================================================
# 3. 对比演示
# ============================================================

def demo_comparison():
    """演示 Grounded vs 不 Grounded 的差异"""

    question = "上海内环高架路早高峰几点最堵？拥堵指数是多少？"

    print("\n" + "="*60)
    print(f"❓ 问题：{question}")
    print("="*60)

    # ------------------ 版本 A: 不 Grounded ------------------
    print("\n🔴 【不 Grounded 版本】直接问 LLM（不提供资料）")
    print("-"*60)

    from langchain_openai import ChatOpenAI
    from langchain.schema import HumanMessage

    llm = ChatOpenAI(
        model="gpt-4o-mini",
        openai_api_key=os.environ.get("OPENAI_API_KEY")
    )
    response = llm.invoke([HumanMessage(content=question)])
    print(response.content)
    print("\n⚠️ 问题：回答中的数据有依据吗？能验证吗？")

    # ------------------ 版本 B: Grounded ------------------
    print("\n\n🟢 【Grounded 版本】RAG + 引用源")
    print("-"*60)

    try:
        qa_chain = build_rag_system()
        result = qa_chain({"query": question})

        print(result["result"])
        print("\n📚 【来源追溯】")
        for i, doc in enumerate(result["source_documents"], 1):
            print(f"\n[{i}] 来源: {doc.metadata.get('source', 'N/A')}")
            print(f"    内容: {doc.page_content[:200]}...")
    except Exception as e:
        print(f"⚠️ RAG 系统构建失败：{e}")
        print("   请检查 API key 和 PDF 路径")


# ============================================================
# 4. 入口
# ============================================================

if __name__ == "__main__":
    print("🚦 第 1 讲课堂演示：Grounded QA")
    print("="*60)

    # 检查环境
    if not os.environ.get("OPENAI_API_KEY"):
        print("⚠️ 未设置 OPENAI_API_KEY 环境变量")
        print("   export OPENAI_API_KEY=sk-...")
        print("   演示将无法运行 RAG 部分")

    create_demo_pdf()
    demo_comparison()
