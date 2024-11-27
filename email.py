import re

email = input("Enter your email").strip()

if re.search(r"^\w+@ac.uk$",email) :
    print("Valid Academic Email")
elif re.search(r"\w+@gov.uk$",email) :
    print("Valid Government Email")
elif re.search(r"\w+@nhs.net$",email) :
    print("Valid NHS Email")
else :
    print("Invalid")
