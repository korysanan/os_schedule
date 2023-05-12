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
    AW=0
    onoff=0
    
    ready_queue.append(index)
    index += 1

    graph = []

    if(core[sunseo] == "P"):
        for i in range(n):
            processes[i][2] = round(processes[i][2])

    while completed < n:

        if(completed==0):
            if(core[sunseo] == "E"):            #전력량 계산
                AW[sunseo] = Ecore(AW[sunseo],onoff[sunseo])
            elif(core[sunseo] == "P"):
                AW[sunseo] = Pcore(AW[sunseo],onoff[sunseo])


        current_process = ready_queue.popleft()
        if remaining_time[current_process] <= quantum:
            re = remaining_time[current_process]
            current_time += remaining_time[current_process]
            remaining_time[current_process] = 0
            completed += 1
            completion_time[current_process] = current_time
            turnaround_time[current_process] = completion_time[current_process] - arrival_time[current_process]
            normalized_turnaround_time[current_process] = turnaround_time[current_process] / burst_time[current_process]
            for u in range(re):
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

        if(completion_time != processes[completed][1]): #연속적으로 사용되지 않으면 off - 완료시간 != 입력된 시간
            onoff = 0
        if(core[sunseo] == "E"):            #전력량 계산
            AW[sunseo] = Ecore(AW[sunseo],onoff[sunseo])
        elif(core[sunseo] == "P"):
            AW[sunseo] = Pcore(AW[sunseo],onoff[sunseo])


        for i in range(n):
            waiting_time[i] = turnaround_time[i] - burst_time[i]
    results = []
    for i in range(n):
        results.append((processes[i][0], arrival_time[i], burst_time[i], waiting_time[i], turnaround_time[i], normalized_turnaround_time[i]))
    results.append(AW)
    results.append(graph)
    return results

n = 5
q = 3
processes = [["p1", 0, 3], ["p2", 1, 7], ["p3", 3, 2], ["p4", 5, 5], ["p5", 6, 3]]
cores = ['P-core', 'P-core', 'E-core', 'E-core']
a = RR(n, processes, q, cores)
print(a)

