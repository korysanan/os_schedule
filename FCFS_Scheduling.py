import math

def Ecore(AW, onoff):
    if onoff == 0: 
        AW += 0.1
        onoff = 1
    AW += 1
    return AW

def Pcore(AW, onoff):
    if onoff == 0:
       AW += 0.5
       onoff = 1 
    AW += 3
    return AW

def FCFS(n, processes, core) :
    processes.sort(key = lambda x:x[1])
    # 실행 순서와 각 프로세스의 실행 완료 시간, 대기 시간을 계산
    completion_time = [0]*n
    waiting_time = [0]*n
    turnaround_time = [0]*n
    graph = []
    AW=0
    onoff=0
    burst_time = [p[2] for p in processes]
    if core == "P":
        new_burst_time = []
        for num in burst_time:
            new_burst_time.append(math.ceil(num/2))

        burst_time = new_burst_time

    for i in range(n):

        if(i==0):
            if(core == "E"):            #전력량 계산
                AW = Ecore(AW,onoff)
            elif(core == "P"):
                AW = Pcore(AW,onoff)

        # 실행 순서
        if i == 0:
            completion_time[i] = processes[i][1] + burst_time[i]
        else:
            completion_time[i] = completion_time[i-1] + burst_time[i]

        if(completion_time != processes[i][1]): #연속적으로 사용되지 않으면 off - 완료시간 != 입력된 시간
           onoff = 0
        if(core == "E"):            #전력량 계산
            AW = Ecore(AW,onoff)
        elif(core == "P"):
            AW = Pcore(AW,onoff)

        waiting_time[i] = completion_time[i] - processes[i][1] - burst_time[i]

        turnaround_time[i] = completion_time[i] - processes[i][1]
        processes[i]=processes[i]+[waiting_time[i],turnaround_time[i]]
        for a in range(turnaround_time[i] - waiting_time[i]):
            graph.append(processes[i][0])
    
    processes.sort(key=lambda x: x[0])
    AW = round(AW,2)
    processes.append(AW)    
    processes.append(graph)
    return processes

n = 5
processes = [["p1", 0, 3], ["p2", 1, 7], ["p3", 3, 2], ["p4", 5, 5], ["p5", 6, 3]]
cores = ["P", "E", "P", "E"]
a = FCFS(n, processes, cores[0])
print(a)

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