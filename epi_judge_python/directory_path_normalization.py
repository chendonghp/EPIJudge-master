from test_framework import generic_test


def shortest_equivalent_path(path: str) -> str:
    # TODO - you fill in here.
    shortest_path=[]
    node=[]
    absolute=False
    for i,c in enumerate(path):
        if c=='/':
            if i==0:
                absolute=True
            else:
                if node ==['.','.']:
                    if shortest_path and shortest_path[-1]!='..':
                        shortest_path.pop()
                    else:
                        shortest_path.append('..')
                    node = []
                elif node == ['.']:
                    node=[]
                elif node:
                    shortest_path.append(''.join(node))
                    node=[]
        else:
            node.append(c)
    if node == ['.', '.']:
        if shortest_path and shortest_path[-1] != '..':
            shortest_path.pop()
        else:
            shortest_path.append('..')
    elif node == ['.']:
        pass
    elif node:
        shortest_path.append(''.join(node))
    if absolute:
        if shortest_path:
            shortest_path[0]='/'+shortest_path[0]
        else:
            shortest_path.append('/')
    return '/'.join(shortest_path)

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('directory_path_normalization.py',
                                       'directory_path_normalization.tsv',
                                       shortest_equivalent_path))
