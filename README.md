# 🛠️ Automation Toolbox

## 📄 Description
Collection of **Python** and **Bash** scripts to automate daily **System Administration** tasks.

---

## 📂 Scripts Included

### 1️⃣ File Organizer (`organizer.py`)

**Logic:**  
Scan directory → Detect file extension → Move files to subfolders based on extension.

**Examples:**
- `.jpg` → `/Images`
- `.pdf` → `/Documents`

**Steps to execute:**
```bash
python3 organizer.py
2️⃣ Auto Backup (backup.py)
Features:

Compresses target folder into a ZIP file

Automatic timestamp naming

Retention policy: deletes backups older than 7 days

Steps to execute:

bash
Copiar código
python3 backup.py
3️⃣ System Monitor (monitor.sh)
Real-time dashboard metrics:

RAM usage

Disk usage (root / partition)

CPU: Top 5 consuming processes

Steps to execute:

bash
Copiar código
chmod +x monitor.sh
./monitor.sh
🤖 Automation with Cron Job
Cron allows you to schedule scripts to run automatically at a specific time.

🔹 Step 1: Open the crontab editor
bash
Copiar código
crontab -e
This opens the cron configuration file for the current user.

🔹 Step 2: Add the scheduled task
bash
Copiar código
0 20 * * * /usr/bin/python3 /path/to/automation-toolbox/backup.py
🔹 Step 3: Understand the cron syntax
bash
Copiar código
# ┌──────── minute (0 - 59)
# │ ┌────── hour (0 - 23)
# │ │ ┌──── day of month (1 - 31)
# │ │ │ ┌── month (1 - 12)
# │ │ │ │ ┌─ day of week (0 - 7) (Sunday = 0 or 7)
# │ │ │ │ │
# 0 20 * * * command
Explanation of this schedule:

0 → At minute 0

20 → At 20:00 (8:00 PM)

* * * → Every day, every month, every weekday

/usr/bin/python3 → Absolute path to Python interpreter

/path/to/automation-toolbox/backup.py → Script to execute

🔹 Step 4: Save and exit
Once saved, the cron job will run automatically every day at 20:00.