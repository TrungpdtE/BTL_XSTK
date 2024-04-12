#1.1
import statistics

Data = [11, 13, 23, 27, 29]
print("Data: ", Data)
OutputOfMean = statistics.mean(Data)
print("mean của Data: ", OutputOfMean)
print()

#1.2
import statistics

Data = [11, 13, 23, 27, 29]
print("Data: ", Data)
OutputOfFmean2 = statistics.fmean(Data)
print("fmean của Data: ", OutputOfFmean2)
print()
#1.3/
import statistics
Data = [3,4,6,8,11,15,20,23,33]
print("Data: ", Data)
OutputOfMedian = statistics.median(Data)
print("median của Data: ", OutputOfMedian)
print()

#1.4/
import statistics
Data = [3,4,6,8,11,15,20,23,33]
print("Data: ", Data)
geometric_mean = statistics.geometric_mean(Data)
print("geometric_mean của Data: ", geometric_mean)
print()

#1.5/
import statistics
Data = [3,4,6,8,11,15,20,23,33]
print("Data: ", Data)
OutputOfHarmonicMean1 = statistics.harmonic_mean(Data)
print("Tính harmonic mean của Data: ", OutputOfHarmonicMean1)
print()

#1.6/
import statistics
Data = [3,4,6,8,11,15,20,23,33]
print("Data: ", Data)
result_5 = statistics.median_low(Data)
print("median low của Data: ", result_5)
print()

#1.7/
import statistics
data = [3,4,6,8,11,15,20,23,33]
print("Data: ", Data)
OutputOfMedanHigh = statistics.median_high(Data)
print("Tính giá trị của median high: ", OutputOfMedanHigh)
print()

#1.8/
import statistics
Data = [33,33.1,34,35,35.2,33.4]
print("Data: ", Data)
OutputOfMedianGrouped1 = statistics.median_grouped(Data)
print("median groupe của Data: ", OutputOfMedianGrouped1)
print()

#1.9/
import statistics
Data = [10,23,33,19,10,90,10,23,90,10]
print("Data: ", Data)
OutputOfMode = statistics.mode(Data)
print("mode của Data1: ", OutputOfMode)
print()

#1.10/
import statistics

Data = ["Facebook", "Youtube", "Twitter", "Zalo", "Youtube", "Twitter", "Twitter"]
print("Data: ", Data)
OutputOfMultiMode = statistics.multimode(Data)
print("multimode của Data: ", OutputOfMultiMode)
print()

#1.11/
import statistics

Data = [5,10,15,20,25,30,35]
print("Data: ", Data)
OutputOfQuantiles = statistics.quantiles(Data,n=4)
print("Quantiles của Data và n=4: ", OutputOfQuantiles)
print()

#1.12/
import statistics

Data = [1.75, 1.5, 0.2, 0.75, 5.5]
print("Data: ", Data)
OutputOfPstdev = statistics.pstdev(Data)
print("Pstdev của Data: ", OutputOfPstdev)
print()


#1.13/
import statistics

Data = [1.75, 1.5, 0.2, 0.75, 5.5]
print("Data: ", Data)
OutputOfPvariance = statistics.pvariance(Data)
print("Pvariance của Data: ", OutputOfPvariance)
print()


#1.14/
import statistics

Data = [1.75, 1.5, 0.2, 0.75, 5.5]
print("Data: ", Data)
OutputOfStdev = statistics.stdev(Data)
print("Stdev của Data: ", OutputOfStdev)
print()

#1.15/
import statistics

data = [5,10,15,20,25,30,35]
print("Data: ", Data)
OutputOfVariance = statistics.variance(Data)
print("Variance của Data: ", OutputOfVariance)
print()


#1.16/
import statistics

x = [1,6,5,9,7,2]
y = [22,18,9,6,8,11]
print("x: ", x)
print("y: ", y)
OutputOfCovariance = statistics.covariance(x,y)
print("Covariance của x,y: ", OutputOfCovariance)
print()

#1.17/
import statistics

x = [8,9,7,15,18,10,20,1]
y = [22,18,9,6,8,11,19,5]
print("x: ", x)
print("y: ", y)
OutputOfCorrelation = statistics.correlation(x, y)
print("Correlation của x,y: ", OutputOfCorrelation)
print()

#1.18/
import statistics

x = [2,3,4,5,6,7,8]
y = [3,4,5,6,7,8,9]
print("x: ", x)
print("y: ", y)
OutputOfLinearRegression = statistics.linear_regression(x, y)
print("Linear Regression của x,y: ",OutputOfLinearRegression)
print()