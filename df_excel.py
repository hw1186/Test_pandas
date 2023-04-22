import pandas as pd

data1 = {'name' : ['Jerry','Riah','Paul'],
        'algol' : ['A','A+','B'],
        'basic' : ['C','B','B+'],
        'c++' : ['B+','C','C+']} # 데이터 1

data2 = {'c0':[1,2,3],
        'c1':[4,5,6],
        'c3':[7,8,9],
        'c4':[10,11,12],
        'c5':[13,14,15]} # 데이터 2

df1 = pd.DataFrame(data1) # df1
df1.set_index('name', inplace=True)

df2 =pd.DataFrame(data2) #df2
df2.set_index('c0', inplace=True)

print(df1)
print('\n')
print(df2)

# set_index inplace = True 는 해당 데이터를 기준으로 정렬을 한다

'''
        <엑셀 파일 만들기>
        
writer = pd.ExcelWriter("test_excel.xlsx") // 엑셀 파일 쓰기
df1.to_excel(writer, sheet_name='1번 시트')  // 시트 저장
df2.to_excel(writer, sheet_name='2번 시트') 
writer.save() // 저다


'''