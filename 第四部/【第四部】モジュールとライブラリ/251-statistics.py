import statistics
import random

data = [random.randint(0, 1000) for _ in range(1000)]
print(data)

#平均値:mean
mean = statistics.mean(data)
print("平均値" , mean)

#中央値:median
median = statistics.median(data)
print("中央値", median)

#分散
variance = statistics.variance(data)
print("分散", variance)

#標準偏差
stdev = statistics.stdev(data)
print("標準偏差", stdev)