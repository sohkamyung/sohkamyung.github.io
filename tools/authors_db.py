#!/usr/bin/env python

# update authors database with entries from incoming markdown file

# parses entries from
# - on-line short stories
# - (todo) short stories from magazines
# - (todo) short stories in anthologies and collections
# - (todo) fiction books
# - (todo) non-fiction books

# uses entries to generate / update these databases:
# - (todo) grouped by author:
#   - (todo) short stories titles, by author
#   - (todo) fiction books, by author
#   -  (todo) non-fiction books, by author

# generates these markdown indexes from the databases:
# - (todo) grouped by author:
#   - (todo) short stories titles
#   - (todo) fiction books
#   - (todo) non-fiction books

import argparse
import re
import sys

def process_file(args) -> int:
    print(f"Processing file {args.file}");
    return 0

if __name__ == '__main__':
    parser = argparse.ArgumentParser(
	description="Update authors database with entries from incoming file"
    )
    parser.add_argument(
        '-d', '--debug', action = 'store_true',
	help = "Print debugging info")
    parser.add_argument(
        "file",
        help = "Markdown File to process")
    args = parser.parse_args()

    sys.exit(process_file(args))
