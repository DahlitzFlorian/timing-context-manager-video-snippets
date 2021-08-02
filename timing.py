import contextlib
import time


class Timer:
    def __init__(self, description: str) -> None:
        self.description = description
    
    def __enter__(self):
        self.start = time.time()
    
    def __exit__(self, type, value, traceback):
        self.end = time.time()
        elapsed_time = self.end - self.start
        print(f"{self.description}: {elapsed_time}")


@contextlib.contextmanager
def measure_exec_time(description: str):
    start = time.time()
    yield
    end = time.time()

    elapsed_time = end - start
    print(f"{description}: {elapsed_time}")


with Timer("Class-based"):
    a = 5 + 5

with measure_exec_time("Generatpr-based"):
    a = 5 + 5
