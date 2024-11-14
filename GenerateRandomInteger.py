# import random
# random_numbers = random.randint(1,10)
# print(random_numbers)

import time
seed = int(time.time()*1000000)
random_numbers= (seed%10)+1
print(random_numbers)