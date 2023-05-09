def OOA(n, processes, quantum, core):
    arrival_time = [p[1] for p in processes]
    burst_time = [p[2] for p in processes]
    remaining_time = burst_time.copy()
    waiting_time = [0] * n
    turnaround_time = [0] * n
    normalized_turnaround_time = [0] * n
    completion_time = [0] * n
    
    ready_queue = []
    current_time = 0
    completed = 0
    
    result = []
    
    while completed < n:
        # Add new processes to the ready queue
        for i in range(n):
            if arrival_time[i] <= current_time and i not in ready_queue and remaining_time[i] > 0:
                ready_queue.append(i)
                
        if not ready_queue:
            # If the ready queue is empty, move to the next process
            current_time += 1
            continue
        
        # Compute response ratio and find the process with the highest priority
        max_priority = -1
        highest_response_ratio_index = 0
        for i in range(len(ready_queue)):
            if remaining_time[ready_queue[i]] == 0:
                # Skip computation if remaining time is zero
                max_priority = 99999999
                highest_response_ratio_index = i
                continue
                
            response_ratio = (current_time - arrival_time[ready_queue[i]] + remaining_time[ready_queue[i]]) / remaining_time[ready_queue[i]]
            if response_ratio > max_priority:
                max_priority = response_ratio
                highest_response_ratio_index = i
        
        current_process = ready_queue[highest_response_ratio_index]
        
        if remaining_time[current_process] <= quantum:
            current_time += remaining_time[current_process]
            completion_time[current_process] = current_time
            remaining_time[current_process] = 0
            completed += 1
            waiting_time[current_process] = completion_time[current_process] - burst_time[current_process] - arrival_time[current_process]
            turnaround_time[current_process] = completion_time[current_process] - arrival_time[current_process]
            normalized_turnaround_time[current_process] = turnaround_time[current_process] / burst_time[current_process]
            
        else:
            current_time += quantum
            remaining_time[current_process] -= quantum
        
        # Remove completed process from the ready queue
        ready_queue.remove(current_process)
        
    # Create result list
    for i in range(n):
        result.append([processes[i][0], processes[i][1], processes[i][2], waiting_time[i], turnaround_time[i], normalized_turnaround_time[i]])
    
    return result
