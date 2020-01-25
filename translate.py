def interpret(phrase):
    elaborate = ""
    for letter in phrase:
        if letter.lower() in "rstql":
            if letter.isupper():
                elaborate = elaborate + "K"
            else:
                elaborate = elaborate + "k"
        else:
            elaborate = elaborate + letter
    return elaborate


print(interpret(input("How is your day: ")))