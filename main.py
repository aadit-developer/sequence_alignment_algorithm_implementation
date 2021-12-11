import calcMemoryTime
import inputStringGenerator
import sequenceAlignmentBasic, sequenceAlignmentMemoryOptimized

if __name__ == '__main__':
    path = r"D:\CS570-Algo\Project\BaseTestcases_CS570FinalProject_Updated\BaseTestcases_CS570FinalProject_Updated" \
           r"\input1.txt "
    s1, s2 = inputStringGenerator.get_input_string(path)
    with open('output_basic.txt', 'w') as out:
        time, memory, res = calcMemoryTime.run(sequenceAlignmentBasic.run, s1, s2)
        out.write(res[0] + ' ' + res[1] + '\n')
        out.write(res[2] + ' ' + res[3] + '\n')
        out.write(res[4] + '\n')
        out.write(str(time) + '\n')
        out.write(str(memory))

    with open('output_memory_optimized.txt', 'w') as out:
        time, memory, res = calcMemoryTime.run(sequenceAlignmentMemoryOptimized.run, s1, s2)
        out.write(res[0] + ' ' + res[1] + '\n')
        out.write(res[2] + ' ' + res[3] + '\n')
        out.write(res[4] + '\n')
        out.write(str(time) + '\n')
        out.write(str(memory))
