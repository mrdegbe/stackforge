
# 🚀 `stackforge`

**One-Click DevOps Templates for African Devs.**

StackForge is a developer-first CLI tool that generates and deploys smart pipelines for your apps — Laravel, Django, React, Flutter, and more — using simple commands and low-cost or free-tier infrastructure.

---

## ✨ Why `stackforge`?

DevOps shouldn't be expensive or confusing for indie developers, students, or small teams — especially across Africa. StackForge bridges that gap with:

- 🌍 Local VPS support (e.g. Contabo)
- ☁️ Free-tier cloud deploy (e.g. Railway, Render)
- 📱 Optional USSD triggers for edge-case deployment
- 🔧 Plug-and-play templates for common stacks

---

## 📦 Features

- Generate CI/CD pipelines for:
  - Laravel
  - Django
  - React
  - Flutter
- Deploy to:
  - Contabo VPS (via SSH)
  - Railway/Render free tiers
- Template customization support
- Offline-first friendly CLI
- USSD-based deployment (for fun & future rural use)

---

## 🛠 Installation

Make sure you have Python 3.10+ and [Poetry](https://python-poetry.org/) installed.

```bash
git clone https://github.com/mrdegbe/stackforge
cd stackforge
poetry install
````

---

## 🚀 Usage

```bash
poetry run python -m cli.main init pipeline
```

You’ll be prompted to choose a framework and deployment target. StackForge will generate the pipeline and configure the files for you.

More commands coming soon:

```bash
stackforge deploy
stackforge debug
stackforge template list
```

---

## 📅 Roadmap

| Feature                    | Status     |
| -------------------------- | ---------- |
| Init pipeline templates    | ✅ Done     |
| Deploy to Contabo VPS      | 🔜 Planned |
| Deploy to Railway/Render   | 🔜 Planned |
| Custom USSD triggers       | 🔜 Planned |
| Pipeline debugging support | 🔜 Planned |
| Template marketplace       | 🔜 Planned |

---

## 💰 Monetization Plan

* Free base templates
* Paid premium templates (queues, auth, multi-stage deploys)
* On-demand debugging support
* Deploy-as-a-service (DaaS) tier

---

## 🤝 Contributing

PRs, issues, and feedback welcome!

```bash
# Format with Black
poetry run black src/
```

---

## 👨🏾‍💻 Created for African Devs

StackForge is proudly built to make DevOps accessible for local developers, campus coders, and small startups across the continent.

> Built with 💡 in Africa.

---

## 📄 License

MIT
