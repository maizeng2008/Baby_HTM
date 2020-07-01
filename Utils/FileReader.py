TEST_FILE_BUNDLE_1 = ('./Test/Instruction_Test.txt', './Results/Results.txt')
TEST_FILE_BUNDLE_2 = ('./Test/Instruction_Test_2.txt', './Results/Results_2.txt')
TEST_FILE_BUNDLE_3 = ('./Test/Instruction_Test_3.txt', './Results/Results_3.txt')


def read_instruction_test_file():
    file = open(TEST_FILE_BUNDLE_1[0], 'r')
    lines = file.readlines()
    file_write = open(TEST_FILE_BUNDLE_1[1], 'w')
    file_write.close()
    return [lines, file_write]
