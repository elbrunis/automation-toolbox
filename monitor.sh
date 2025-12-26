#!/bin/bash

# ===============================================================
#  SYSTEM RESOURCE MONITOR
#  Description: Displays real-time CPU, RAM, Disk, and Process info.
# ===============================================================

# --- Configuration: Colors ---
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
CYAN='\033[0;36m'
BOLD='\033[1m'
RESET='\033[0m'

# --- Helper Function for Headers ---
print_header() {
    echo -e "\n${BOLD}${BLUE}======================================${RESET}"
    echo -e "${BOLD}${CYAN}   $1${RESET}"
    echo -e "${BOLD}${BLUE}======================================${RESET}"
}

# 1. CPU USAGE
print_header "🧠 CPU USAGE"
# Extract user+system load using top and awk
CPU_LOAD=$(top -bn1 | grep "Cpu(s)" | awk '{print $2 + $4}')
echo -e "${YELLOW}Current Load:${RESET} ${GREEN}${CPU_LOAD}%${RESET}"
echo -e "${GRAY}(Based on User + System activity)${RESET}"


# 2. MEMORY USAGE (RAM)
print_header "💾 MEMORY (RAM)"
# Extract used and total memory using free and awk
free -h | awk '/^Mem:/ {
    print "\033[1;33mTotal:\033[0m " $2 
    print "\033[1;33mUsed: \033[0m " $3 
    print "\033[1;33mFree: \033[0m " $4
}'


# 3. DISK USAGE (Root Partition)
print_header "HARD DISK (Root /)"
# Show only the relevant line for /
df -h / | awk 'NR==2 {
    print "\033[1;33mSize:\033[0m  " $2
    print "\033[1;33mUsed:\033[0m  " $3 " (" $5 ")"
    print "\033[1;33mFree:\033[0m  " $4
}'


# 4. TOP PROCESSES
print_header "🚀 TOP 5 PROCESSES (By CPU)"
# Custom format for ps command to show specific columns
echo -e "${BOLD}PID\t%CPU\t%MEM\tCOMMAND${RESET}"
ps -eo pid,%cpu,%mem,comm --sort=-%cpu | head -n 6 | awk 'NR>1 {
    printf "%s\t%s\t%s\t%s\n", $1, $2, $3, $4
}'

echo -e "\n${GREEN}✨ System check complete.${RESET}\n"