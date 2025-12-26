# 🛠️ Automation Toolbox

## 📄 Description
Collection of **Python** and **Bash** scripts to automate daily **System Administration** tasks.

---

## 📂 Scripts Included

### 1. File Organizer (`organizer.py`)

**Logic:**  
Scan directory → Detect extension → Move to subfolder

**Examples:**
- `.jpg` → `/Images`
- `.pdf` → `/Documents`

**Usage:**
```bash
python3 organizer.py
2. Auto Backup (backup.py)
Features:

✓ Compresses target folder into a ZIP

✓ Automatic timestamp naming

✓ Retention policy: deletes backups older than 7 days

Usage:

bash
Copiar código
python3 backup.py
3. System Monitor (monitor.sh)
Real-time Dashboard Metrics:

🧠 RAM usage

💾 Disk usage (root /)

⚙️ CPU: Top 5 consuming processes

Usage:

bash
Copiar código
chmod +x monitor.sh
./monitor.sh
🤖 Automation (Cron Job)
Schedule: Daily at 20:00 (8:00 PM)

Crontab configuration:

bash
Copiar código
# m h  dom mon dow   command
0 20 * * * /usr/bin/python3 /path/to/automation-toolbox/backup.py
🎓 Notes
Created as part of the DevOps / SysAdmin Bootcamp.

markdown
Copiar código

Si lo quieres **aún más minimal**, o adaptado a **README.md**, **Obsidian**,