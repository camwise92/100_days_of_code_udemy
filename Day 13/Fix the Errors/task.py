try:
    age = int(input("How old are you?"))
    if age > 18:
      print("You can drive at age {age}.")
except ValueError:
    print("Please enter numerical values only.")