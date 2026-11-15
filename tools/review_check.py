#!/usr/bin/env python3

###
# Script to check reviews
#
# - currently does nothing but returns true
###

import sys

def main():
    # pre-commit passes the list of matching filenames as arguments
    filenames = sys.argv[1:]

    print(f"Running pre-commit check. Received {len(filenames)} file(s):")
    for filename in filenames:
        print(f"  - {filename}")

    # Exit code 0 means success (returns true)
    sys.exit(0)

if __name__ == "__main__":
    main()
