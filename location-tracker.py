import phonenumbers
from phonenumbers import carrier, geocoder

# Get the phone number as input
phone_number = input("Enter phone number: ")

# Parse the phone number with the specified region
parsed_number = phonenumbers.parse(phone_number, "PK")  # Replace "PK" with the appropriate region code

# Get the carrier
carrier_name = carrier.name_for_number(parsed_number, 'en')  # The second argument 'en' is for the English language
print(f"Carrier: {carrier_name}")

# Get the location
location = geocoder.description_for_number(parsed_number, 'en')
print(f"Location: {location}")