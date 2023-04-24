from bayes import BayesianFilter

bf = BayesianFilter()

# 학습 데이터 준비하기
with open('corpus.txt', 'r', encoding='utf-8') as f:
    lines = f.readlines()
    for line in lines:
        line = line.strip()  # 공백 제거
        if len(line) < 8:  # 짧은 문자열은 건너뛰기
            continue
        text = line[6:-3]
        category = line[-1]
        if category == "0":
            category = "광주과학고"
            print("\r광주과학고 학습중")
        elif category == "1":
            category = "욕설"
            print("\r욕설 학습중")
        elif category == "4":
            category = "일상대화"
            print("\r일상대화 학습중")
        else:
            print(category + "누락")
            continue
        bf.fit(text, category)

# 예측
pre, scorelist = bf.predict("광주과학고등학교 기숙사 사칙 준수 요망")
print("결과 =", pre)
print(scorelist)