import os ## operating system interfaces

def main():
    filenames = os.listdir('/home/amirmasp/goo-py-ex/my_exercises')
    for filename in filenames:
        print(filename)
       






if __name__ == '__main__':
    main()