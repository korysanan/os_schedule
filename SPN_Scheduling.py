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
def SPN(n, processes, core):
    # 실행 순서와 각 프로세스의 실행 완료 시간, 대기 시간을 계산
    completion_time = 0
    waiting_time = [0]*n
    turnaround_time = [0]*n
    CURRENTLY = 0
    result = []
    graph = []
    AW=0
    onoff=0
    for a in range(n):
        if(a==0):
            if(core == "E"):            #전력량 계산
                AW = Ecore(AW,onoff)
            elif(core == "P"):
                AW = Pcore(AW,onoff)
        pl = processes[0][2]
        for r in range(n):
            if(completion_time>=processes[r][1]):
                if(pl>=processes[r][2]):
                    pl = processes[r][2]
                    CURRENTLY = r
        if core == "P":
<<<<<<< HEAD
            completion_time = completion_time + math.ceil(processes[CURRENTLY][2] / 2)
            turnaround_time = completion_time - processes[CURRENTLY][1]
            waiting_time =  turnaround_time-math.ceil(processes[CURRENTLY][2] / 2)
            result.append([processes[CURRENTLY][0],processes[CURRENTLY][1],processes[CURRENTLY][2],waiting_time,turnaround_time])
=======
             completion_time = completion_time + math.ceil(processes[CURRENTLY][2] / 2)
             turnaround_time = completion_time - processes[CURRENTLY][1]
             waiting_time =  turnaround_time-math.ceil(processes[CURRENTLY][2] / 2)
             result.append([processes[CURRENTLY][0],processes[CURRENTLY][1],processes[CURRENTLY][2],waiting_time,turnaround_time])
>>>>>>> 8cd2560df15e1dbfde4e5e4d5d6de327eaf59ac5
        else :
            completion_time = completion_time + processes[CURRENTLY][2]
            turnaround_time = completion_time - processes[CURRENTLY][1]
            waiting_time =  turnaround_time-processes[CURRENTLY][2]
            result.append([processes[CURRENTLY][0],processes[CURRENTLY][1],processes[CURRENTLY][2],waiting_time,turnaround_time])
        
<<<<<<< HEAD
=======
        if(completion_time != processes[a][1]): #연속적으로 사용되지 않으면 off - 완료시간 != 입력된 시간
           onoff = 0
        if(core == "E"):            #전력량 계산
            AW = Ecore(AW,onoff)
        elif(core == "P"):
            AW = Pcore(AW,onoff)

>>>>>>> 8cd2560df15e1dbfde4e5e4d5d6de327eaf59ac5
        for u in range(turnaround_time - waiting_time):
            graph.append(processes[CURRENTLY][0])
        del processes[CURRENTLY]
        n=n-1
    result.sort(key=lambda x: x[0])
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
a = SPN(n, processes, cores[0])
print(a)
>>>>>>> 8cd2560df15e1dbfde4e5e4d5d6de327eaf59ac5
