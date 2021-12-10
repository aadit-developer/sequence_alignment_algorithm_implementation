import calcMemoryTime
import inputStringGenerator
import sequenceAlignmentBasic, sequenceAlignmentMemoryOptimized

if __name__ == '__main__':
    path = r"D:\CS570-Algo\Project\BaseTestcases_CS570FinalProject_Updated\BaseTestcases_CS570FinalProject_Updated" \
           r"\input2.txt "
    s1, s2 = inputStringGenerator.get_input_string(path)

    print(calcMemoryTime.run(sequenceAlignmentBasic.run, s1, s2))
    print(calcMemoryTime.run(sequenceAlignmentMemoryOptimized.run, s1, s2))
