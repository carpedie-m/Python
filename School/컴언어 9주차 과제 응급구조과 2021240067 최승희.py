while True:
    in_str = input("input your exquation (or press q for quit) : ")
    if in_str == "q":
        break

    cnt = len(in_str.split(" "))
    if cnt != 3:
            print(" usage : num1 op num2, seperated by blank.")
            continue
    num1, op, num2 = in_str.split(" ")

    num1 = int(num1)
    num2 = int(num2)

    if op in ("/", "//", "%"):
        if num2 == 0:
            print(f' {num2 = } with {op = } can not be permitted!')
        else:
            if op == "+":
                print(f' {in_str} = {num1 + num2}')
            elif op == "-":
                print(f' {in_str} = {num1 - num2}')
            elif op == "*":
                print(f' {in_str} = {num1 * num2}')
            elif op == "/":
                print(f' {in_str} = {num1 / num2}')
            elif op == "%":
                print(f' {in_str} = {num1 % num2}')
            elif op == "//":
                print(f' {in_str} = {num1 // num2}')
            else:
                print(f' {in_str} is not suported!')
    else:
        if op == "+":
            print(f' {in_str} = {num1 + num2}')
        elif op == "-":
            print(f' {in_str} = {num1 - num2}')
        elif op == "*":
            print(f' {in_str} = {num1 * num2}')
        elif op == "/":
            print(f' {in_str} = {num1 / num2}')
        elif op == "%":
            print(f' {in_str} = {num1 % num2}')
        elif op == "//":
            print(f' {in_str} = {num1 // num2}')
        else:
            print(f' {in_str} is not suported!')