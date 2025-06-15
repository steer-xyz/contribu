# 🧠 ConTribu

**Find. Contribute. Network.**

ConTribu is a CLI tool (and future web app) that helps you get involved in meaningful open-source contributions, tailored to your skills and interests. It’s powered by GitHub’s API, a splash of LLM magic, and your own developer profile.

---

## 💡 What It Does

- Scans GitHub for repos that match your skills/interests
- Uses LLMs to suggest possible contributions (docs, bugs, features)
- Helps you draft high-quality PRs (coming soon)
- Stores your preferences locally so it personalizes everything

This is a passion project I’m building as part of my journey into ML + open source.

---

## 🔧 How It Works

1. You install the CLI.
2. Run `tribu init` to set up your profile.
3. Run `tribu find-repos` to discover relevant projects.
4. (Soon) Run `tribu suggest-prs` to see how you can help.
5. You show up, do the work, and leave the repo better than you found it.

---

## 🚀 Why I’m Building This

I love the idea of contributing to open source, but I hate the “where do I even start?” feeling. So I'm using this tool to scratch my own itch — and if it helps others do the same, even better.

It's also a way for me to:
- Learn to write production-grade Python
- Build CLI and API tooling with real-world UX
- Work with GitHub, LLMs, and contributor discovery workflows

---

## 🛠️ Tech Stack

- Python 3.12+
- [Typer](https://typer.tiangolo.com/) (CLI framework)
- [Rich](https://rich.readthedocs.io/en/stable/) (pretty terminal UI)
- [Pydantic](https://docs.pydantic.dev/) (data models)
- [httpx](https://www.python-httpx.org/) (GitHub API calls)
- FastAPI (coming soon for the web version)

---

## 🗺️ Roadmap

- [x] CLI app with profile setup
- [x] GitHub repo scanner
- [ ] LLM-assisted PR suggestions
- [ ] Web app interface (FastAPI)
- [ ] Social/contributor matching layer

---

## 🧪 Try It Out

```bash
uv venv .venv && source .venv/bin/activate  # or use direnv/poetry/etc
uv add typer rich pydantic httpx
uv run contribu init
uv run contribu find-repos
```
## 🙌 Contributions
This project is still early, but if it resonates with you — ideas, feedback, or even a PR are welcome. Hit me up!

---

## 👋 About Me
I'm a technical senior data analyst at a private real estate investment firm called Faropoint, focusing on investment and market research. Pasisonate about AI engineering and looking to enroll in grad school in the near future. You can find me at steerxyz.bearblog.dev or on X @steerdev.
