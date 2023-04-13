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
response_ratio = [0]*n

total_waiting_time = 0
total_turnaround_time = 0

# 최초 대기시간은 도착시간으로 초기화
current_time = processes[0][0]

while True:
    remaining_time = []  # 남은 실행 시간
    process_indexes = []  # 대기 중인 프로세스의 인덱스

    # 대기 중인 프로세스 찾기
    for i, process in enumerate(processes):
        if process[0] <= current_time and completion_time[i] == 0:
            remaining_time.append(process[1])
            process_indexes.append(i)
    
    # 모든 프로세스가 완료된 경우 종료
    if len(process_indexes) == 0:
        break
    
    # 우선순위 계산 (고응답률 우선)
    for i, idx in enumerate(process_indexes):
        response_ratio[idx] = (waiting_time[idx] + processes[idx][1]) / processes[idx][1]

    # 가장 높은 우선순위를 가진 프로세스 실행
    min_idx = process_indexes[response_ratio.index(max(response_ratio))]
    min_burst_time = processes[min_idx][1]
    completion_time[min_idx] = current_time + min_burst_time
    waiting_time[min_idx] = current_time - processes[min_idx][0]
    turnaround_time[min_idx] = completion_time[min_idx] - processes[min_idx][0]
    response_ratio[min_idx] = 0

    # 총 대기 시간, 총 회전 시간 계산
    total_waiting_time += waiting_time[min_idx]
    total_turnaround_time += turnaround_time[min_idx]

    current_time = completion_time[min_idx]

# 평균 대기 시간과 평균 회전 시간을 계산
avg_waiting_time = total_waiting_time / n
avg_turnaround_time = total_turnaround_time / n

# 결과 출력
print("\nRound Robin 스케줄링 결과")
print("프로세스\t도착 시간\t실행 시간\t완료 시간\t대기 시간\t회전 시간")
for i in range(n):
    print(f"{i+1}\t\t{processes[i][0]}\t\t{processes[i][1]}\t\t{completion_time[i]}\t\t{waiting_time[i]}\t\t{turnaround_time[i]}")
print(f"\n평균 대기 시간: {avg_waiting_time}")
print(f"평균 회전 시간: {avg_turnaround_time}")