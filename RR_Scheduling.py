def RR(n, processes, quantum):
    completion_time = [0]*n
    waiting_time = [0]*n
    turnaround_time = [0]*n
    remaining_time = [burst_time for arrival_time, burst_time in processes]

    # 현재 시간
    current_time = 0
    # 대기 큐
    queue = []

    while True:
        # 대기 큐에 들어갈 프로세스 선택
        for i, (arrival_time, burst_time) in enumerate(processes):
            if arrival_time <= current_time and remaining_time[i] > 0:
                queue.append(i)

        if not queue:
            # 대기 큐가 비어있다면 모든 프로세스가 실행 완료된 것
            break

        # 대기 큐에서 프로세스 실행
        i = queue.pop(0)
        # 남은 실행 시간이 시간 할당량보다 작은 경우
        if remaining_time[i] <= quantum:
            current_time += remaining_time[i]
            completion_time[i] = current_time
            remaining_time[i] = 0
        # 남은 실행 시간이 시간 할당량보다 큰 경우
        else:
            current_time += quantum
            remaining_time[i] -= quantum
            queue.append(i)

    # 대기 시간과 회전 시간 계산
    for i in range(n):
        turnaround_time[i] = completion_time[i] - processes[i][0]
        waiting_time[i] = turnaround_time[i] - processes[i][1]

    # 평균 대기 시간과 평균 회전 시간 계산
    avg_waiting_time = sum(waiting_time)/n
    avg_turnaround_time = sum(turnaround_time)/n
    
    return processes