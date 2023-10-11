#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    new_set = set()

    for x in set_1:
        if x not in set_2:
<<<<<<< HEAD
            new_set.add(x)
=======
            new_set.add(x):
>>>>>>> b422a82b57ec9333be64f0ab28db91519c1b19c5
    return new_set
