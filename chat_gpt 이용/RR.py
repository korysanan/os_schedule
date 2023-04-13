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

# 시간 할당량(time quantum)
time_quantum = int(input("시간 할당량을 입력하세요: "))

# 실행 순서와 각 프로세스의 실행 완료 시간, 대기 시간을 계산
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
    if remaining_time[i] <= time_quantum:
        current_time += remaining_time[i]
        completion_time[i] = current_time
        remaining_time[i] = 0
    # 남은 실행 시간이 시간 할당량보다 큰 경우
    else:
        current_time += time_quantum
        remaining_time[i] -= time_quantum
        queue.append(i)

# 대기 시간과 회전 시간 계산
for i in range(n):
    turnaround_time[i] = completion_time[i] - processes[i][0]
    waiting_time[i] = turnaround_time[i] - processes[i][1]

# 평균 대기 시간과 평균 회전 시간 계산
avg_waiting_time = sum(waiting_time)/n
avg_turnaround_time = sum(turnaround_time)/n

# 결과 출력
print("\nRound Robin 스케줄링 결과")
print("프로세스\t도착 시간\t실행 시간\t완료 시간\t대기 시간\t회전 시간")
for i in range(n):
    print(f"{i+1}\t\t{processes[i][0]}\t\t{processes[i][1]}\t\t{completion_time[i]}\t\t{waiting_time[i]}\t\t{turnaround_time[i]}")
print(f"\n평균 대기 시간: {avg_waiting_time}")
print(f"평균 회전 시간: {avg_turnaround_time}")