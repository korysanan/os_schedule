def OOA(n, processes, quantum):
    completion_time = 0
    waiting_time = [0]*n
    turnaround_time = [0]*n
    result = []
    ready_queue = []

    while len(processes) > 0 or len(ready_queue) > 0:
        # Check for new arrivals
        for i in range(len(processes)):
            if processes[i][1] <= completion_time:
                ready_queue.append(processes.pop(i))
                break

        if len(ready_queue) > 0:
            # Choose the process with the highest response ratio
            max_priority = -1
            highest_response_ratio_index = 0
            for i in range(len(ready_queue)):
                response_ratio = (completion_time - ready_queue[i][1] + ready_queue[i][2]) / ready_queue[i][2]
                if response_ratio > max_priority:
                    max_priority = response_ratio
                    highest_response_ratio_index = i
            
            process = ready_queue.pop(highest_response_ratio_index)

            if process[2] <= quantum:
                # Process execution time is less than or equal to the quantum
                waiting_time[int(process[0][1:]) - 1] = completion_time - int(process[1])
                turnaround_time[process[0][1:] - 1] = completion_time + int(process[2]) - int(process[1])
                completion_time += int(process[2])
                result.append([process[0], process[1], process[2], waiting_time[process[0] - 1], turnaround_time[process[0] - 1]])
            else:
                # Process execution time is greater than the quantum
                waiting_time[int(process[0][1:]) - 1] = completion_time - int(process[1])
                turnaround_time[int(process[0][1:]) - 1] = completion_time + quantum - int(process[1])
                process[2] -= quantum
                completion_time += quantum
                ready_queue.append(process)

        else:
            # There are no processes in ready_queue, but there are still processes to arrive
            process = processes.pop(0)
            waiting_time[int(process[0]) - 1] = 0
            turnaround_time[int(process[0]) - 1] = process[2]
            completion_time = process[1] + process[2]
            result.append([process[0], process[1], process[2], waiting_time[process[0] - 1], turnaround_time[process[0] - 1]])

    return result
