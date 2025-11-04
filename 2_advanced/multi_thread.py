import threading


def calculate_square():
    for i in range(1, 10):
        square = i ** 2
        print(f"T1 Le carré de {i} est : {square}")


def calculate_cube():
    for i in range(1, 10):
        cube = i ** 3
        print(f"T2 Le cube de {i} est : {cube}")


if __name__ == "__main__":
    square_thread = threading.Thread(target=calculate_square)
    cube_thread = threading.Thread(target=calculate_cube)
    square_thread.start()
    cube_thread.start()
    square_thread.join()
    cube_thread.join()