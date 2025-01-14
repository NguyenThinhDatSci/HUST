def fitness(timeDepotToCusByDrone, timeOfDesToDesByTruck, destination):  #version chưa tính đến gene của drone & số lượng drone (drone resupply tại mọi điểm trong khoảng cách bay)
  #split gene trucks_routing to list truck_routing
  truckDestinations = [[] for i in range(NUMBER_OF_TRUCKS) ]
  tmp=0
  for location in destination:
    if (location != -1):
        truckDestinations[tmp].append(location)
    else:
        tmp += 1
  del tmp
  
  #
  Dj = timeDepotToCusByDrone
  Tij =  timeOfDesToDesByTruck
  service_time = 0
  index_Ehi0 = copy.deepcopy(truckDestinations)
  
  #Calculate Time_visit 
  Ti = [[] for i in range(NUMBER_OF_TRUCKS)]
  for truck_i in range(NUMBER_OF_TRUCKS):
    if len(index_Ehi0[truck_i]) == 0:
      Ti[truck_i].append(0)
    else:
      if Dj[index_Ehi0[truck_i][0]] == -1:                                    #check first visit by truck
        i=1
        while ( i < len(index_Ehi0[truck_i])) and (Dj[index_Ehi0[truck_i][i]] == -1):
          i = i + 1
        Ti[truck_i].append(np.max(releaseDate[index_Ehi0[truck_i][:i]]) + Tij[0][index_Ehi0[truck_i][0]] )
      else:
        Ti[truck_i].append(Tij[0][index_Ehi0[truck_i][0]])       #khoi tao T0
     

      for i in range(len(index_Ehi0[truck_i]) - 1):               
        if Dj[index_Ehi0[truck_i][i]] == -1:                              #có đường đi của drone: check vị trí đó trên mảng drone
          waitting_time = 0
        else:
          j=i+1
          while( j < len(index_Ehi0[truck_i]) ) and (Dj[index_Ehi0[truck_i][j]] == -1)  :
            j = j+1
          waitting_time = max(0, np.max(releaseDate[index_Ehi0[truck_i][i:j]] )  - Ti[truck_i][-1] - service_time) + Dj[index_Ehi0[truck_i][i]] 
        Ti[truck_i].append(Ti[truck_i][-1] + service_time + waitting_time  + Tij[index_Ehi0[truck_i][i]][index_Ehi0[truck_i][i+1]] )
      #add time truck return to depot
      Ti[truck_i].append(Ti[truck_i][-1] + service_time + Tij[index_Ehi0[truck_i][-1]][0])

#    #Time_visit[0][j]: thoi gian truck 0 đến khach hang thu j+1 trong list khach hang can tham
#    #khởi tạo Time_visit[0][0]:  thời gian truck 0 đến khách hàng thứ 1 trong list khách hàng mình cần đến 
#    #Time_visit[0][j] = Time_visit[0][j-1]  + watting_time_tai_j + service_time + Truck_time[khach_hang_thu_j][khach hang_thu_j+1]   
#    #waitting_time = max(0, releaseDate của những điểm tiếp theo truck cần phải đến thăm (giữa 2 điểm khách hàng được resupply bởi drone)) + flying time
#             #giới hạn drone ->waitting_time: + thời gian chờ drone khác bay về depot + thời gian sạc của drone 
  
  #return 60/max(tv[-1] for tv in Ti)       #1/complete_time  (hour)
  return Ti             
