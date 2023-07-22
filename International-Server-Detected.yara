rule Foreign_Connection
{
    meta:
        description = "Connection to servers hosted in specific countries"
        author = "CyberDefender_Greg"
        version = "1.0"

    strings:
        $b = /.*\.mm/i fullword wide
        $c = /.*\.cu/i fullword wide
        $d = /.*\.kp/i fullword wide
        $e = /.*\.er/i fullword wide
        $i = /.*\.ir/i fullword wide
        $n = /.*\.ni/i fullword wide
        $p = /.*\.pk/i fullword wide
        $cn = /.*\.cn/i fullword wide
        $r = /.*\.ru/i fullword wide
        $s = /.*\.sa/i fullword wide
        $tj = /.*\.tj/i fullword wide
        $tm = /.*\.tm/i fullword wide
        $a = /.*\.dz/i fullword wide
        $ca = /.*\.cf/i fullword wide
        $k = /.*\.km/i fullword wide
        $v = /.*\.vn/i fullword wide

    condition:
        any of ($b, $c, $d, $e, $i, $n, $p, $cn, $r, $s, $tj, $tm, $a, $ca, $k, $v)
}
