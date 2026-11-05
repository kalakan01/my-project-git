while True:

    print("1. جمع")
    print("2. تفریق")
    print("3. ضرب")
    print("4. تقسیم")
    print("5. خروج")

    choice = input("انتخاب کن: ")
    if choice == "5":
        print("خدانگهدار!")
        break
    try:
        num1 = float(input("عدد اول: "))
        num2 = float(input("عدد دوم: "))
    except ValueError:
        print("لطفاً فقط عدد وارد کن")
        continue

    if choice == "1":
        print("نتیجه:", num1 + num2)

    elif choice == "2":
        print("نتیجه:", num1 - num2)

    elif choice == "3":
        print("نتیجه:", num1 * num2)

    elif choice == "4":
        if num2 != 0:
            print("نتیجه:", num1 / num2)
        else:
            print("تقسیم بر صفر ممکن نیست")


    else:
        print("انتخاب اشتباه است")
	

