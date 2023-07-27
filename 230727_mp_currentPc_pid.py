import multiprocessing as mp


if __name__ == "__main__":
    proc = mp.current_process()
    print(proc.name)
    print(proc.pid)

# MainProcess
# 7672

# MainProcess
# 15012