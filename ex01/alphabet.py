import random
TaishouMoji = 10
KessonMoji  = 2
#グローバル変数として定義
Alphabet = [chr(i) for i in range(65,91)]
Alphabet_random =  random.sample(Alphabet, k = TaishouMoji)

print("対象文字：")
print(Alphabet_random)
#アルファベットの配列をランダムで10回出力
