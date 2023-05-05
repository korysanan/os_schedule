def OOA(n, processes, quantam):
    # 실행 순서와 각 프로세스의 실행 완료 시간, 대기 시간을 계산
    completion_time = 0
    waiting_time = [0]*n
    turnaround_time = [0]*n
    result = []
    remaining_time = [process[2] for process in processes]

    while True:
        done = True
        for i in range(n):
            if remaining_time[i] > 0:
                done = False
                if remaining_time[i] > quantam:
                    completion_time += quantam
                    remaining_time[i] -= quantam
                else:
                    completion_time += remaining_time[i]
                    waiting_time[i] = completion_time - processes[i][2] - processes[i][1]
                    turnaround_time[i] = completion_time - processes[i][1]
                    remaining_time[i] = 0
                    result.append([processes[i][0], processes[i][1], processes[i][2], waiting_time[i], turnaround_time[i]])
        
        if done == True:
            break

        # 우선순위를 반영하여 실행할 프로세스 선택
        max_priority = -1
        highest_response_ratio_index = 0
        for i in range(n):
            if remaining_time[i] > 0:
                response_ratio = (completion_time - processes[i][1] + processes[i][2]) / processes[i][2]
                if response_ratio > max_priority:
                    max_priority = response_ratio
                    highest_response_ratio_index = i
        
        # 선택한 프로세스가 이미 실행했던 프로세스인 경우, 우선순위를 다시 계산
        if len(result) > 0 and result[-1][0] == processes[highest_response_ratio_index][0]:
            max_priority = -1
            for i in range(n):
                if remaining_time[i] > 0 and i != highest_response_ratio_index:
                    response_ratio = (completion_time - processes[i][1] + processes[i][2]) / processes[i][2]
                    if response_ratio > max_priority:
                        max_priority = response_ratio
                        highest_response_ratio_index = i
        
        # 선택한 프로세스 실행
        remaining_time[highest_response_ratio_index] -= quantam if remaining_time[highest_response_ratio_index] > quantam else remaining_time[highest_response_ratio_index]
        
    # 프로세스의 입력 순서대로 결과 리스트 정렬
    result.sort(key=lambda x: x[0])

    return result