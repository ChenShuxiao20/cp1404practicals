# Emails
"""
Emails
Estimate: 15 minutes
Actual:   23 minutes
"""
email_name = {}
email = input("Email: ")
while email != "":
    local_part = email.split('@')[0]
    name_parts = local_part.split('.')
    name = ' '.join(name_parts).title()
    is_correct = input(f"Is your name {name}? (Y/n): ").upper()
    if is_correct != "Y" and is_correct != "":
        name = input("Name: ")
    email_name[email] = name
    email = input("Email: ")
for email, name in email_name.items():
    print(f"{name} ({email})")