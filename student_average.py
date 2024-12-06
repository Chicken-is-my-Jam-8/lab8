def main():
    input_file = input("Please enter a file name: ")
    print()
    student_average(input_file)

def student_average(file):
    line_num = count_lines(file)
    f = open(file, 'r')
    for x in range(line_num):
        total = 0
        count = 0
        s = f.readline()
        s = s.rstrip('\n')
        s_list = s.split(',')
        for y in s_list:
            total += int(y)
            count += 1
        print(s_list)
        print(f"Average: {total/count}")
    
def count_lines(file):
    try:
        f = open(file, 'r')
        s = f.read()
        lines = 0
        try:
            for x in s:
                if x.isdigit() == False and x != ',':
                    lines += 1
            return lines
        except Exception as E:
            print(f"Error: {E}")
        finally:
            f.close
    except FileNotFoundError:
        print("Error: file not found")
    except PermissionError:
        print("Error: insificient permission")
    except IsADirectoryError:
        print("Error: argument is a directory")
    except Exception as e:
        print(f"Error: {e}")
main()
