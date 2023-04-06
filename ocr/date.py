import re

ocr_text = "9 March 2023, Smart Classroom, 10:00am - 3:00pm"

date_pattern = r"(\d{1,2})\s(January|February|March|April|May|June|July|August|September|October|November|December|JANUARY|FEBRUARY|MARCH|APRIL|MAY|JUNE|JULY|AUGUST|SEPTEMBER|OCTOBER|NOVEMBER|DECEMBER|JAN|FEB|MAR|APR|MAY|JUN|JUL|AUG|SEP|OCT|NOV|DEC|Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)\s(\d{4})"
venue_pattern = r"\b(?:[A-Z][a-z]*\s)*[A-Z][a-z]*\s(?:[A-Z][a-z]*\s)*\b(?: Classroom|Remibai Auditorium|Room 253|Room|Lab|Venue)\b"

# Extract all dates and venues from the OCR text
dates = re.findall(date_pattern, ocr_text)

# Print the detected dates and places
print("Dates:", dates)
time_pattern = r'\b\d{1,2}:\d{2}\s*(?:AM|PM|am|pm)?\b'

# Extract all times from the OCR text
times = re.findall(time_pattern, ocr_text)

# Print the detected times
print("Times:", times)


