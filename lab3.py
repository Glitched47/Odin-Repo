#this will be our continue flag... if it's set to 'N', we're done, if it's
#set to 'Y' (or anything else really), we add more runners
cont = "Y"
#lists to hold our runners and their times, so runner[n] will be the name of
#the n'th place finisher and times[n] will be their time (in minutes)
runners = []
times = []
#loop until the user says they're out of runners to process
while (cont != "N"):
    runner_name = input("Please enter name of next runner: ")
    runner_time = float(input("Please enter runner time: "))

    runners.append(runner_name)
    times.append(runner_time)

    cont = input("Any more runners to add? (Y/N)")
average_time = sum(times)/len(times)
print ("Average time of all runners: " + str(average_time) + " minutes")


cutoff_time = float(input("Enter cutoff time to qualify: "))

qualifying_runner_name =[]
qualifying_runners_time = []  

for runner_name, runner_time in zip(runners, times):
    if runner_time <= cutoff_time:
        qualifying_runner_name.append(runner_name)
        qualifying_runners_time.append(runner_time)

print("Qualified runners:")
for runner_name in qualifying_runner_name:
    print(runner_name)

average_qualifying_time = sum(qualifying_runners_time)/len(qualifying_runners_time)
print(("Average time of all runners: " + str(average_qualifying_time) + " minutes"))





