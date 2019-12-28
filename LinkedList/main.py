from methods import *
import time
import matplotlib.pyplot as plt
import statistics

# Read, tokenize and insert words in the set and print the set size
print("Conducting Adding Time Experiment")
Total_Add_Average = []
for i in range(10):
    with open('pride-and-prejudice.txt', 'r', encoding="utf-8") as f:
        new_list = LinkedList()
        add_time = []
        num_words = []
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        for line in f:
            for x in line.lower():
                if x in punctuations:
                    line = line.replace(x, " ")
            for x in line.split():
                start_time = time.time()
                added = new_list.add(x)
                end_time = time.time()
                if added:
                    add_time.append((end_time - start_time) * (10**9))
                    num_words.append(new_list.size())
    Total_Add_Average.append(statistics.stdev(add_time))
    print("Experiment--", i+1)
    print("The size of the binary tree set is", new_list.size())
    print('The average time of adding an element is', statistics.mean(add_time), "nanoseconds")


# Print the number of words in the second file that are not in the previous set
# Do the experiment 10 times
print("Conducting Searching Time Experiment")
Total_Search_Average = []
for i in range(10):
    with open('words-shuffled.txt', 'r', encoding="utf-8") as f:
        count = 0
        search_time = []
        for line in f:
            for word in line.split():
                time1 = time.time()
                contains_result = new_list.contains(word)
                time2 = time.time()
                search_time.append(time2 - time1)
                if not contains_result:
                    count += 1
    Total_Search_Average.append(statistics.mean(search_time))
    print("Experiment--", i+1)
    print("The number of words that are not in the set is", count)
    print("the worst searching time is:", max(search_time) * 10 ** 9, "nanoseconds")
    print("the average searching time is:", statistics.mean(search_time) * 10 ** 9, "nanoseconds")
    print("the best searching time is:", min(search_time) * 10 ** 9, "nanoseconds")

plt.scatter(num_words, add_time)
plt.xlabel('number of words in the set')
plt.ylabel('time it takes to insert another word (nanoseconds)')
plt.ylim(0, 1250000)
plt.show()

print("========================================================================")
print("Summary:")
print("The average adding time for all 10 experiments is", statistics.mean(Total_Add_Average), "nanoseconds")
print("The standard deviation adding time for all 10 experiments is", statistics.stdev(Total_Add_Average), "nanoseconds")
print("The average searching time for all 10 experiments is", statistics.mean(Total_Search_Average) * 10 ** 9, "nanoseconds")
print("The standard deviation searching time for all 10 experiments is", statistics.stdev(Total_Search_Average) * 10 ** 9, "nanoseconds")
