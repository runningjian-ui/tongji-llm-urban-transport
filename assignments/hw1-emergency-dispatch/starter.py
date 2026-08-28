"""
HW 1 Starter: 应急车辆调度 - 对比普通 LLM 和推理 LLM

运行前：
1. 设置环境变量
   export DEEPSEEK_API_KEY=sk-...
   export OPENAI_API_KEY=sk-...
2. pip install openai

运行：
python starter.py
"""

import os
import time
from openai import OpenAI


# ============================================================
# 配置
# ============================================================

# DeepSeek R1
DEEPSEEK_CLIENT = OpenAI(
    api_key=os.environ.get("DEEPSEEK_API_KEY"),
    base_url="https://api.deepseek.com/v1"
)

# OpenAI GPT-4o-mini
OPENAI_CLIENT = OpenAI(
    api_key=os.environ.get("OPENAI_API_KEY"),
    base_url="https://api.openai.com/v1"
)


# ============================================================
# 问题
# ============================================================

QUESTION = """
你是上海市交通应急调度专家。请基于专业知识回答应急车辆调度问题。

【场景】
上海市人民广场附近发生重大交通事故，需要从 3 个急救中心调度救护车：
- 急救中心 A：新华医院 (121.42, 31.20)
- 急救中心 B：瑞金医院 (121.46, 31.21)
- 急救中心 C：仁济医院 (121.49, 31.19)
- 事故现场：人民广场 (121.47, 31.23)

要求：每辆救护车 8 分钟内到达（急救白金 10 分钟原则）。
当前：早高峰，市区严重拥堵，但应急车辆可借道公交专用道、临时逆行。

【任务】
请详细回答：
1. 路径推荐：从 3 个急救中心分别推荐最优路径
2. 时间估算：每辆救护车预计到达时间
3. 优先级决策：若 A 路上严重拥堵，是否改派 B、C？
4. 风险评估：早高峰调度应急车辆对其他交通流的影响
5. 替代方案：如救护车无法 8 分钟内到达，启动什么备用方案？

请给出专业、可执行的调度建议。
"""


# ============================================================
# 调用模型
# ============================================================

def call_gpt4o_mini(question: str) -> str:
    """调用 GPT-4o-mini（普通模型）"""
    print("🔵 调用 GPT-4o-mini ...")
    start = time.time()

    response = OPENAI_CLIENT.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": question}],
        temperature=0.3,
        max_tokens=2000
    )

    elapsed = time.time() - start
    answer = response.choices[0].message.content
    print(f"   ✅ 完成，耗时 {elapsed:.1f}s")
    return answer


def call_deepseek_r1(question: str) -> dict:
    """调用 DeepSeek R1（推理模型）"""
    print("🧠 调用 DeepSeek R1 ...")
    start = time.time()

    response = DEEPSEEK_CLIENT.chat.completions.create(
        model="deepseek-reasoner",
        messages=[{"role": "user", "content": question}],
        temperature=0.3,
        max_tokens=4000
    )

    elapsed = time.time() - start
    result = {
        "reasoning": response.choices[0].message.reasoning_content,
        "answer": response.choices[0].message.content,
    }
    print(f"   ✅ 完成，耗时 {elapsed:.1f}s")
    print(f"   📝 推理过程长度：{len(result['reasoning'])} chars")
    print(f"   📝 最终答案长度：{len(result['answer'])} chars")
    return result


# ============================================================
# 主流程
# ============================================================

def main():
    print("🚨 HW 1: 应急车辆调度 - 对比实验")
    print("=" * 60)

    if not os.environ.get("DEEPSEEK_API_KEY"):
        print("⚠️ 未设置 DEEPSEEK_API_KEY")
        return
    if not os.environ.get("OPENAI_API_KEY"):
        print("⚠️ 未设置 OPENAI_API_KEY")
        return

    # 调用两个模型
    gpt_answer = call_gpt4o_mini(QUESTION)
    r1_result = call_deepseek_r1(QUESTION)

    # 保存结果
    os.makedirs("outputs", exist_ok=True)

    with open("outputs/model_A_response.txt", "w", encoding="utf-8") as f:
        f.write("=" * 60 + "\n")
        f.write("模型 A: GPT-4o-mini（普通模型）\n")
        f.write("=" * 60 + "\n\n")
        f.write(gpt_answer)

    with open("outputs/model_B_response.txt", "w", encoding="utf-8") as f:
        f.write("=" * 60 + "\n")
        f.write("模型 B: DeepSeek R1（推理模型）\n")
        f.write("=" * 60 + "\n\n")
        f.write("【推理过程】\n")
        f.write(r1_result["reasoning"])
        f.write("\n\n【最终答案】\n")
        f.write(r1_result["answer"])

    print("\n💾 结果已保存到 outputs/")
    print("\n📊 下一步：")
    print("   1. 阅读 outputs/model_A_response.txt 和 model_B_response.txt")
    print("   2. 填写 analysis.md，对比两个模型的回答")
    print("   3. 提交 hw1-emergency-dispatch/{your-name}/")


if __name__ == "__main__":
    main()
