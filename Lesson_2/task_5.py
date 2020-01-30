my_user = 'liza2109'
my_password = "parol'"
while True:
    user = input("Enter username: ")
    if user == my_user:
        while True:
            password = input("Enter password:")
            if my_password == password:
                answer = 'Password for user "{}" is correct.'.format(user)
                print(answer)
                break
            elif my_password != password:
                answer = 'Password for user "{}" is incorrect.' \
                         '\nPlease try again'.format(user)
                print(answer)
        break
    else:
        print('Username "{}" is incorrect.' \
              '\nPlease try again'.format(user))

