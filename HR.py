def RR(n, processes):
    quantum = 2
    # initialize variables
    remaining_time = [processes[i][2] for i in range(n)]
    completion_time = [0] * n
    waiting_time = [0] * n
    turnaround_time = [0] * n
    time = 0
    queue = []

    # loop until all processes are completed
    while True:
        # add arriving processes to the queue
        for i in range(n):
            if processes[i][1] <= time and remaining_time[i] > 0 and i not in queue:
                queue.append(i)

        # exit loop if all processes are completed
        if not queue:
            break

        # select the next process from the queue
        process_id = queue.pop(0)

        # execute the process for the time quantum or until completion
        if remaining_time[process_id] <= quantum:
            time += remaining_time[process_id]
            completion_time[process_id] = time
            remaining_time[process_id] = 0
        else:
            time += quantum
            remaining_time[process_id] -= quantum
            queue.append(process_id)

        # update waiting and turnaround times for all processes
        for i in range(n):
            if remaining_time[i] > 0 and processes[i][1] <= time and i not in queue:
                waiting_time[i] += time - completion_time[i]
            turnaround_time[i] = completion_time[i] - processes[i][1]

    # add waiting and turnaround times to the processes list
    for i in range(n):
        processes[i] += [waiting_time[i], turnaround_time[i]]

    # calculate average waiting and turnaround times
    avg_waiting_time = sum(waiting_time) / n
    avg_turnaround_time = sum(turnaround_time) / n

    # return the processes list
    return processes
