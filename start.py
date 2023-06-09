import argparse
import subprocess

def main():
    # Create argument parser
    parser = argparse.ArgumentParser(description="A simple command-line program to launch and mannage our application.")

    # Add arguments
    parser.add_argument("--test", action="store_true", help="Enable test mode")

    # Parse command line arguments
    args = parser.parse_args()

    # Access parsed arguments
    test_mode = args.test

    # Implement functionality based on passed arguments
    exe(args)

def exe(test_mode):
    result = subprocess.run("mosquitto -c mosquitto.conf -v" , stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, shell=True)
    

if __name__ == "__main__":
    main()