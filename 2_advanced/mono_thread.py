shared_counter = 5


def calculate_square():
    global shared_counter 
    for i in range(10):
        square = i**2

        shared_counter = shared_counter + 1
        print(f"Le carré de {i} est : {square}")
    
    print("shared_counter :", shared_counter)


if __name__ == "__main__":
    calculate_square()
    print(shared_counter)
