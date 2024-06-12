#!/bin/bash

echo "Enter IP: "
read IP

# Check if the input IP is empty
if [ -z "$IP" ]; then
    echo "IP address cannot be empty. Exiting."
    exit 1
fi

# Run Nmap
nmap -spoof-mac 94:38:70:3A:A2:F6 -sS -A "$IP"
echo "-------E--n--d----o-f--------N--m--a--p-----------"

echo "N..I..K..T..O..S..C..A..N"
# Run Nikto
nikto -h "$IP"

echo "Detailed Information: "
curl "ipinfo.io/$IP"

echo
echo

echo "Do you want to check for extra possible vulnerabilities? (Enter Y/N)"
read answer

if [[ "$answer" != "y" && "$answer" != "Y" && "$answer" != "yes" && "$answer" != "YES" ]]; then
    echo "No vulnerability check performed."
else
echo "And they are: "
    nmap --script=/usr/share/nmap/scripts/vulners.nse "$IP"
fi

