# if 语句中在嵌套if语句

ticket = input("是否买到了车票？")
if ticket == "yes" :
    print("买到了车票，可以进站！")
    safe = input("安检是否通过？")
    if safe == "yes":
        print("安检通过，进入候车室")
    else:
        print("安检未通过，请检查携带物品")
else:
    print("车票没有，请先购买车票")