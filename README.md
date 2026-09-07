# OpenCode Session Header Generator ⚡

批量生成符合 **OpenCode Go / Zen** 网关验证规范的 `x-opencode-session` 标头值。包含开箱即用的轻量 Web 页面与命令行工具。

---

## 📌 背景与规则

OpenCode 近期收紧了 **OpenCode Go** 套餐的风控机制，旨在打击滥用并提升服务端 Prompt Caching 命中率。未携带会话标头或使用泛用 User-Agent 的第三方客户端请求常会遭遇以下报错：

- `HTTP 403 Forbidden`（Cloudflare 客户端指纹拦截）
- `HTTP 400 Bad Request`（如 `Model is unavailable`）
- `HTTP 429 Too Many Requests`（匿名降级严格限流）

### 官方推荐 Headers 配置

在各类客户端（如 NextChat, Chatbox, Cherry Studio 等）的 **自定义 Headers** 中填入：

| Header 名称 | 推荐值 | 作用说明 |
| :--- | :--- | :--- |
| `User-Agent` | `opencode-cli/1.0.0` | 官方客户端标识，绕过 CF 规则拦截 |
| `x-opencode-client` | `cli` | 标明客户端类型 |
| `x-opencode-session` | `<生成的 session 值>` | **核心项**，维持会话上下文与缓存路由 |
| `x-opencode-project` | `default` | 默认项目标识 |

---

## 🚀 使用方法

### 1. Web 页面（手机/电脑极佳体验）

直接双击打开仓库中的 `index.html`：
- 零外部依赖，纯本地原生 JS 运行，秒开无延迟。
- 针对手机端竖屏与暗黑模式深度适配。
- 支持单条点击即复制、一键复制全部。
- 支持 **标准 UUID v4**、**官方 CLI 前缀 (ses_xxx)**、**完整 Header 键值对** 与 **JSON 格式**。

### 2. Python 命令行脚本 (`generate_session.py`)

无需安装任何第三方库，Python 3 原生支持。

```bash
# 默认生成 5 个标准 UUID 格式 Session
python3 generate_session.py

# 生成 10 个官方前缀风格 (ses_...)
python3 generate_session.py -n 10 -t ses

# 生成完整 Header 键值对格式
python3 generate_session.py -n 3 -t header

# 导出为 JSON 格式
python3 generate_session.py -n 5 -t json
```

#### 参数说明
- `-n, --count`: 生成数量（默认 `5`）
- `-t, --type`: 生成格式，可选 `uuid`（默认）、`ses`、`header`、`json`

---

## 📄 开源许可

MIT License © 2026 MorphieEndless
