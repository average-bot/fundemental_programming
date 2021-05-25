import sys

def read_file(filename):
    numberfile = open(filename, 'r')
    for i in numberfile:
        line = numberfile.readlines()

def main():
    file1 = sys.argv[1]
    file2 = sys.argv[2]
    #num_list1 = read_file(file1)
    #num_list2 = read_file(file2)



    file1.close()
    file2.close()
main()