import re
import specificimg
ocr_text = text

# Define a pattern to detect venues
venue_pattern = r'\b(?:[A-Z][a-z]*\s)*[A-Z][a-z]*\s(?:[A-Z][a-z]*\s)*\b(?:Auditorium|Classroom|Hotel|Floor|Venue)\b'

# Extract all venues from the OCR text
venues = re.findall(venue_pattern, ocr_text)

# Print the detected venues
print("Venues:", venues)
