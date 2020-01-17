user = str 
end = "0" 
hours = round(8,2) 
print("給料計算機") 
while user != end: 
    print() 
    user = input("名前を入力してください(止める場合は0を入力): ") 
    if user == end: 
        print("終了") 
    else: 
        hours = (float(input("働いた時間: ",))) 
        payrate =(float(input("時給: ￥",))) 
    if hours < 8: 
        print("名前: ", user) 
        print("残業時間: 0") 
        print("残業手当: ￥0.00") 
        regularpay = round(hours * payrate, 2) 
        print("総支給額: ￥", regularpay) 
    elif hours > 8: 
        overtimehours = round(hours - 8.00,2) 
        print("残業時間: ", overtimehours) 
        print("名前: ", user) 
        regularpay = round(8.00 * payrate,2) 
        overtimerate = round(payrate * 1.25, 2) 
        overtimepay = round(overtimehours * overtimerate) 
        grosspay = round(regularpay+overtimepay,2) 
        print("基本給: ￥", regularpay) 
        print("残業手当: ￥",overtimepay) 
        print("総支給額: ￥", grosspay) 