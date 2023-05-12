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
    #프로세스 시작 반복문
    while processes[cr][1] != 0:
        
    #현재 시간을 1만큼 증가    
        cr += 1
        
    #총 시간 저장, 각 프로세스의 실행시간을 runtime 배열에 저장
    for a in range(n):
        if core == "P":
            alltime += math.ceil(processes[a][2] / 2)
            runtime[a] = math.ceil(processes[a][2] / 2)
        else :
            alltime += processes[a][2]
            runtime[a] = processes[a][2]
    
    #프로세스 동작 코드
    while n != 0:
        if len(runtime) > 1:
    #현재 프로세스보다 잔여 실행 시간이 적은 프로세스를 찾는 반복문 
            for i in range(n):
                if runtime[cr] > runtime[i] and processes[i][1] <= ct:
                    cr = i
            ct += 1
            runtime[cr] -= 1
        else:
            cr = 0
            ct += 1
            runtime[cr] -= 1
     #프로세스의 실행이 완료되었을때 시간 계산
        if runtime[cr] == 0:
            if core == "P":
                tt = ct - processes[cr][1]
                wt = tt - math.ceil(processes[cr][2] / 2)
            else:
                tt = ct - processes[cr][1]
                wt = tt - processes[cr][2]
            
            #스케줄링 결과 리스트에 저장
            result.append([processes[cr][0], processes[cr][1], processes[cr][2], wt, tt])
            for u in range(tt - wt):
                graph.append(processes[cr][0])
            del runtime[cr]
            del processes[cr]
            n -= 1
            if cr > len(runtime) - 1:
                cr = 0
                
    #결과 리스트 정렬 후 반환   
    result.sort(key=lambda x:x[1])
    result.append(graph)
    return result
