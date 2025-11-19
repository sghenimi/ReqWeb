import time


def do_task_sync(n):
    print(f"# start task {n}")
    time.sleep(2)
    print(f"# End task {n}")


def sync_main():
    start = time.perf_counter()
    do_task_sync(1)
    do_task_sync(2)
    end = time.perf_counter()
    print(f"--> Taken : {end-start}")


sync_main()
