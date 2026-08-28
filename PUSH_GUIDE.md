# 推送指南

> 5 步把课程仓库从本地推送到 GitHub 并上线。

---

## Step 0: 安装必要工具

你的机器需要：

### ✅ Git（已安装）
```bash
git --version
# 应该是 git version 2.x
```

### ⚠️ Node.js（需要安装）
VitePress 和 Slidev 都依赖 Node.js 18+。

**macOS 安装方法（推荐）**：

```bash
# 方式 1: 用 Homebrew
brew install node

# 方式 2: 用 nvm（更灵活）
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.7/install.sh | bash
nvm install 20
nvm use 20
```

**Linux 安装**：
```bash
curl -fsSL https://deb.nodesource.com/setup_20.x | sudo -E bash -
sudo apt-get install -y nodejs
```

**Windows**：用 [nvm-windows](https://github.com/coreybutler/nvm-windows)

**验证**：
```bash
node --version   # v20.x.x
npm --version    # 10.x.x
```

---

## Step 1: 在 GitHub 创建仓库

1. 打开 https://github.com/new
2. 填写：
   - **Repository name**: `tongji-llm-urban-transport`
   - **Description**: LLM-Powered Urban Transportation Governance @ Tongji University
   - **Public** (公开)
   - ❌ 不要勾选 "Add a README file"（我们已经有本地版本了）
   - ❌ 不要勾选 "Add .gitignore"
   - ❌ 不要选择 License
3. 点击 **Create repository**

---

## Step 2: 关联并推送

在项目目录执行：

```bash
cd /Users/lijian1/.minimax-agent-cn/projects/tongji-llm-urban-transport

# 添加所有文件
git add .

# 首次提交
git commit -m "feat: initialize course repo

- 12 lectures, 4 labs, 8 assignments outline
- VitePress course website
- Slidev slides for lecture 1 (Grounded AI)
- Lab 1: Deploy LLM
- HW 1: Emergency Vehicle Dispatch with Reasoning Models
- Allowed with disclosure AI policy
- GitHub Actions for site deployment and slides build"

# 添加远程仓库
git remote add origin https://github.com/runningjian-ui/tongji-llm-urban-transport.git

# 推送到 main
git branch -M main
git push -u origin main
```

如果要求认证：
- 用 GitHub Personal Access Token (PAT)
- 或用 SSH key

**生成 PAT 方法**：
1. https://github.com/settings/tokens/new
2. 勾选 `repo` 权限
3. 复制 token，用作密码

---

## Step 3: 启用 GitHub Pages

1. 进入 https://github.com/runningjian-ui/tongji-llm-urban-transport/settings/pages
2. **Source**: 选择 "GitHub Actions"
3. 保存

接下来，`.github/workflows/deploy-site.yml` 会自动运行，部署完成后会显示：
- 你的课程网站地址：`https://runningjian-ui.github.io/tongji-llm-urban-transport/`

---

## Step 4: 本地预览（可选但推荐）

安装依赖：
```bash
cd /Users/lijian1/.minimax-agent-cn/projects/tongji-llm-urban-transport
npm install
```

启动课程网站：
```bash
npm run docs:dev
# 访问 http://localhost:5173
```

启动第 1 讲课件：
```bash
npm run slidev:dev
# 访问 http://localhost:3030
```

构建静态文件（用于检查错误）：
```bash
npm run docs:build
npm run slidev:build
```

---

## Step 5: 邀请协作者

如果是团队课程：
1. https://github.com/runningjian-ui/tongji-llm-urban-transport/settings/access
2. 点击 **Add people**
3. 输入助教 GitHub 用户名
4. 选择角色（建议选 **Maintain**）

---

## 🚀 完成后你的成果

✅ 完整的课程仓库（公开可访问）
✅ 自动部署的课程网站
✅ 自动化 CI/CD（部署 / 编译 / 死链检查）
✅ 12 讲的目录结构（先做 1 讲，剩下 11 讲按模板复制）
✅ 4 个 Lab 框架
✅ 8 个作业框架
✅ 10 个项目选题
✅ 完整的 AI 使用政策
✅ 标准的开源协议

---

## ❓ 常见问题

### Q1: 推送时被要求输入密码？
A: GitHub 不再支持密码推送，需要用 PAT 或 SSH key。
- PAT: https://github.com/settings/tokens/new
- SSH: `ssh-keygen -t ed25519`，然后把公钥加到 https://github.com/settings/keys

### Q2: GitHub Actions 部署失败？
A: 检查：
1. Settings → Pages → Source 是否选了 "GitHub Actions"
2. Actions 标签页查看具体错误
3. 大概率是依赖问题，等几分钟后重新 push

### Q3: VitePress build 失败？
A: 本地先 `npm install` 试 `npm run docs:build`，看具体报错。

### Q4: 想换仓库名？
A: Settings → General → Rename。或者：
```bash
git remote set-url origin https://github.com/runningjian-ui/{new-name}.git
```

### Q5: 想私有化？
A: Settings → General → Danger Zone → Change visibility。但注意 GitHub Pages 对私有仓库需要付费。

---

## 📞 遇到问题？

- 在仓库开 Issue：https://github.com/runningjian-ui/tongji-llm-urban-transport/issues
- 邮件：lijian@tongji.edu.cn

---

> 🎉 **祝你开课顺利！**
