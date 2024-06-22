# Basic SQL Injection Scanner

A simple python script to test a URL's parameters for basic SQL Injection vulnerabilities.

## Description
This script parses the query parameters of a given URL, appends a single quote (`'`) to each parameter one by one, and inspects the HTTP response for common SQL database error messages.

## Usage
Run the script with Python 3:
```bash
python sqli_scanner.py "http://example.com/page.php?id=1&cat=2"
```
