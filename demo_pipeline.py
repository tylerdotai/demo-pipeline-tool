#!/usr/bin/env python3
"""
Hoss Demo Pipeline — Python Wrapper
====================================
Run the demo pipeline with a JSON config file.

Usage:
    python3 demo_pipeline.py --config project.json

Config format (project.json):
{
    "app_name": "MyApp",
    "source": "https://github.com/user/repo",
    "source_type": "git",              # "git" | "local"
    "local_path": "/path/to/repo",    # only if source_type=local
    "flows": "click Login, enter creds, submit form",
    "codeberg_user": "tylerdotai",
    "codeberg_token": "YOUR_TOKEN",
    "port": 3000,
    "package_manager": "npm"           # "npm" | "pip" | "cargo" | "go" | "auto"
}
"""

import argparse
import json
import subprocess
import os
import sys
import time
import signal

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
BASH_PIPELINE = os.path.join(SCRIPT_DIR, "demo_pipeline.sh")


def run_pipeline(config: dict) -> int:
    cmd = [
        BASH_PIPELINE,
        "--app-name", config["app_name"],
        "--source", config["source"],
        "--flows", config.get("flows", "navigate and explore main UI"),
        "--codeberg-user", config["codeberg_user"],
        "--codeberg-token", config["codeberg_token"],
        "--port", str(config.get("port", 3000)),
    ]

    print(f"Running: {' '.join(cmd)}")
    result = subprocess.run(cmd)
    return result.returncode


def main():
    parser = argparse.ArgumentParser(description="Hoss Demo Pipeline")
    parser.add_argument("--config", required=True, help="Path to project config JSON")
    args = parser.parse_args()

    with open(args.config, "r") as f:
        config = json.load(f)

    # Validate required fields
    required = ["app_name", "source", "codeberg_user", "codeberg_token"]
    missing = [k for k in required if k not in config or not config[k]]
    if missing:
        print(f"ERROR: Missing required config fields: {missing}")
        sys.exit(1)

    # Resolve source
    if config.get("source_type") == "local":
        config["source"] = config["local_path"]

    exit_code = run_pipeline(config)
    sys.exit(exit_code)


if __name__ == "__main__":
    main()
