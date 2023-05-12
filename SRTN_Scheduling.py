import math

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
    while processes[cr][1] != 0:
        cr += 1
    for a in range(n):
        if core == "P":
            alltime += math.ceil(processes[a][2] / 2)
            runtime[a] = math.ceil(processes[a][2] / 2)
        else :
            alltime += processes[a][2]
            runtime[a] = processes[a][2]
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
    result.append(graph)
    return result