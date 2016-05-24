
import sys

def parse_quotes(fn):
    """Generates pairs of (quote, author)"""
    with open(fn) as quotefile:
        for line in quotefile:
            columns = tuple(line.strip().split('\t'))
            assert len(columns) == 2
            yield columns


if __name__ == '__main__':
    for quote, author in parse_quotes(sys.argv[1]):
        print(quote, author)
