def SRTN(n,processes):
    # 현재까지 실행된 시간
    current_time = 0
    # 실행 완료된 프로세스의 수
    completed_processes = 0
    # 대기 중인 프로세스
    waiting_processes = []
    # 실행 중인 프로세스
    running_process = None
    # 실행 순서와 각 프로세스의 실행 완료 시간, 대기 시간, 남은 실행 시간을 계산
    completion_time = [0]*n
    waiting_time = [0]*n
    turnaround_time = [0]*n
    remaining_time = []
    for r in range(n):
        remaining_time.append(processes[r][2])
    result = []

    while completed_processes < n:
        # 도착한 프로세스를 대기 큐에 추가
        for i in range(n):
            if processes[i][1] == current_time:
                waiting_processes.append(i)
        # 대기 중인 프로세스 중 가장 짧은 실행 시간을 가진 프로세스 선택
        if running_process is None and waiting_processes:
            shortest_process_index = waiting_processes[0]
            for i in waiting_processes:
                if remaining_time[i] < remaining_time[shortest_process_index]:
                    shortest_process_index = i
            running_process = shortest_process_index
            waiting_processes.remove(shortest_process_index)
        # 현재 실행 중인 프로세스가 있는 경우
        if running_process is not None:
            # 실행 중인 프로세스의 실행 시간을 1만큼 감소
            remaining_time[running_process] -= 1
            # 실행이 완료된 경우
            if remaining_time[running_process] == 0:
                completion_time[running_process] = current_time + 1
                waiting_time[running_process] = completion_time[running_process] - processes[running_process][1] - processes[running_process][2]
                turnaround_time[running_process] = completion_time[running_process] - processes[running_process][1]
                running_process = None
                completed_processes += 1
        current_time += 1

    for i in range(n):
        result.append([processes[i][0],processes[i][1],processes[i][2],waiting_time[i],turnaround_time[i]])
    return result
