import pandas as pd

'''
<파일 읽고 쓰기 예제>
1. DF를 만든다
2. csv 파일에 저장한
index = False 는 df에 추가된 인덱스 없이 저장해준다
3. 읽기 때는 첫 번째 행을 header 로 지정해서 불러온다 불러올 데이터가 없으면 header=None 옵션을 추가해야 한다
'''

# 파일 쓰기
df = pd.DataFrame({'c0':[0,1,2],'c1':[1,2,3],'c2':[4,5,6],'c3':[7,8,9]})
df.to_csv("test.csv", index=False) # 쓰기

# 파일 읽기
df2 = pd.read_csv("test.csv",header=None)

# c0을 불러옴 인덱스 값으로 불러온다
df3 = pd.read_csv("test.csv",index_col='c0')

# 열 이름 지정하기
df4 = pd.read_csv("test.csv",names=['1열','2열','3열','4열'])





