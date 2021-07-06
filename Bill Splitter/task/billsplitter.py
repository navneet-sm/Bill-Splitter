# write your code here
import random

x, dinner = int(input('Enter the number of friends joining (including you):\n')), {}
if x <= 0:
    print("No one is joining for the party")
else:
    print('\nEnter the name of every friend (including you), each on a new line:')
    dinner = {input(): 0 for _ in range(x)}
    bill = int(input('\nEnter the total bill value:'))
    dinner = {k: round((bill / x), 2) for k in dinner.keys()}
    luck = input('\nDo you want to use the "Who is lucky?" feature? Write Yes/No:\n')
    if luck == "Yes":
        friends = [name for name in dinner.keys()]
        lucky = random.choice(friends)
        print(f'\n{lucky} is the lucky one!\n')
        dinner = {k: round((bill / (x - 1)), 2) for k in dinner.keys()}
        dinner[lucky] = 0
        print(dinner)
    else:
        print('\nNo one is going to be lucky\n')
        print(dinner)

