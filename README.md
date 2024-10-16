Usage: 
- python3 xrecon.py
* or
- chmod +x xrecon.py and ./xrecon.py

Latest version includes Dmitry and Fierce.  This script was made for a project of my needs, feel free to modify/contribute as needed.

Tools built in script:
- Nikto/Nuclei (detect web app vulns; poor man's scanner :D)
- SSH Algos, wafw00f (web app FW fingerprinting), curl (to identify redirects), lbd (to detect if DNS or HTTP load balancer is used, OpenSSL cipher negotiation.
- Ping Sweep (~95% host detection rate; if you are not sure if an ip is live or not this will detect if there is anything live behind an IP)
- What Web (Identify Web Technologies used)
- Dmitry (DNS  Deep Info Gathering tool -- Catch subdomains, email addresses, uptime info, etc).
- Fierce (DNS Interrogation tool used to locate non-contiguous IP spaces and hostnames against specified domains or subdomains).  This tool alone will probably yield a bunch of vuln hosts.

Screenshot:
![image](https://github.com/user-attachments/assets/bc0a4408-2132-4650-90de-8b5dd5d917d9)
