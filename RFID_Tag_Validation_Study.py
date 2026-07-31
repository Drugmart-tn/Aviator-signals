# RFID Tag Validation (Study Example)
tag = input("Enter RFID tag: ").strip()

valid = (
    len(tag) == 8 and
    tag[:2].isalpha() and
    tag[:2].isupper() and
    tag[2:].isdigit()
)

if valid:
    print("RFID tag is valid.")
else:
    print("RFID tag is invalid.")
