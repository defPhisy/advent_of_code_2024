import re
import utils


def main():
    # get single string from memory.txt
    memory_txt = utils.get_text(utils.FILE_PATH)

    # find and extract all valid number pairs as tuples in a list
    muls = re.findall(utils.MUL_PATTERN, memory_txt)

    # calculate the sum of all valid multiplication pairs
    total = utils.calculate_sum(muls)

    # CORRECT RESULT = 178886550
    print(total)


if __name__ == "__main__":
    main()
