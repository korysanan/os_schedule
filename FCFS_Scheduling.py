import math

def FCFS(n, processes, core) :
    processes.sort(key = lambda x:x[1])
    # 실행 순서와 각 프로세스의 실행 완료 시간, 대기 시간을 계산
    completion_time = [0]*n
    waiting_time = [0]*n
    turnaround_time = [0]*n
    graph = []
    burst_time = [p[2] for p in processes]
    if core == "P":
        new_burst_time = []
        for num in burst_time:
            new_burst_time.append(math.ceil(num/2))

        burst_time = new_burst_time

    for i in range(n):
        # 실행 순서
        if i == 0:
            completion_time[i] = processes[i][1] + burst_time[i] # 처음 들어온 프로세스의 CT = AT + BT
        else:
            completion_time[i] = completion_time[i-1] + burst_time[i] # 그 외의 프로세스 CT = 전 프로세스CT + 현 프로세스BT

        waiting_time[i] = completion_time[i] - processes[i][1] - burst_time[i]  # i번째 WT = i번째 CT - i번째 AT - i번째 BT

        turnaround_time[i] = completion_time[i] - processes[i][1]   # i번째 TT = CT - AT
        processes[i]=processes[i]+[waiting_time[i],turnaround_time[i]]  # 각 i번째 프로세스 이름과 WT, TT를 i번째 processes에 append
        for a in range(turnaround_time[i] - waiting_time[i]):
            graph.append(processes[i][0])
    processes.sort(key=lambda x: x[0])
    processes.append(graph)
    return processes