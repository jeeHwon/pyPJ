array = [
    [[1,2,3,4],[5,6,7,8]], 
    [[10,20,30,40],[50,60,70,80]],
    [[1,2,3,4],[5,6,7,8]], 
    [[10,20,30,40],[50,60,70,80]],
    [[1,2,3,4],[5,6,7,8]], 
    [[10,20,30,40],[50,60,70,80]]
]

# print(array[0][0])
temp = []
# temp.extend(array[0])
# temp.extend(array[1])
# print(temp)
# temp.remove([50, 60, 70, 80])
# print(temp)
array[1].remove([50, 60, 70, 80])
print(array)

# import pandas as pd
# df = pd.DataFrame(temp)
# print(df)