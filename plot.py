import random
import matplotlib.pyplot as plt
import calcMemoryTime, time
import inputStringGenerator
import sequenceAlignmentBasic
import sequenceAlignmentMemoryOptimized


def generate_input():
    vals = ['A', 'C', 'G', 'T']

    with open('input.txt', 'w') as inp:
        ini_str = ''
        for i in range(random.randint(2, 5)):
            index = random.randint(0, 3)
            ini_str += vals[index]
        inp.write(ini_str)

        for i in range(1, random.randint(2, 8)):
            inp.write('\n' + str(random.randint(1, i*len(ini_str) - 1)))

        ini_str = ''
        for i in range(random.randint(2, 5)):
            index = random.randint(0, 3)
            ini_str += vals[index]
        inp.write('\n' + ini_str)

        for i in range(1, random.randint(2, 8)):
            inp.write('\n' + str(random.randint(1, i * len(ini_str) - 1)))


cost_dict = {}
for i in range(25):
    time.sleep(.5)
    generate_input()
    s1, s2 = inputStringGenerator.get_input_string(r'input.txt')
    length = len(s1)+len(s2)
    time1, memory1, res = calcMemoryTime.run(sequenceAlignmentBasic.run, s1, s2)
    time2, memory2, res = calcMemoryTime.run(sequenceAlignmentMemoryOptimized.run, s1, s2)
    cost_dict[length] = ((time1, time2), (memory1, memory2))

keys = sorted(cost_dict)
t1 = []
t2 = []
m1 = []
m2 = []
for key in keys:
    t1.append(cost_dict[key][0][0])
    t2.append(cost_dict[key][0][1])
    m1.append(cost_dict[key][1][0])
    m2.append(cost_dict[key][1][1])
print(cost_dict)
print(t1,t2,m1,m2)
plt.plot(keys, m1, label='Basic')
plt.plot(keys, t2, label='Optimized')
plt.legend()
plt.show()
