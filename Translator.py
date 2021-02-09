import Calculator

# swaps every vowel with a g

def translate(phrase):
   translation = ""
   for letter in phrase:
        if(letter.lower in "aeiou"):
            if letter.isupper():
                translation = translation + "G"
            translation = translation + "g"
        else:
            translation = translation + letter

    return translation

print(translate(input("Enter a phrase: ")))
print(Calculator.fiwnr)
