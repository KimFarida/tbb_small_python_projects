#!/usr/bin/env python3
import datetime, random, time

def print_intro(intro):
    for string in intro:
        print(string)
        time.sleep(1.5)
    
def getBirthdays(numBirthdays):
    birthdays = []

    for i in range(numBirthdays):
        start_year = datetime.date(2001,1,1)

        #random birthday
        rand_day = datetime.timedelta(random.randint(0,364))
        birthday = start_year + rand_day
        birthdays.append(birthday)

    return birthdays

def getMatch(birthdays):
    #Use a set to reduce time complexity
    seen_birthday = set()

    for date in birthdays:
        if date in seen_birthday:
            return date
        seen_birthday.add(date)
    #Looped through and could find no matching date.
    return None

introduction = ['Birthday Paradox, by Al Sweigart al@inventwithpython.com',
                'The birthday paradox shows us that in a group of N people,',
                 'the odds that two of them have matching birthdays is surprisingly large.',
                'This program does a Monte Carlo simulation (that is, repeated random simulations) to explore this concept.',
                f"(It's not actually a paradox, it's just a surprising result.)"]


print_intro(introduction)

while True:
    no_birthdays = input("How many birthdays shall I generate? (Max 100): ")
    if no_birthdays.isdecimal():
        no_birthdays = int(no_birthdays)
        if 0 < no_birthdays <= 100:
            no_birthdays = int(no_birthdays)
            break
    print("Invalid input. Please enter a number between 1 and 100.")

print(f"Here are {no_birthdays} birthdays")

birthdays = getBirthdays(no_birthdays)

for birthday in birthdays:
    print(birthday.strftime("%B"), str(birthday.day) + ', ',end='')
    time.sleep(0.1)

print("\n")
time.sleep(1)

match = getMatch(birthdays)
if match:
    print(f"In this simulation, multiple people have a birthday on {match.strftime('%B')} {match.day}")
else:
    print("there are no matching birthdays.")

time.sleep(1.5)

print(f"Generating {no_birthdays} random birthdays 100,000 times...")
input("Press Enter to begin...")

print('Let\'s run another 100,000 simulations.')
sim_match = 0

for i in range(100_000):
    if i % 10_000 == 0:
        print(f"{i} simulations run...")
        time.sleep(0.5)
    birthdays = getBirthdays(no_birthdays)
    if getMatch(birthdays):
        sim_match += 1

print("100,000 simulations run")
time.sleep(1)

probability = round(sim_match/ 100_000 * 100, 2)
print(f"Out of 100,000 simulations of {no_birthdays} people, there was a")
print(f"matching birthday in that group {sim_match} times. This means")
print(f"that, {no_birthdays},people have a' {probability} '%' chance of")
print("having a matching birthday in their group.")
print(f"That\'s probably more than you would think!")