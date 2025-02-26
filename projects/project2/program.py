
from projects.project2.kbhit import KBHit
import time

def main():
    
    print("Hello, World!")

    kb = KBHit()

    print('Hit any key, or ESC to exit')

    iteration = 0

    while True:

        print(f'In loop: {iteration}')
        iteration += 1
        time.sleep(1)

        if kb.kbhit():
            key = (kb.getch())
            print(f'key you pressed is {key}')
            # c_ord = ord(c)
           # print(c)
            print(c_ord)
            time.sleep(2)
            if key.to_upper() == "Q": # ESC
                break
            print(c)


if __name__ == '__main__':
    main()
