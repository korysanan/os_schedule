from collections import deque
import math
<<<<<<< HEAD
=======
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
>>>>>>> 8cd2560df15e1dbfde4e5e4d5d6de327eaf59ac5

def RR(n, processes, quantum, core):
    arrival_time = [p[1] for p in processes]
    burst_time = [p[2] for p in processes]
    if core == "P":
<<<<<<< HEAD
        new_burst_time = []
        for num in burst_time:
            new_burst_time.append(math.ceil(num/2))

        burst_time = new_burst_time
=======
         new_burst_time = []
         for num in burst_time:
             new_burst_time.append(math.ceil(num/2))

         burst_time = new_burst_time
>>>>>>> 8cd2560df15e1dbfde4e5e4d5d6de327eaf59ac5

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

    AW=0
    onoff=0
    
    while completed < n:

        if(completed==0):
            if(core == "E"):            #전력량 계산
                AW = Ecore(AW,onoff)
            elif(core == "P"):
                AW = Pcore(AW,onoff)

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
        
        for i in range(n):
            waiting_time[i] = turnaround_time[i] - burst_time[i]

        if(completion_time != processes[completed][1]): #연속적으로 사용되지 않으면 off - 완료시간 != 입력된 시간
           onoff = 0
        if(core == "E"):            #전력량 계산
            AW = Ecore(AW,onoff)
        elif(core == "P"):
            AW = Pcore(AW,onoff)
    results = []
    AW = round(AW,2)
    for i in range(n):
        results.append((processes[i][0], arrival_time[i], processes[i][2], waiting_time[i], turnaround_time[i], normalized_turnaround_time[i]))
<<<<<<< HEAD
    results.append(graph)
    return results
=======
    processes.append(AW)
    results.append(graph)
    return results

n = 5
q = 3
processes = [["p1", 0, 3], ["p2", 1, 7], ["p3", 3, 2], ["p4", 5, 5], ["p5", 6, 3]]
cores = ["P", "E", "P", "E"]
a = RR(n, processes, q, cores[0])
print(a)
>>>>>>> 8cd2560df15e1dbfde4e5e4d5d6de327eaf59ac5
