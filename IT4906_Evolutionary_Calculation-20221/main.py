# import libraries
import random
import numpy as np
import math
# files
import file
from common import func as commonFunc
from genetic_algorithm import partial_mapped_crossover as algorithm

# Hằng số
NUMBER_OF_TRUCKS = 3
NUMBER_OF_DRONES = 3
TRUCK_SPEED = 30  # km/h
DRONE_SPEED = TRUCK_SPEED * 1.5
DRONE_LIMIT_TIME = 15  # phút
N = 6  # Lấy dữ liệu từ dòng số 6
LIMITED_GENS = 50  # Số lượng gen giới hạn

# Lấy mảng chứa các dòng dữ liệu trong file
lines = file.readFollowingLines(N)

# Khởi báo các biến
numberOfTrucks = NUMBER_OF_TRUCKS  # số lượng xe tải
# số lượng khách hàng + 1
numberOfCustomers = len(lines)
numberOfDrones = NUMBER_OF_DRONES  # số lượng drone
customerX = []  # Lưu trữ hoành độ của các khách hàng
customerY = []  # Lưu trữ tung độ của các khách hàng
releaseDate = []  # Lưu thời gian sản phẩm sẵn sàng của các khách hàng
vector = []  # vector nối các depot với các vị trí khách hàng
angles = np.zeros((numberOfCustomers, numberOfCustomers)
                  )  # chứa góc các vector với nhau
# Mảng chứa thời gian bay của drone đến các vị trí khách hàng
# Nếu vị trí khách hàng nằm ngoài khoảng bay được của drone -> gán -1
timeDepotToCusByDrone = []
# mảng chứa tổng thời gian từ depot đến vị trí khách hàng và release date
heuristicTime = [0]
# Trung bình (Thời gian từ depot đến vị trí các khách hàng + release date)
averageOfHeuristicTime = 0
# Mảng chứa vị trí các khách hàng đến thăm của từng xe tải
destination = []
# Mảng chứa điểm đến của các xe tải
truckDestinations = [[]]
# Phương sai
variance = 0
# Mảng chứa các thời gian di chuyển của truck giữa các điểm
timeOfDesToDes = np.zeros((numberOfCustomers, numberOfCustomers))

# Khởi tạo các biến
for line in lines:
    lineNum = line.split()
    customerX.append(int(lineNum[0]))  # customerX[0] : depot
    customerY.append(int(lineNum[1]))
    releaseDate.append(int(lineNum[-1]))
    # khởi tạo vector tạo bởi all data point (include depot point) and depot
    # vector by depot point and all data point (include depot)
    vector.append([customerX[-1] - customerX[0], customerY[-1] - customerY[0]])

# Khởi tạo mảng chứa các thời gian di chuyển của truck giữa các điểm
for i in range(0, numberOfCustomers):
    for j in range(i + 1, numberOfCustomers):
        # Tinh khoang cach theo mahattan
        distance = abs(customerX[i] - customerY[i]) + \
            abs(customerX[j] - customerY[j])
        # t = s / v
        time = distance / TRUCK_SPEED
        timeOfDesToDes[i][j] = timeOfDesToDes[j][i] = time * \
            60  # Truck_time all data point

# khởi tạo mảng chứa thời gian bay của drone
for arr in vector:
    # Tính khoảng cách theo eclip
    distance = math.sqrt(arr[0] * arr[0] + arr[1] * arr[1])
    # Tính thời gian
    time = distance / DRONE_SPEED * 60  # đổi ra phút
    # Kiểm tra giới hạn bay
    if (time <= DRONE_LIMIT_TIME):
        timeDepotToCusByDrone.append(time)
    else:
        timeDepotToCusByDrone.append(-1)  # flying time: include depot to depot

# Khởi tạo mảng các góc giữa các vector


def getAngle(v1, v2):
    numerator = v1[0] * v2[0] + v1[1] * v2[1]
    denominator = math.sqrt(v1[0] * v1[0] + v1[1] * v1[1]) * \
        math.sqrt(v2[0] * v2[0] + v2[1] * v2[1])
    cos = round(numerator/denominator, 10)
    angle = math.degrees(math.acos(cos))
    return angle  # ?tinh cos nay khong the hien duoc goc tu` -> tinh

#0 <=  max_angle <= 180
# truong hop: max_angle < 180, max_angle = 180 ( 360, < 360)
# objective: tu 1 diem -> xac dinh thu tu cac diem theo 1 vong tron


    # vector[0] = 0 (vector by depot point & itself)
for i in range(1, numberOfCustomers):
    for j in range(i, numberOfCustomers):
        angles[i][j] = getAngle(vector[i], vector[j])
        # matrix angles: angle by customer i and customer j (numberOfCustomer x numberOfCustomer)
        angles[j][i] = angles[i][j]
        #vector[0], vector[j] = 0

# Khởi tạo mảng chứa thời gian ước lượng từ gốc depot đến vị trí các khách hàng
for i in range(1, numberOfCustomers):
    # append thời gian
    heuristicTime.append(timeOfDesToDes[0][i] + releaseDate[i])
    # tính tổng
    averageOfHeuristicTime += heuristicTime[-1]

# Khời tạo giá trị trung bình
averageOfHeuristicTime /= NUMBER_OF_TRUCKS
# Khởi tạo phương sai
variance = averageOfHeuristicTime / 5

# chuyển đổi list sang array
customerX = np.array(customerX)
customerY = np.array(customerY)
releaseDate = np.array(releaseDate)
vector = np.array(vector)

# Lấy 1 vị trí khách hàng ngẫu nhiên
customerLocation = random.randint(1, numberOfCustomers - 1)

# Lặp từ phần tử đầu đến kế cuối,
# Vì khi đến phần tử cuối là đã sắp xếp thành công


def getCustomerList(arr):
    # Khởi tạo vị trí khách hàng
    location = []
    for i in range(0, numberOfCustomers):
        location.append(i)
    # Hoán đổi vị trí
    for i in range(0, numberOfCustomers):
        for j in range(i + 1, numberOfCustomers):
            if (arr[i] > arr[j]):
                # Hoán đổi giá trị
                tmp = arr[i]
                arr[i] = arr[j]
                arr[j] = tmp
                # hoán đổi vị trí
                tmp = location[i]
                location[i] = location[j]
                location[j] = tmp
    return location


# Sắp xếp vị trí các khách hàng theo góc quay từ bé đến lớn
# angles[7]: list of angles is created by vector(depot, customer_7) and other vectors ???
locations = getCustomerList(angles[customerLocation])
# and then sort them ?
# issue: trường hợp tốt nhất các điểm customer ở xung quanh depot, sắp xếp theo angles giữa 1 điểm và các điểm còn lại thì thứ tự các điểm vẫn bị lộn xộn theo 2 phía của điểm được chọn ban đầu
# -> correct: xây dựng location: xuất phát từ 1 điểm bất kì, điểm tiếp theo  = góc nhỏ nhất giữa điểm đang xét và tất cả các điểm còn lại


# Cập nhật mảng đích đến
count = NUMBER_OF_TRUCKS - 1
lastIndex = 1
for i in range(1, numberOfCustomers):
    if (count > 0):
        sum = 0
        for j in range(lastIndex, i + 1):
            sum += heuristicTime[locations[j]]
        if (abs(sum - averageOfHeuristicTime) <= variance):
            for k in range(lastIndex, i + 1):
                destination.append(locations[k])
            lastIndex = i + 1
            destination.append(-1)
            count -= 1

for k in range(lastIndex, numberOfCustomers):
    destination.append(locations[k])

# Cập nhật mảng 2 chiều chứa các điểm đến của từng xe
for location in destination:
    if (location != -1):
        truckDestinations[-1].append(location)
    else:
        truckDestinations.append([])

# Algorithm
# Thiết lập mảng chứa các đoạn gen chưa hoàn chỉnh
subGensTable = []
for i in range(NUMBER_OF_TRUCKS):
    subGensTable.append(commonFunc.getAllPermutations(truckDestinations[i]))

# Thiết lập mảng chứa các gen hoàn chỉnh
# Bảng gen drone
gensDroneTable = []
for i in range(LIMITED_GENS):
    # Khởi tạo từng gen
    gensDroneTable.append([])
    for j in range(numberOfCustomers + NUMBER_OF_TRUCKS - 2):
        # Lấy ngẫu nhiên 1 số từ 0 đến 1
        randomNum = random.random()
        # Đẩy vào mảng cuối cùng của bảng genes
        gensDroneTable[-1].append(randomNum)
# Bảng gen Trucks
gensTable = []
for i in range(LIMITED_GENS):
    # Khởi tạo từng gen
    gensTable.append([])
    for subgen in subGensTable:
        # Lấy ngẫu nhiên 1 đoạn gen
        randomIndex = random.randint(0, len(subgen) - 1)
        # Đẩy vào đoạn gen chưa hoàn chỉnh
        gensTable[-1] += subgen[randomIndex] + [-1]
    # Loại bỏ -1 ở cuối mảng
    gensTable[-1].pop()

# Tạo bảng gen mới
newGensDroneTable = []
newGensTable = []
for i in range(LIMITED_GENS):
    # Lấy ngẫu nhiên 2 gen trong bảng gen
    nextIndex = random.randint(0, LIMITED_GENS - 1)
    while (nextIndex == i):
        nextIndex = random.randint(0, LIMITED_GENS - 1)
    # Lai ghép tạo gen mới
    newGens = algorithm.PMX_crossover(
        gensTable[i], gensTable[nextIndex], gensDroneTable[i], gensDroneTable[nextIndex])
    count = 0
    for i in newGens[0]:
        if (i == -1):
            count += 1
    if (count > 2):
        print(newGens[0])
    count = 0
    for i in newGens[1]:
        if (i == -1):
            count += 1
    if (count > 2):
        print(newGens[1])

    newGensTable.append(newGens[0])
    newGensTable.append(newGens[1])
    newGensDroneTable.append(newGens[2])
    newGensDroneTable.append(newGens[3])

print(newGens)
