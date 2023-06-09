import math

def HRRN(n, processes, core):
    # 실행 순서와 각 프로세스의 실행 완료 시간, 대기 시간을 계산
    completion_time = 0
    waiting_time = [0]*n
    turnaround_time = [0]*n
    result = []
    graph = []
    burst_time = [p[2] for p in processes]
    if core == "P":
        new_burst_time = []
        for num in burst_time:
            new_burst_time.append(math.ceil(num/2))

        burst_time = new_burst_time

    while len(processes) > 0:
        max_priority = -1
        highest_response_ratio_index = 0
        # max_priority와 highest_response_ratio_index를 -1과 0으로 초기화
        for i in range(len(processes)):
            response_ratio = (completion_time - processes[i][1] + burst_time[i]) / burst_time[i]
            if response_ratio > max_priority:
                max_priority = response_ratio
                highest_response_ratio_index = i
        
        process = processes.pop(highest_response_ratio_index)
        # 실행 시간이 가장 높은 프로세스를 선택하고 해당 프로세스를 제거
        bt = process[2]
        if core == "P":
            bt = math.ceil(bt / 2)
        # P_core일때는 실행시간을 반 줄인다.

        waiting_time[highest_response_ratio_index] = completion_time - process[1]
        turnaround_time[highest_response_ratio_index] = completion_time + bt - process[1]
        # 해당 프로세스의 대기 시간, 반환 시간 계산
        
        completion_time += bt
        # 실행 완료 시간 갱신
        
        result.append([process[0], process[1], process[2], waiting_time[highest_response_ratio_index], turnaround_time[highest_response_ratio_index]])
        # 결과 리스트에 추가
        for u in range(turnaround_time[highest_response_ratio_index] - waiting_time[highest_response_ratio_index]):
            graph.append(process[0])
        # 해당 프로세스 이름 graph 추가
    result.append(graph)
    return result