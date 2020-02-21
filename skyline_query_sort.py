import numpy as np
import matplotlib.pyplot as plt
import math

############################# 거리함수
def euclidean_distance_2d(x, y):
    distance = math.sqrt(sum([(a - b) ** 2 for a, b in zip(x, y)]))
    return distance

def euclidean_distance(x,y):
    n= x**2 + y**2
    return math.sqrt(n)


############################# NN 인덱스 반환
def boundedNNSearch(data, distance_function):
        
    data_distance = []
    for x, y in data:
#         data_distance.append(distance_function([0,0], [x,y])) # 원점과 현재 데이터의 거리 계산 후 data_distance에 append한다
        data_distance.append(distance_function(x, y)) # 원점과 현재 데이터의 거리 계산 후 data_distance에 append한다

    return data_distance


############################# 메인 함수
def getskylines(data, distance_function=euclidean_distance):
    ######## 데이터셋 정규화 ## 정규화를 안하면 스카이라인을 찾는 순서가 실제로 NN아닐 수 있음
    from sklearn.preprocessing import MinMaxScaler
    scaler = MinMaxScaler()
    data = scaler.fit_transform(data)
    
    skylines = []

    data_dist = boundedNNSearch(data, distance_function) # 데이터 전체에 대한 Distance 값을 반환 받는다
    _, data = zip(*sorted(zip(data_dist, data))) # 데이터를 Distance의 순서로 sorting
    data = scaler.inverse_transform(data).tolist() #역정규화

    # 첫 NN
    skylines.append(data[0])
    print(data[0])

    index = 1
    while True:
        temp_data = []
        for i in range(1, len(data), 1):
            x, y = data[i]

            if x >= skylines[index - 1][0] and y >=  skylines[index - 1][1]: # REGION 3면
                continue
            temp_data.append(data[i])
        data = temp_data
        if len(data) == 0 :
            break
        skylines.append(data[0])
        print(data[0])
        index += 1

    
    return skylines