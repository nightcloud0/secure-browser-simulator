# Secure Browser Simulator

A Python command-line browser simulator that tracks navigation history with a custom stack data structure and flags suspicious URLs using simple rule-based detection. Built as a cybersecurity awareness tool and a data structures exercise. It does not make real web requests.

## Features
- **Back / forward navigation** using two stacks, the same model real browsers use for history
- **Malicious URL detection** based on a list of known-bad domains and phishing-related keywords
- **Stored security alerts** that you can review later with the `alerts` command
- **Custom `Stack` class** (`stack.py`) with push, pop, peek, and is_empty

## How to run
Requires Python 3.8 or newer. No external packages.

```bash
git clone https://github.com/nightcloud0/secure-browser-simulator.git
cd secure-browser-simulator
python secure_browser_simulator.py
```

## Commands
| Command | What it does |
|---|---|
| `visit <url>` | Visit a URL and check it for malicious indicators |
| `back` | Go to the previous page |
| `forward` | Go to the next page after going back |
| `history` | Show the back stack, current page, and forward stack |
| `alerts` | Show all stored security alerts |
| `exit` | Quit |

## Example session
```
Enter command: visit https://example.com
Enter command: visit https://phishing-login.net/verify
WARNING: Malicious URL Detected https://phishing-login.net/verify
Enter command: visit https://openai.com
Enter command: back
Enter command: back
Enter command: forward
Enter command: history
===Browser History===
Back Stack
['https://example.com']
Current Page
https://phishing-login.net/verify
Forward Stack
['https://openai.com']
```

## How it works
- Visiting a page pushes the current page onto the **back** stack and clears the **forward** stack.
- Going back pushes the current page onto the **forward** stack and pops from the **back** stack. Going forward does the reverse.
- `is_malicious()` lowercases the URL and checks it against a set of known-bad domains and a set of phishing-related keywords (such as `login`, `verify`, `password`, `urgent`).

## Limitations
This is a learning project, not a security product.
- Detection uses simple substring matching, so it can flag harmless URLs (for example, any URL containing "login" or "free") and miss real threats that avoid those words.
- The malicious domain list is a small hardcoded sample, not a live threat feed.
- No real network requests are made.

## Possible improvements
- Compare the parsed hostname against the domain list instead of searching the whole URL
- Load domains and keywords from a configuration file
- Add URL reputation checks or an allowlist to cut down on false positives
- Add unit tests for the stack and detection logic

## What I learned
Stack (LIFO) behavior in a real-world setting, URL parsing with `urllib`, object-oriented design in Python, and how basic rule-based phishing detection works and where it falls short.
