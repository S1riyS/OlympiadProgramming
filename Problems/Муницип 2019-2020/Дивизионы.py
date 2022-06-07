# https://codeforces.com/gym/102906/problem/C
# 100 / 100

r = int(input()) # Rating
competitions = list(input()) # List of competitions

if r <= 1600:
    user_division = '3'
elif 1601 <= r <= 1900:
    user_division = '2'
else:
    user_division = '1'

answer = []
own_division = False
for competition_division in competitions:
    if user_division == competition_division:
        print(competition_division)
        own_division = True
        break
    elif user_division > competition_division:
        answer.append(competition_division)
    else:
        answer.append(competition_division + '*')

if not own_division:
    print('\n'.join(answer))
