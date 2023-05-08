from collections import deque

def round_robin(processes, quantum):
    n = len(processes)
    arrival_time = [p[1] for p in processes]
    burst_time = [p[2] for p in processes]
    remaining_time = burst_time.copy()
    waiting_time = [0] * n
    turnaround_time = [0] * n
    normalized_turnaround_time = [0] * n
    completion_time = [0] * n
    
    ready_queue = deque()
    current_time = 0
    time_slice = quantum
    completed = 0
    index = 0
    
    # Add the first process to the ready queue
    ready_queue.append(index)
    index += 1
    
    while completed < n:
        # Get the next process from the ready queue
        current_process = ready_queue.popleft()
        
        # Check if the process has completed
        if remaining_time[current_process] <= time_slice:
            current_time += remaining_time[current_process]
            remaining_time[current_process] = 0
            completed += 1
            completion_time[current_process] = current_time
            turnaround_time[current_process] = completion_time[current_process] - arrival_time[current_process]
            normalized_turnaround_time[current_process] = turnaround_time[current_process] / burst_time[current_process]
            
        # If the process has not completed
        else:
            current_time += time_slice
            remaining_time[current_process] -= time_slice
            
        # Add any newly arrived processes to the ready queue
        while index < n and arrival_time[index] <= current_time:
            ready_queue.append(index)
            index += 1
        
        # Add the current process back to the ready queue if it has not completed
        if remaining_time[current_process] > 0:
            ready_queue.append(current_process)
        
        # Calculate waiting time for each process
        for i in range(n):
            waiting_time[i] = turnaround_time[i] - burst_time[i]
    
    # Return the results
    results = []
    for i in range(n):
        results.append((processes[i][0], arrival_time[i], burst_time[i], waiting_time[i], turnaround_time[i], normalized_turnaround_time[i]))
    return results

processes = [("P1", 0, 3), ("P2", 1, 7), ("P3", 3, 2), ("P4", 5, 5), ("P5", 6, 3)]
quantum = 3
results = round_robin(processes, quantum)
for process in results:
    print(process)
