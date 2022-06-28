import random 
def main():
    correct = shutudai()
    kaito(correct) 

def shutudai():
    question_ans = [{"q":"サザエの旦那の名前は？","a": ["マスオ","ますお","鱒男"]},{"q":"カツオの妹の名前は?","a":["ワカメ","わかめ"]},{"q": "タラオはカツオから見てどんな関係?","a":["甥","おい","甥っ子","おいっこ"]}]
    print("問題：")
    r = random.randint(0,2) 
    print(question_ans[r]["q"])
    return question_ans[r]["a"]

def kaito(correct):
    answer  = input("答えよ")
    if answer in correct:
        print("正解！")
    else:
        print("不正解！")

if __name__ == "__main__":
    main()
