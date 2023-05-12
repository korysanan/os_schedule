def FCFS(n, processes, core) :
    processes.sort(key = lambda x:x[1])     #AT에 따라 모든 프로세스 정렬
    # 실행 순서와 각 프로세스의 실행 완료 시간, 대기 시간을 계산
    completion_time = [0]*n
    waiting_time = [0]*n
    turnaround_time = [0]*n

    #어떤 코어가 무슨 코어를 쓰는지, 코어갯수 확인
    core_number = 0

    for i in range(len(core)):      #코어 갯수 확인. 단일 코어랑 멀티코어랑 계산이 달라짐
        if(core[i]=="E"):
            core_number += 1
        elif(core[i]=="P"):
            core_number += 1

    graph = [[],[],[],[]]
    check = [0, 0, 0, 0]
    time_list = [[],[],[],[]]
    AW = [0, 0, 0, 0]
    onoff = [0, 0, 0, 0]
  
    sunseo = 0
    for i in range(n):
        # 실행 순서
        if(sunseo >= 4):
            sunseo = 0
        while(core[sunseo] == "O"):     #코어 중 하나라도 있을경우 작동 - sunseo는 사용할 코어 순서
            sunseo += 1
            if(sunseo >= 4):
                sunseo = 0
            

        if(check[sunseo] == 0):         #프로세스의 처음 입력 구분

            if(core[sunseo] == "E"):            #코어에 따른 계산 - 지금 사용할 코어가 E인가?
                completion_time[i] = processes[i][1] + processes[i][2] # 현재 CT = i번째 AT + BT
                time_list[sunseo].append(completion_time[i])
                check[sunseo] = 1
            elif(core[sunseo] == "P"):
                completion_time[i] = processes[i][1] + round(processes[i][2]/2)
                time_list[sunseo].append(completion_time[i])
                check[sunseo] = 1

            if(core[sunseo] == "E"):            #전력량 계산
                AW[sunseo] = Ecore(AW[sunseo],onoff[sunseo])
            elif(core[sunseo] == "P"):
                AW[sunseo] = Pcore(AW[sunseo],onoff[sunseo])


        elif(check[sunseo] == 1):
            if(processes[i][1] < time_list[sunseo][-1]):            #현재 도착 프로세스 시간 < 순서 번째 코어의 전 프로세스 종료시간

                if(core[sunseo] == "E"):            #코어에 따른 계산 - 지금 사용할 코어가 E인가?
                    completion_time[i] = time_list[sunseo][-1] + processes[i][2]    # 현재CT = 해당 코어의 이전 프로세스 CT + 현재 프로세스 BT
                elif(core[sunseo] == "P"):
                    completion_time[i] = time_list[sunseo][-1] + round(processes[i][2]/2)

                if(core[sunseo] == "E"):            #전력량 계산
                    AW[sunseo] = Ecore(AW[sunseo],onoff[sunseo])
                elif(core[sunseo] == "P"):
                    AW[sunseo] = Pcore(AW[sunseo],onoff[sunseo])

            else:            #현재 도착 프로세스 시간 >= 순서 번째 코어의 전 프로세스 종료시간 - 해당 코어가 비어있음
                if(core_number == 1):   #단일 코어라면,
                    if(core[sunseo] == "E"):            #코어에 따른 계산 - 지금 사용할 코어가 E인가?
                        completion_time[i] = turnaround_time[i-1] + processes[i][2]  #현재 CT =  전 프로세스 끝나는 시간 + 현재 프로세스 BT
                    elif(core[sunseo] == "P"):
                        completion_time[i] = turnaround_time[i-1] + round(processes[i][2]/2)
                else:
                    if(core[sunseo] == "E"):            #코어에 따른 계산 - 지금 사용할 코어가 E인가?
                        completion_time[i] = processes[i][1] + processes[i][2] 
                    elif(core[sunseo] == "P"):
                        completion_time[i] = processes[i][1] + round(processes[i][2]/2)


                if(processes[i][1] != time_list[sunseo][-1]): #프로세스 끝나는시간과 시작시간이 같지 않을경우에는 코어 off
                    onoff[sunseo] = 0

                if(core[sunseo] == "E"):            #전력량 계산
                    AW[sunseo] = Ecore(AW[sunseo],onoff[sunseo])
                elif(core[sunseo] == "P"):
                    AW[sunseo] = Pcore(AW[sunseo],onoff[sunseo])
                
            #completion_time[i] = completion_time[i-1] + processes[i][2] # CT = 전CT + BT
        print(completion_time[i])
        if(core[sunseo] == "E"):            #코어에 따른 계산 - 지금 사용할 코어가 E인가?
            waiting_time[i] = completion_time[i] - processes[i][1] - processes[i][2] # i번째 WT =  CT - AT - BT
        elif(core[sunseo] == "P"):
            waiting_time[i] = completion_time[i] - processes[i][1] - round(processes[i][2]/2) # CT - AT - BT

        if(core_number == 1):
            turnaround_time[i] = completion_time[i]
        else:
            if(core[sunseo] == "E"):  
                turnaround_time[i] = waiting_time[i] + processes[i][2]
            elif(core[sunseo] == "P"):
                turnaround_time[i] = waiting_time[i] + round(processes[i][2]/2)

        processes[i]=processes[i]+[waiting_time[i],turnaround_time[i]]

        graph[sunseo].append([processes[i][0],processes[i][2]]) #사용한 코어 위치에 사용한 프로세스 이름과 BT저장
        sunseo += 1
    #for문 끝
    


    processes.sort()
    processes.append(AW)
    processes.append(graph)
    return processes

n = 5
processes = [["p1", 0, 3], ["p2", 1, 7], ["p3", 3, 2], ["p4", 5, 5], ["p5", 6, 3]]
cores = ['P-core', 'P-core', 'E-core', 'E-core']
a =FCFS(n, processes, cores)
print(a)

"""
# 프로세스 정보를 담은 리스트
if __name__ == "__main__":
    processes = []
    # 프로세스의 개수
    n = int(input("프로세스의 개수를 입력하세요: "))
    # 각 프로세스의 정보를 입력받아 리스트에 추가
    for i in range(n):
        print("프로세스 ", i+1)
        arrival_time = int(input("도착 시간을 입력하세요: "))
        burst_time = int(input("실행 시간을 입력하세요: "))
        processes.append((arrival_time, burst_time))

    # FCFS 함수를 호출하고 반환된 값을 저장
    completion_time, waiting_time, turnaround_time, avg_waiting_time, avg_turnaround_time = FCFS()

    print("\nFCFS 스케줄링 결과")
    print("프로세스\t도착 시간\t실행 시간\t완료 시간\t대기 시간\t회전 시간")
    for i in range(n):
        print(f"{i+1}\t\t{processes[i][0]}\t\t{processes[i][1]}\t\t{completion_time[i]}\t\t{waiting_time[i]}\t\t{turnaround_time[i]}")
    print(f"\n평균 대기 시간: {avg_waiting_time}")
    print(f"평균 회전 시간: {avg_turnaround_time}")
"""