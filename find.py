import argparse
import logging
from functools import partial

def parse_arg():
    res = dict()

    parser = argparse.ArgumentParser()
    parser.add_argument("-p", "--pattern", help="e.g. pattern __A__, must size 5", default="?????")
    parser.add_argument("-e", "--exclude", help="must exclude", default="")
    parser.add_argument("-f", "--file", help="word list file", default="wordlist.txt")
    parser.add_argument("-o", "--output", help="word list output file", default="wordlist_filter.txt")
    args = parser.parse_args()

    res['p'] = str(args.pattern).lower()
    res['e'] = str(args.exclude).lower()
    res['f'] = args.file
    res['o'] = args.output

    if len(res['p']) != 5:
        parser.print_usage()
        exit()

    return res

def word_filter(target, character):
    if target == character:
        return True
    else:
        return False

def ex_filter(excluding, character):
    if character not in excluding:
        return True
    else:
        return False

def gen_filter(res):
    filters = []

    exclude = res['e']
    pattern = res['p']

    logging.info("pattern %s, exclude %s", pattern, exclude)

    for i in range(5):
        character = pattern[i]
        if not character.isalpha():
            fn = partial(ex_filter, exclude)
            filters.append(fn)
        else:
            fn = partial(word_filter, character)
            filters.append(fn)

    if len(filters) != 5:
        exit()

    return filters

def is_filter(w, filters):

    for i in range(5):
        char = w[i]
        filt = filters[i]
        if filt(char) is False:
            return False

    return True


def main():
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s %(levelname)s : %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S'
    )

    arg = parse_arg()
    wordfile = arg['f']
    outputfile = arg['o']
    filters = gen_filter(arg)

    found = []
    count = 0

    with open(wordfile, 'r') as fp:
        while True:
            line = fp.readline()
            if not line:
                break

            line = line.rstrip('\n')
            if len(line) != 5:
                logging.warning("word %s is not length 5 (%d)", line, len(line))
                continue

            if is_filter(line, filters):
                found.append(line)

            count += 1

    with open(outputfile, 'w') as fp:
        for word in found:
            fp.write(word + '\n')

    logging.info("Handled line %d found: %d", count, len(found))

if __name__ == '__main__':
    main()