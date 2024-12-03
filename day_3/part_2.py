import re
import utils


def main():
    # get single string from memory.txt
    memory_txt = utils.get_text(utils.FILE_PATH)

    # find all start and end indexes for do() and don't()
    dos = list(re.finditer(utils.DO_PATTERN, memory_txt))
    donts = list(re.finditer(utils.DONT_PATTERN, memory_txt))

    # extract end indexes for do() and don't()
    do_ends = [do.end() for do in dos]
    dont_ends = [dont.end() for dont in donts]

    # create ranges for all do's
    do_ranges = utils.get_do_range(memory_txt, do_ends, dont_ends)

    # iterate only over do range
    total_sum = utils.calculate_in_range_of(memory_txt, do_ranges, utils.MUL_PATTERN)

    # CORRECT RESULT = 87163705
    print("RESULT: ", total_sum)


if __name__ == "__main__":
    main()
