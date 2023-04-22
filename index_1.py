import pandas as pd

exam_data = {'이름': ['서준', '우현', '인아'],
             '수학': [90, 80, 70],
             '영어': [98, 89, 95],
             '음악': [85, 95, 100],
             '체육': [100, 90, 90]}

df = pd.DataFrame(exam_data)
print(df)
print('\n')

ndf1 = df.set_index('이름')
print(ndf1)
print('\n')

ndf2 = ndf1.set_index(['음악'])
print(ndf2)
print('\n')

ndf3 = ndf1.set_index(['수학', '음악'])
print(ndf3)

'''

    < 인덱스로 지정을 하고 기존열을 남겨놓는다 >

print(ndf1.set_index('음악', drop = False))
print('\n')


'''