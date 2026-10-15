#!/usr/bin/env python3
"""
Auto Commit Script
Generates a random number of commits (1-10 by default) every run.
Compatible with GitHub Actions and local execution.
"""

import os
import random
import subprocess
import sys
from datetime import datetime, timezone, timedelta

# Configuration
MIN_COMMITS = 1
MAX_COMMITS = 10
LOG_FILE = "ACTIVITY.md"
GIT_AUTHOR_NAME = "Isronursalaam"
GIT_AUTHOR_EMAIL = "Isronursalaam@gmail.com"

# Realistic and varied commit message templates
COMMIT_MESSAGES = [
    "chore(activity): update daily activity log",
    "docs(log): refresh timestamp and progress record",
    "refactor(tracker): maintain routine sync entry",
    "perf(sync): register automated contribution pulse",
    "ci(activity): record heartbeat checkpoint",
    "chore(metrics): append daily streak verification",
    "docs(readme): keep repository activity active",
    "feat(routine): log periodic contribution check",
    "style(log): format daily status entries",
    "test(ping): verify repository synchronization"
]

def run_cmd(cmd: list[str], check: bool = True) -> subprocess.CompletedProcess:
    """Run a shell command safely."""
    print(f"-> {' '.join(cmd)}")
    return subprocess.run(cmd, check=check, capture_output=True, text=True)

def ensure_git_identity():
    """Ensure git user name and email are configured for attribution."""
    try:
        name = run_cmd(["git", "config", "user.name"], check=False).stdout.strip()
        email = run_cmd(["git", "config", "user.email"], check=False).stdout.strip()
        if not name:
            run_cmd(["git", "config", "user.name", GIT_AUTHOR_NAME])
        if not email:
            run_cmd(["git", "config", "user.email", GIT_AUTHOR_EMAIL])
    except Exception as e:
        print(f"Warning setting git config: {e}")

def ensure_log_file():
    """Create the log file if it doesn't already exist."""
    if not os.path.exists(LOG_FILE):
        header = (
            "# 📈 Daily Contribution & Activity Tracker\n\n"
            "This repository automatically records daily commits via GitHub Actions and local scripts.\n\n"
            "| # | Date & Time (WIB / UTC+7) | Commit Index | Message | Status |\n"
            "|---|---------------------------|--------------|---------|--------|\n"
        )
        with open(LOG_FILE, "w", encoding="utf-8") as f:
            f.write(header)

def make_commit(index: int, total: int):
    """Update log file and make a single git commit."""
    # Compute timestamps (UTC and WIB / UTC+7)
    utc_now = datetime.now(timezone.utc)
    wib_now = utc_now + timedelta(hours=7)
    wib_str = wib_now.strftime("%Y-%m-%d %H:%M:%S")

    selected_msg = random.choice(COMMIT_MESSAGES)
    commit_msg = f"{selected_msg} [{index}/{total}]"

    # Append to markdown log
    entry = f"| auto | {wib_str} | {index}/{total} | `{commit_msg}` | ✅ recorded |\n"
    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write(entry)

    # Git stage and commit
    run_cmd(["git", "add", LOG_FILE])
    run_cmd([
        "git",
        "-c", f"user.name={GIT_AUTHOR_NAME}",
        "-c", f"user.email={GIT_AUTHOR_EMAIL}",
        "commit",
        "-m", commit_msg
    ])
    print(f"Committed: {commit_msg}")

def main():
    # Random commit count between 1 and 10
    total_commits = random.randint(MIN_COMMITS, MAX_COMMITS)
    print(f"🚀 Starting Auto Commit run: Generating {total_commits} commits today...")

    ensure_git_identity()
    ensure_log_file()

    for i in range(1, total_commits + 1):
        make_commit(i, total_commits)

    print(f"🎉 Successfully created {total_commits} commits!")

    # Check if push requested or running in GitHub Actions
    is_ci = os.getenv("GITHUB_ACTIONS") == "true"
    should_push = "--push" in sys.argv or is_ci

    if should_push:
        print("Pushing commits to remote repository...")
        res = run_cmd(["git", "push"], check=False)
        if res.returncode == 0:
            print("🚀 Commits pushed successfully!")
        else:
            print(f"Failed to push: {res.stderr}")
            if not is_ci:
                print("Make sure your remote 'origin' is set up with 'git remote add origin <url>'")
    else:
        print("💡 Local run complete without --push. Run 'git push' or add '--push' flag to send to GitHub.")

if __name__ == "__main__":
    main()
