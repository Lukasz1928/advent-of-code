import re


def has_abba(s):
    for i in range(len(s) - 3):
        if '[' not in s[i:i+4] and ']' not in s[i:i+4] and s[i] == s[i + 3] and s[i + 1] == s[i + 2] and s[i] != s[i + 1]:
            return True
    return False


def has_TLS(ip):
    matches = re.findall('\[(\w*)\]', ip)
    for m in matches:
        if has_abba(m):
            return False
    return has_abba(ip)


with open('input', 'r') as f:
    ips = [l.strip() for l in f]

ip_tls = [ip for ip in ips if has_TLS(ip)]
tls_count = len(ip_tls)
print(tls_count)
