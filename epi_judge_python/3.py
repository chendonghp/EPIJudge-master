from typing import List



def gray_code(num_bits: int) -> List[int]:
    # TODO - you fill in here.
    # return []

    def backtracking(i, val, code_list):
        if i == 2**num_bits-1:
            return code_list.copy()
        for j in range(num_bits):
            # toggle ith bit
            new_val = val ^ (1 << j)
            if new_val not in code_list:
                res = backtracking(i+1, new_val, code_list+[new_val])
                if res:
                    break
        return res
    res = backtracking(0, 0, [0])
    return res

print(gray_code(1))