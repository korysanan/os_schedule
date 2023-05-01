    def FCFS() :
        # 프로세스 정보를 담은 리스트
       # processes = [] #여기에, n =  프로세스수.

        # 실행 순서와 각 프로세스의 실행 완료 시간, 대기 시간을 계산
        completion_time = [0]n
        waiting_time = [0]n
        turnaround_time = [0]*n

        for i in range(n):
            # 실행 순서
            if i == 0:
               # completion_time[i] = processes[i][0] + processes[i][1]
                completion_time[i] = self.tableWidget_2.item(i,0) + self.tableWidget_2.item(i,1)
            else:
                #completion_time[i] = completion_time[i-1] + processes[i][1]
                completion_time[i] = completion_time[i-1] + self.tableWidget_2.item(i,1)

            # 대기 시간
            #waiting_time[i] = completion_time[i] - processes[i][0] - processes[i][1]
            waiting_time[i] = completion_time[i] - self.tableWidget_2.item(i,0) - self.tableWidget_2.item(i,1)
            # 회전 시간
            #turnaround_time[i] = completion_time[i] - processes[i][0]
            turnaround_time[i] = completion_time[i] - self.tableWidget_2.item(i,0)

        # 계산된 값들을 튜플로 반환
        return completion_time, waiting_time, turnaround_time