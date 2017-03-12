import sys
import random
random.randint(1, 10)
count = int(sys.argv[1])
for x in range(0, count):
    randomized_start_time = random.randint(1, count*100)
    print(str(randomized_start_time) + " " + str(randomized_start_time +random.randint(1, count*100)) + " " + str(random.randint(1, count/10)))
