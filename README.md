
# ⚡ StackForge

**One-Click DevOps Templates for Devs.**

StackForge helps solo devs, student teams, and scrappy startups deploy full-stack apps with zero DevOps headaches.

---

## ✨ Why StackForge?

DevOps shouldn't be expensive or confusing for indie developers, students, or small teams — especially across Africa. StackForge bridges that gap with:

- 🌍 Local VPS support (e.g. Contabo)
- ☁️ Free-tier cloud deploy (e.g. Railway, Render)
- 📱 Optional USSD triggers for edge-case deployment
- 🔧 Plug-and-play templates for common stacks

---

## 🚀 What It Does
- Generates ready-to-use deployment pipelines for:
  - Laravel, Django, React, Flutter, etc.
- Supports:
  - Local VPS (e.g. Contabo)
  - Free-tier cloud (e.g. Railway, Render)
- Optional:
  - USSD deployment triggers for fun or edge cases

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
# Clone and enter the repo
git clone https://github.com/mrdegbe/stackforge.git
cd stackforge

# Install dependencies with Poetry
poetry install

# Run CLI
poetry run python -m cli.main
````

---

## 🧪 Example Usage

### ✅ Generate Pipeline with Framework + Target

```bash
poetry run python -m cli.main init pipeline --framework laravel --target railway
```

### ✅ Or Use Template Name Directly

```bash
poetry run python -m cli.main init pipeline --template laravel-railway
```
---

## 📦 CLI Commands

#### `init pipeline`

Generates a pipeline file based on the selected stack.

Options:

* `--framework` – e.g. `django`, `laravel`
* `--target` – e.g. `render`, `railway`
* `--template` – (alternative) full template name like `django-render`

Examples:

```bash
# With separate options
stackforge init pipeline --framework django --target render

# Or using a single template name
stackforge init pipeline --template laravel-railway
```

---

#### `list templates`

Lists all available templates:

```bash
stackforge list templates
```

Example output:

```
Available templates:
• laravel-railway
• django-render
• react-railway
• flutter-render
```
---
## 🔜 Roadmap

* [x] Init CLI with Typer
* [x] Support `--framework` + `--target` or `--template`
* [x] `list templates` command
* [ ] USSD deploy trigger (experimental)
* [ ] Backend API to serve cloud templates
* [ ] Web dashboard for preview & customization
* [ ] `stackforge deploy` (auto-deploy via GitHub Actions)


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

## 👨🏾‍💻 Created for Devs

StackForge is proudly built to make DevOps accessible for local developers, campus coders, and small startups.

> Built with 💡 in Africa.

---

## 📄 License

MIT
