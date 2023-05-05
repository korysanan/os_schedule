def OOA(n, processes, quantum):
    # 실행 순서와 각 프로세스의 실행 완료 시간, 대기 시간을 계산
    completion_time = 0
    waiting_time = [0]*n
    turnaround_time = [0]*n
    response_ratio = [0]*n
    currently = -1  # 현재 실행 중인 프로세스
    result = []
    name = []

    while True:
        # 대기 중인 프로세스 중에서 응답 비율이 가장 높은 프로세스 선택
        max_ratio = -1
        for i in range(n):
            if processes[i][1] <= completion_time and processes[i][2] > 0:
                ratio = (waiting_time[i] + processes[i][2]) / processes[i][2]
                if ratio > max_ratio:
                    max_ratio = ratio
                    currently = i

        # 모든 프로세스가 실행을 완료한 경우 종료
        if max_ratio == -1:
            break

        # 현재 프로세스 실행
        if processes[currently][2] > quantum:
            processes[currently][2] -= quantum
            completion_time += quantum
        else:
            completion_time += processes[currently][2]
            processes[currently][2] = 0

        # 대기 시간, 반환 시간, 응답 비율 계산
        for i in range(n):
            if i != currently and processes[i][1] <= completion_time and processes[i][2] > 0:
                waiting_time[i] += quantum if i != currently else 0
                response_ratio[i] = (waiting_time[i] + processes[i][2]) / processes[i][2]
            else:
                response_ratio[i] = -1

        turnaround_time[currently] = completion_time - processes[currently][1]
        waiting_time[currently] = turnaround_time[currently] - processes[currently][3]
        response_ratio[currently] = -1  # 현재 실행 중인 프로세스의 응답 비율은 계산하지 않음

        # 실행 결과 저장
        result.append([processes[currently][0], processes[currently][1], processes[currently][3], waiting_time[currently], turnaround_time[currently]])
        name.append(processes[currently][0])

    return result