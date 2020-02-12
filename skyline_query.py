import numpy as np
import matplotlib.pyplot as plt

############################# 거리함수
def euclidean_distance(x, y):
    import math
    distance = math.sqrt(sum([(a - b) ** 2 for a, b in zip(x, y)]))
    return distance

############################# NN 인덱스 반환
def boundedNNSearch(data, distance_function):
        
    data_distance = []
    for x, y in data:
        data_distance.append(distance_function([0,0], [x,y])) # 원점과 현재 데이터의 거리 계산 후 data_distance에 append한다

    nn_idx = data_distance.index(min(data_distance)) # Nearest Neighbor의 인덱스를 얻는다
    return nn_idx



############################# #Region을 0, 1, 2으로 나눠주는 함수
def data_cut(data, todo, nn, region_idx):
    region = []
    for i in range(len(data)):
        x, y = data[i]

        region_dict ={0: x >= nn[0] and y >= nn[1], 1: y < nn[1], 2: x < nn[0]} #Region 0인지 1인지 2인지 딕셔너리
            
        if region_dict[region_idx]:
            continue
        region.append(data[i])
        
    if region_idx == 0:
        return region #Region의 데이터 반환

    else:
        if len(region) != 0: 

            todo.append(region) #해야할 일에 Region의 데이터 추가


############################# 메인 함수
def getskylines(data, distance_function=euclidean_distance):
    ######### 데이터셋 정규화
    from sklearn.preprocessing import MinMaxScaler
    scaler = MinMaxScaler()
    data = scaler.fit_transform(data)
    
    # norm_data = pd.DataFrame(norm_data, columns=data.columns)
    # norm_data.plot.scatter(x="price", y="distance")


    todo = []
    todo.append(data) # Todo에 데이터 추가
    del data

    skylines = []

    #### Todo 만큼 반복. Todo를 추가하면 추가된Todo 실행
    for i, region in enumerate(todo):
        nn = region[boundedNNSearch(region, distance_function)] ## NN 구하기
        
        data = data_cut(region, todo, nn, 0) # Region 3을 제외한 데이터 반환
        data_cut(data, todo, nn, 1)  # Region 1 을 todo에 추가
        data_cut(data, todo, nn, 2) # Region 2 todo에 추가

        
        nn = scaler.inverse_transform([nn]) #역정규화
        skylines.append(nn.reshape(2).tolist()) #스카이라인 추가
        print(skylines)

        todo[i] = None # 필요없는 변수 없애기

    return skylines




################################ PLOT용
# data2 = scaler.inverse_transform(region)

# plt.scatter(data2[:, 0], data2[:, 1])
# plt.xlim(0.34752048913785316,  190.65247951086215) 
# plt.ylim(-0.06839386840927793, 2.0993498601356593)
# plt.savefig("Region")
# plt.show()