import { defineConfig } from 'vitepress'

export default defineConfig({
  title: '大模型驱动的城市交通治理技术',
  titleTemplate: ':title | 同济大学交通学院',
  description: 'Grounded LLM for Urban Transportation @ Tongji University',
  lang: 'zh-CN',
  lastUpdated: true,
  cleanUrls: true,
  // GitHub Pages 子路径
  base: '/tongji-llm-urban-transport/',

  // GitHub 信息
  // @ts-ignore
  editLink: {
    pattern: 'https://github.com/runningjian-ui/tongji-llm-urban-transport/edit/main/docs/:path',
    text: '在 GitHub 上编辑此页'
  },

  // 主题配置
  themeConfig: {
    logo: { src: '/logo.svg', alt: 'Tongji LLM Transport' },
    siteTitle: 'LLM × 城市交通',

    nav: [
      { text: '首页', link: '/' },
      { text: '大纲', link: '/syllabus' },
      {
        text: '讲义',
        items: [
          { text: '12 讲总览', link: '/lectures' },
          { text: '第 1 讲：导论', link: '/lectures/01-introduction' },
          { text: '第 2 讲：LLM 机理', link: '/lectures/02-llm-mechanism' },
          { text: '...', link: '/lectures' }
        ]
      },
      { text: '实验', link: '/labs' },
      { text: '项目', link: '/projects' },
      { text: '政策', link: '/policy' }
    ],

    sidebar: {
      '/lectures/': [
        {
          text: '基础与背景',
          items: [
            { text: '1. 导论：Grounded AI', link: '/lectures/01-introduction' },
            { text: '2. LLM 内部机理', link: '/lectures/02-llm-mechanism' },
            { text: '3. 推理大模型', link: '/lectures/03-reasoning-models' }
          ]
        },
        {
          text: '核心技术',
          items: [
            { text: '4. Prompt 与适配', link: '/lectures/04-prompt-adaptation' },
            { text: '5. RAG 进阶', link: '/lectures/05-rag' },
            { text: '6. Agent', link: '/lectures/06-agents' }
          ]
        },
        {
          text: '进阶',
          items: [
            { text: '7. 多智能体', link: '/lectures/07-multi-agent' },
            { text: '8. 多模态 VLM', link: '/lectures/08-multimodal' },
            { text: '9. 端到端 AD', link: '/lectures/09-e2e-ad' }
          ]
        },
        {
          text: '应用与治理',
          items: [
            { text: '10. 治理全景', link: '/lectures/10-applications' },
            { text: '11. 评测', link: '/lectures/11-evaluation' },
            { text: '12. 治理与前沿', link: '/lectures/12-governance-future' }
          ]
        }
      ]
    },

    socialLinks: [
      { icon: 'github', link: 'https://github.com/runningjian-ui/tongji-llm-urban-transport' }
    ],

    footer: {
      message: '基于 CC-BY-SA-4.0 开源',
      copyright: '© 2026 同济大学交通学院 · 李健'
    },

    search: {
      provider: 'local',
      options: {
        miniSearch: {
          searchOptions: { fuzzy: 0.2, prefix: true }
        }
      }
    },

    outline: { level: [2, 3], label: '本页大纲' },

    docFooter: { prev: '上一篇', next: '下一篇' }
  },

  // Markdown 扩展
  markdown: {
    lineNumbers: true,
    theme: { light: 'github-light', dark: 'github-dark' }
  },

  // 死链处理：暂时忽略（等链接优化后再开启）
  ignoreDeadLinks: true,

  // 国际化（先 zh-CN，预留 en）
  locales: {
    'zh-CN': {
      label: '简体中文',
      lang: 'zh-CN',
      themeConfig: {
        outlineTitle: '本页大纲'
      }
    }
  }
})
