def main():
    email_list = []
    new_list = []
    while True:
        email = input("Input email (or type 'quit' to stop): ")
        if email.upper() == "QUIT":
            break
        else:
            email_list.append(email)
    print(replace_email(email, email_list, new_list))

def replace_email(email, email_list, new_list):
    if email not in email_list:
        for email in email_list:
            if "@ulab.edu.bd" in email:
                index = email.index("@ulab.edu.bd")
                new_email = email[0:index] + "@gmail.com"
                new_list.append(new_email)
            else:
                new_list.append(email)
    else:
        print("Email already exists!")

    return new_list

main()

