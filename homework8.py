import threading
import random


numbers = []
list_ready = threading.Event()


def fill_list():
    global numbers
    print("T1: Filling the list has begun")
    numbers = [random.randint(1, 100) for _ in range(10_000)]
    print("T1: The list is full.")
    list_ready.set()

def calculate_sum():
    list_ready.wait()
    print("T2: The calculation of the amount has begun")
    total_sum = sum(numbers)
    print(f"T2: Sum of list elements = {total_sum}")
    return total_sum


def calculate_average():
    list_ready.wait()
    print("T3: The calculation of the average has begun")
    average = sum(numbers) / len(numbers)
    print(f"T3: Arithmetic mean = {average:.2f}")
    return average


def main():
    thread1 = threading.Thread(target=fill_list)
    thread2 = threading.Thread(target=calculate_sum)
    thread3 = threading.Thread(target=calculate_average)
    thread1.start()
    thread2.start()
    thread3.start()
    thread1.join()
    thread2.join()
    thread3.join()

    print("All threads have completed execution.")

if __name__ == "__main__":
    main()