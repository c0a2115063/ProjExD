import random
TaishouMoji = 10
KessonMoji  = 2
#グローバル変数として定義
Alphabet = [chr(i) for i in range(65,91)]
Alphabet_random =  random.sample(Alphabet, k = TaishouMoji)

print("対象文字：")
print(Alphabet_random)
#ランダムされたアルファベットの１０文字をリスト型で出力

hyouji = random.sample(Alphabet_random,8)
print("表示文字")
print(hyouji)
#表示文字だけ書けるように追加した