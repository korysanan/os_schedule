from collections import deque
import math

def RR(n, processes, quantum, core):
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
    
    ready_queue = deque()
    current_time = 0
    completed = 0
    index = 0
    
    ready_queue.append(index)
    index += 1

    graph = []
    
    while completed < n:
        current_process = ready_queue.popleft()
        if remaining_time[current_process] <= quantum:  
            #현재 프로세스의 남은 시간 <= quantum일 경우,
            re = remaining_time[current_process] 
            # re에 현재 프로세스의 남은 시간을 저장
            current_time += remaining_time[current_process] 
            # 현재시간에 현재 프로세스의 남은 시간을 더함
            remaining_time[current_process] = 0 
            # 현재 프로세스의 남은 시간을 0으로 함
            completed += 1
            #완료된 프로세스의 갯수를 1증가
            completion_time[current_process] = current_time
            # 현재 프로세스의 완료시간을 현재시간으로
            turnaround_time[current_process] = completion_time[current_process] - arrival_time[current_process]  
            normalized_turnaround_time[current_process] = turnaround_time[current_process] / burst_time[current_process] 
            # 현재 프로세스의 TT, NTT를 계산
            for u in range(re):
                graph.append(processes[current_process][0])
            # 해당 프로세스 이름 graph 추가

        else:
            #현재 프로세스의 남은 시간 > quantum일 경우,
            current_time += quantum
            #현재 시간에 quantum을 더함
            remaining_time[current_process] -= quantum
            #현재 프로세스의 남은 시간에 quantum을 뺀다
            for u in range(quantum):
                graph.append(processes[current_process][0])
            # 해당 프로세스 이름 graph 추가
            
        while index < n and arrival_time[index] <= current_time:
            #index < n 이고 인덱스 값의 도착 시간이 현재 시간보다 작을 때
            ready_queue.append(index)
            #ready_queue에 index 값 삽입
            index += 1
            # index 1 증가

        if remaining_time[current_process] > 0:
            ready_queue.append(current_process)
            # 현재 프로세스의 남은 시간이 0보다 크면 ready_queue에 현재 프로세스를 삽입
        for i in range(n):
            waiting_time[i] = turnaround_time[i] - burst_time[i]
    results = []
    for i in range(n):
        results.append((processes[i][0], arrival_time[i], processes[i][2], waiting_time[i], turnaround_time[i], normalized_turnaround_time[i]))
    results.append(graph)
    return results
