rule Foreign_Connection
{
    meta:
        description = "Detects connections to servers in specific countries based on TLDs"
        author = "CyberDefender_Greg"
        version = "1.1"

    strings:
        $foreign_tld = /\.((mm|cu|kp|er|ir|ni|pk|cn|ru|sa|tj|tm|dz|cf|km|vn))\b/i

    condition:
        any of them
}
