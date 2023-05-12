def SRTN(n,processes, core):
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

    if(core[sunseo] == "P"):
        for i in range(n):
            processes[i][2] = round(processes[i][2])

    while processes[cr][1] != 0:
        cr+=1
    for a in range(n):
        alltime += processes[a][2]
        runtime[a] = processes[a][2]
    while n != 0:

        if(a==0):
            if(core[sunseo] == "E"):            #전력량 계산
                AW[sunseo] = Ecore(AW[sunseo],onoff[sunseo])
            elif(core[sunseo] == "P"):
                AW[sunseo] = Pcore(AW[sunseo],onoff[sunseo])

        if(len(runtime)>1):
            for i in range(n):
                if runtime[cr]>runtime[i] and processes[i][1]<=ct:
                    cr=i
            ct+=1
            runtime[cr]-=1
        else:
            cr=0
            ct+=1
            runtime[cr]-=1
        if runtime[cr]==0:

            if(completion_time != processes[i][1]): #연속적으로 사용되지 않으면 off - 완료시간 != 입력된 시간
                onoff = 0

            if(core[sunseo] == "E"):            #전력량 계산
                AW[sunseo] = Ecore(AW[sunseo],onoff[sunseo])
            elif(core[sunseo] == "P"):
                AW[sunseo] = Pcore(AW[sunseo],onoff[sunseo])

            tt = ct-processes[cr][1]
            wt = tt-processes[cr][2]
            result.append([processes[cr][0],processes[cr][1],processes[cr][2],wt,tt])
            #for u in range(tt - wt):
            #    graph.append(processes[cr][0])
            del runtime[cr]
            del processes[cr]
            n-=1
            if (cr>len(runtime)-1):
                cr=0
    #print(graph)
    result.sort(key=lambda x:x[1])
    result.append(AW)
    return result

n = 5
processes = [["p1", 0, 3], ["p2", 1, 7], ["p3", 3, 2], ["p4", 5, 5], ["p5", 6, 3]]
cores = ['P-core', 'P-core', 'E-core', 'E-core']
a = SRTN(n, processes, cores)
print(a)