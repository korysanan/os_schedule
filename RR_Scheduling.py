def RR(n, processes, quantum):
    remaining_burst_time = [p[2] for p in processes]
    completion_time = [0]*n
    waiting_time = [0]*n
    turnaround_time = [0]*n
    current_time = 0
    queue = []

    while True:
        done = True
        for i in range(n):
            if processes[i][1] <= current_time and remaining_burst_time[i] > 0:
                done = False
                if remaining_burst_time[i] > quantum:
                    current_time += quantum
                    remaining_burst_time[i] -= quantum
                    queue.append(i)
                else:
                    if remaining_burst_time[i] <= quantum: # 추가된 if문
                        current_time += remaining_burst_time[i]
                        completion_time[i] = current_time
                        waiting_time[i] = completion_time[i] - processes[i][1] - processes[i][2]
                        turnaround_time[i] = completion_time[i] - processes[i][1]
                        remaining_burst_time[i] = 0
                        processes[i] = processes[i] + [waiting_time[i], turnaround_time[i]]
                        while len(queue) > 0 and remaining_burst_time[queue[0]] == 0:
                            j = queue.pop(0)
                            completion_time[j] = current_time
                            waiting_time[j] = completion_time[j] - processes[j][1] - processes[j][2]
                            turnaround_time[j] = completion_time[j] - processes[j][1]
                            processes[j] = processes[j] + [waiting_time[j], turnaround_time[j]]
                    else:
                        current_time += quantum # p[i][2] > quantum 인 경우
                        remaining_burst_time[i] -= quantum
                        queue.append(i)
                    
        if done == True:
            break

    return processes
