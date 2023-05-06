def round_robin(processes, quantum):
    n = len(processes)
    waiting_time = [0] * n
    turnaround_time = [0] * n
    remaining_burst_time = [processes[i][2] for i in range(n)]
    time = 0
    done = [False] * n
    
    while True:
        done_count = 0
        for i in range(n):
            if remaining_burst_time[i] > 0:
                if remaining_burst_time[i] > quantum:
                    time += quantum
                    remaining_burst_time[i] -= quantum
                else:
                    time += remaining_burst_time[i]
                    waiting_time[i] = time - processes[i][1] - processes[i][2]
                    remaining_burst_time[i] = 0
                    turnaround_time[i] = time - processes[i][1]
                    done[i] = True
                    done_count += 1
        
        if done_count == n:
            break
    
    avg_waiting_time = sum(waiting_time) / n
    avg_turnaround_time = sum(turnaround_time) / n
    
    for i in range(n):
        print("Process:", processes[i][0][0], "WT:", waiting_time[i], "TT:", turnaround_time[i])
    print("Average WT:", avg_waiting_time)
    print("Average TT:", avg_turnaround_time)

processes = [["p1", 0, 3], ["p2", 1, 7], ["p3", 3, 2], ["p4", 5, 5], ["p5", 6, 3]]
quantum = 2

round_robin(processes, quantum)