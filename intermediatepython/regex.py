import re

# Checking for valid email
pattern_email = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
email = "roshanpandey.deepqore@gmail.com"
if re.match(pattern_email, email):
    print("Valid Email")
else:
    print("Invalid Email")

# Extracting numbers from text
text_numbers = "hello i am roshan. i am 22 years old. we have 2 dogs and 1 cat."
numbers = re.findall(r'\d+', text_numbers)
print("Numbers found:", numbers)

# Replacing multiple spaces with a single space
text_spaces = "Python    is    awesome!"
cleaned = re.sub(r'\s+', ' ', text_spaces)
print("Cleaned text:", cleaned)

# String split by punctuation
text_split = "Hello, how are you? I'm fine!"
parts = re.split(r'[,.?!]', text_split)
print("Split parts:", parts)

# Checking phone number format
text_phone = "My phone is 123-456-7890 or 987-654-3210."
match_phone = re.search(r"\d{3}-\d{3}-\d{4}", text_phone)
if match_phone:
    print("First phone number found:", match_phone.group())

# Anchors and boundaries
text_boundary = "Hello world"
print("Starts with 'Hello':", re.findall(r'^Hello', text_boundary))
print("Ends with 'world':", re.findall(r'world$', text_boundary))

# Groups and capturing
text_phone2 = "My phone is 123-456-7890"
match_groups = re.search(r"(\d{3})-(\d{3})-(\d{4})", text_phone2)
if match_groups:
    print("Captured groups:", match_groups.groups())

# Named groups
match_named = re.search(r"(?P<area>\d{3})-(?P<prefix>\d{3})-(?P<line>\d{4})", text_phone2)
if match_named:
    print("Area code captured:", match_named.group('area'))

# Quantifiers
text_quant = "Year 2025, age 22, code 12345"
print("Numbers with 2-4 digits:", re.findall(r'\d{2,4}', text_quant))

# Lookahead and Lookbehind
text_look = "We have 2 dogs and 1 cat"
print("Digit before 'dogs':", re.findall(r'\d(?= dogs)', text_look))
print("Digit not before 'dogs':", re.findall(r'\d(?! dogs)', text_look))
print("Word after 'dogs':", re.findall(r'(?<=dogs )\w+', text_look))

# Substitutions
text_sub = "My number is 123-456-7890"
masked_text = re.sub(r'\d', '#', text_sub)
print("Masked digits:", masked_text)

# Using function in replacement
def mask_ssn(match):
    return '*' * len(match.group())

text_ssn = "My SSN is 123-45-6789"
masked_ssn = re.sub(r'\d{3}-\d{2}-\d{4}', mask_ssn, text_ssn)
print("Masked SSN:", masked_ssn)

# Flags (case-insensitive)
text_flag = "Hello\nhello"
print("Case-insensitive findall:", re.findall(r'hello', text_flag, re.I))

# Extracting complex patterns
text_urls = "Visit https://example.com or http://test.org"
urls = re.findall(r'https?://\S+', text_urls)
print("URLs found:", urls)

text_dates = "Today is 17-10-2025 and tomorrow is 18-10-2025"
dates = re.findall(r'\b\d{2}-\d{2}-\d{4}\b', text_dates)
print("Dates found:", dates)


# Password Validation
# Rules: 8-16 chars, at least 1 uppercase, 1 lowercase, 1 digit, 1 special char
def validate_password(password):
    pattern = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,16}$'
    return bool(re.match(pattern, password))

passwords_to_test = ["Password123!", "pass123", "Strong@1Pass"]
for p in passwords_to_test:
    print(f"Password '{p}' valid?:", validate_password(p))

# Phone Number Validation
# Format: XXX-XXX-XXXX
def validate_phone(phone):
    pattern = r'^\d{3}-\d{3}-\d{4}$'
    return bool(re.match(pattern, phone))

phones_to_test = ["123-456-7890", "9876543210", "555-555-5555"]
for ph in phones_to_test:
    print(f"Phone '{ph}' valid?:", validate_phone(ph))
