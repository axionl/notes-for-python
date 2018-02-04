import gc
import waste_memory

def find_in_memory():
    found_objects = gc.get_objects()
    print('%d objects before' % len(found_objects))

def check_waste_memory():
    x = waste_memory.run()
    found_objects = gc.get_objects()
    print('%d objects after' % len(found_objects))
    for obj in found_objects[:3]:
        print(repr(obj)[:100])

def main():
    find_in_memory()
    check_waste_memory()
    pass

if __name__ == '__main__':
    main()
