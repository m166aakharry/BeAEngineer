while True:
    try:
        number = int(input("請輸入數字:"))
        print(f"你輸入的是:{number}")
        break
    except ValueError:
            print("輸入錯誤，請重新輸入數字！")
