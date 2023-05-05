def RR(n, processes, quantum):
    remaining_burst_time = [p[2] for p in processes]
    completion_time = [0]*n
    waiting_time = [0]*n
    turnaround_time = [0]*n
    current_time = 0

    while True:
        done = True
        for i in range(n):
            if remaining_burst_time[i] > 0:
                done = False

                if remaining_burst_time[i] > quantum:
                    current_time += quantum
                    remaining_burst_time[i] -= quantum
                else:
                    current_time += remaining_burst_time[i]
                    completion_time[i] = current_time
                    waiting_time[i] = completion_time[i] - processes[i][1] - processes[i][2]
                    turnaround_time[i] = completion_time[i] - processes[i][1]
                    remaining_burst_time[i] = 0
                    processes[i] = processes[i] + [waiting_time[i], turnaround_time[i]]
        
        if done == True:
            break

    return processes