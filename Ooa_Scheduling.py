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
    graph = []
    
    AW=0
    onoff=0
    if(core[sunseo] == "P"):
        for i in range(n):
            processes[i][2] = round(processes[i][2])

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

            if(i==0):
                if(core[sunseo] == "E"):            #전력량 계산
                    AW[sunseo] = Ecore(AW[sunseo],onoff[sunseo])
                elif(core[sunseo] == "P"):
                    AW[sunseo] = Pcore(AW[sunseo],onoff[sunseo])


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
            re = remaining_time[current_process]
            current_time += remaining_time[current_process]
            completion_time[current_process] = current_time
            remaining_time[current_process] = 0
            completed += 1

            if(completion_time != processes[i][1]): #연속적으로 사용되지 않으면 off - 완료시간 != 입력된 시간
                onoff = 0
            if(core[sunseo] == "E"):            #전력량 계산
                AW[sunseo] = Ecore(AW[sunseo],onoff[sunseo])
            elif(core[sunseo] == "P"):
                AW[sunseo] = Pcore(AW[sunseo],onoff[sunseo])

            waiting_time[current_process] = completion_time[current_process] - burst_time[current_process] - arrival_time[current_process]
            turnaround_time[current_process] = completion_time[current_process] - arrival_time[current_process]
            normalized_turnaround_time[current_process] = turnaround_time[current_process] / burst_time[current_process]
            for u in range(re):
                graph.append(processes[current_process][0])
            
        else:   #이부분도 전력량 더해야함?

            current_time += quantum
            remaining_time[current_process] -= quantum
            for u in range(quantum):
                graph.append(processes[current_process][0])
        
        # Remove completed process from the ready queue
        ready_queue.remove(current_process)
    # Create result list
    for i in range(n):
        result.append([processes[i][0], processes[i][1], processes[i][2], waiting_time[i], turnaround_time[i], normalized_turnaround_time[i]])
    resule.append(AW)
    result.append(graph)
    return result