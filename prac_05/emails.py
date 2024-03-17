def extract_name(email):
    """Extracts a name from an email address."""
    username = email.split('@')[0]
    name_parts = username.split('.')
    return ' '.join(part.capitalize() for part in name_parts)


def main():
    user_dict = {}
    while True:
        email = input("Email: ").strip()
        if not email:
            break

        name = extract_name(email)
        confirm = input(f"Is your name {name}? (Y/n) ").strip().lower()
        if confirm not in ['y', 'yes']:
            name = input("Name: ")

        user_dict[email.lower()] = name

    for email, name in user_dict.items():
        print(f"{name} ({email})")


main()
