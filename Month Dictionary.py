monthConversions = {
    "Jan": "January",
    "Feb": "February",
    "Mar": "March"
    #  etc, all keys have to be unique
}

print(monthConversions["Jan"])
print(monthConversions.get("Bak", "Not a valid key"))
# will print not a valid key as default for get
# keys dont have to be strings

