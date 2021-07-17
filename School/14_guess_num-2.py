start_num: int = 1
end_num: int = 100
print(f'You can pick and choose your number between {start_num} and {end_num}')
print("So, I will catch the number...")

attempt: int = 1
logging: bool = False
inner_while_stop: bool = False

while True: # for first question
    if logging:
        print(f' start : {start_num} ~ {end_num}')

    print(f'\n Attempt #{attempt}...')
    guess_num = int((start_num + end_num)/2)
    first_question = f' Q1. I guess...your number is {guess_num}, right? (y)es or (n)o, and (q)uit : ' 
    first_ans = input(first_question)

    if first_ans.lower() == "y":    # guess_num is equal to your number.
        print(" Thx...")
        break
    elif first_ans.lower() == "n":  # guess_num is not equal to your number.
        while True: # for second question
            second_question  = f' Q2. Hmm, is your number, ... greater than {guess_num}, (y)es or (n)o, and (q)uit :'
            second_ans = input(second_question)
            if second_ans.lower() == 'q':   # stop
                inner_while_stop = True
                break
            elif second_ans.lower() == 'y': # guess_num is grater than your number
                start_num = guess_num + 1
                break
            elif second_ans.lower() == 'n': # guess_num is less than your number
                end_num = guess_num - 1
                break
            else:
                if logging:
                    print(f' ==> your hit to me is {second_ans}. try again!')
    elif first_ans.lower() == "q": # stop
        break
    else:
        if logging:
            print(f' ==> your hit to me is {first_ans}. try again!')
        continue

    attempt += 1                    # How many time computer was trying.

    if inner_while_stop:            # the second answer is 'q'
        break
    elif start_num >= end_num:      # User givies no answer apparently.
        print(f'May be....your number is {end_num}')
        break

print("\n Programm terminated!!!")
