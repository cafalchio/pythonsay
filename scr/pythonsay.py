import argparse
import sys
from pythonsay import draws

def main():
    """Main function"""
    
    parser = argparse.ArgumentParser()
    parser.add_argument("-c", "--cow", help="Print a cow", action="store_true")
    parser.add_argument("-py", "--python", help="Print a python", action="store_true")
    parser.add_argument("-pb", "--big", help="Print a big python", action="store_true", default=False)
    parser.add_argument("phrase", help="Print a phrase", nargs="?")
    ## Read arguments from the command line
    args = parser.parse_args()
    if args.cow:
        draws.cowsay(args.phrase if args.phrase else draws.random_cow_prases())
    elif args.python or args.big:
        draws.pythonsay(args.phrase if args.phrase else draws.random_python_prases(), args.big)
    else:   
        print('Please enter a valid argument\n')
        parser.print_help()
        sys.exit(0)



if __name__ == "__main__":
    main()