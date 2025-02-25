import random
import string

def generate_password(length=8):
    """Generate a random password with letters and digits."""
    characters = string.ascii_letters + string.digits
    return ''.join(random.choices(characters, k=length))

def process_emails(input_file, output_file):
    """Read emails, generate usernames and passwords, and write to output file."""
    with open(input_file, "r") as file:
        emails = [line.strip() for line in file.readlines()]
    
    user_data = []
    for email in emails:
        username = email.split("@")[0]  # Extract username from email
        password = generate_password()  # Generate random password
        user_data.append(f"{email},{username},{password}")
    
    with open(output_file, "w") as file:
        file.write("\n".join(user_data))

if __name__ == "__main__":
    input_file = "emails.txt"  # Input file containing emails
    output_file = "output.txt"  # Output file to store results
    process_emails(input_file, output_file)
    print(f"User credentials saved to {output_file}")
