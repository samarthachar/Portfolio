import json


def to_morse(msg):
    output = ""
    for char in msg:
        try:
            end = morse[char]
            output += f"{end} "
        except KeyError:
            output += "* "
    return output.strip()

def to_text(msg):
    output = ""
    msg = msg.split(' ')

    space_count = 0
    for char in msg:
        if char == '':
            space_count += 1
        if space_count == 4:
            output = output[:-3]
            output += " "
            space_count = 0
            continue
        try:
            end = text[char]
            output += end
        except KeyError:
            output += "*"
    return output

with open("data.json") as file:
    data = json.load(file)

morse = data["morse"]
text = data["text"]

app_on = True
while app_on:
    inp = input("Enter 'morse' to convert text to morse code, or enter 'text' to convert morse code to text: ").lower()
    if inp == "morse":
        message = input("Enter text: ").lower()
        display = to_morse(message)
        print(f" '{message}'\n in morse is\n '{display}'")
    elif inp == "text":
        message = input("Enter morse: ").lower()
        display = to_text(message)
        print(f" '{message}'\n in text is\n '{display}'")
    else:
        print("Please enter 'morse' or 'text' to use this application.")
        continue

    if '*' in display:
        print("WARNING: '*' is the placeholder for any symbol or character that is not supported in morse")
    inp = input("Do you want to continue using the application? Type 'y' for yes, type 'n' for no: ").lower()
    if inp != "y":
        app_on = False


