from zeep import Client

def Main():
    client = Client('http://127.0.0.1:5000/verScore')

if __name__ == '__main__':
    Main()
