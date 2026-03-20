# Demo Pipeline Tool

<!-- Improved compatibility of back to top link: See: https://github.com/othneildrew/Best-README-Template/pull/73 -->
<a id="readme-top"></a>

[![Codeberg][codeberg-shield]][codeberg-url]
[![License][license-shield]][license-url]

<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/tylerdotai/demo-pipeline-tool">
    <img src="assets/logo.png" alt="Logo" width="80" height="80">
  </a>

  <h3 align="center">Hoss Demo Pipeline Tool</h3>

  <p align="center">
    Autonomous end-to-end demo & deployment pipeline for client projects.
    <br />
    Clone → Build → Document → Record → Deploy to Codeberg.
    <br />
    <br />
    <a href="https://github.com/tylerdotai/demo-pipeline-tool"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="https://github.com/tylerdotai/demo-pipeline-tool">View Demo</a>
    &middot;
    <a href="https://github.com/tylerdotai/demo-pipeline-tool/issues/new?labels=bug&template=bug-report---.md">Report Bug</a>
    &middot;
    <a href="https://github.com/tylerdotai/demo-pipeline-tool/issues/new?labels=enhancement&template=feature-request---.md">Request Feature</a>
  </p>
</div>

---

## About The Project

Built by **Hoss** — an autonomous Developer Relations and QA Agent running on a Mac mini. This tool automates the entire lifecycle of capturing client demos: cloning repos, installing dependencies, launching apps, recording the screen, generating documentation, and deploying to Codeberg.

**What it does (5 phases):**

| Phase | Step |
|-------|------|
| **1** | Clone/download source, install deps, start dev server |
| **2** | Analyze codebase, auto-generate `README.md` |
| **3** | Capture screenshots + record screencast demo (via `screencapture`) |
| **4** | Create Codeberg repo via API, push everything |
| **5** | Report live URL, stop dev server |

<p align="right">(<a href="#readme-top">back to top</a>)</p>

---

## Getting Started

### Prerequisites

- macOS (for `screencapture`, `osascript`)
- `git`
- `curl`
- Node.js / Python 3 / pip (depending on project type)

### Installation

1. Clone this repo:
   ```sh
   git clone https://github.com/tylerdotai/demo-pipeline-tool.git
   cd demo-pipeline-tool
   ```

2. Make scripts executable:
   ```sh
   chmod +x demo_pipeline.sh demo_pipeline.py
   ```

<p align="right">(<a href="#readme-top">back to top</a>)</p>

---

## Usage

### Option 1 — Bash (all arguments inline)

```bash
./demo_pipeline.sh \
  --app-name "MyApp" \
  --source "https://github.com/user/repo" \
  --flows "click Login, enter creds, submit form" \
  --codeberg-user "tylerdotai" \
  --codeberg-token "YOUR_TOKEN" \
  --port 3000
```

### Option 2 — Python wrapper (JSON config)

```bash
python3 demo_pipeline.py --config project.json
```

**`project.json` format:**
```json
{
    "app_name": "MyApp",
    "source": "https://github.com/user/repo",
    "source_type": "git",
    "local_path": "/path/to/local/repo",
    "flows": "create a board, add a card, drag between lists",
    "codeberg_user": "tylerdotai",
    "codeberg_token": "YOUR_TOKEN",
    "port": 3000,
    "package_manager": "npm"
}
```

### Phase 3: Demo Recording

During Phase 3, the script will:
1. Open the app in the browser and maximize the window
2. Start a background screen recording via `screencapture -v`
3. **Prompt you to manually perform the demo flows** (30–60 seconds)
4. Stop recording when you press Enter

> **Tip:** Have your browser/app ready and windowed before starting. The recording captures whatever is on screen.

### Output Structure

```
~/Desktop/client_demos/{App_Name}/
├── README.md
├── assets/
│   ├── demo.mp4        ← screen recording
│   └── screenshots/
│       ├── screen_1.png
│       ├── screen_2.png
│       ├── screen_3.png
│       └── screen_4.png
└── {source code}
```

<p align="right">(<a href="#readme-top">back to top)</a></p>

---

## Demo & Assets

> Visual demo and UI screenshots captured during automated demo run.

**Screen Recording:** `./assets/demo.mp4`

**Screenshots:** `./assets/screenshots/`

<p align="right">(<a href="#readme-top">back to top</a>)</p>

---

## Roadmap

- [x] Core 5-phase pipeline
- [x] Bash + Python wrapper
- [x] Codeberg API repo creation
- [x] Automatic dependency detection (npm, pip, cargo, go)
- [ ] Auto-detect browser and focus app window
- [ ] Interactive TUI for flow configuration
- [ ] Upload assets to Codeberg Releases automatically
- [ ] Config file support for credentials (env file, not JSON)

<p align="right">(<a href="#readme-top">back to top</a>)</p>

---

## Contributing

Contributions are welcome! Open an issue or submit a PR.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<p align="right">(<a href="#readme-top">back to top</a>)</p>

---

## License

Distributed under the Unlicense License. See `LICENSE.txt` for more information.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

---

## Contact

**Tyler Delano** — [@TheTylerBueno](https://twitter.com/TheTylerBueno) — tyler.delano@icloud.com

**Project Link:** [https://github.com/tylerdotai/demo-pipeline-tool](https://github.com/tylerdotai/demo-pipeline-tool)

<p align="right">(<a href="#readme-top">back to top</a>)</p>

---

<!-- MARKDOWN LINKS & IMAGES -->
[codeberg-shield]: https://img.shields.io/badge/Codeberg-otherwise?logo=codeberg&style=for-the-badge
[codeberg-url]: https://github.com/tylerdotai/demo-pipeline-tool
[license-shield]: https://img.shields.io/github/license/tylerdotai/demo-pipeline-tool?style=for-the-badge
[license-url]: https://github.com/tylerdotai/demo-pipeline-tool/blob/main/LICENSE
