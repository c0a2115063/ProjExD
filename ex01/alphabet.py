import random
TaishouMoji = 10
KessonMoji  = 2
#グローバル変数として定義
Alphabet = [chr(i) for i in range(65,91)]
random.shuffle(Alphabet)

print("対象文字：")
#アルファベットの配列をランダムで10回出力
for i in range(10):
    print(Alphabet)
