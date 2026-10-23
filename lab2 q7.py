import re

mixed_data = """
Transactions:
2023-12-25 - Payment of $50.00 using card 1234-5678-9012-3456
12/31/2023 - Refund processed for card 1111 2222 3333 4444

Server logs:
192.168.1.1 [25/Dec/2023:10:30:45] HTTP 200
10.0.0.5 [25/Dec/2023:10:31:22] HTTP 404
Invalid: 2023-13-40, 99/99/9999, 1234-5678-9012
"""
#USED AI FOR THIS QUESTION

# Extract dates in YYYY-MM-DD or MM/DD/YYYY format.
dates = re.findall(r"\b(?:\d{4}-\d{2}-\d{2}|\d{2}/\d{2}/\d{4})\b", mixed_data)

# Extract 16-digit card numbers, with optional spaces or dashes.
cards = re.findall(r"(?<!\d)(?:\d{4}[ -]?){3}\d{4}(?!\d)", mixed_data)

# Extract IP addresses, timestamps, and HTTP status codes from log lines.
log_pattern = (
    r"(?P<ip>(?:\d{1,3}\.){3}\d{1,3})\s+"
    r"\[(?P<timestamp>[^\]]+)\]\s+"
    r"HTTP\s+(?P<status>\d{3})"
)
logs = re.finditer(log_pattern, mixed_data)

print("Dates:")
for date in dates:
    print(date)

print("\nCredit card numbers:")
for card in cards:
    print(card)

print("\nLog entries:")
for log in logs:
    print(
        "IP:", log.group("ip"),
        "| Timestamp:", log.group("timestamp"),
        "| HTTP status:", log.group("status")
    )