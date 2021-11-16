from test_framework import generic_test


def ss_decode_col_id(col: str) -> int:
    # TODO - you fill in here.
    sum=0
    for s in col:
        sum=sum*26+ord(s)-ord('A')+1
    return sum


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('spreadsheet_encoding.py',
                                       'spreadsheet_encoding.tsv',
                                       ss_decode_col_id))
