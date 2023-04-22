import pandas as pd

a_data = {
    1 : 'a',
    2 : 'b',
    3 : 'c'
}


b_data = {
    4 : 'd',
    5 : 'e',
    6 : 'g'
}

data1 = pd.Series(a_data)
data2 = pd.Series(b_data)

DataFrame = pd.DataFrame({
    'data1' : data1,
    'data2' : data2
})