# Function getnormal
# generate a list with 10 digits from normal distributions
import random
import numpy
import matplotlib.pyplot as plt
def getnormal(scale, sd, number):
    # return a list of random digits from normal distribution
    # scale is the mean of normal distribution
    # sd is the standard devision of normal distributon
    # number is the number of digits from normal distribution
    i=0
    listnormal=[]
    while i <= number:
        i = i + 1
        a=random. gauss(scale,sd)
        listnormal.append(a)
    return listnormal



# Funtion one way anova

def onewayanova (list1, list2, list3):
    from scipy import stats
    # list1, 2 ,3 are three lists
    # perform one way anova and return p value
    F, p=stats.f_oneway(list1, list2, list3)
    # this function generate F value and p value
    return p  



# Function do the getnormal and onewayanova several times

def severalanova (sa1, sd1, sa2, sd2, sa3, sd3, number123, numberrun):
    # sa1,sa2,sa3 means the mean of 1st, 2nd,and 3rd normal distribution respectively
    # sd1,sd2, sd3 means the standard deveriation of 1st, 2nd,and 3rd normal distribution respectively
    # number123 is the number of digits randomly chosen from normal distribution
    # numberrun is the number of times run one way anova
    # this funciton returns a list of p values of one way a anova
    in_i=0
    in_A=[]
    numberrun=numberrun-1
    while in_i<=numberrun:
        in_i = in_i +1
        inlist1= getnormal (sa1, sd1, number123)
        inlist2= getnormal (sa2, sd2, number123)
        inlist3= getnormal (sa3, sd3, number123)
        in_a=onewayanova(inlist1, inlist2, inlist3)
        in_A.append(in_a)
    return in_A

#Function do getnormal and onewayanova after normalizing to sample variance

def severalanova2(sa1, sd1, sa2, sd2, sa3, sd3, number123, numberrun):
    import statistics
    in_i=0
    in_A=[]
    numberrun=numberrun-1
    while in_i<=numberrun:
        in_i = in_i +1
        inlist1= getnormal (sa1, sd1, number123)
        inlist2= getnormal (sa2, sd2, number123)
        inlist3= getnormal (sa3, sd3, number123)
        variance1=statistics.pvariance(inlist1)
        ilist1=0
        while ilist1<len(inlist1):
            inlist1[ilist1]=float(inlist1[ilist1])/float(variance1)
            ilist1=ilist1+1
            
        variance2=statistics.pvariance(inlist2)
        ilist2=0
        while ilist2<len(inlist2):
            inlist2[ilist2]=float(inlist2[ilist2])/float(variance2)
            ilist2=ilist2+1
            
        variance3=statistics.pvariance(inlist3)
        ilist3=0
        while ilist3<len(inlist3):
            inlist3[ilist3]=float(inlist3[ilist3])/float(variance3)
            ilist3=ilist3+1
            
        in_a=onewayanova(inlist1, inlist2, inlist3)
        in_A.append(in_a)
    return in_A
    

# Function to calculate the percentage of numbers less than 0.05

def lessthan (listlessthan, alpha):
    # listlessthan5 is a list of numbers, alpha is a number 
    # this function returns percentage of numbers less than alpha
    lessthanlen=len (listlessthan)
    lessthan_i=0
    numberless=0.000
    while lessthan_i < lessthanlen:
        if listlessthan[lessthan_i]<alpha:
            numberless=numberless+1
        lessthan_i=lessthan_i+1
    percentage=numberless/lessthanlen
    return (percentage)


#A= severalanova (1,1,1,1,1,1,20,20)

# Function to plot the two lists

def plottwolists (listx, listy,xaxisrange, yaxisrange):
    # listx is the list for x-axis and listy is the list for y-axis
    # title is a string of title
    # x_axis, y_axis are two strings of x-axis title and y-axis respectively
    # this function will plot a scatter plot
    import matplotlib.pyplot as plt
    axes = plt.gca()
    axes.set_xlim(xaxisrange)
    axes.set_ylim(yaxisrange)
    plt.plot(listx, listy, marker='o', linestyle='-',color='r')
    plt.legend()
    plt.show()

#The following generating a list of numbers from 1 to 10, increasing by 0.2
#listA=numpy.arange (1, 10.01, 0.2)
#print listA

#A= severalanova (0, 1, 0, 1, 1, 1.5, 30, 1000)
#print A

#a= lessthan(A, 0.05)
#print 'a='
#print a

listofsd=numpy.arange(1, 3.01, 0.1)
# this generate 1 to 1.7 numbers, increasing by 0.1
i=0
powerlist=[]
# this is the list of p values
while i<len(listofsd):
    variance=listofsd[i]
    pvaluelist= severalanova (0, 1, 0, 1, 1, variance, 30, 1000)
    i=i+1
    power=lessthan(pvaluelist, 0.05)
    powerlist.append(power)

listofsdpoint=0
while listofsdpoint<len(listofsd):
    a=listofsd[listofsdpoint]
    listofsd[listofsdpoint]=a*a
    listofsdpoint+=1
    
print listofsd

print powerlist

plottwolists (listofsd, powerlist, [0.9,9.1], [0, 1])






