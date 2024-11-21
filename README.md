# LFI-fuzz3r
<p align="center"> 
<a href="https://www.python.org/"><img alt="Python Version" src="https://img.shields.io/badge/python-3.6%2B-blue?logo=python&logoColor=white"/></a>
&nbsp;
<a href="https://pypi.org/project/requests/"><img alt="Dependency" src="https://img.shields.io/badge/dependency-requests-orange?logo=pypi&logoColor=white"/></a>
&nbsp;
<a href="#"><img alt="Vulnerability Testing" src="https://img.shields.io/badge/tool-LFI%20Fuzzer-%23#1ccc1d"/></a>
&nbsp;
<a href="#"><img alt="Security Tool" src="https://img.shields.io/badge/category-Security-blue"/></a>
&nbsp;
<a href="#"><img alt="Purpose" src="https://img.shields.io/badge/purpose-Pentesting-red"/></a>
&nbsp;
<a href="https://book.hacktricks.xyz/pentesting-web/file-inclusion"><img alt="LFI Reference" src="https://img.shields.io/badge/LFI-HackTricks-%23f51c00"/></a><br>
<a href="https://github.com/3rr0r-505/LFI-fuzz3r/blob/main/LICENSE"><img alt="License" src="https://img.shields.io/badge/license-MIT-green"/></a>
&nbsp;
<a href="https://github.com/3rr0r-505/LFI-fuzz3r"><img alt="Stars" src="https://img.shields.io/github/stars/3rr0r-505/LFI-fuzz3r.svg?style=social"/></a>
&nbsp;
<a href="https://github.com/3rr0r-505/LFI-fuzz3r/issues"><img alt="Issues" src="https://img.shields.io/github/issues/3rr0r-505/LFI-fuzz3r"/></a>
&nbsp;
<a href="https://github.com/3rr0r-505/LFI-fuzz3r"><img alt="Forks" src="https://img.shields.io/github/forks/3rr0r-505/LFI-fuzz3r?style=social"/></a><br>
</p>

This tool is designed to identify and exploit potential Local File Inclusion (LFI) vulnerabilities in web applications. It automates testing for file inclusion by appending common file paths to a base URL.

## Features
- **Customizable URL and file paths**: Test any URL and use a file containing paths for exploration.
- **Default file paths**: Includes a comprehensive list of commonly targeted files.
- **Directory traversal**: Easily prepend traversal strings (e.g., `../../../`) to file paths.
- **Multithreading**: Speed up requests with configurable thread usage.
- **Timeouts**: Set a timeout for each request to handle slow responses.
- **Verbose output**: Enable detailed logs of requests and responses.

## Requirements
- Python 3.6 or higher
- `requests` module

Install dependencies using:
```bash
pip install requests argformat
```

## Useage
```bash
python3 lfi-fuzzer.py -h
usage: lfi-fuzzer.py [-h] -u URL [-f FILE] [--traversal TRAVERSAL] [--timeout TIMEOUT] [-v] [-t THREADS]

Fetch and display content from a URL with potential LFI. For more information, visit:
https://book.hacktricks.xyz/pentesting-web/file-inclusion

options:
  -h, --help             show this help message and exit
  -u URL, --url URL      Base URL (e.g., 'http://dev.site/script.php?page=')
  -f FILE, --file FILE   File containing paths to be appended to the base URL
  --traversal TRAVERSAL  Directory traversal string to prepend to paths (e.g., '../../../')
  --timeout TIMEOUT      Timeout for each request in seconds (default: 10)
  -v, --verbose          Enable verbose output
  -t, --threads THREADS  Number of threads to use (default: 10)
```
## PathList
The [default pathlist](https://github.com/3rr0r-505/LFI-fuzz3r/edit/main/paths.txt) is already included in the tool (for linux only). For more exhaustive pathlists visit the following links:
- [file_inclusion_paths_linux.txt](https://github.com/carlospolop/Auto_Wordlists/blob/main/wordlists/file_inclusion_linux.txt)
- [file_inclusion_paths_windows.txt](https://github.com/carlospolop/Auto_Wordlists/blob/main/wordlists/file_inclusion_windows.txt)

## Note
- The script supports multithreading, but using too many threads may cause server bans or performance issues.
- Always test on authorized targets. Unauthorized testing is illegal.

## Legal Disclaimer
The use of code contained in this repository, either in part or in its totality,
for engaging targets without prior mutual consent is illegal. **It is
the end user's responsibility to obey all applicable local, state and
federal laws.**

Developers assume **no liability** and are not
responsible for misuses or damages caused by any code contained
in this repository in any event that, accidentally or otherwise, it comes to
be utilized by a threat agent or unauthorized entity as a means to compromise
the security, privacy, confidentiality, integrity, and/or availability of
systems and their associated resources. In this context the term "compromise" is
henceforth understood as the leverage of exploitation of known or unknown vulnerabilities
present in said systems, including, but not limited to, the implementation of
security controls, human- or electronically-enabled.

The use of this code is **only** endorsed by the developers in those
circumstances directly related to **educational environments** or
**authorized penetration testing engagements** whose declared purpose is that
of finding and mitigating vulnerabilities in systems, limiting their exposure
to compromises and exploits employed by malicious agents as defined in their
respective threat models.

## License
This project is licensed under the MIT License 2.0 - see the [LICENSE](https://github.com/3rr0r-505/LFI-fuzz3r/blob/main/LICENSE) file for details.
