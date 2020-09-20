import re


def has_SSL(ip):
    patternSB = "\[(\w*)\]"
    matchesSB = re.findall(patternSB, ip)
    patternNotSB = "(?:^|\])(\w+)(?:$|\[)"
    matchesNotSB = re.findall(patternNotSB, ip)
    for p in matchesNotSB:
        for i in range(len(p) - 2):
            if p[i] == p[i + 2] and p[i] != p[i + 1]:
                for q in matchesSB:
                    for j in range(len(q) - 2):
                        if q[j] == q[j + 2] and q[j] == p[i + 1] and q[j + 1] == p[i]:
                            return True
    return False


with open('input', 'r') as f:
    ips = [l.strip() for l in f]

ip_tls = [ip for ip in ips if has_SSL(ip)]
tls_count = len(ip_tls)
print(tls_count)
