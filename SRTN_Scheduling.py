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

def SRTN(n, processes, core):
    # 실행 순서와 각 프로세스의 실행 완료 시간, 대기 시간을 계산
    ct = 0
    wt = 0
    tt = 0
    runtime = [0]*n
    cr = 0
    alltime = 0
    result = []
    graph = []
    AW=0
    onoff=0
    while processes[cr][1] != 0:
        cr += 1
    for a in range(n):
        if(a==0):
            if(core == "E"):            #전력량 계산
                AW = Ecore(AW,onoff)
            elif(core == "P"):
                AW = Pcore(AW,onoff)

        if core == "P":
             alltime += math.ceil(processes[a][2] / 2)
             runtime[a] = math.ceil(processes[a][2] / 2)
        else :
            alltime += processes[a][2]
            runtime[a] = processes[a][2]

        if(completion_time != processes[a][1]): #연속적으로 사용되지 않으면 off - 완료시간 != 입력된 시간
           onoff = 0
        if(core == "E"):            #전력량 계산
            AW = Ecore(AW,onoff)
        elif(core == "P"):
            AW = Pcore(AW,onoff)

    while n != 0:
        if len(runtime) > 1:
            for i in range(n):
                if runtime[cr] > runtime[i] and processes[i][1] <= ct:
                    cr = i
            ct += 1
            runtime[cr] -= 1
        else:
            cr = 0
            ct += 1
            runtime[cr] -= 1
        if runtime[cr] == 0:
            if core == "P":
                 tt = ct - processes[cr][1]
                 wt = tt - math.ceil(processes[cr][2] / 2)
            else:
                tt = ct - processes[cr][1]
                wt = tt - processes[cr][2]
            result.append([processes[cr][0], processes[cr][1], processes[cr][2], wt, tt])
            for u in range(tt - wt):
                graph.append(processes[cr][0])
            del runtime[cr]
            del processes[cr]
            n -= 1
            if cr > len(runtime) - 1:
                cr = 0
    result.sort(key=lambda x:x[1])
    AW = round(AW,2)
    processes.append(AW)
    result.append(graph)
    return result

n = 5
processes = [["p1", 0, 3], ["p2", 1, 7], ["p3", 3, 2], ["p4", 5, 5], ["p5", 6, 3]]
cores = ["P", "E", "P", "E"]
a = SRTN(n, processes, cores[0])
print(a)