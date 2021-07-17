start_num = 1
end_num = 100


print(f' {start_num = } ~ {end_num =}')

while True:
    print(f' {start_num =}, {end_num = }')

    guess_num = int((start_num + end_num)/2)
    first_ans = input(f'is your number {guess_num} ?, (y)es or (n)o ')
    if first_ans == "y":
        print("Ok")
        break
    elif first_ans == "n":
        print("No")
        while True:
            second_ans = input(f' greater than {guess_num}, (y)es or (n)o ')
            if second_ans == "y":
                print("greater than")
                start_num = guess_num + 1
                break
            elif second_ans == "n":
                end_num = guess_num - 1
                break
            else:
                print("try again...")
    else:
        print("try again...")
        continue
    
    if start_num == end_num:
        break
