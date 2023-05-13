#!/bin/bash

echo "Enter file location:"
read file_location

echo "Enter selection:"
echo "1. DNS packets"
echo "2. TCP packets"
echo "3. RTP packets"
echo "4. HTTP image packets"
echo "5. All packets"
echo "6. Filter packets"
echo "7. Hex dump of data packets"
echo "8. Heuristics filter on all packets"
echo "9. Exit"

read sel

while [ "$sel" != "9" ]
do
    case "$sel" in
        "1") 
            tshark -r "$file_location" -Y "dns" -T fields -e frame.time -e ip.src -e tcp.srcport -e ip.dst -e tcp.dstport
            ;;
        "2") 
            tshark -r "$file_location" -Y "tcp" -T fields -e frame.time -e ip.src -e tcp.srcport -e ip.dst -e tcp.dstport
            ;;
        "3") 
            tshark -r "$file_location" -Y "rtp" -T fields -e frame.time -e ip.src -e tcp.srcport -e ip.dst -e tcp.dstport
            ;;
        "4") 
            tshark -r "$file_location" -Y "http.content_type contains \"image\"" -T fields -e frame.time -e ip.src -e tcp.srcport -e ip.dst -e tcp.dstport
            ;;
        "5") 
            tshark -r "$file_location" -T fields -e frame.time -e ip.src -e tcp.srcport -e ip.dst -e tcp.dstport
            ;;
        "6")
            echo "Enter filter expression:"
            read filter_expr
            tshark -r "$file_location" -Y "$filter_expr" -T fields -e frame.time -e ip.src -e tcp.srcport -e ip.dst -e tcp.dstport
            ;;
        "7")
            tshark -r "$file_location" -x
            ;;
        "8")
            tshark -r "$file_location" -O smb -T fields -e frame.time -e ip.src -e tcp.srcport -e ip.dst -e tcp.dstport
            ;;
        *) 
            echo "Invalid selection."
            ;;
    esac

    echo "Enter selection:"
    echo "1. DNS packets"
    echo "2. TCP packets"
    echo "3. RTP packets"
    echo "4. HTTP image packets"
    echo "5. All packets"
    echo "6. Filter packets"
    echo "7. Hex dump of data packets"
    echo "8. Heuristics filter on all packets"
    echo "9. Exit"

    read sel
done
