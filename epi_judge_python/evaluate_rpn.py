from test_framework import generic_test


def evaluate(expression: str) -> int:
    # TODO - you fill in here.
    # return 0
    expr=expression.split(',')
    computation_stack=[]
    import operator
    ops={'+':operator.add,'-':operator.sub,'*':operator.mul,'/':operator.truediv}
    for op in expr:
        if op not in ops:
            computation_stack.append(int(op))
        else:
            r_op=computation_stack.pop()
            l_op=computation_stack.pop()
            computation_stack.append(int(ops[op](l_op,r_op)))
    return computation_stack.pop()

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('evaluate_rpn.py', 'evaluate_rpn.tsv',
                                       evaluate))
