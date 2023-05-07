def SRTN(n,processes):
    # 실행 순서와 각 프로세스의 실행 완료 시간, 대기 시간을 계산
    ct = 0
    wt = 0
    tt = 0
    runtime = [0]*n
    cr = 0
    alltime = 0
    result = []
    arrive = []
    while processes[cr][1] != 0:
        cr+=1
    for a in range(n):
        alltime += processes[a][2]
        runtime[a] = processes[a][2]
    pl = processes[cr][2]
    print(runtime)
    while n != 0:
        if(len(runtime)>1):
            for i in range(n):
                if runtime[cr]>processes[i][2] and processes[i][1]<=ct:
                    cr=i
            ct+=1
            runtime[cr]-=1
        else:
            cr=0
            ct+=1
            runtime[cr]-=1
        if runtime[cr]==0:
            tt = ct-processes[cr][1]
            wt = tt-processes[cr][2]
            result.append([processes[cr][0],processes[cr][1],processes[cr][2],wt,tt])
            del runtime[cr]
            del processes[cr]
            n-=1
            print(runtime)
            print(processes)
    result.sort(key=lambda x:x[1])
    return result

