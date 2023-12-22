a = input()

if a.isdigit() == True:
    print("Your message includes numbers only.")
elif a.isalpha() == True:
    print("Your message includes letters only.")
else:
    print("Your message includes numbers and letters.")