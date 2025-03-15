
def count_lines_in_file(file_path):
    try:
        with open(file_path, 'r') as file:
            lines = file.readlines()
            return len(lines)
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' does not exist.")
        return 0
    except Exception as e:
        print(f"An error occurred: {e}")
        return 0

file_path = input("Enter the path of the file: ")
line_count = count_lines_in_file(file_path)
if line_count > 0:
    print(f"The file contains {line_count} lines.")
