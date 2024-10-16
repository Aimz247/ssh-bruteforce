# SSH-bruteforce

This Python-based tool is designed for educational purposes to demonstrate SSH authentication testing techniques. It is strictly intended for authorized security testing and educational use only.

## ⚠️ WARNING: ETHICAL USE ONLY ⚠️

This tool is for EDUCATIONAL AND AUTHORIZED TESTING PURPOSES ONLY! Unauthorized use of this tool against systems you do not own or have explicit permission to test is ILLEGAL and UNETHICAL. The author takes no responsibility for any misuse of this tool. Always ensure you have written permission before conducting any kind of security testing.

## Features

- Demonstrates SSH authentication testing using a list of passwords
- Cross-platform compatibility (Windows and Linux)
- Simple command-line interface

## Prerequisites

Before you begin, ensure you have met the following requirements:

- Python 3.6 or higher
- Paramiko library

## Installation

1. Clone this repository:
   ```
   git clone https://github.com/YoAimz/SSH-bruteforce.git
   cd SSH-bruteforce
   ```

2. Install the required dependencies:
   ```
   pip install paramiko
   ```

## Usage

Run the script with the following command:

```
python ssh_bruteforce.py
```

You will be prompted to enter:
1. The target IP address
2. The username to test
3. The location of the password file

The password file should be a text file with one password per line.

## Ethical Considerations

- This tool is meant for education and improving security, NOT for malicious purposes.
- Only use this tool on systems you own or have explicit written permission to test.
- Unauthorized access to computer systems is illegal and unethical.
- Be aware of and comply with all relevant laws and regulations in your jurisdiction.

## Legal Disclaimer

The use of this tool for attacking targets without prior mutual consent is illegal. It is the end user's responsibility to obey all applicable local, state, and federal laws. The author assumes no liability and is not responsible for any misuse or damage caused by this program.


## Acknowledgements

- [Paramiko](http://www.paramiko.org/) - The Python SSH library used in this project.

