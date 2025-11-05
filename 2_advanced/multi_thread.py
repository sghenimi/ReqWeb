import threading

shared_counter = 5


def calculate_square():
    global shared_counter
    for i in range(100):
        square = i**2
        shared_counter = shared_counter + 1
        print(f"T1 Le carré de {i} est : {square}")
    print("#T1 shared_counter :", shared_counter)


def calculate_cube():
    global shared_counter
    for i in range(100):
        cube = i**3
        shared_counter = shared_counter + 1
        print(f"T2 Le cube de {i} est : {cube}")
    print("#T2 shared_counter :", shared_counter)


if __name__ == "__main__":
    square_thread = threading.Thread(target=calculate_square)
    cube_thread = threading.Thread(target=calculate_cube)
    square_thread.start()
    cube_thread.start()
    square_thread.join()
    cube_thread.join()
