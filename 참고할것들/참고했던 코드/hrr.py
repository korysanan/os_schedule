import math
# P_core 계산을 위해 math 모듈을 import한다.

def HRRN(n, processes, core):
    # HRRN의 인자 n = 프로세스 수, processes = 프로세스의 정보, core = P, E 코어 정보
    completion_time = 0
    waiting_time = [0]*n
    turnaround_time = [0]*n
    result = []
    # completion_time은 모든 프로세스가 실행되고 종료되는 시간을 저장하는 변수이며, 초기값으로 0을 할당
    # waiting_time은 각 프로세스의 대기 시간을 저장하는 리스트이며, n만큼의 길이를 가진 리스트를 생성하고, 각 원소를 0으로 초기화
    # turnaround_time은 각 프로세스의 turnaround 시간을 저장하는 리스트이며, n만큼의 길이를 가진 리스트를 생성하고, 각 원소를 0으로 초기화
    co1 = []
    co2 = []
    co3 = []
    co4 = []
    # 첫번째 core ~ 네번째 core에 들어갈 프로세스를 저장할 리스트
    u = [[0], [0], [0]]
    # 몇번째 코어를 써야할 지 비교할 때 사용할 리스트
    re = 0
    re2 = 0
    # P, E코어일 때 burst_time을 맞추기 위한 변수
    graph =[[], [], [], []]
    # 메인에서 그래프로 나타내기 위해 들어오는 순서를 넣는 리스트
    while len(processes) > 0:
    # processes에 들어있는 게 없을때까지
        process = processes.pop(0)
        # processes 리스트에서 첫 번째 프로세스를 뽑아와서 process 변수에 할당
        core_select_num = 0
        # 코어 번호 선택
        if len(u[0]) > 0:
        # u[0]이 0 보다 클때 실행, u[0]이 0이면 아직 아무것도 실행이 안되었다는 것 
            if u[0][0] > process[1]:
                core_select_num += 1
        # u[0][0] > process[1]이면 현재 core0을 사용중이라는 뜻이기에 다음 core를 사용
                if len(u[1]) > 0:
        #u[1]이 0 보다 클때 실행, u[1]이 0이면 core1부터 사용하지 않고 있다는 걸 이야기
                    if u[1][0] > process[1]:
                        core_select_num += 1
        # u[1][0] > process[1]이면 현재 core1을 사용중이라는 뜻이기에 다음 core를 사용
                        if len(u[2]) > 0:
        #u[2]이 0 보다 클때 실행, u[2]이 0이면 core2부터 사용하지 않고 있다는 걸 이야기
                            if u[2][0] > process[1]:
                                core_select_num += 1
        # u[2][0] > process[1]이면 현재 core2를 사용중이라는 뜻이기에 다음 core를 사용
                            else:
                                u[2][0] = process[1]
                    else:
                        u[1][0] = process[1]
            else:
                u[0][0] = process[1]
        # 각각 상황에서 process[1]이 크거나 같으면 해당 core를 실행
        if core[core_select_num] == "P":
            re = math.ceil(process[2] / 2)
        elif core[core_select_num] == "E":
            re = process[2]
        # 각 core가 P_core인지, E_core인지 확인
        # P_core이면 re를 해당 프로세스의 실행시간에다가 2를 나눈 값을 저장, 단 소수점일 시 올림 처리

        if core_select_num == 0:
            co1.append([process[0], process[1], process[2]])
            u[0][0] += re
        elif core_select_num == 1:
            co2.append([process[0], process[1], process[2]])
            u[1][0] += re
        elif core_select_num == 2:
            co3.append([process[0], process[1], process[2]])
            u[2][0] += re
        else :
            co4.append([process[0], process[1], process[2]])
        # 각 core일 때 그 코어에 맞는 리스트에 해당 프로세스 이름, 도착시간, 실행시간을 넣는다.
    
    for num in range(4):
        if num == 0:
            H_process = co1
        elif num == 1:
            H_process = co2
        elif num == 2:
            H_process = co3
        else :
            H_process = co4
        # 각 core별로 저장한 리스트끼리 HRRN기법으로 계산
        while len(H_process) > 0:
        # H_process에 들어있는 게 없을때까지
            max_priority = -1
            highest_response_ratio_index = 0
        # max_priority와 highest_response_ratio_index를 -1과 0으로 초기화
            for i in range(len(H_process)):
                response_ratio = (completion_time - H_process[i][1] + H_process[i][2]) / H_process[i][2]
                if response_ratio > max_priority:
                    max_priority = response_ratio
                    highest_response_ratio_index = i
            H_process_all = H_process.pop(highest_response_ratio_index)
            # 실행 시간이 가장 높은 프로세스를 선택하고 해당 프로세스를 H_process_all 변수에 할당
            if core[num] == "P":
                re2 = math.ceil(H_process_all[2] / 2)
            elif core[num] == "E":
                re2 = H_process_all[2]
            # 각 core가 P_core인지, E_core인지 확인
            # P_core이면 re2를 해당 프로세스의 실행시간에다가 2를 나눈 값을 저장, 단 소수점일 시 올림 처리
            # E_core이면 re2를 해당 프로세스의 실행시간을 저장
            waiting_time[highest_response_ratio_index] = completion_time - H_process_all[1]
            if waiting_time[highest_response_ratio_index] < 0:
                waiting_time[highest_response_ratio_index] = 0
            turnaround_time[highest_response_ratio_index] = waiting_time[highest_response_ratio_index] + re2
            # 대기 시간, 실행시간 계산
            # 대기 시간이 0보다 작으면 0으로 저장
            completion_time += re2
            # 완료시간에 re2값을 더함
            
            result.append([H_process_all[0], H_process_all[1], H_process_all[2], waiting_time[highest_response_ratio_index], turnaround_time[highest_response_ratio_index]])
            # 결과 리스트에 해당 process_name, arrival_time, burst_time, waiting_time, turnaround_time을 넣는다.
            for auu in range(turnaround_time[highest_response_ratio_index] - waiting_time[highest_response_ratio_index]):
                graph[num].append(H_process_all[0])
            #해당 core graph에 프로세스의 이름을 turnaround_time - waiting_time 값 만큼 저장
    result.sort(key=lambda x: x[0])
    # 결과를 이름순으로 정렬
    for i in range(4):
        result.append(graph[i])
    # 각 core들의 graph를 result에 추가
    return result