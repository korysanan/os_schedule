from collections import deque

def RR(n, processes, quantum, core):
    processes.sort(key = lambda x:x[1])
    processes_name = [p[0] for p in processes]
    arrival_time = [p[1] for p in processes] 
    burst_time = [p[2] for p in processes]
    remaining_time = burst_time.copy()
    waiting_time = [0] * n
    turnaround_time = [0] * n
    completion_time = [0] * n
    normalized_turnaround_time = [0] * n
    
    ready_queue = deque()
    current_time = 0
    completed = 0
    index = 0
    ready_queue.append(index)
    index += 1
    process_insert_list = []
    core_list_2 = []
    num1 = []
    num2 = []
    num3 = []
    num4 = []
    core_list_2.append(num1)
    core_list_2.append(num2)
    core_list_2.append(num3)
    core_list_2.append(num4)

    while completed < n:
        current_process = ready_queue.popleft()
        print(current_process, ready_queue)
        x = 0
        for x in range(len(core_list_2)):
            if core_list_2[x][current_time] == "":
                ah = x
                au = x + 1
                if au < len(core_list_2):
                    for au in range(len(core_list_2)):
                        core_list_2[au][current_time] = None
                break
            else :
                continue


        if core[ah] == "E":
            continue
        elif core[ah] == "P":
            remaining_time[current_process] = remaining_time[current_process] / 2
        else :
            continue
       
        if remaining_time[current_process] <= quantum:
            current_time += remaining_time[current_process]
            count = 0
            remaintime = remaining_time[current_process]
            remaining_time[current_process] = 0
            completed += 1
            completion_time[current_process] = current_time
            turnaround_time[current_process] = completion_time[current_process] - arrival_time[current_process]
            waiting_time[current_process] = turnaround_time[current_process] - burst_time[current_process]
            normalized_turnaround_time[current_process] = turnaround_time[current_process] / burst_time[current_process]
            for count in range(remaintime):
                core_list_2[ah].append(processes_name[current_process])
                count += 1
        else:
            count = 0
            current_time += quantum
            remaining_time[current_process] -= quantum
            for count in range(quantum):
                core_list_2[ah].append(processes_name[current_process])

            
        while index < n and arrival_time[index] <= current_time:
            ready_queue.append(index)
            index += 1
        
        if remaining_time[current_process] > 0:
            ready_queue.append(current_process)
    results = []
    for i in range(n):
        results.append((processes[i][0], arrival_time[i], burst_time[i], waiting_time[i], turnaround_time[i], normalized_turnaround_time[i]))
    results.sort()
    results.append(process_insert_list)
    return results

core_list = ["E", "P", "P", "E"]
process = [["p1", 0, 3], ["p2", 1, 7], ["p3", 3, 2], ["p4", 5, 5], ["p5", 6, 3]]
n = 5
q = 2
h = RR(n, process, q, core_list)
print(len(h[len(h) - 1]))
