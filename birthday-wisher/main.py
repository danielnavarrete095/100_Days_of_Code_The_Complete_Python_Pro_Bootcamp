##################### Extra Hard Starting Project ######################
import datetime as dt
import pandas
import random
from login_info import *
from smtp import *
letters = []
for i in range(1, 4):
    letters.append(fr"letter_templates\letter_{i}.txt") 
print(letters)
def get_current_date():
    now = dt.datetime.now()
    return (now.year, now.month, now.day)
    
def get_birthdays_list():
    try:
        data = pandas.read_csv("birthdays.csv")
    except FileNotFoundError:
        print("birthdays.csv doesn't exist")
        return None
    return data.to_dict(orient="records")

def read_file(_file):
    with open(_file, "r") as file:
        return file.read()

def main():
# 2. Check if today matches a birthday in the birthdays.csv
    # Get list from csv file
    birthdays_list = get_birthdays_list()
    print(birthdays_list)
    # Get current date (year, month, day)
    date = get_current_date()
    # Check if a birthday matches
    name = ""
    mail = ""
    for line in birthdays_list:
        birthday = (line["year"], line["month"], line["day"])
        if date == birthday:
            name = line['name']
            mail = line["email"]
            print(f"Happy birthday {name}")
    print(date)
# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv
    letter = read_file(random.choice(letters))
    letter = letter.replace("[NAME]", name)
    letter = letter.replace("[SENDER]", SENDER)
    print(letter)
# 4. Send the letter generated in step 3 to that person's email address.
    print("Sending mail to " + name)
    send_mail((GMAIL_USER, GMAIL_PASSWORD), mail, "Happy Birthday!", letter)

if __name__ == '__main__':
    main()

