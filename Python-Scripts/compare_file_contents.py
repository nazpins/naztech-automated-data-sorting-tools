import filecmp

def compare_files(file1, file2):
    if filecmp.cmp(file1, file2):
        print("The files are identical.")
    else:
        print("The files are different.")

if __name__ == '__main__':
    file1 = input("Enter the path to the first file: ")
    file2 = input("Enter the path to the second file: ")
    compare_files(file1, file2)