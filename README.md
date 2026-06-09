<div align="center">
  <h2 align="center">Automation Toolbox</h2>

  <p align="center">
    <strong>A lightweight collection of Python and Bash scripts for automating common system administration chores: file organization, directory backup with retention, and real-time resource monitoring.</strong>
    <br />
    <br />
    <a href="https://github.com/elbrunis/automation-toolbox/issues">Report Bug</a>
    ·
    <a href="https://github.com/elbrunis/automation-toolbox/issues">Request Feature</a>
  </p>

  <p align="center">
    <img src="https://img.shields.io/badge/License-MIT-blue.svg" alt="License">
    <img src="https://img.shields.io/badge/Build-Passing-brightgreen.svg" alt="Build Status">
  </p>
</div>

## 📑 Table of Contents
- [✨ Key Features](#-key-features)
- [🛠 Tech Stack](#-tech-stack)
- [🚀 Getting Started](#-getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [💡 Usage](#-usage)
- [🗺 Roadmap](#-roadmap)
- [🤝 Contributing](#-contributing)
- [📄 License](#-license)

---

## ✨ Key Features
* **File Organizer:** Scans a target directory and automatically moves files into categorized subfolders (Images, Documents, Videos, Compressed, Executables, Installers) based on file extension.
* **Auto Backup with Retention:** Compresses a source directory into a timestamped `.zip` archive and automatically purges backups older than 7 days (configurable).
* **System Resource Monitor:** Displays a colorized real-time dashboard showing CPU load, RAM usage, disk usage, and the top-5 CPU-consuming processes.
* **Cron-Ready:** All scripts are designed to be scheduled via `cron` for hands-free automation.

---

## 🛠 Tech Stack

| Category | Technologies |
| :--- | :--- |
| **Core** | Python 3, Bash |
| **Tools** | POSIX utilities (`top`, `free`, `df`, `ps`, `awk`) |

---

## 🚀 Getting Started

Follow these instructions to set up the project locally.

### Prerequisites
* Python 3
* Bash (`/bin/bash`)
* Standard POSIX tools (pre-installed on all Linux distributions)

### Installation

1. Clone the repository:
```bash
git clone https://github.com/elbrunis/automation-toolbox.git
```

2. Make the shell script executable:
```bash
cd automation-toolbox
chmod +x monitor.sh
```

No additional dependencies required — all Python scripts use only the standard library.

---

## 💡 Usage

**File Organizer:**
```bash
python3 organizer.py
```

**Auto Backup:**
```bash
python3 backup.py
```

**System Monitor:**
```bash
./monitor.sh
```

**Schedule with Cron:**
```bash
crontab -e
# Add: 0 20 * * * /usr/bin/python3 /path/to/backup.py
```

---

## 🗺 Roadmap

- [ ] Add CLI argument parsing for configurable paths
- [ ] Implement logging to file
- [ ] Add email/Slack notifications for backup status

---

## 🤝 Contributing

Contributions are welcome! Feel free to open an issue or submit a pull request.

---

## 📄 License

Distributed under the MIT License. See `LICENSE` for more information.
