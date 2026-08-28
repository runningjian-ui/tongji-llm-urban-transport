#!/bin/bash
# 推送到 GitHub 脚本
# 运行：./push.sh

set -e

cd /Users/lijian1/.minimax-agent-cn/projects/tongji-llm-urban-transport

echo "🔗 关联远程仓库..."
git remote remove origin 2>/dev/null || true
git remote add origin https://github.com/runningjian-ui/tongji-llm-urban-transport.git

echo "📝 确认 main 分支..."
git branch -M main

echo "🚀 推送到 GitHub..."
git push -u origin main

echo ""
echo "✅ 推送完成！"
echo ""
echo "🌐 接下来在 GitHub 启用 Pages："
echo "   https://github.com/runningjian-ui/tongji-llm-urban-transport/settings/pages"
echo "   Source: GitHub Actions"
echo ""
echo "⏳ 然后等 1-2 分钟，Actions 会自动部署网站到："
echo "   https://runningjian-ui.github.io/tongji-llm-urban-transport/"
