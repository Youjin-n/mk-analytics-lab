# 🛡️ Week 01: Python OOP & Security Simulation

Topic: Object-Oriented Programming (OOP), Regex, and Log Analysis Simulation.

Focus: Building a "Sentinel" tool to generate and parse server logs for threat detection.

## 🎯 Learning Objectives

* **OOP Architecture:** Moving away from functional spaghetti code to structured Classes (`LogEntry`, `LogParser`).
* **Data Simulation:** Generating realistic Apache-style access logs using Python's `random` and `datetime` modules.
* **Regex Mastery:** Using Regular Expressions (`re` module) to extract IP addresses, timestamps, and status codes from raw text.
* **Security Mindset:** Identifying potential "Brute Force" attacks by analyzing 403/500 error rates.

## 📂 File Structure & Logic

| **File**       | **Description**                                                                                   |
| -------------------- | ------------------------------------------------------------------------------------------------------- |
| `src/log_entry.py` | Defines the**LogEntry**class. Serves as the data model for a single log line.                     |
| `src/generator.py` | **Chaos Engine.**Generates fake Apache access logs with configurable error rates (to simulate attacks). |
| `src/parser.py`    | **The Extractor.**Reads raw text files and converts them into LogEntry objects using Regex.             |
| `src/analyzer.py`  | **Threat Intel.**Analyzes parsed logs to find suspicious IPs (e.g., high failure rate).                 |
| `tests/`           | Contains `pytest`unit tests to ensure regex patterns and file generation work correctly.              |

## 🛠️ Key Concepts & Snippets

### 1. The Log Entry Class

Instead of using dictionaries, I used a class to enforce structure:

```
class LogEntry:
    def __init__(self, ip, timestamp, status_code):
        self.ip = ip
        self.timestamp = timestamp
        self.status_code = status_code

```

### 2. Regex Pattern for Apache Logs

The core logic for parsing the logs:

```
# Captures IP, Date, Method, Endpoint, Status, Size
LOG_PATTERN = r'^(\S+) \S+ \S+ \[([\w:/]+\s[+\-]\d{4})\] "(\S+) (\S+)\s*(\S+)?\s*" (\d{3}) (\S+)'

```

## 📝 Weekly Journal

* **Day 1:** Set up the environment (`venv`), learned about `__init__` and `__str__` methods.
* **Day 2:** Built the generator. Learned that real logs have a specific format (Apache CLF), so I mimicked that instead of random strings.
* **Day 3:** Regex was challenging! Used regex101.com to debug the pattern for capturing IP addresses.
* **Day 4:** Implemented basic analysis logic.
* **Day 5:** Refactoring and Documentation.

## 🔗 Resources

* [Corey Schafer: Python OOP Tutorials](https://www.youtube.com/playlist?list=PL-osiE80TeTsWmV9i9c58mdDCSskIFdDS "null")
* [Regex101 (for testing patterns)](https://regex101.com/ "null")
