def SPN(n, processes):
    # 실행 순서와 각 프로세스의 실행 완료 시간, 대기 시간을 계산
    completion_time = 0
    waiting_time = [0]*n
    turnaround_time = [0]*n
    CURRENTLY = 0
    result = []
    name = []
    for a in range(n):
        pl = processes[0][2]
        for r in range(n):
            if(completion_time>=processes[r][1]):
                if(pl>=processes[r][2]):
                    pl = processes[r][2]
                    CURRENTLY = r
        completion_time = completion_time + processes[CURRENTLY][2]
        turnaround_time = completion_time - processes[CURRENTLY][1]
        waiting_time =  turnaround_time-processes[CURRENTLY][2]
        result.append([processes[CURRENTLY][0],processes[CURRENTLY][1],processes[CURRENTLY][2],waiting_time,turnaround_time])
        del processes[CURRENTLY]
        n=n-1
    
    result.sort(key=lambda x: x[0])

    return result