# Simulation & Modeling Sessional

# Group_07
   1. Mohimul Hoque(CSE-01205958) [Team Leader]
   2. Kutub Uddin Radin(CSE-01306153)
   3. Shafiqul Islam(CSE-01206037)
   4. Suva Dev Showrv(CSE-01205974)
   5. Trisha Dhar(CSE-01205991)
   6. Salma Akter(CSE-01206041)
   
# Course Instructor: 

Mr. Muhtadir Rahman

Lecturer, Department of CSE

Port City International University

# Single-Channel-Queue-System:
## What is Discrete Variable?

Discrete variables are countable in a finite amount of time. For example, we can count the change in our pocket. we can count the money in your bank account. we could also count the amount of money in everyone’s bank accounts. It might take us a long time to count that last item, but it’s still countable.

 ![image](https://user-images.githubusercontent.com/41919560/114293331-0811a980-9ab7-11eb-9c90-9c0e812a05e2.png)


 ## What is Continuous Variable?
 
Continuous variables can take on an unlimited number of values between the lowest and highest points of measurement. Continuous variables include such things as speed and distance.

![image](https://user-images.githubusercontent.com/41919560/114313496-923e2a00-9b18-11eb-8288-a48fc566ca0e.png)



## What is Probability Distribution?
A probability distribution is a function that describes the likelihood of obtaining the possible values that a random variable can assume. In other words, the values of the variable vary based on the underlying probability distribution. Poisson Distribution and Exponential Distribution are among the other types of probability distribuiton.

![image](https://user-images.githubusercontent.com/41919560/114313942-7a67a580-9b1a-11eb-829f-cfd67905a498.png)


## What is a Single Channel Queuing System?
A single-channel service system consisting of a service facility and queue, in which the possible times of arrival of units and the possible service times are discrete, is analyzed. A method of calculating the moments of the total service time of units in the system is developed. This total service time is related to the delay caused by the system. When arrivals at different times are assumed to be independent, the “values” of the resulting Markov process can be calculated. 


These values lead to information about the transient behavior, autocorrelation function, expected first passage time, and expected extra delay that arises if another unit is inserted into the system. An expression for the geometric transform or moment generating function of the probability distribution of the total service time of units in the system is determined. The results are derived for arbitrary arrival and service time distributions.


![image](https://user-images.githubusercontent.com/41919560/114314302-e565ac00-9b1b-11eb-9d17-d283168ef049.png)



## Brief Introduction to Poisson Distribution and why it used:-
A Poisson distribution is a tool that helps to predict the probability of certain events from happening when you know how often the event has occurred. It gives us the probability of a given number of events happening in a fixed interval of time.
![image](https://user-images.githubusercontent.com/41919560/113600536-f9b03180-9661-11eb-9b9d-0327ce1434eb.png)
Poisson distributions, valid only for integers on the horizontal axis. λ (also written as μ) is the expected number of event occurrences. If we want to calculate the poisson Distribution

pmf is: P(x; μ) = (e-μ * μx) / x!

Where: • The symbol “!” is a factorial. • μ (the expected number of occurrences) is sometimes written as λ. Sometimes called the event rate or rate parameter.

In general, Poison distribution works with a discrete value. As we know inter-arrival time does not occur in sequential manner, it works randomly. Thus poisson distribution are used for that.

## Brief Introduction to Exponential Distribution and why it used:-
The exponential distribution is often concerned with the amount of time until some specific event occurs. For example, the amount of time (beginning now) until an earthquake occurs has an exponential distribution. Other examples include the length, in minutes, of long distance business telephone calls, and the amount of time, in months, a car battery lasts. It can be shown, too, that the value of the change that you have in your pocket or purse approximately follows an exponential distribution.

Exponential Distribution deals with the time between occurrences of successive events as we know time flows continuously and in this project the starting and the ending of service can be considered as two successive events.


![image](https://user-images.githubusercontent.com/41919560/114314154-56589400-9b1b-11eb-849c-3e88867a385b.png)




## QUICK LINK:
https://www.statisticshowto.com/probability-and-statistics/statistics-definitions/discrete-vs-continuous-variables/
https://www.sciencedirect.com/topics/computer-science/continuous-variable
https://www.investopedia.com/terms/p/probabilitydistribution.asp
https://www.researchgate.net/publication/255684386_Stationary_characteristics_of_a_single-channel_queuing_system_with_one_waiting_space




## [ Note: here I used 'POISSON DISTRIBUTION' for Inter Arrival Time generation & I used 'EXPONENTIAL DISTRIBUTION' for service time generation]
