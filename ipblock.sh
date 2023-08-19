#!/bin/bash

AUTH_LOG="/var/log/auth.log"
MAX_ATTEMPTS=3

while true; do
    awk -v max_attempts=$MAX_ATTEMPTS '/Failed password/ {count[$(NF-3)]++} END {for (ip in count) if (count[ip] >= max_attempts) print ip}' "$AUTH_LOG" |
    while read -r ip; do
        if ! iptables -C INPUT -s "$ip" -j DROP &>/dev/null; then
            iptables -A INPUT -s "$ip" -j DROP
            echo "Blocked IP address: $ip"
        fi
    done

    sleep 60
done
