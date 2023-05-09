from collections import deque

def RR(n, processes, quantum, core):
    arrival_time = [p[1] for p in processes]
    burst_time = [p[2] for p in processes]
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
    
    while completed < n:
        current_process = ready_queue.popleft()
        
        if remaining_time[current_process] <= quantum:
            current_time += remaining_time[current_process]
            remaining_time[current_process] = 0
            completed += 1
            completion_time[current_process] = current_time
            turnaround_time[current_process] = completion_time[current_process] - arrival_time[current_process]
            normalized_turnaround_time[current_process] = turnaround_time[current_process] / burst_time[current_process]
            
        else:
            current_time += quantum
            remaining_time[current_process] -= quantum
            
        while index < n and arrival_time[index] <= current_time:
            ready_queue.append(index)
            index += 1
        
        if remaining_time[current_process] > 0:
            ready_queue.append(current_process)
        
        for i in range(n):
            waiting_time[i] = turnaround_time[i] - burst_time[i]
    
    results = []
    for i in range(n):
        results.append((processes[i][0], arrival_time[i], burst_time[i], waiting_time[i], turnaround_time[i], normalized_turnaround_time[i]))
    return results