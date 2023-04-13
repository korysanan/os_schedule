# 프로세스 정보를 담은 리스트
processes = []
# 프로세스의 개수
n = int(input("프로세스의 개수를 입력하세요: "))
# 각 프로세스의 정보를 입력받아 리스트에 추가
for i in range(n):
    print("프로세스 ", i+1)
    arrival_time = int(input("도착 시간을 입력하세요: "))
    burst_time = int(input("실행 시간을 입력하세요: "))
    processes.append((arrival_time, burst_time))

# 실행 순서와 각 프로세스의 실행 완료 시간, 대기 시간을 계산
completion_time = [0]*n
waiting_time = [0]*n
turnaround_time = [0]*n

# 프로세스 도착 시간순으로 정렬
processes = sorted(processes, key=lambda x: x[0])

# 현재까지 수행된 프로세스 중 가장 짧은 실행 시간을 가진 프로세스의 인덱스를 저장
current_process_index = -1
# 현재까지 수행된 프로세스 중 가장 짧은 실행 시간
current_process_burst_time = float('inf')

# 시간 경과에 따라 프로세스를 실행
for time in range(max(processes)[0]+1):
    # 현재까지 도착한 모든 프로세스 중 실행 시간이 가장 짧은 프로세스를 선택
    for i in range(n):
        if processes[i][0] <= time and processes[i][1] < current_process_burst_time and completion_time[i] == 0:
            current_process_index = i
            current_process_burst_time = processes[i][1]

    # 프로세스 실행 시간을 1 감소시킴
    current_process_burst_time -= 1

    # 프로세스 실행이 완료된 경우
    if current_process_burst_time == 0:
        completion_time[current_process_index] = time + 1
        current_process_burst_time = float('inf')

# 대기 시간과 회전 시간을 계산
for i in range(n):
    waiting_time[i] = completion_time[i] - processes[i][0] - processes[i][1]
    turnaround_time[i] = completion_time[i] - processes[i][0]

# 평균 대기 시간과 평균 회전 시간을 계산
avg_waiting_time = sum(waiting_time)/n
avg_turnaround_time = sum(turnaround_time)/n

# 결과 출력
print("\nSPN 스케줄링 결과")
print("프로세스\t도착 시간\t실행 시간\t완료 시간\t대기 시간\t회전 시간")
for i in range(n):
    print(f"{i+1}\t\t{processes[i][0]}\t\t{processes[i][1]}\t\t{completion_time[i]}\t\t{waiting_time[i]}\t\t{turnaround_time[i]}")
print(f"\n평균 대기 시간: {avg_waiting_time}")
print(f"평균 회전 시간: {avg_turnaround_time}")