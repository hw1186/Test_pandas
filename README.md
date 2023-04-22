# venv 가상 환경 접속 방법

source venv/bin/activate

# pandas install

pip3 install pandas

# pandas 자료구조 

Series : 인덱스와 값으로 구성 자료구조

DataFrame : Series 들의 집합

# csv 

표 형태의 데이터를 저장하는 파일 형식

# pandas 인덱스 활용 및 정

1. 인덱스란

범위에서 특정 순번의 위치하는 값을 의미한다

2. se_index 인덱스를 세팅한다

3. 인덱스를 다시 세팅할시 기존의 인덱스는 사라진다

4. 인덱스를 재베치 하고 싶을때는 reindex() 를 사용한

5. drop=True 기존의 인덱스를 버리고 재배치를 시켜준다

6. sort_index 인덱스 기준으로 내림차순 정렬 (디폴트는 오름차순이다)

# 파이썬 패키지 관리하기

Terminal 

pip freeze > requirements.txt

- 사용하던 패키지를 txt 파일에 저장함

$ pip install -r requirements.txt

- 사용하던 패키지를 다운받음




# Test_pandas
