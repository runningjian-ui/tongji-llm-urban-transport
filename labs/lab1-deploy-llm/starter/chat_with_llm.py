"""
Lab 1 Starter: 通过本地 Ollama 与 LLM 对话

运行前准备：
1. 安装 Ollama：https://ollama.com/download
2. 拉取模型：ollama pull qwen2.5:7b
3. 启动 server：ollama serve（另开终端）
4. 安装依赖：pip install -r requirements.txt
5. 运行：python chat_with_llm.py
"""

import os
import time
import requests
from typing import List, Dict


# ============================================================
# 配置
# ============================================================

OLLAMA_BASE_URL = os.environ.get("OLLAMA_BASE_URL", "http://localhost:11434")
MODEL_NAME = os.environ.get("MODEL_NAME", "qwen2.5:7b")


# ============================================================
# LLM 客户端
# ============================================================

class LocalLLM:
    """本地 Ollama LLM 客户端（OpenAI 兼容 API）"""

    def __init__(self, base_url: str = OLLAMA_BASE_URL, model: str = MODEL_NAME):
        self.base_url = base_url
        self.model = model
        self.api_url = f"{base_url}/v1/chat/completions"
        self.total_tokens = 0

    def chat(self, messages: List[Dict[str, str]], temperature: float = 0.7) -> str:
        """
        与 LLM 对话

        Args:
            messages: OpenAI 格式的对话历史，例如 [{"role": "user", "content": "..."}]
            temperature: 采样温度，0 = 确定性，1 = 多样性

        Returns:
            LLM 的回复文本
        """
        payload = {
            "model": self.model,
            "messages": messages,
            "temperature": temperature,
        }

        start_time = time.time()
        try:
            response = requests.post(self.api_url, json=payload, timeout=60)
            response.raise_for_status()
            result = response.json()
            elapsed = time.time() - start_time

            content = result["choices"][0]["message"]["content"]
            usage = result.get("usage", {})
            tokens = usage.get("total_tokens", 0)
            self.total_tokens += tokens

            print(f"   ⏱️  {elapsed:.2f}s | 🪙 {tokens} tokens")
            return content

        except requests.exceptions.ConnectionError:
            return "❌ 连接失败：请确认 Ollama 已启动（运行 `ollama serve`）"
        except Exception as e:
            return f"❌ 调用失败：{e}"

    def is_available(self) -> bool:
        """检查 Ollama 是否可用"""
        try:
            response = requests.get(f"{self.base_url}/v1/models", timeout=5)
            return response.status_code == 200
        except:
            return False

    def list_models(self) -> list:
        """列出已下载的模型"""
        try:
            response = requests.get(f"{self.base_url}/v1/models", timeout=5)
            return [m["id"] for m in response.json()["data"]]
        except:
            return []


# ============================================================
# 演示
# ============================================================

def demo():
    """演示与 LLM 对话"""

    llm = LocalLLM()

    print("🚦 Lab 1: 本地 LLM 对话演示")
    print("=" * 60)

    # 检查连接
    print(f"\n🔌 检查 Ollama 连接：{OLLAMA_BASE_URL}")
    if not llm.is_available():
        print(f"❌ Ollama 未启动或无法访问")
        print(f"   请运行：ollama serve")
        return

    print(f"✅ Ollama 已连接")
    models = llm.list_models()
    print(f"📦 已下载模型：{models}")

    if MODEL_NAME not in models:
        print(f"⚠️ 模型 {MODEL_NAME} 未找到")
        print(f"   请运行：ollama pull {MODEL_NAME}")
        return

    print(f"✅ 使用模型：{MODEL_NAME}")

    # 系统提示
    system_prompt = {
        "role": "system",
        "content": "你是交通领域的专家，擅长用简洁准确的语言回答问题。"
    }

    # 5 个交通领域问题
    questions = [
        "解释什么是'信号配时'，并说明它的优化目标。",
        "上海外滩附近有几个地铁站？请列出名字。",
        "列出 3 种常见的交通需求预测方法，并简述其优缺点。",
        "ITS 是什么？它在城市交通治理中起什么作用？",
        "简述 RAG（检索增强生成）在交通领域的应用场景。",
    ]

    results = []

    for i, q in enumerate(questions, 1):
        print(f"\n📝 问题 {i}：{q}")
        print("-" * 60)

        answer = llm.chat([system_prompt, {"role": "user", "content": q}])
        print(f"🤖 回答：{answer}")

        # ⭐ TODO: 在这里评估回答质量
        # 提示：你可以问自己：这个回答答对了吗？有没有编造？
        quality = input("\n   评价 [g=好/o=一般/b=编造/不确定]: ").strip().lower()
        quality_map = {"g": "good", "o": "ok", "b": "bad", "": "unknown"}
        quality = quality_map.get(quality, quality)

        results.append({
            "question": q,
            "answer": answer,
            "quality": quality
        })

    # 输出统计
    print("\n" + "=" * 60)
    print("📊 统计")
    print("=" * 60)
    print(f"   - 总问题数：{len(questions)}")
    print(f"   - 总 token 数：{llm.total_tokens}")
    print(f"   - 模型：{MODEL_NAME}")

    quality_count = {"good": 0, "ok": 0, "bad": 0, "unknown": 0}
    for r in results:
        quality_count[r["quality"]] += 1
    print(f"   - 质量分布：{quality_count}")

    # 保存到文件
    import json
    with open("lab1_results.json", "w", encoding="utf-8") as f:
        json.dump(results, f, ensure_ascii=False, indent=2)
    print(f"\n💾 结果已保存到 lab1_results.json")


# ============================================================
# 进阶：交互式对话
# ============================================================

def interactive():
    """交互式对话模式"""
    llm = LocalLLM()
    print("🚦 进入交互模式（输入 'quit' 退出）\n")

    messages = [{"role": "system", "content": "你是交通领域的专家。"}]

    while True:
        user_input = input("👤 你: ").strip()
        if user_input.lower() in ["quit", "exit", "q"]:
            break
        if not user_input:
            continue

        messages.append({"role": "user", "content": user_input})
        response = llm.chat(messages)
        print(f"🤖 LLM: {response}\n")
        messages.append({"role": "assistant", "content": response})


# ============================================================
# 入口
# ============================================================

if __name__ == "__main__":
    import sys
    if len(sys.argv) > 1 and sys.argv[1] == "interactive":
        interactive()
    else:
        demo()
