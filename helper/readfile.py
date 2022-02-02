
#FOR SMALL FILES
def read_file(path):
    with open(path, 'r') as file:
        text = file.read()
    
    return text