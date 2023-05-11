def HRRN(n, processes, core):
    # 실행 순서와 각 프로세스의 실행 완료 시간, 대기 시간을 계산
    completion_time = 0
    waiting_time = [0]*n
    turnaround_time = [0]*n
    result = []
    graph = []

    while len(processes) > 0:
        max_priority = -1
        highest_response_ratio_index = 0
        for i in range(len(processes)):
            response_ratio = (completion_time - processes[i][1] + processes[i][2]) / processes[i][2]
            if response_ratio > max_priority:
                max_priority = response_ratio
                highest_response_ratio_index = i
        
        # 실행 시간이 가장 높은 프로세스를 선택하고 해당 프로세스를 제거
        process = processes.pop(highest_response_ratio_index)
        
        # 해당 프로세스의 대기 시간, 반환 시간 계산
        waiting_time[highest_response_ratio_index] = completion_time - process[1]
        turnaround_time[highest_response_ratio_index] = completion_time + process[2] - process[1]
        
        # 실행 완료 시간 갱신
        completion_time += process[2]
        
        # 결과 리스트에 추가
        result.append([process[0], process[1], process[2], waiting_time[highest_response_ratio_index], turnaround_time[highest_response_ratio_index]])
        for u in range(turnaround_time[highest_response_ratio_index] - waiting_time[highest_response_ratio_index]):
            graph.append(process[0])
    result.append(graph)
    return result

n = 5
processes = [["p1", 0, 3], ["p2", 1, 7], ["p3", 3, 2], ["p4", 5, 5], ["p5", 6, 3]]
cores = ['P-core', 'P-core', 'E-core', 'E-core']
a =HRRN(n, processes, cores)
print(a)