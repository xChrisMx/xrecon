Usage: python3 jwrecon.py 
or
chmod +x jwrecon.py and ./jerecon.py

Latest versions have Dmitry and Fierce scans.  This script is/was made for a project of my needs, feel free to modify/contribute as needed.

Tools built in script:
- Nikto/Nuclei (detect web app vulns; poor man's scanner :D)
- SSH Algos, wafw00f (web app FW fingerprinting), curl (to identify redirects), lbd (to detect if DNS or HTTP load balancer is used, OpenSSL cipher negotiation.
- Ping Sweep (~95% host detection rate; if you are not sure if an ip is live or not this will detect if there is anything live behind an IP)
- What Web (Identify Web Technologies used)
- Dmitry (DNS  Deep Info Gathering tool -- Catch subdomains, email addresses, uptime info, etc).
- Fierce (DNS Interrogation tool used to locate non-contiguous IP spaces and hostnames against specified domains or subdomains).  This tool alone will probably yield a bunch of vuln hosts.

![image](https://github.com/user-attachments/assets/db61d355-a2c5-4272-a487-1c8ae05e6516)
