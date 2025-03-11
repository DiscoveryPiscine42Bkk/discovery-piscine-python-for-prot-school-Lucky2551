def i_got_that():
   while True:
        user_input = input("What you gotta say?\n")

        if user_input == "STOP":
            break
        else:
            print("I got that! Anything else?")

if name == "main":
    i_got_that()
