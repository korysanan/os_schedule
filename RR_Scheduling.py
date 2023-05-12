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
        if remaining_time[current_process] <= quantum:  #현재 프로세스의 남은 시간 <= quantum일 경우,
            re = remaining_time[current_process] #색칠을 위한 저장
            current_time += remaining_time[current_process] 
            remaining_time[current_process] = 0 
            completed += 1  
            completion_time[current_process] = current_time # 현재 CT = 현재 시간
            turnaround_time[current_process] = completion_time[current_process] - arrival_time[current_process]  # 현재 TT = CT - AT
            normalized_turnaround_time[current_process] = turnaround_time[current_process] / burst_time[current_process] # 현재 NT = TT/BT
            for u in range(re): # 현재 프로세스의 남은시간 만큼 색칠
                graph.append(processes[current_process][0])

        else:
            current_time += quantum
            remaining_time[current_process] -= quantum
            for u in range(quantum):
                graph.append(processes[current_process][0])
            
        while index < n and arrival_time[index] <= current_time:
            ready_queue.append(index)
            index += 1
        
        if remaining_time[current_process] > 0:
            ready_queue.append(current_process)
        
        for i in range(n):
            waiting_time[i] = turnaround_time[i] - burst_time[i]
    results = []
    for i in range(n):
        results.append((processes[i][0], arrival_time[i], processes[i][2], waiting_time[i], turnaround_time[i], normalized_turnaround_time[i]))
    results.append(graph)
    return results
