from scipy.stats import
from colored import fg, attr
green = fg('green')
red = fg('red')
yellow = fg('yellow')
reset_color = attr('reset')


print("Enter Number of Customer: ", end=" ")
n = int(input())
print("Do  you Want to generate (Inter Arrival & Service Time) Randomly?? <'y = yes'> or <'n = no'>: ", end=" ")
optn = str(input().lower())
print()

# -------- Variable Declaration ------
intArrivalTime = []
arrivalTime = []
serviceTime = []
SBT = []
waitingTime = []
SET = []
customerSpendInSystem = []
idleTime = []

int_arrivalT = 0
total_arrivalTime = 0
total_serviceTime = 0
total_waitingTime = 0
total_idleTime = 0
total_spendTime = 0
wait_count = 0
idel_count = 0


if optn[0] == 'n':
    # -------- inter arrival Time 'User Choosen' input ------
    for i in range(n):
        if i == 0:
            intArrivalTime.append(0)
            print("Inter Arrival Time for customer 1: 0")
        else:
            intArrivalTime.append(int(input("Inter Arrival Time for Customer %i: " % (i + 1))))

    # -------- service Time 'User Choosen' input ------
    print()
    for i in range(n):
        serviceTime.append(int(input("Service Time for Customer %i: " % (i + 1))))
        total_serviceTime = total_serviceTime + serviceTime[i]

if optn[0] == 'y':
    print(":: R  a  n  d  o  m  ::\n\t  Distribution "+yellow+"\n\n[+] P O I S O N "+reset_color)
    intArrivalTime.append(0)
    data_poisson = str(poisson.rvs(mu=5.6, size=(n - 1)))  # μ = 5.6 customer/min (for n-1 customer) when n = 0, None of customer Inter Arrives Times
    for i in range(data_poisson.__len__()):
        if data_poisson[i].isnumeric():
            intArrivalTime.append(int(data_poisson[i]))
    for i in range(n):
        print("Inter Arrival Time Customer %i: %i" % (i + 1, intArrivalTime[i]))


    print(yellow+"\n[+] E X P O N E N T I A L ✎"+reset_color)
    data_expon = str(expon.rvs(scale=1, size=n))  # and  λ= 1 customer/min (for n customer)
    data_expon = data_expon.replace("[", "")
    data_expon = data_expon.replace("]", "")

    serviceTime = list(map(float, data_expon.split()))

    for i in range(n):
        print("Service Time Customer %i: %f" % (i + 1, serviceTime[i]))

for i in range(n):
    # -------- arrival time ------
    if i == 0:
        arrivalTime.append(0)
    else:
        int_arrivalT = int_arrivalT + intArrivalTime[i]
        arrivalTime.append(int_arrivalT)

    # -------- Service Begin Time ------
    if i == 0:
        SBT.append(0)
    else:
        if float(arrivalTime[i]) > float(SET[i - 1]):
            SBT.append(float(arrivalTime[i]))
        else:
            SBT.append(float(SET[i - 1]))

    # -------- waiting time ------
    if i == 0:
        waitingTime.append(0)
    else:
        if SBT[i] - arrivalTime[i] > 0:
            waitingTime.append(float(SBT[i] - arrivalTime[i]))
            wait_count += 1
        else:
            waitingTime.append(0)

    # -------- Service End Time time ------
    if i == 0:
        SET.append(float(serviceTime[i] + arrivalTime[i]))
    else:
        SET.append(float(serviceTime[i] + SBT[i]))

    # -------- customer spend time in system ------
    customerSpendInSystem.append(float(waitingTime[i] + serviceTime[i]))

    # -------- server idle time ------
    if i == 0:
        idleTime.append(0)
    else:
        if float(arrivalTime[i]) > float(SET[i - 1]):
            idleTime.append(float(arrivalTime[i] - SET[i - 1]))
            idel_count += 1
        else:
            idleTime.append(0)

# ---- Total ----
for i in range(n):
    total_arrivalTime = total_arrivalTime + int(arrivalTime[i])
    total_serviceTime = float(total_serviceTime) + float(serviceTime[i])
    total_waitingTime = float(total_waitingTime) + float(waitingTime[i])
    total_spendTime = float(total_spendTime) + float(customerSpendInSystem[i])
    total_idleTime = float(total_idleTime) + float(idleTime[i])

print(red+"                              S I N G L E    S E R V E R    Q U E U E    P R O B"+reset_color)
print("   ║ Cust. | Inter Arrival | Arrival | Service | Service T. | Waiting T. | Service T. | C. Spend T. | Server   ║")
print("   ║  No.  |  Time         |  Time   |  Time   |   Begin    |  in Queue  |   End      |  in System  | Idle T.  ║")


for i in range(n):
    if i == 0:
        print(
            "   ║ %3i           -           %3i     %1f     %1.2f      %1.4f        %5.3f         %5.3f          -     ║"
            % (i + 1, arrivalTime[i], serviceTime[i], SBT[i], waitingTime[i], SET[i], customerSpendInSystem[i]))
    else:
        print(
            "   ║ %3i         %3i           %3i     %1f     %1.2f      %1.4f        %5.3f         %5.3f       %5.3f  ║"
            % (i + 1, intArrivalTime[i], arrivalTime[i], serviceTime[i], SBT[i], waitingTime[i], SET[i],
               customerSpendInSystem[i], idleTime[i]))


print(" \t\t\t\t\t\t\t  =%4i    =%.5f   \t\t\t\t=%3.2f \t\t\t\t\t  =%4.2f     \t=%3.3f "% (total_arrivalTime, total_serviceTime, total_waitingTime, total_spendTime, total_idleTime))


print(green + "\n\n[+]" + reset_color + " Average waiting time, (%f / %i) = %.2f" % (total_waitingTime, n, float(total_waitingTime) / n))
print(green + "[+]" + reset_color + " Average service time, (%f / %i) = %.2f" % (total_serviceTime, n, float(total_serviceTime / n)))
print(green + "[+]" + reset_color + " Average time between arrival, (%i / %i) = %.2f" % (total_arrivalTime, (n - 1), float(total_arrivalTime / (n - 1))))
print(green + "[+]" + reset_color + " Average time customer spends in the system, (%f / %i) = %.2f" % (total_spendTime, n, float(total_spendTime / n)))
if wait_count != 0:
    print(green + "[+]" + reset_color + " Probability(wait), (%i / %i) = %.2f" % (wait_count, n, float(wait_count / n)))
    print(green + "[+]" + reset_color + " Average waiting time of those who wait, (%f / %i) = %.2f" % (total_waitingTime, wait_count, float(total_waitingTime / wait_count)))
else:
    print(red + "[-]" + reset_color + " Probability(wait), (%i / %i) = Zero or Not Countable" % (wait_count, n))
    print(red + "[-]" + reset_color + " Average waiting time of those who wait, (%f / %i) = Zero or Not Countable" % (total_waitingTime, wait_count))
if idel_count != 0:
    print(green + "[+]" + reset_color + " Probability of idle server, (%f / %i) = %.2f" % (total_idleTime, idel_count, float(total_idleTime / idel_count)))
else: print(red + "[-]" + reset_color + " Probability of idle server, (%f / %i) = Zero or Not Countable" % (total_idleTime, idel_count))
print("\n\n\n\n")

-------------------------------------------------------------------------------------------------
|  Customer No  |  Interarrival Time  |  Arrival Time   |  Service Time      |  Service Time Begin  |  Service Time End  |  Waiting Time  |  Time Spend in System   |  Server Idle Time  |
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
|	 1 	    |		 0 	    |	 0 		|	 5.76 		|	  0.00 	   |		5.76	    |	  0.00 	|		5.76   	|	0.00 		|
|	 2 	    |		 8 	    |	 8 		|	 5.15 		|	  8.00 	   |		13.15	    |	  0.00 	|		5.15   	|	2.24 		|
|	 3 	    |		 8 	    |	 16 		|	 6.58 		|	  16.00 	   |		22.58	    |	  0.00 	|		6.58   	|	2.85 		|
|	 4 	    |		 6 	    |	 22 		|	 5.03 		|	  22.58 	   |		27.61	    |	  0.58 	|		5.61   	|	0.00 		|
|	 5 	    |		 5 	    |	 27 		|	 5.0 		|	  27.61 	   |		32.61	    |	  0.61 	|		5.61   	|	0.00 		|
|	 6 	    |		 3 	    |	 30 		|	 5.13 		|	  32.61 	   |		37.74	    |	  2.61 	|		7.74   	|	0.00 		|
|	 7 	    |		 8 	    |	 38 		|	 5.6 		|	  38.00 	   |		43.60	    |	  0.00 	|		5.60   	|	0.26 		|
|	 8 	    |		 3 	    |	 41 		|	 5.16 		|	  43.60 	   |		48.76	    |	  2.60 	|		7.76   	|	0.00 		|
|	 9 	    |		 3 	    |	 44 		|	 5.2 		|	  48.76 	   |		53.96	    |	  4.76 	|		9.96   	|	0.00 		|
|	 10 	    |		 5 	    |	 49 		|	 5.21 		|	  53.96 	   |		59.17	    |	  4.96 	|		10.17   	|	0.00 		|
|	 11 	    |		 3 	    |	 52 		|	 5.45 		|	  59.17 	   |		64.62	    |	  7.17 	|		12.62   	|	0.00 		|
|	 12 	    |		 3 	    |	 55 		|	 5.65 		|	  64.62 	   |		70.27	    |	  9.62 	|		15.27   	|	0.00 		|
|	 13 	    |		 5 	    |	 60 		|	 5.48 		|	  70.27 	   |		75.75	    |	  10.27 	|		15.75   	|	0.00 		|
|	 14 	    |		 5 	    |	 65 		|	 5.72 		|	  75.75 	   |		81.47	    |	  10.75 	|		16.47   	|	0.00 		|
|	 15 	    |		 5 	    |	 70 		|	 5.21 		|	  81.47 	   |		86.68	    |	  11.47 	|		16.68   	|	0.00 		|
|	 16 	    |		 3 	    |	 73 		|	 5.12 		|	  86.68 	   |		91.80	    |	  13.68 	|		18.80   	|	0.00 		|
|	 17 	    |		 5 	    |	 78 		|	 5.1 		|	  91.80 	   |		96.90	    |	  13.80 	|		18.90   	|	0.00 		|
|	 18 	    |		 9 	    |	 87 		|	 5.27 		|	  96.90 	   |		102.17	    |	  9.90 	|		15.17   	|	0.00 		|
|	 19 	    |		 3 	    |	 90 		|	 5.01 		|	  102.17 	   |		107.18	    |	  12.17 	|		17.18   	|	0.00 		|
|	 20 	    |		 1 	    |	 91 		|	 5.39 		|	  107.18 	   |		112.57	    |	  16.18 	|		21.57   	|	0.00 		|
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
|	Sum: 	    |		= 91 	    |			|	= 107.22 	|			   |			    |	= 131.13 	|		= 238.35 	|	= 5.35   	|
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
Average Waiting Time:  6.56
Average Time Spend in System:  11.92
Average Time Between Arrival:  4.79
Average Service Time:  5.36
The probability of the server being idle:  0.05
