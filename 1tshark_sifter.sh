  GNU nano 6.2                                                                  1tshark_sifter.sh                                                                            
#!/bin/bash

# Get PCAP file location from user
echo "Please enter PCAP file location:"
read pcap_file

# Check if file exists
if [ ! -f "$pcap_file" ]; then
    echo "File not found"
    exit 1
fi

# Filter options
echo "Your Filters Are: 
l for All Packets, 
C for Packet Count, 
Packets W/ A Treat, 
A for Packet containing Applications, 
AD for Packets Containing Audio, 
I for Packets containing an Image, 
MI For Pacets containing Multiple Images or 
P for Ports of Packets[tshark -T fields -e tcp.srcport -e tcp.dstport -r "$pcap_file"]
For Destination"

echo "Your selection is:"
read filter_option

# Run tshark command
echo "Conversations:"
sudo tshark -r "$pcap_file" -qz conv,$filter_option
echo ""
echo "Two-pass analysis and heuristics filter:"
sudo tshark -r "$pcap_file" -R "http.request or http.response" -2R "http.request || http.response" -T fields -e frame.number -e frame.len -e ip.src -e tcp.srcport -e ip.dst>






                                                                              [ Read 33 lines ]
^G Help          ^O Write Out     ^W Where Is      ^K Cut           ^T Execute       ^C Location      M-U Undo         M-A Set Mark     M-] To Bracket   M-Q Previous
^X Exit          ^R Read File     ^\ Replace       ^U Paste         ^J Justify       ^/ Go To Line    M-E Redo         M-6 Copy         ^Q Where Was     M-W Next

