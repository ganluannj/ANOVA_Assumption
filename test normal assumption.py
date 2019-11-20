import numpy
import matplotlib.pyplot as plt
import matplotlib.mlab as mlab
import scipy.stats as stats
import random

def pdf (x, pdfmean, uniformvalue):
    #print uniformvalue
    return (1-uniformvalue)*stats.norm.pdf(x-pdfmean)+0.289*uniformvalue

def findminandmax(mean,uniformvalue1):
    # this function is to find the minimum and maximum value of a pdf
    # pdf is the pdf, range1 is the range
    # this function return a list with minimun and maximum
    minx=100000
    maxx=0
    rangen=[-1.732+mean, 1.732+mean]
    listofrange=numpy.arange(rangen[0], rangen[1],0.01)
    listpoint=0
    returnlist=[]
    while listpoint<len(listofrange):
        number=listofrange[listpoint]
        if pdf(number,mean,uniformvalue1)< minx:
            minx=pdf(number,mean,uniformvalue1)
        if pdf(number,mean,uniformvalue1)>maxx:
            maxx=pdf(number,mean, uniformvalue1)

        listpoint=listpoint+1

    returnlist.append(minx)
    returnlist.append(maxx)
    return returnlist


def getmix (mean, mixfactor, number, minofy, maxofy):
    # return a list of random digits from mix distribution of normal and unform distribution
    # mean is the overall mean
    # variance is 1
    # number is the number of digits from normal distribution
    #minofy=findminandmax(mean,mixfactor)[0]
    #maxofy=findminandmax(mean,mixfactor)[1]
    timei=0
    returnlist1=[]
    while timei<number:
        x=numpy.random.uniform((-1.73-mean),(1.73+mean))
        y=numpy.random.uniform (minofy, maxofy)
        if y<pdf(x, mean, mixfactor):
            returnlist1.append(x)
            timei=timei+1
    return returnlist1



# Funtion one way anova

def onewayanova (list1, list2, list3):
    from scipy import stats
    # list1, 2 ,3 are three lists
    # perform one way anova and return p value
    F, p=stats.f_oneway(list1, list2, list3)
    # this function generate F value and p value
    return p


def severalanova (meanofnormal1,meanofnormal2,meanofmix,mixfactor2, number123,numberrun):
    in_i=0
    in_A=[]
    minofy1=findminandmax(meanofnormal1,0)[0]
    maxofy1=findminandmax(meanofnormal1,0)[1]
    minofy2=findminandmax(meanofnormal2,0)[0]
    maxofy2=findminandmax(meanofnormal2,0)[1]
    minofy3=findminandmax(meanofmix,0)[0]
    maxofy3=findminandmax(meanofmix,0)[1]
    while in_i<numberrun:
        in_i=in_i+1
        inlist1= getmix (meanofnormal1, 0, number123,minofy1, maxofy1)
        inlist2= getmix (meanofnormal2, 0, number123,minofy2, maxofy2)
        inlist3= getmix (meanofmix, mixfactor2, number123,minofy3, maxofy3)
        in_a=onewayanova(inlist1, inlist2, inlist3)
        in_A.append(in_a)
    return in_A

#print severalanova(0, 0, 0, 0.1, 30, 10)

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

listofmixfactor=numpy.arange(0.1, 0.51, 0.05)
i=0
powerlist=[]

while i< len(listofmixfactor):
    mixfactor3=listofmixfactor[i]
    pvaluelist=severalanova(0, 0, 0, mixfactor3, 30, 1000)
    i=i+1
    power=1-lessthan(pvaluelist, 0.05)
    powerlist.append(power)
    print listofmixfactor
    print powerlist

plottwolists (listofmixfactor, powerlist, [0.09,0.55],[0,1.05])





