def copy_file_contents(source_file, destination_file):
    try:
        with open(source_file, 'r') as src:
            content = src.read()

        with open(destination_file, 'w') as dest:
            dest.write(content)
        
        print(f"Content successfully copied from {source_file} to {destination_file}")
    
    except FileNotFoundError:
        print(f"Error: The file {source_file} was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")


source = 'source.txt'
destination = 'destination.txt'
copy_file_contents(source, destination)
