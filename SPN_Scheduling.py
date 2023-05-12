def SPN(n, processes, core):
    # 실행 순서와 각 프로세스의 실행 완료 시간, 대기 시간을 계산
    completion_time = 0
    waiting_time = [0]*n
    turnaround_time = [0]*n
    CURRENTLY = 0
    AW=0
    onoff=0
    result = []
    graph = []

    if(core[sunseo] == "P"):
        for i in range(n):
            processes[i][2] = round(processes[i][2])

    for a in range(n):

        if(a==0):
            if(core[0] == "E"):            #전력량 계산
                AW = Ecore(AW,onoff)
            elif(core[0] == "P"):
                AW = Pcore(AW,onoff)

        pl = processes[0][2]
        for r in range(n):
            if(completion_time>=processes[r][1]):
                if(pl>=processes[r][2]):
                    pl = processes[r][2]
                    CURRENTLY = r

        if(completion_time != processes[CURRENTLY][1]): #연속적으로 사용되지 않으면 off - 완료시간 != 입력된 시간
            onoff = 0

        if(core[0] == "E"):            #전력량 계산
            AW = Ecore(AW,onoff)
        elif(core[0] == "P"):
            AW = Pcore(AW,onoff)

        completion_time = completion_time + processes[CURRENTLY][2]
        turnaround_time = completion_time - processes[CURRENTLY][1]
        waiting_time =  turnaround_time-processes[CURRENTLY][2]
        result.append([processes[CURRENTLY][0],processes[CURRENTLY][1],processes[CURRENTLY][2],waiting_time,turnaround_time])
        for u in range(turnaround_time - waiting_time):
            graph.append(processes[CURRENTLY][0])
        del processes[CURRENTLY]
        n=n-1
    result.sort(key=lambda x: x[0])
    result.append(AW)
    result.append(graph)
    return result

n = 5
processes = [["p1", 0, 3], ["p2", 1, 7], ["p3", 3, 2], ["p4", 5, 5], ["p5", 6, 3]]
cores = ['P-core', 'P-core', 'E-core', 'E-core']
a = SPN(n, processes, cores)
print(a)