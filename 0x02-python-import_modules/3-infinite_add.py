#!/usr/bin/python3
if __name__ == "__main__":
    def main():
        import sys
        n = len(sys.argv)
        result = 0
        for i in range(1, n):
            result = result + int(sys.argv[i])
        print(result)
    main()
