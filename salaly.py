
import sqlite3
import sys
import datetime

#今から何をしたいかを選択
def  checksalary_or_addtime():
    print("今月の現在までの給料を確認する場合は『C』を入力してください")
    print("新たに労働時間を追加する場合は『A』を入力してください")
    print("＊注意：追加の場合は今年度の分以外は入力できません")
    push_word = raw_input(">>> ")
    if push_word == "C" or push_word == "c":
        print("--------------------------------------------------------------")
        print("\n今月の現在までの給料を確認します\n")
        check_no = 1
    elif push_word == "A" or push_word == "a":
        check_no = 2
    else:
        print("\n誤入力を確認しました。再度入力し直してください\n")
        print("--------------------------------------------------------------")
        check_no = 0
    return check_no

#＝＝＝＝新たに労働時間を追加に関する関数|START＝＝＝＝
def alert01(today):
    print("--------------------------------------------------------------")
    print("\n＊注意＊")
    print("今日は%d年%d月%d日です。\n現在入力できるのは\n" % (today.year,today.month,today.day))
    if today.month >= 4:
        print("『%d年4月1日〜%d年%d月%d日』" % (today.year,today.year,today.month,today.day))
    else:
        print("『%d年4月1日〜%d年%d月%d日』" % (today.year-1,today.year,today.month,today.day))
    print("の間だけです。\nそれ以外の期間を入力しようとすると誤入力になります\n")
    print("--------------------------------------------------------------")

#入力されたのが1月〜12月の間かを確認
def check_month(input_word,today):
    if input_word <= 0 or input_word >12:
                return 0
    else:
        if today.month >= 4:
            if input_word <4 or today.month < input_word:
                print("入力された月は対象外の期間です")
                return 0
        else:
            return 1

#入力された文字が数値かを判定【月バージョン】
def check_inputword_month(input_word,today):
    check_no = 0
    while check_no == 0:
        if input_word.isdigit() == True:
            input_word = int(input_word)
            check_no = check_month(input_word,today)
        else:
            check_no = 0
        if check_no == 0:
            print("\n誤入力を確認しました。再度入力し直してください")
            print("--------------------------------------------------------------")
            print("追加したい月を入力してください")
            input_word = raw_input(">>> ")
    return input_word

#入力されたのが正しい日付の範囲内か確認
def check_day(input_word,input_month,input_year):
    if input_word <= 0 or input_word >31:
        return 0
    else:
        if input_month == 2:
            if input_year%4 == 0:
                if input_year%100 == 0:
                    if input_year%400 == 0:
                        if input_word>29:
                            return 0
                        else:
                            return 1
                    else:
                        if input_word>28:
                            return 0
                else:
                    if input_word>29:
                        return 0
            else:
                if input_word>28:
                    return 0
        elif input_month == 4 or input_month == 6 or input_month == 9 or input_month == 11:
            if input_word>30:
                return 0
            else:
                return 1
        else:
            if input_word>31:
                return 0
            else:
                return 1


#入力された文字が数値かを判定【日バージョン】
def check_inputword_day(input_word,today,input_month,input_year):
    check_no = 0
    while check_no == 0:
        if input_word.isdigit() == True:
            input_word = int(input_word)
            if today.month == input_month:
                if today.day < input_word or input_word <= 0:
                    check_no = 0
                else:
                    check_no = 1
            else:
                check_no = check_day(input_word,input_month,input_year)
        else:
            check_no = 0
        if check_no == 0:
            print("\n誤入力を確認しました。再度入力し直してください")
            print("--------------------------------------------------------------")
            print("追加したい月を入力してください。")
            input_word = raw_input(">>> ")
    return input_word

#入力された文字が数値かを判定【時間バージョン】
def check_inputword_time(input_word):
    check_no = 0
    while check_no == 0:
        if input_word.isdigit() == True:
            input_word = int(input_word)
            check_no = 1
        else:
            check_no = 0
        if check_no == 0:
            print("\n誤入力を確認しました。再度入力し直してください")
            print("--------------------------------------------------------------")
            print("追加したい月を入力してください。")
            input_word = raw_input(">>> ")
    return input_word

#続行確認
def  check_continue():
    print("このまま続ける場合は『Y』、やめてプログラムを終了する場合は『N』を入力してください")
    push_word = raw_input(">>> ")
    if push_word == "Y" or push_word == "y":
        check_no = 1
    elif push_word == "n" or push_word == "N":
        check_no = 2
    else:
        print("\n誤入力を確認しました。再度入力し直してください\n")
        print("--------------------------------------------------------------")
        check_no = 0
    return check_no

#＝＝＝＝新たに労働時間を追加に関する関数|FINISH＝＝＝＝

#＝＝＝＝今月の現在までの給料を確認に関する関数|START＝＝＝＝

#入力された年が異常ではないか確認
def check_year_cs(input_word,today):
    if input_word > today.year or input_word <= 0:
        return 0
    else:
        return 1

#入力された文字が数値かを判定【年バージョン】
def check_inputword_year_cs(input_word,today):
    check_no = 0
    while check_no == 0:
        if input_word.isdigit() == True:
            input_word = int(input_word)
            check_no = check_year_cs(input_word,today)
        else:
            check_no = 0
        if check_no == 0:
            print("\n誤入力を確認しました。再度入力し直してください")
            print("--------------------------------------------------------------")
            print("確認したい月を入力してください")
            input_word = raw_input(">>> ")
    return input_word

#入力されたのが1月〜12月の間かを確認
def check_month_cs(input_word,today,input_word_year):
    if input_word <= 0 or input_word >12:
        return 0
    else:
        if input_word_year == today.year:
            if input_word > today.month:
                return 0
            else:
                return 1
        else:
            return 1

#入力された文字が数値かを判定【月バージョン】
def check_inputword_month_cs(input_word,today,input_word_year):
    check_no = 0
    while check_no == 0:
        if input_word.isdigit() == True:
            input_word = int(input_word)
            check_no = check_month_cs(input_word,today,input_word_year)
        else:
            check_no = 0
        if check_no == 0:
            print("\n誤入力を確認しました。再度入力し直してください")
            print("--------------------------------------------------------------")
            print("確認したい月を入力してください")
            input_word = raw_input(">>> ")
    return input_word

def check_day_cs(input_month,input_year):
    if input_month == 2:
        if input_year%4 == 0:
            if input_year%100 == 0:
                if input_year%400 == 0:
                    return 29
                else:
                    return 28
            else:
                return 29
        else:
            return 28
    elif input_month == 4 or input_month == 6 or input_month == 9 or input_month == 11:
        return 30
    else:
        return 31

#＝＝＝＝今月の現在までの給料を確認に関する関数|FINISH＝＝＝＝

#今月の現在までの給料を確認
def check_salary(db,cur):
    today = datetime.date.today()

    print("給料を確認したい年を入力してください")
    check_salary_year = raw_input(">>> ")
    check_salary_year = check_inputword_year_cs(check_salary_year,today)
    print(check_salary_year)

    print("給料を確認したい月を入力してください")
    check_salary_month = raw_input(">>> ")
    check_salary_month = check_inputword_month_cs(check_salary_month,today,check_salary_year)

    if check_salary_month == today.month and check_salary_year == today.year:
        j = today.day + 1
    else:
        check_salary_day = check_day_cs(check_salary_month,check_salary_year)
        j = check_salary_day + 1
    n_time = [0] * j
    s_time = [0] * j
    sum_n_time = 0
    sum_s_time = 0
    for i in xrange(1,j):
        sql = "select * from sms where days = '%d年%d月%d日'" % (check_salary_year,check_salary_month,i)
        row = cur.execute(sql)
        for salary_time in row:
            n_time[i]=salary_time[1]
            s_time[i]=salary_time[2]
    for i in xrange(1,today.day+1):
        sum_n_time = sum_n_time + n_time[i]
        sum_s_time = sum_s_time + s_time[i]
    sum_salary = sum_n_time * 868 + sum_s_time * 868 * 1.35
    print("--------------------------------------------------------------")
    if check_salary_month == today.month and check_salary_year == today.year:
        print("あなたの%d年%d月%d日現在までの給料は...\n\n%d円\n\nです" % (check_salary_year,check_salary_month,today.day,sum_salary))

    else:
        print("あなたの%d年%d月の給料は...\n\n%d円\n\nです" % (check_salary_year,check_salary_month,sum_salary))
    print("--------------------------------------------------------------")


#新たに労働時間を追加
def add_time(db,cur):
    today = datetime.date.today()
    alert01(today)

    print("追加したい月を入力してください")
    input_month = raw_input(">>> ")
    input_month = check_inputword_month(input_month,today)
    input_year = today.year
    if today.month < 4:
        if input_month >= 4:
            input_year = input_year - 1
    print("追加したい日を入力してください")
    input_day = raw_input(">>> ")
    input_day = check_inputword_day(input_day,today,input_month,input_year)
    print("--------------------------------------------------------------")
    print("\n追加したい日は...\t%d年%d月%d日\tですね" % (input_year,input_month,input_day))
    print("--------------------------------------------------------------")
    check_no = 0
    while check_no == 0:
        check_no = check_continue()
    if check_no == 1:
        print("--------------------------------------------------------------")
        print("\n今月の現在までの給料を確認します\n")
    elif check_no == 2:
        print("確認しました。プログラムを終了します")
        sys.exit()

    print("\n%d年%d月%d日に働いた総時間数を入力してください" % (input_year,input_month,input_day))
    input_totaltime = raw_input(">>> ")
    input_totaltime = check_inputword_time(input_totaltime)
    print("--------------------------------------------------------------")
    print("\n%d時間の中で特別に加算される(深夜給などの)時間帯の時間数を入力してください。" % input_totaltime)
    input_sp_time = raw_input(">>> ")
    input_sp_time = check_inputword_time(input_sp_time)         
    input_no_time = input_totaltime - input_sp_time
    print("--------------------------------------------------------------")
    print("\n以下の内容をデータベースに保存します。\n")
    print("--------------------------------------------------------------")
    print("\n%d年%d月%d日" % (input_year,input_month,input_day))
    print("総時間数：%d" % input_totaltime)
    print("特別加算対象の時間帯の時間数：%d" % input_sp_time)
    print("--------------------------------------------------------------")
    #-----------メモ-----------
    #ここで、以前に同じ日にちにすでに入力されているかを確認して、入力されていたら上書きをするかを尋ねるようにする
    #すでに入力されている日は上書き保存のみの選択にさせる。めんどくさいので。
    #すでに入力されていれば"Y"、まだ入力されていなければ"N"を返す。
    sql = "select case when days = '%d年%d月%d日' then 'Y' else 'N' end from sms;" % (input_year,input_month,input_day)
    row = cur.execute(sql)
    for double_check in row:
        if double_check[0] == "Y":
            print("すでに%d年%d月%d日にはデータが入力されています。")
            print("更新作業を続けますか？")
            check_no = 0
            while check_no == 0:
                check_no = check_continue()
                if check_no == 1:
                    print("確認しました。では、データを更新します")
                    sql = "update sms set n_wt = %d and s_wt = %d where days = '%d年%d月%d日'" % (input_no_time,input_sp_time,input_year,input_month,input_day)
                    cur.execute(sql)
                    db.commit()
                    print("データの更新が完了しました。さらに入力を続けますか？")
                elif check_no == 2:
                    print("確認しました。プログラムを終了します")
                    sys.exit()
        elif double_check[0] == "N":
            sql = "insert into sms values('%d年%d月%d日',%d,%d)" % (input_year,input_month,input_day,input_no_time,input_sp_time)
            cur.execute(sql)
            db.commit()
            print("データベースにデータを追加しました。さらに入力を続けますか？")
    check_no = 0
    while check_no == 0:
        check_no = check_continue()
    if check_no == 1:
        print("--------------------------------------------------------------")
        print("\nではデータベースに追加します。\n")
        return 2
    elif check_no == 2:
        print("確認しました。プログラムを終了します。お疲れさまでした")
        cur.close()
        db.close()
        sys.exit()

#メイン
if __name__ == '__main__':
    db = sqlite3.connect("salary.db")
    cur = db.cursor()
    sql = "create table sms(days,n_wt,s_wt);"

    try:
        cur.execute(sql)
        print("--------------------------------------------------------------")
        print("\nデータベースを作成しました...")
        print("データベースへのアクセスに成功しました")
        print("--------------------------------------------------------------")
    except sqlite3.OperationalError:
        print("--------------------------------------------------------------")
        print("\nデータベースにアクセスに成功しました\n")
        print("--------------------------------------------------------------")

    check_no = checksalary_or_addtime()

    while check_no == 0:
        check_no = checksalary_or_addtime()

    if check_no == 1:
        check_salary(db,cur)
    elif check_no == 2:
        while check_no == 2:
            check_no == add_time(db,cur)
