def FCFS(n, processes) :
    # 실행 순서와 각 프로세스의 실행 완료 시간, 대기 시간을 계산
    completion_time = [0]*n
    waiting_time = [0]*n
    turnaround_time = [0]*n

    for i in range(n):
        # 실행 순서
        if i == 0:
            completion_time[i] = processes[i][1] + processes[i][2]
        else:
            completion_time[i] = completion_time[i-1] + processes[i][2]
        # 대기 시간
        waiting_time[i] = completion_time[i] - processes[i][1] - processes[i][2]
        # 회전 시간
        turnaround_time[i] = completion_time[i] - processes[i][1]
        processes[i]=processes[i]+[waiting_time[i],turnaround_time[i]]

    # 평균 대기 시간과 평균 회전 시간을 계산
    avg_waiting_time = sum(waiting_time)/n
    avg_turnaround_time = sum(turnaround_time)/n

    # 계산된 값들을 튜플로 반환
    return processes

"""
# 프로세스 정보를 담은 리스트
if __name__ == "__main__":
    processes = []
    # 프로세스의 개수
    n = int(input("프로세스의 개수를 입력하세요: "))
    # 각 프로세스의 정보를 입력받아 리스트에 추가
    for i in range(n):
        print("프로세스 ", i+1)
        arrival_time = int(input("도착 시간을 입력하세요: "))
        burst_time = int(input("실행 시간을 입력하세요: "))
        processes.append((arrival_time, burst_time))

    # FCFS 함수를 호출하고 반환된 값을 저장
    completion_time, waiting_time, turnaround_time, avg_waiting_time, avg_turnaround_time = FCFS()

    print("\nFCFS 스케줄링 결과")
    print("프로세스\t도착 시간\t실행 시간\t완료 시간\t대기 시간\t회전 시간")
    for i in range(n):
        print(f"{i+1}\t\t{processes[i][0]}\t\t{processes[i][1]}\t\t{completion_time[i]}\t\t{waiting_time[i]}\t\t{turnaround_time[i]}")
    print(f"\n평균 대기 시간: {avg_waiting_time}")
    print(f"평균 회전 시간: {avg_turnaround_time}")
"""