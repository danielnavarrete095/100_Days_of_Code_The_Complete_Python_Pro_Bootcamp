# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
true_total = 0
love_total = 0
love_score = 0
combined_name = name1 + name2
#Daniel Navarrete
#Melissa Bustamante
# You could also use .count() method to count the times each letter appears in a 🔼 # e.g. t = combined_name.count("t")
for name_letter in combined_name.lower():
    if name_letter in "true":
        true_total += 1
for name_letter in combined_name.lower():
    if name_letter in "love":
        love_total += 1
# print("true_total:", true_total)
# print("love_total:", love_total)
love_score = int(str(true_total) + str(love_total))

if love_score < 10 or love_score > 90:
    print(f"Your score is {love_score}, you go together like coke and mentos.")
elif love_score >= 40 and love_score <= 50:
    print(f"Your score is {love_score}, you are alright together.")
else:
    print(f"Your score is {love_score}.")