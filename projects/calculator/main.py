import sys
import os
# from projects.calculator.controler import Controller

if __name__ == "__main__":
    print("run controler")
    # Controller().run()
    x = os.getcwd() + "\\database"
    
    sys.path.append(x)

    print(sys.path)

