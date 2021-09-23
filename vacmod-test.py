from raepy import VacuumModule
from signal import signal, SIGINT
import time

warmup = False

def handler(signal_received, frame):
    v.release()
    exit(0)

if __name__ == "__main__":
    signal(SIGINT, handler)
    v = VacuumModule()
    if warmup:
        v.warmup()
        print("warumup-done")

    v.suck(v.print_state,v.print_state)
    time.sleep(10)
    v.release()

