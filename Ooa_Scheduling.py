import math

def OOA(n, processes, quantum, core):
    arrival_time = [p[1] for p in processes]
    burst_time = [p[2] for p in processes]
    if core == "P":
        new_burst_time = []
        for num in burst_time:
            new_burst_time.append(math.ceil(num/2))

        burst_time = new_burst_time

    remaining_time = burst_time.copy()
    waiting_time = [0] * n
    turnaround_time = [0] * n
    normalized_turnaround_time = [0] * n
    completion_time = [0] * n
    
    ready_queue = []
    current_time = 0
    completed = 0
    
    result = []
    graph = []
    
    while completed < n:
        for i in range(n):
            if arrival_time[i] <= current_time and i not in ready_queue and remaining_time[i] > 0:
                ready_queue.append(i)
        # 프로세스 수만큼 반복을 하고, i번째 프로세스가 현재 시간보다 작거나 같고, 
        # ready_queue에 없고, i번째 프로세스의 남은 실행 시간이 0보다 크면 ready_queue에 i를 추가
                
        if not ready_queue:
            current_time += 1
            continue
        # ready_queue에 값이 없으면 현재시간을 1 증가시킴
        
        max_priority = -1
        highest_response_ratio_index = 0
        # max_priority와 highest_response_ratio_index를 -1과 0으로 초기화
        for i in range(len(ready_queue)):
            if remaining_time[ready_queue[i]] == 0:
                max_priority = 99999999
                highest_response_ratio_index = i
                continue
            # 만약 i번째 프로세스의 남은 실행 시간이 0이라면, 
            # 해당 프로세스는 이미 실행이 완료된 프로세스이므로 건너뜀
                
            response_ratio = (current_time - arrival_time[ready_queue[i]] + remaining_time[ready_queue[i]]) / remaining_time[ready_queue[i]]
            if response_ratio > max_priority:
                max_priority = response_ratio
                highest_response_ratio_index = i
            # 현재까지 가장 높은 응답률을 가진 프로세스의 응답률을 비교하여, 
            # 새로운 높은 우선순위가 나타나면 이를 max_priority에 저장하고, 
            # 해당 프로세스의 인덱스를 highest_response_ratio_index에 저장
        
        current_process = ready_queue[highest_response_ratio_index]
        # 현재 프로세스를 ready_queue[highest_response_ratio_index]로 지정

        if remaining_time[current_process] <= quantum:
            #현재 실행중인 프로세스의 남은 시간이 quantum보다 작거나 같을때
            re = remaining_time[current_process]
            # re 변수에 현재 실행 중인 프로세스의 남은 실행 시간을 저장합니다.
            current_time += remaining_time[current_process]
            # 현재 실행 중인 프로세스의 남은 실행 시간만큼 증가
            completion_time[current_process] = current_time
            remaining_time[current_process] = 0
            # 남은 실행시간을 0으로
            completed += 1
            # 완료된 프로세스 갯수 1 증가
            waiting_time[current_process] = completion_time[current_process] - burst_time[current_process] - arrival_time[current_process]
            turnaround_time[current_process] = completion_time[current_process] - arrival_time[current_process]
            normalized_turnaround_time[current_process] = turnaround_time[current_process] / burst_time[current_process]
            #현재 실행중인 프로세스의 waiting_time, turnaroun_time, normalized_turnaround_time
            for u in range(re):
                graph.append(processes[current_process][0])
            # 해당 프로세스 이름 graph에 추가
            
        else:
            #현재 실행중인 프로세스의 남은 시간이 quantum보다 클때
            current_time += quantum
            #실행시간에 quantum 더하고
            remaining_time[current_process] -= quantum
            #현재 프로세스의 남은 시간에 quantum을 뺌
            for u in range(quantum):
                graph.append(processes[current_process][0])
            # 해당 프로세스 이름 graph 추가
        
        ready_queue.remove(current_process)
        # ready_queue 안에 있는 current-process 삭제
    for i in range(n):
        result.append([processes[i][0], processes[i][1], processes[i][2], waiting_time[i], turnaround_time[i], normalized_turnaround_time[i]])
    result.append(graph)
    return result
