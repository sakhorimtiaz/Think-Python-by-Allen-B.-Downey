def eval_loop():
    last_result = None
    while True:
        user_input = input("Enter an expression (or 'done' to exit): ")
        if user_input.upper() == 'DONE':
            break
        try:
            last_result = eval(user_input)
            print(last_result)
        except Exception as e:
            print(e)
            print("Error:",e)
    return last_result
eval_loop()
