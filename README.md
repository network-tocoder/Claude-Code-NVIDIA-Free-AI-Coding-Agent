# 🤖 Claude Code + NVIDIA — Free AI Coding Agent

![GitHub stars](https://img.shields.io/github/stars/kskroyal/claude-code-nvidia-setup?style=for-the-badge&color=purple)
![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)
![Platform](https://img.shields.io/badge/Platform-Windows%20%7C%20Mac%20%7C%20Linux-blue?style=for-the-badge)
![Cost](https://img.shields.io/badge/Cost-Zero-brightgreen?style=for-the-badge)
![GPU](https://img.shields.io/badge/GPU-Not%20Required-red?style=for-the-badge)
![Model](https://img.shields.io/badge/Model-DeepSeek%20V4%20Flash-76b900?style=for-the-badge)

> **Run Claude Code with NVIDIA's free API. No GPU, no subscription, no credit card. 150+ models including DeepSeek V4 Flash.**

---

## 📺 Watch the Full Video

[![YouTube](https://img.shields.io/badge/YouTube-Watch%20Now-red?style=for-the-badge&logo=youtube)](https://youtube.com/@kskroyal)

> *Built a complete AI Ventures landing page in 6 minutes. 573 lines of code. Zero cost. This repo is the complete setup guide.*

---

## ⚡ What Is This?

Connect **Claude Code** to **NVIDIA's free API** using **LiteLLM** as a translation proxy. Run any of 150+ models — including DeepSeek V4 Flash — without paying a cent.

| Tool | Role |
|------|------|
| 💻 **Claude Code** | Anthropic's terminal-based AI coding agent |
| 🔀 **LiteLLM** | Translation proxy (Anthropic ↔ OpenAI format) |
| 🟢 **NVIDIA NIM API** | Free model hosting platform |
| 🐋 **DeepSeek V4 Flash** | 284B MoE model — coding-optimized, 1M context |

---

## 🖥️ Requirements

| Requirement | Detail |
|------------|--------|
| OS | Windows / Mac / Linux |
| Python | 3.10 or higher |
| Node.js | v18 or higher |
| GPU | ❌ Not required |
| API Key | Free — build.nvidia.com |

---

## 🚀 Installation Guide

### Step 1 — Verify Prerequisites

```bash
python --version
node --version
npm --version
```

Need Python 3.10+. If lower, upgrade below.

<details>
<summary>🪟 Windows — Upgrade Python</summary>

```powershell
winget install Python.Python.3.12
```
Close PowerShell, open a fresh one, verify.
</details>

<details>
<summary>🍎 macOS — Upgrade Python</summary>

```bash
brew install python@3.12
python3 --version
```
</details>

<details>
<summary>🐧 Linux — Upgrade Python</summary>

```bash
sudo apt update
sudo apt install python3.12 python3-pip
python3 --version
```
</details>

---

### Step 2 — Install LiteLLM

```bash
pip install litellm python-dotenv
litellm --version
```

---

### Step 3 — Install Claude Code

```bash
npm install -g @anthropic-ai/claude-code
claude --version
```

---

### Step 4 — Get Your NVIDIA API Key

1. Go to [build.nvidia.com](https://build.nvidia.com)
2. Sign up — free, no credit card required
3. Click profile → **API Keys** → **Generate API Key**
4. Copy your key — starts with `nvapi-`

---

### Step 5 — Create Project Folder

<details>
<summary>🪟 Windows (PowerShell)</summary>

```powershell
mkdir nvidia-claudecode-demo
cd nvidia-claudecode-demo
```
</details>

<details>
<summary>🍎 macOS / 🐧 Linux</summary>

```bash
mkdir nvidia-claudecode-demo && cd nvidia-claudecode-demo
```
</details>

---

### Step 6 — Create `config.yaml`

```yaml
model_list:
  - model_name: "*"
    litellm_params:
      model: nvidia_nim/deepseek-ai/deepseek-v4-flash
      api_base: https://integrate.api.nvidia.com/v1
      api_key: nvapi-YOUR-KEY-HERE

litellm_settings:
  drop_params: true
```

> ⚠️ `drop_params: true` is **critical** — strips Claude-specific parameters NVIDIA rejects.

---

### Step 7 — Configure Claude Code

<details>
<summary>🪟 Windows (PowerShell)</summary>

```powershell
mkdir $env:USERPROFILE\.claude
code $env:USERPROFILE\.claude\settings.json
```
</details>

<details>
<summary>🍎 macOS / 🐧 Linux</summary>

```bash
mkdir -p ~/.claude
nano ~/.claude/settings.json
```
</details>

Paste:

```json
{
  "env": {
    "ANTHROPIC_BASE_URL": "http://localhost:4000",
    "ANTHROPIC_AUTH_TOKEN": "any-key-works"
  }
}
```

---

### Step 8 — Run It

**Terminal 1 — Start LiteLLM proxy:**
```bash
litellm --config config.yaml --port 4000
```

**Terminal 2 — Launch Claude Code:**
```bash
cd nvidia-claudecode-demo
claude
```

Test prompt:
```
write hello world in python
```

Watch Terminal 1 — you'll see requests flowing through to NVIDIA. ✅

---

## 🔧 How It Works

```
You type a prompt in Claude Code
        ↓
Claude Code sends request (Anthropic format) to localhost:4000
        ↓
LiteLLM strips Claude-specific params, converts to OpenAI format
        ↓
LiteLLM forwards to NVIDIA's API → DeepSeek V4 Flash
        ↓
Response flows back through LiteLLM → Claude Code
        ↓
You see the result in your terminal
```

> No GPU on your machine. Models run on NVIDIA's servers.

---

## 🎯 Demo Prompts

### Simple Test
```
write a Python function to calculate fibonacci
```

### Full Use Case — AI Ventures Landing Page
```
Create a modern landing page for "AI Ventures 2026" — showcasing AI technology trends and funding opportunities.

Include:
1. HERO with headline and CTAs
2. KEY STATS (4 cards): $215B Market, 12,000+ Startups, 340% Growth, Top 10 Unicorns
3. AI CATEGORIES grid: Autonomous Agents, LLM Infrastructure, AI Coding Tools, Enterprise AI, Edge AI
4. TOP COMPANIES: OpenAI, Anthropic, Mistral, Cohere, Stability AI
5. INVESTMENT TIMELINE 2024-2026
6. FOOTER

Design:
- Dark theme with purple/blue gradients
- Glass-morphism cards
- Animated stats
- Smooth scroll animations
- Single HTML file with inline CSS/JS

Make it look like a professional VC platform!
```

---

## 📊 NVIDIA Free Tier — What to Know

| Item | Detail |
|------|--------|
| Cost | $0.00 — completely free |
| Rate limit | 40 requests/minute |
| Models | 150+ available, ~50 free endpoints |
| Top picks | DeepSeek V4 Flash/Pro, Llama 3.3, Nemotron, Qwen |
| Monitor | LiteLLM debug logs |

---

## 🐛 Troubleshooting

| Error | Fix |
|-------|-----|
| `401 Unauthorized` | Check API key in `config.yaml` |
| `500 Internal Error` | Add `drop_params: true` to config |
| `Connection refused` | LiteLLM not running — check Terminal 1 |
| `Health check 408` | Normal — sensitive endpoint, API still works |

**Enable debug mode for detailed logs:**
```bash
litellm --config config.yaml --port 4000 --debug
```

---

## 💡 Tips

- **Switch models:** Change `model:` in `config.yaml` to any NVIDIA model
- **Use `.env` for keys:** Use `os.environ/NVIDIA_API_KEY` in config
- **Monitor traffic:** Run with `--debug` flag to see every API call
- **Kill stale Claude config:** `Remove-Item -Recurse -Force "$env:USERPROFILE\.claude"`

---

## 🤝 Contributing

Found an issue or want to add more model configs? Pull requests welcome.

---

## 📄 License

MIT License — free to use, modify, share.

---

## 🔗 Links

[![YouTube](https://img.shields.io/badge/YouTube-KSK%20Royal-red?style=for-the-badge&logo=youtube)](https://youtube.com/@kskroyal)
[![GitHub](https://img.shields.io/badge/GitHub-Follow-black?style=for-the-badge&logo=github)](https://github.com/kskroyal)
[![NVIDIA Build](https://img.shields.io/badge/NVIDIA-Free%20API-76b900?style=for-the-badge&logo=nvidia)](https://build.nvidia.com)
[![Claude Code](https://img.shields.io/badge/Claude%20Code-Docs-orange?style=for-the-badge)](https://docs.claude.com/en/docs/claude-code)
[![LiteLLM](https://img.shields.io/badge/LiteLLM-Docs-purple?style=for-the-badge)](https://docs.litellm.ai)

---

<p align="center">
  <strong>Zero Cost. No GPU. Any Machine.</strong><br/>
  <em>Built with Claude Code + LiteLLM + NVIDIA NIM + DeepSeek V4 Flash</em>
</p>
