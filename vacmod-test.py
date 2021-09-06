from raepy import VacuumModule
warmup = False
if __name__ == "__main__":
    v = VacuumModule()
    if warmup:
        v.warmup()
        print("warumup-done")
    v.suck(v.print_state,v.print_state)