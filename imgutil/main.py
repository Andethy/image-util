from imgutil.controller import FunctionController


class Main:

    def __init__(self):
        self.controller = FunctionController()

    def menu_loop(self):
        print("Welcome to image util!")
        while True:
            pass


if __name__ == '__main__':
    m = Main()
    m.menu_loop();
