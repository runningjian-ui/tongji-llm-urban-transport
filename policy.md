# 课程政策：AI 使用与学术规范

> **Allowed with disclosure**
> 本课程允许并鼓励在合理范围内使用生成式 AI 工具，但**必须如实披露**。

---

## 一、AI 使用总原则

> "教 GenAI 的课，禁止用 GenAI 是矛盾的。"
> — Prof. Seongjin Choi, UMN

我们采用 **"Allowed with disclosure"** 政策：

✅ **允许**：用 GenAI 协助完成作业、调试代码、生成文档、头脑风暴
❌ **禁止**：完全代写、用 AI 完成"展示能力"的核心任务
📋 **必须**：如实披露使用情况

---

## 二、允许 vs 禁止场景

### ✅ 允许使用 AI 的场景

| 场景 | 示例 | 披露要求 |
|---|---|---|
| 代码辅助 | Cursor / Copilot 写 boilerplate | 在代码注释中标注 |
| Debug | 让 GPT-4 看报错找问题 | 提交时附原始报错 + AI 建议 |
| 文档润色 | 让 Claude 帮你改 README 措辞 | 在 commit message 注明 |
| 头脑风暴 | 让 LLM 列出 10 个可能的研究方向 | 提交 brainstorm log |
| 学习概念 | 用 LLM 解释 Transformer 注意力 | 不需要披露（学习用） |
| 翻译 | 让 LLM 翻译文献 | 注明翻译工具 |
| 数据分析 | 让 LLM 写 SQL / pandas 代码 | 注明 + 解释 |

### ❌ 禁止使用 AI 的场景

| 场景 | 理由 |
|---|---|
| 完全代写作业 | 不展示你的思考 |
| 完全代写项目报告 | 不展示你的写作 |
| 让 AI 完成考试 | 违反学术诚信 |
| 让 AI 假装是你的观点 | 学术欺骗 |
| 抄袭 AI 生成的代码而不理解 | 不能维护、不能改进 |

### ⚠️ 灰色地带（需要谨慎 + 充分披露）

- **生成示例数据**：可，但需标注是合成数据
- **让 AI 写整个函数**：可，但你必须能用自然语言解释每行
- **用 AI 写 PPT 视觉稿**：可，但内容必须是你自己的

---

## 三、披露规范

### 3.1 每次作业必须附 `.ai-disclosure.md`

**模板**：

```markdown
# AI 使用披露

**作业名称**：HW1 - 应急车辆调度
**作者**：[你的名字]
**日期**：2026-XX-XX

## 使用的 AI 工具
- ChatGPT-4o（OpenAI）
- Cursor（IDE 内置）
- DeepSeek R1（API）

## 使用场景

### 1. 代码生成（约占 30%）
- **使用**：让 Cursor 生成 R1 API 调用的 boilerplate
- **Prompt**：`"用 Python 写一个调用 DeepSeek API 的函数，输入是 prompt 字符串，输出是 response 文本"`
- **修改**：我重写了错误处理部分，因为原代码没有处理 rate limit

### 2. Debug（约占 10%）
- **问题**：API 返回 500 错误
- **AI 建议**：检查 API key 是否过期 + 调整 timeout
- **结果**：发现是 timeout 太短，调大到 60s 后解决

### 3. 文献整理（约占 5%）
- **使用**：让 GPT-4 列出 5 篇关于应急调度的论文
- **核实**：我手动在 Google Scholar 验证了每篇都是真实存在的

## 没有使用 AI 的部分
- 问题分析（100% 自己写）
- 实验设计（100% 自己设计）
- 结果讨论（100% 自己写）
- 结论（100% 自己写）

## 个人反思
- AI 大大加快了 boilerplate 编写速度
- 但在算法选择上 AI 建议未必最优，需要自己判断
- 我认为 AI 是工具，不是答案的来源
```

### 3.2 提交格式

- 文件命名：`{hw_name}_ai-disclosure.md`
- 必须随作业一起提交
- 字数不限，但**必须具体到"用在哪一步"**

---

## 四、学术诚信规范

### 4.1 抄袭零容忍
- 抄袭同学作业：0 分 + 通报
- 抄袭网络资源：0 分 + 通报
- 抄袭 AI 生成内容而不披露：按学术不端处理

### 4.2 引用规范
使用 **GB/T 7714—2015** 国标格式：

```bibtex
@article{vaswani2017attention,
  title={Attention is all you need},
  author={Vaswani, Ashish and Shazeer, Noam and Parmar, Niki and others},
  journal={Advances in Neural Information Processing Systems},
  volume={30},
  year={2017}
}
```

正文中：
> Transformer 由 Vaswani 等 [1] 提出，已成为大语言模型的基础架构。

### 4.3 数据使用规范
- 严格遵守各数据集的 License
- 商业数据需先获得授权
- 涉及个人隐私的数据需脱敏

### 4.4 合作规范
- 作业：**个人独立完成**（除明确说明的小组作业）
- 项目：3 人一组，组内分工需在 README 写明
- 引用组员贡献：在文档中明确"X 负责 A，Y 负责 B"

---

## 五、AI 答疑机器人的使用

课程网站接入基于本仓库的 AI 答疑 Bot。

✅ **允许**：问"第 5 讲讲了什么"、"RAG 和 Fine-tuning 怎么选"
❌ **禁止**：问"帮我写作业"、"给我答案"
📋 **记录**：所有问答会被记录，助教可查看异常使用

---

## 六、违规处理

| 违规等级 | 处理 |
|---|---|
| 轻微（未披露但影响小） | 扣 50% 作业分 + 警告 |
| 中等（未披露且有抄袭嫌疑） | 0 分 + 通报 |
| 严重（明确作弊） | 0 分 + 通报 + 教务处记录 |

---

## 七、政策迭代

本政策是**活的文档**，会根据实际情况调整：
- 每学期末收集学生反馈
- 重大调整需在 GitHub Releases 发布说明
- 欢迎提交 PR 改进

---

## 八、参考资料

- UMN "Generative AI for Transportation Research" 政策
- MIT Academic Integrity Handbook
- 同济大学学术规范

---

> **本政策的核心精神**：AI 是放大器，放大的是你自己的能力。披露不是为了限制，而是为了让大家（包括你自己）清楚"我到底做了什么"。
