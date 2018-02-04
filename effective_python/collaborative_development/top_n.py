import tracemalloc
import waste_memory

def main():
    tracemalloc.start(10)
    time1 = tracemalloc.take_snaphot()

    x = waste_memory.run()

    time2 = tracemalloc.take_snaphot()
    
    stats = time2.compare_to(time1, 'lineno')
    for stat in stats[:3]:
        print(stat)

if __name__ == '__main__':
    main()
