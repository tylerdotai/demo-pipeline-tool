# Demo Pipeline Tool

Autonomous demo capture and deployment pipeline for client projects, built to clone apps, run them locally, document them, record walkthroughs, and publish the result.

<p align="center">
  <img src="assets/logo.png" alt="Demo Pipeline Tool logo" width="120"/>
</p>

[![License: Unlicense](https://img.shields.io/badge/License-Unlicense-green.svg)](LICENSE.txt)
[![Codeberg](https://img.shields.io/badge/Deploy-into%20Codeberg-2185D0?style=flat-square&logo=codeberg)](#)

## Live Demo

- Repository: `https://github.com/tylerdotai/demo-pipeline-tool`
- Bash entrypoint: `demo_pipeline.sh`
- Python wrapper: `demo_pipeline.py`

## About

Demo Pipeline Tool automates the end-to-end workflow for capturing product demos from source repositories. It is designed to clone or open a codebase, install dependencies, launch the app, generate project documentation, record the demo flow, and publish the output to Codeberg.

## Tech Stack

| Layer | Technology |
|-------|------------|
| Orchestration | Bash |
| Wrapper | Python |
| Recording | macOS `screencapture` and `osascript` |
| Repo Publishing | Codeberg API |
| Source Support | Git, local repos, common package managers |

## Features

### Pipeline Flow
- Clone or load a source project
- Detect and install dependencies
- Launch the app locally for review
- Generate README-style documentation
- Capture screenshots and screen recordings
- Push the resulting package to Codeberg

### Operator Experience
- Bash-first execution with Python wrapper support
- JSON config file workflow via `example_project.json`
- Built for repeatable internal demo creation

## Project Structure

```text
demo_pipeline.sh       Main pipeline script
demo_pipeline.py       Python wrapper around the bash pipeline
example_project.json   Example config file
assets/logo.png        Project logo
README.md              Repository overview
LICENSE.txt            License file
```

## Getting Started

### Prerequisites

- macOS
- `git`
- `curl`
- Node.js or Python depending on target project type
- A Codeberg account and token for publishing

### Installation

```bash
git clone https://github.com/tylerdotai/demo-pipeline-tool.git
cd demo-pipeline-tool
chmod +x demo_pipeline.sh demo_pipeline.py
```

## Deployment

This tool is intended for local operator use and publishes generated demo artifacts to Codeberg.

- Repository: `https://github.com/tylerdotai/demo-pipeline-tool`

## Usage

```bash
./demo_pipeline.sh \
  --app-name "MyApp" \
  --source "https://github.com/user/repo" \
  --flows "click Login, enter creds, submit form" \
  --codeberg-user "tylerdotai" \
  --codeberg-token "YOUR_TOKEN" \
  --port 3000
```

Or with the Python wrapper:

```bash
python3 demo_pipeline.py --config example_project.json
```

## Current Limitations

- Optimized for macOS because of the screen capture workflow
- Recording still depends on a human performing the guided demo flow
- Publishing target is centered on Codeberg rather than multiple platforms

## Roadmap

- Improve browser focusing and app window targeting
- Add a more interactive UI for flow setup
- Expand artifact publishing beyond the current Codeberg path
- Improve config and credential management

## License

Distributed under the Unlicense. See `LICENSE.txt` for details.
