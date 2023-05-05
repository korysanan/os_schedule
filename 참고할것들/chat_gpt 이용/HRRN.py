processes = []
n = int(input("Enter the number of processes: "))

for i in range(n):
    print("Process ", i+1)
    arrival_time = int(input("Enter the arrival time: "))
    burst_time = int(input("Enter the burst time: "))
    processes.append((arrival_time, burst_time))

completion_time = [0]*n
waiting_time = [0]*n
turnaround_time = [0]*n
remaining_burst_time = [process[1] for process in processes]
current_time = 0

while True:
    if all(burst_time == 0 for burst_time in remaining_burst_time):
        break

    available_processes = [i for i in range(n) if processes[i][0] <= current_time and remaining_burst_time[i] > 0]
    if not available_processes:
        current_time += 1
        continue

    response_ratios = [(i, (current_time - processes[i][0] + remaining_burst_time[i]) / remaining_burst_time[i]) for i in available_processes]
    highest_ratio_process = max(response_ratios, key=lambda x: x[1])
    highest_ratio_process_index = highest_ratio_process[0]

    current_time += remaining_burst_time[highest_ratio_process_index]
    remaining_burst_time[highest_ratio_process_index] = 0

    completion_time[highest_ratio_process_index] = current_time
    waiting_time[highest_ratio_process_index] = current_time - processes[highest_ratio_process_index][0] - processes[highest_ratio_process_index][1]
    turnaround_time[highest_ratio_process_index] = current_time - processes[highest_ratio_process_index][0]

avg_waiting_time = sum(waiting_time)/n
avg_turnaround_time = sum(turnaround_time)/n

print("\nHRRN Scheduling Results")
print("Process\tArrival Time\tBurst Time\tCompletion Time\tWaiting Time\tTurnaround Time\tNomalized TT")
for i in range(n):
    print(f"{i+1}\t\t{processes[i][0]}\t\t{processes[i][1]}\t\t{completion_time[i]}\t\t{waiting_time[i]}\t\t{turnaround_time[i]}\t\t{turnaround_time[i] / processes[i][1]}")
print(f"\nAverage waiting time: {avg_waiting_time}")
print(f"Average turnaround time: {avg_turnaround_time}")