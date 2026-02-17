import sys


def main():
    print("Simple Calculator")
    print("1. CLI Mode")
    print("2. GUI Mode")
    
    choice = input("Select mode (1 or 2): ").strip()
    
    if choice == "1":
        from cli import main as cli_main
        sys.argv = ["cli.py"] + sys.argv[1:]
        cli_main()
    elif choice == "2":
        from gui import main as gui_main
        gui_main()
    else:
        print("Invalid choice. Please select 1 or 2.")
        sys.exit(1)


if __name__ == "__main__":
    main()