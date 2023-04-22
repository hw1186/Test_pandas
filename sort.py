import pandas as pd

dict_data = {'c0':[1,2,3], 'c1':[4,5,6], 'c2':[7,8,9], 'c3':[10,11,12], 'c4':[13,14,15]}
df = pd.DataFrame(dict_data, index = ['r0','r1','r2'])

ndf = df.sort_index(ascending=True)
print(ndf)

'''

    < 인덱스 기준으로 정렬 >

ndf = df.sort_index(ascending=False)


'''


'''

    < 특정 열의 데이터 값을 정렬 >

ndf = df.sort_values(by = 'c1',ascending=False)


'''