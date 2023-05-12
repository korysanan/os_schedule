import math
def Ecore(AW, onoff):
    if onoff == 0: 
        AW += 0.1
        onoff = 1
    AW += 1
    return AW

def Pcore(AW, onoff):
    if onoff == 0:
       AW += 0.5
       onoff = 1 
    AW += 3
    return AW

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

    AW=0
    onoff=0
    
    while completed < n:

        if(completed==0):
            if(core == "E"):            #전력량 계산
                AW = Ecore(AW,onoff)
            elif(core == "P"):
                AW = Pcore(AW,onoff)

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

        if(completion_time != processes[completed][1]): #연속적으로 사용되지 않으면 off - 완료시간 != 입력된 시간
           onoff = 0
        if(core == "E"):            #전력량 계산
            AW = Ecore(AW,onoff)
        elif(core == "P"):
            AW = Pcore(AW,onoff)

        current_process = ready_queue[highest_response_ratio_index]
        
        if remaining_time[current_process] <= quantum:
            re = remaining_time[current_process]
            current_time += remaining_time[current_process]
            completion_time[current_process] = current_time
            remaining_time[current_process] = 0
            completed += 1
            waiting_time[current_process] = completion_time[current_process] - burst_time[current_process] - arrival_time[current_process]
            turnaround_time[current_process] = completion_time[current_process] - arrival_time[current_process]
            normalized_turnaround_time[current_process] = turnaround_time[current_process] / burst_time[current_process]
            for u in range(re):
                graph.append(processes[current_process][0])
            
        else:
            current_time += quantum
            remaining_time[current_process] -= quantum
            for u in range(quantum):
                graph.append(processes[current_process][0])
        
        # Remove completed process from the ready queue
        ready_queue.remove(current_process)
    # Create result list
    for i in range(n):
        result.append([processes[i][0], processes[i][1], processes[i][2], waiting_time[i], turnaround_time[i], normalized_turnaround_time[i]])
    AW = round(AW,2)
    processes.append(AW)    
    result.append(graph)
    return result

n = 5
q = 3
processes = [["p1", 0, 3], ["p2", 1, 7], ["p3", 3, 2], ["p4", 5, 5], ["p5", 6, 3]]
cores = ["P", "E", "P", "E"]
a = OOA(n, processes, q, cores[0])
print(a)