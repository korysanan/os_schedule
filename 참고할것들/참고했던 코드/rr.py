from collections import deque
import math

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

    co1 = []
    co2 = []
    co3 = []
    co4 = []
    u1 = [0]
    u2 = [0]
    u3 = [0]
    ru = 0

    graph = []
    
    while completed < n:
        current_process = ready_queue.popleft()

        ah = 0
        if len(u1) > 0:
            if u1[0] > processes[current_process][1]:
                ah += 1
                if len(u2) > 0:
                    if u2[0] > processes[current_process][1]:
                        ah += 1
                        if len(u3) > 0:
                            if u3[0] > processes[current_process][1]:
                                ah += 1
                            else:
                                u3[0] = processes[current_process][1]
                    else:
                        u2[0] = processes[current_process][1]
            else:
                u1[0] = processes[current_process][1]
        
        if core[ah] == "P":
            ru = math.ceil(remaining_time[current_process])
        elif core[ah] == "E":
            ru = remaining_time[current_process]

        if ru <= quantum:
            re = ru
            current_time += ru
            remaining_time[current_process] = 0
            completed += 1
            completion_time[current_process] = current_time
            turnaround_time[current_process] = completion_time[current_process] - arrival_time[current_process]
            waiting_time[current_process] = turnaround_time[current_process] - burst_time[current_process]
            normalized_turnaround_time[current_process] = turnaround_time[current_process] / burst_time[current_process]
            if ah == 0:
                co1.append([processes[current_process][0], processes[current_process][1], processes[current_process][2]])
                u1[0] += quantum
            elif ah == 1:
                co2.append([processes[current_process][0], processes[current_process][1], processes[current_process][2]])
                u2[0] += quantum
            elif ah == 2:
                co3.append([processes[current_process][0], processes[current_process][1], processes[current_process][2]])
                u3[0] += quantum
            else :
                co4.append([processes[current_process][0], processes[current_process][1], processes[current_process][2]])

        else:
            current_time += quantum
            ru -= quantum
            if remaining_time[current_process] % 2 == 0:
                remaining_time[current_process] = 2 * ru
            else:
                remaining_time[current_process] = 2 * ru - 1
        
            if ah == 0:
                co1.append([processes[current_process][0], processes[current_process][1], processes[current_process][2]])
                u1[0] += ru
            elif ah == 1:
                co2.append([processes[current_process][0], processes[current_process][1], processes[current_process][2]])
                u2[0] += ru
            elif ah == 2:
                co3.append([processes[current_process][0], processes[current_process][1], processes[current_process][2]])
                u3[0] += ru
            else :
                co4.append([processes[current_process][0], processes[current_process][1], processes[current_process][2]])
            
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
    results.append(graph)
    return results

n = 5
q = 2
processes = [["p1", 0, 3], ["p2", 1, 7], ["p3", 3, 2], ["p4", 5, 5], ["p5", 6, 3]]
cores = ["P", "E", "P", "E"]
a = RR(n, processes, q, cores)
print(a)

