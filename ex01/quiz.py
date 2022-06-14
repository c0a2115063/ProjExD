import random 
def main():
    correct = shutudai()
    kaito(correct) 

def shutudai():
    question_ans1 = ["マスオ","ますお"]               # サザエの旦那の名前の回答例
    question_ans2 = ["ワカメ","わかめ"]               #カツオの妹の名前の回答例
    question_ans3 = ["甥","おい","甥っ子","おいっこ"] #タラオはカツオから見てどんな関係
    question_list = ["サザエの旦那の名前は？","カツオの妹の名前は？","タラオはカツオから見てどんな関係？"]
    print("問題：")
    Question = random.randint(question_list)
    print(Question)

def kaito(correct):
    answer  = input("答えよ")
    if answer in correct:
        print("正解！")
    else:
        print("不正解！")
