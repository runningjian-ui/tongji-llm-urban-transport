# HW 1: 用推理大模型解应急车辆调度

> **对应讲次**：第 3 讲 - 推理大模型
> **难度**：⭐⭐⭐☆☆
> **分值**：10 分
> **截止**：W5 课程结束前

---

## 一、作业目标

通过本作业，你将：

1. ✅ 体验**推理大模型**（如 DeepSeek R1、OpenAI o1）的"慢思考"过程
2. ✅ 对比**普通模型** vs **推理模型**在复杂交通问题上的表现
3. ✅ 理解 Test-Time Compute Scaling 的意义
4. ✅ 学会用 Grounded 思维评估模型输出

---

## 二、问题背景

**应急车辆调度**（Emergency Vehicle Dispatch）是城市交通治理中的重要问题。当某地发生交通事故或突发公共事件时，救护车、消防车需要快速到达现场。路径选择涉及：

- **实时路况**：拥堵程度
- **优先级**：与普通车辆相比的优先权
- **多目标**：最短时间 vs 最少干扰其他交通
- **约束**：单行道、限行、桥梁承重等

**这是一个典型的"多约束、多目标"问题**，正是推理大模型的用武之地。

---

## 三、问题设置

### 3.1 场景描述

> 上海市内某地发生重大交通事故，需要调度 3 辆救护车从 3 个不同的急救中心前往现场。
>
> - **急救中心 A**：新华医院，坐标 (121.42, 31.20)
> - **急救中心 B**：瑞金医院，坐标 (121.46, 31.21)
> - **急救中心 C**：仁济医院，坐标 (121.49, 31.19)
> - **事故现场**：人民广场附近，坐标 (121.47, 31.23)
>
> 每辆救护车需要在 **8 分钟内** 到达现场（急救"白金 10 分钟"原则）。
>
> 当前早高峰时段，市区主要道路严重拥堵，但应急车辆可以借道公交专用道、临时逆行。
>
> 假设你作为交通调度员，请制定调度方案。

### 3.2 具体任务

请 LLM 回答以下 5 个子问题：

1. **路径推荐**：从 3 个急救中心分别推荐最优路径（写明主干道、关键节点）
2. **时间估算**：估算每辆救护车到达时间
3. **优先级决策**：如果救护车 A 路上遇到严重拥堵，是否应改派 B、C？还是等待 A 继续？
4. **风险评估**：在早高峰调度应急车辆，可能带来哪些次生影响（对其他交通流）？
5. **替代方案**：如果救护车无法在 8 分钟内到达现场，应启动什么备用方案？

---

## 四、实验要求

### 4.1 必须测试的模型

| 模型类型 | 模型 | 用途 |
|---|---|---|
| 普通 LLM | GPT-4o-mini（或 Qwen2.5-7B） | 基线 |
| 推理 LLM | DeepSeek R1（或 OpenAI o1-mini） | 推理版 |

### 4.2 对比维度

对每个模型的回答，按以下维度评分（1-5 分）：

| 维度 | 说明 |
|---|---|
| 准确性 | 路径是否符合上海实际路网？ |
| 完整性 | 是否覆盖 5 个子问题？ |
| 推理过程 | 推理模型是否展示了"思考过程"？ |
| 实用性 | 调度方案是否可执行？ |
| Grounded 程度 | 是否引用了具体数据/规则？ |

### 4.3 输出格式

提交一个 `analysis.md`，包含：

1. **模型 A（普通）的回答**（完整粘贴）
2. **模型 B（推理）的回答**（完整粘贴）
3. **对比分析**（每个维度打分 + 理由）
4. **Grounded 评估**（哪个回答更"扎根"上海实际？）

### 4.4 代码要求

提交 `dispatch_solver.py`（或 Jupyter Notebook），实现：
- 调用至少 2 个模型（API）
- 解析 LLM 输出
- 自动评分（可选：手动也行）
- 生成 `analysis.md`

---

## 五、提交物

```
hw1-emergency-dispatch/
└── {your-name}/
    ├── analysis.md              # 主要分析报告
    ├── dispatch_solver.py       # 代码
    ├── outputs/
    │   ├── model_A_response.txt # 普通模型完整输出
    │   └── model_B_response.txt # 推理模型完整输出
    └── ai-disclosure.md         # AI 使用披露
```

**提交方式**：
1. Fork 本仓库
2. 在 `assignments/hw1-emergency-dispatch/{your-name}/` 下提交文件
3. 创建 Pull Request

---

## 六、评分标准（10 分）

| 维度 | 分值 |
|---|---|
| 代码可运行、调用成功 | 2 |
| 两个模型对比完整 | 2 |
| 5 个子问题都有答案 | 2 |
| 对比分析有深度 | 2 |
| AI 披露规范 | 1 |
| 思考有 Grounded 思维 | 1 |

---

## 七、AI 协作指南

### ✅ 强烈建议用 AI
- 写调用 API 的 boilerplate
- 让 LLM 解释推理模型的输出
- 让 AI 帮你设计评分标准

### ⚠️ 谨慎用
- 让 AI 帮你"分析"两个模型的差异（必须自己思考）
- 让 AI 帮你"判断"哪个回答更好

### ❌ 禁止
- 让 AI 替你完成 5 个子问题（这是作业核心）
- 抄袭 AI 生成的"分析"而不修改

### 📋 必披露
- 所有用 AI 写 / 改的代码段
- 所有用 AI 解释的概念
- 任何 AI 直接生成的分析内容

---

## 八、DeepSeek R1 API 使用示例

```python
from openai import OpenAI

client = OpenAI(
    api_key="sk-...",  # DeepSeek API key
    base_url="https://api.deepseek.com/v1"
)

response = client.chat.completions.create(
    model="deepseek-reasoner",  # R1 模型
    messages=[
        {"role": "user", "content": "请解应急车辆调度问题：..."}
    ],
    temperature=0.3
)

# 推理过程在 reasoning_content 字段
print("推理过程：", response.choices[0].message.reasoning_content)
print("最终回答：", response.choices[0].message.content)
```

**OpenAI o1 用法类似**，但 API 调用方式略有不同（见 OpenAI 文档）。

---

## 九、思考题

1. **为什么推理模型在这个问题上可能更优？** 试从算法角度解释
2. **Test-Time Compute**：如果给普通模型更多"思考时间"（如 CoT prompting），能达到推理模型效果吗？
3. **Grounded 现实**：上述场景如果接入上海实时路网数据，模型回答会怎么变？

---

## 十、参考资料

- [DeepSeek R1 Tech Report](https://github.com/deepseek-ai/DeepSeek-R1)
- [OpenAI Learning to Reason with LLMs (o1)](https://openai.com/index/learning-to-reason-with-llms/)
- [Wei et al. (2022). Chain-of-Thought Prompting](https://arxiv.org/abs/2201.11903)
- 上海交通运行报告（公开版）

---

> 🚀 **下一步**：完成本作业后，你将理解推理大模型的核心价值。下一讲（第 4 讲）我们将深入 Prompt 与适配技术。
