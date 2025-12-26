#!/bin/bash

echo "===== SYSTEM MONITOR ====="

echo "--- CPU ---"
top -bn1 | grep "Cpu"

echo "--- RAM ---"
free -h | grep Mem

echo "--- DISK ---"
df -h /

echo "--- TOP 5 PROCESSES ---"
ps aux --sort=-%cpu | head -n 6