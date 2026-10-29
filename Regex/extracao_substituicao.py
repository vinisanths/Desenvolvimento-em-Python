import re
log = """
2026-08-30 10:00:00 192.168.1.1 GET /index.html
2026-08-30 10:05:00 10.0.0.5 POST /login
2026-08-30 10:10:00 192.168.1.1 GET /dashboard
"""

padraoIp = r"\d{1,3}(?:\.\d{1,3}){3}"
ips = re.findall(padraoIp, log)
print(ips)

#IPs únicos
print(set(ips))

texto = "CPF: 123.456.789-00, outro: 987.654.321-00"
mascarado = re.sub(r"\d{3}\.\d{3}\.\d{3}-\d{2}", "***.***.***-**", texto)
print(mascarado) # "CPF: ***.***.***-**, outro: ***.***.***-**"