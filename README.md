# RepoReaper

## Overview
RepoReaper is a precision tool designed to automate the identification of exposed `.git` repositories across a list of domains and subdomains. By processing a user-provided text file with domain names, RepoReaper systematically checks each for publicly accessible `.git` files. This enables rapid assessment and protection against information leaks, making RepoReaper an essential resource for security teams and web developers.

## Features
- Automated scanning of domains and subdomains for exposed `.git` repositories.
- Streamlines the detection of sensitive data exposures.
- User-friendly command-line interface.
- Ideal for security audits and Bug Bounty.

## Installation
Clone the repository and install the required dependencies:
```bash
git clone https://github.com/YourUsername/RepoReaper.git
cd RepoReaper
pip install -r requirements.txt
chmod +x RepoReaper.py
```

## Usage 
RepoReaper is executed from the command line and will prompt for the path to a file containing a list of domains or subdomains to be scanned.

To start RepoReaper, simply run:
```bash
./RepoReaper.py
  or
python3 RepoReaper.py
```
Upon execution, RepoReaper will ask for the path to the file containing the domains or subdomains:
Enter the path of the file containing domains

Provide the path to your text file when prompted. The file should contain one domain or subdomain per line, like so:
```bash
example.com
subdomain.example.com
anotherdomain.com
```
RepoReaper will then proceed to scan the provided domains or subdomains for exposed .git repositories and report its findings.
![Repo_Reaper](https://github.com/chaudharyarjun/RepoReaper/assets/66072013/906163b5-1050-41c8-963d-9c0efdd0aba7)

# Disclaimer

This tool is intended for educational purposes and security research only. The user assumes all responsibility for any damages or misuse resulting from its use.


