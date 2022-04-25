# Ask for First name, last name, email address, phone number, job title, ID number
print("Please enter the following information: \n")
first = input("First Name: ")
last = input("Last Name: ")
email = input("Email Address: ")
phone = input("Phone Number: ")
job = input("Job Title: ")
id = input("ID Number: ")
hair = input("Hair Color: ")
eye = input("Eye Color: ")
month = input("Month You Started Working: ")
trained = input("(Please Enter Y for yes or N for no) Have You Been Trained: ")


if trained.lower() == "y":
    trained = "Yes"
else:
    trained = "No"



#Print ID in required order

print("\nThe ID Card is:")
print("----------------------------------------")
print(last.upper() + ", " + first.title())
print(job.title())
print("ID: " + id + "\n")
print(email.lower())
print(phone + "\n")
print(f"{'Hair: ' + hair.title():<18} Eyes: {eye.title()}")
print(f"{'Month: ' + month.title():<18} Training: {trained}")
print("----------------------------------------")
