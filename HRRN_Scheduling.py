import math
<<<<<<< HEAD

=======
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
>>>>>>> 8cd2560df15e1dbfde4e5e4d5d6de327eaf59ac5
def HRRN(n, processes, core):
    # 실행 순서와 각 프로세스의 실행 완료 시간, 대기 시간을 계산
    completion_time = 0
    waiting_time = [0]*n
    turnaround_time = [0]*n
    result = []
    graph = []
<<<<<<< HEAD
    burst_time = [p[2] for p in processes]
    if core == "P":
        new_burst_time = []
        for num in burst_time:
            new_burst_time.append(math.ceil(num/2))

        burst_time = new_burst_time
=======
    AW=0
    onoff=0
    burst_time = [p[2] for p in processes]
    if core == "P":
         new_burst_time = []
         for num in burst_time:
             new_burst_time.append(math.ceil(num/2))

         burst_time = new_burst_time
>>>>>>> 8cd2560df15e1dbfde4e5e4d5d6de327eaf59ac5

    while len(processes) > 0:
        if(core == "E"):            #전력량 계산
                AW = Ecore(AW,onoff)
        elif(core == "P"):
                AW = Pcore(AW,onoff)
        max_priority = -1
        highest_response_ratio_index = 0
        for i in range(len(processes)):
<<<<<<< HEAD
=======
            if(i==0):
                if(core == "E"):            #전력량 계산
                    AW = Ecore(AW,onoff)
                elif(core == "P"):
                    AW = Pcore(AW,onoff)

>>>>>>> 8cd2560df15e1dbfde4e5e4d5d6de327eaf59ac5
            response_ratio = (completion_time - processes[i][1] + burst_time[i]) / burst_time[i]
            if response_ratio > max_priority:
                max_priority = response_ratio
                highest_response_ratio_index = i

        # 실행 시간이 가장 높은 프로세스를 선택하고 해당 프로세스를 제거
        process = processes.pop(highest_response_ratio_index)
        bt = process[2]
<<<<<<< HEAD
        if core == "P":
            bt = math.ceil(bt / 2)
        # 해당 프로세스의 대기 시간, 반환 시간 계산
        waiting_time[highest_response_ratio_index] = completion_time - process[1]
        turnaround_time[highest_response_ratio_index] = completion_time + bt - process[1]
=======
        # if core == "P":
        #     bt = math.ceil(bt / 2)
        # 해당 프로세스의 대기 시간, 반환 시간 계산
        waiting_time[highest_response_ratio_index] = completion_time - process[1]
        #turnaround_time[highest_response_ratio_index] = completion_time + bt - process[1]
>>>>>>> 8cd2560df15e1dbfde4e5e4d5d6de327eaf59ac5
        
        # 실행 완료 시간 갱신
        completion_time += bt
        
        # 결과 리스트에 추가
        result.append([process[0], process[1], process[2], waiting_time[highest_response_ratio_index], turnaround_time[highest_response_ratio_index]])
        for u in range(turnaround_time[highest_response_ratio_index] - waiting_time[highest_response_ratio_index]):
            graph.append(process[0])
    AW = round(AW,2)
    processes.append(AW)  
    result.append(graph)
<<<<<<< HEAD
    return result
=======
    return result

n = 5
processes = [["p1", 0, 3], ["p2", 1, 7], ["p3", 3, 2], ["p4", 5, 5], ["p5", 6, 3]]
cores = ["P", "E", "P", "E"]
a = HRRN(n, processes, cores[0])
print(a)
>>>>>>> 8cd2560df15e1dbfde4e5e4d5d6de327eaf59ac5
