

# for linux
# import getch

# for windows
# import msvcrt

if __name__ == '__main__':
    getch = getch_anywhere()
    s = ""
    for i in range(10):
        s += str(getch())
        print(i)

    print(s)
