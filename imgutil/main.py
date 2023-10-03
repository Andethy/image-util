from imgutil.controller import FunctionController


class Main:

    def __init__(self):
        self.controller = FunctionController()

    def menu_loop(self):
        print("Welcome to image util!")
        while True:
            print("---Enter one the following:\n"
                  "[1] Compress Images in a given directory\n"
                  "[0] Exit program")
            x = int(input())
            if x == 0:
                break;
            elif x == 1:
                self.controller.compress()



if __name__ == '__main__':
    m = Main()
    m.menu_loop();
