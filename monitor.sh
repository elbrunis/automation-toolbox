#!/bin/bash
#
# monitor.sh - Real-time system resource dashboard.
#
# Displays current CPU load, RAM usage, disk usage (root partition),
# and the top 5 CPU-consuming processes in a colourised terminal view.
#
# @requires top, free, df, ps, awk
# @example
#     ./monitor.sh

# =============================================================================
#  Colour Constants
#  ANSI escape codes for terminal colour output.
# =============================================================================
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
CYAN='\033[0;36m'
BOLD='\033[1m'
RESET='\033[0m'

# =============================================================================
#  print_header
#  Print a formatted section header with coloured decoration.
#
#  @param {string} $1 - The title text to display inside the header.
# =============================================================================
print_header() {
    echo -e "\n${BOLD}${BLUE}======================================${RESET}"
    echo -e "${BOLD}${CYAN}   $1${RESET}"
    echo -e "${BOLD}${BLUE}======================================${RESET}"
}

# =============================================================================
#  1. CPU Usage
#  Extracts user + system CPU load percentage via top + awk.
# =============================================================================
print_header "🧠 CPU USAGE"
CPU_LOAD=$(top -bn1 | grep "Cpu(s)" | awk '{print $2 + $4}')
echo -e "${YELLOW}Current Load:${RESET} ${GREEN}${CPU_LOAD}%${RESET}"
echo -e "${GRAY}(Based on User + System activity)${RESET}"

# =============================================================================
#  2. Memory Usage (RAM)
#  Extracts total, used, and free RAM via free + awk.
# =============================================================================
print_header "💾 MEMORY (RAM)"
free -h | awk '/^Mem:/ {
    print "\033[1;33mTotal:\033[0m " $2
    print "\033[1;33mUsed: \033[0m " $3
    print "\033[1;33mFree: \033[0m " $4
}'

# =============================================================================
#  3. Disk Usage (Root Partition)
#  Reports size, used, and free space on / via df + awk.
# =============================================================================
print_header "HARD DISK (Root /)"
df -h / | awk 'NR==2 {
    print "\033[1;33mSize:\033[0m  " $2
    print "\033[1;33mUsed:\033[0m  " $3 " (" $5 ")"
    print "\033[1;33mFree:\033[0m  " $4
}'

# =============================================================================
#  4. Top Processes
#  Lists the 5 most CPU-intensive processes using ps + awk.
# =============================================================================
print_header "🚀 TOP 5 PROCESSES (By CPU)"
echo -e "${BOLD}PID\t%CPU\t%MEM\tCOMMAND${RESET}"
ps -eo pid,%cpu,%mem,comm --sort=-%cpu | head -n 6 | awk 'NR>1 {
    printf "%s\t%s\t%s\t%s\n", $1, $2, $3, $4
}'

echo -e "\n${GREEN}✨ System check complete.${RESET}\n"