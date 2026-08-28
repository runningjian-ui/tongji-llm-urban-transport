# 第 3 讲 讲义：推理大模型

> 🎯 **本讲核心**：让机器"慢慢想"——o1/R1 是范式突破
>
> 📅 上课时间：2026/10/9（五）13:30-15:00 · 嘉定 C208
>
> 👨‍🏫 授课：李健

## 一、本讲目标

1. **理解推理模型与普通模型的区别**
2. **掌握 Test-Time Compute Scaling**
3. **熟悉代表模型**：o1、o3、DeepSeek R1
4. **能选对模型解决复杂交通问题**

## 二、本讲内容

### Part 1：推理大模型现象
- OpenAI o1 的范式突破
- 慢思考 vs 快思考
- "思考过程"的可读性

### Part 2：核心机制
- Test-Time Compute Scaling
- Process Reward Model（PRM）
- 推理路径搜索
- 自我对弈（Self-Play）

### Part 3：代表模型
- OpenAI o1 / o3 系列
- DeepSeek R1（开源）
- Claude Extended Thinking
- Qwen QwQ

### Part 4：交通场景
- 复杂路径规划
- 多目标调度
- 应急车辆协调
- 博弈决策

### Part 5：何时用推理模型
- 决策树：什么时候用
- 成本 vs 收益
- Hybrid 方案

## 三、推荐阅读

- **OpenAI (2024)**. *Learning to Reason with LLMs (o1)*.
- **DeepSeek (2025)**. *DeepSeek R1 Tech Report*.

## 四、本讲作业

**HW 1：应急车辆调度对比实验**
- 对比 GPT-4o-mini vs DeepSeek R1
- 提交 outputs + analysis.md
- ⏰ 截止：W5（10/23）
