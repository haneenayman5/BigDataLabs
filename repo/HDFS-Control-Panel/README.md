# HDFS Control Panel 🖥️

A browser-based GUI for interacting with HDFS (Hadoop Distributed File System) — no terminal required.

## Features

- ▶️ Start / Stop DFS and YARN
- 📂 Browse HDFS paths (`ls`)
- 📄 View file contents (`cat`)
- 📋 Copy and Move files (`cp`, `mv`)
- 📁 Create directories (`mkdir`)
- 🗑️ Delete files and directories (`rm -r`)
- ✅ JPS process checker

## Files

| File | Description |
|------|-------------|
| `app.py` | Flask app — routes and request handling |
| `hdfs_runner.py` | Executes shell commands via `subprocess` |
| `ui.py` | Terminal-style dark HTML/CSS UI template |

## How to Run

### Requirements
```bash
pip install flask
```

### Start the App
```bash
python app.py
```

Then open your browser at: **http://127.0.0.1:5000**

> ⚠️ Must be run on a machine where Hadoop is installed and configured in `~/.bashrc`.

## Screenshots
> *(Add a screenshot of the UI here)*

## UI Design
Dark terminal aesthetic with amber accents. Built entirely with vanilla HTML/CSS — no external frameworks.
