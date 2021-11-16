from test_framework import generic_test


def snake_string(s: str) -> str:
    # TODO - you fill in here.
    # return ''
    # snake=['']*len(s)
    # i=0
    # while 4*i+1 <len(s):
    #     snake.append(s[4*i+1])
    #     i+=1
    # i = 0
    # while 2*i < len(s):
    #     snake.append(s[2*i])
    #     i+=1
    # i = 0
    # while 4 * i + 3 < len(s):
    #     snake.append(s[4 * i + 3])
    #     i+=1
    # return ''.join(snake)

    return s[1::4] + s[::2] + s[3::4]

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('snake_string.py', 'snake_string.tsv',
                                       snake_string))
