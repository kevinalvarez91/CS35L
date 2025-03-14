#!/usr/bin/python
import sys
import random
import argparse

class Shuf:
    def __init__(self, echo_input=None, filename=None):
        """
        Initialize the Shuf object.
        - If echo_input is provided, use that as the input lines.
        - Else if filename is provided (and not '-'), read lines from file.
        - Else if filename == '-', read from stdin.
        - Otherwise, self.lines remains empty (handled later if needed).
        """
        self.lines = []
        if echo_input is not None:
            # Convert each item to string (in case they're not already)
            self.lines = [str(x) for x in echo_input]
        elif filename and filename != "-":
            try:
                with open(filename, 'r') as f:
                    # Strip trailing newlines so that we can print cleanly
                    self.lines = [line.rstrip('\n') for line in f]
            except FileNotFoundError:
                print("Error: File not found.")
                sys.exit(1)
        elif filename == "-":
            # Read from stdin
            self.lines = [line.rstrip('\n') for line in sys.stdin]

    def e(self, echo_input):
        """
        Set self.lines to the echo_input, but do NOT print here.
        """
        self.lines = [str(x) for x in echo_input]

    def i(self, i_input):
        """
        Parse a range of the form START-END, populate self.lines with
        that integer range as strings. Do NOT shuffle or print here.
        """
        try:
            start, end = map(int, i_input.split('-'))
            self.lines = [str(x) for x in range(start, end + 1)]
        except ValueError:
            print("Error: Invalid input range.")
            sys.exit(1)

    def n(self, count, repeat=False):
        """
        Print output lines limited to 'count'.
        If 'repeat' is True, choose lines with replacement;
        otherwise, use random.sample (without replacement).
        """
        if not self.lines:
            print("Error: No lines available to output.")
            return

        if repeat:
            # With repetition, we can always print exactly 'count' lines
            for _ in range(count):
                print(random.choice(self.lines))
        else:
            # Without repetition, if count > number of lines,
            # we only print the available lines (as GNU shuf does).
            if count > len(self.lines):
                count = len(self.lines)
            for item in random.sample(self.lines, count):
                print(item)

    def r(self, count=None):
        """
        Repeated mode. If count is given, print exactly that many lines (with repetition).
        If no count, print infinitely (until a pipe breaks or user cancels).
        """
        if not self.lines:
            print("Error: No lines to repeat.")
            return
        if count is not None:
            self.n(count, repeat=True)
        else:
            # Infinite repetition
            try:
                while True:
                    print(random.choice(self.lines))
            except BrokenPipeError:
                # This occurs if output is piped and the pipe closes.
                pass

    def default(self):
        """
        Default behavior (no -n, no -r specified): shuffle all lines once, then print them.
        """
        random.shuffle(self.lines)
        for item in self.lines:
            print(item)

def main():
    parser = argparse.ArgumentParser(
        description="This program implements the GNU shuf program (limited functionality).",
    )
    parser.add_argument(
        "-e", "--echo",
        nargs="+",
        help="Echo the provided items as input instead of reading from a file or stdin."
    )
    parser.add_argument(
        "-i", "--input-range",
        type=str,
        help="Specify a range of integers as START-END (e.g. 1-10)."
    )
    parser.add_argument(
        "-n", "--head-count",
        type=int,
        help="Output at most this many lines."
    )
    parser.add_argument(
        "-r", "--repeat",
        action="store_true",
        help="Allow repetition of output lines."
    )
    parser.add_argument(
        "input_file",
        nargs="?",
        default=None,
        help="Optional input file or '-' for standard input."
    )

    args = parser.parse_args()

    # Ensure the user isn't mixing multiple input modes:
    # e.g., -e with -i, or with an input_file, etc.
    input_modes = sum(bool(x) for x in [args.echo, args.input_range, args.input_file])
    if input_modes > 1:
        parser.error("Cannot combine -e, -i, and an input file in one command.")

    # Create the Shuf object appropriately
    # We'll initialize with nothing, then call the right method,
    # unless we have an input_file, in which case we read it in directly.
    shuf = Shuf()

    if args.echo:
        # If user gave -e, use that
        shuf.e(args.echo)
    elif args.input_range:
        # If user gave -i, parse that range
        shuf.i(args.input_range)
    else:
        # Otherwise, read from a file (or stdin if '-' or no file given)
        shuf = Shuf(filename=args.input_file)

    # Now decide how to produce the final output
    if args.repeat:
        # If we are repeating
        if args.head_count is not None:
            # Finite repeated lines
            shuf.r(args.head_count)
        else:
            # Infinite repeated lines
            shuf.r()
    else:
        # Not repeating
        if args.head_count is not None:
            shuf.n(args.head_count, repeat=False)
        else:
            # Default (shuffle once and print all)
            shuf.default()

if __name__ == "__main__":
    main()
