import numpy as np

class AssertTest(object):
    '''Defines general test behavior.'''
    def __init__(self, params):
        self.assert_param_message = '\n'.join([str(k) + ': ' + str(v) + '' for k, v in params.items()])
    
    def test(self, assert_condition, assert_message):
        assert assert_condition, assert_message + '\n\nUnit Test Function Parameters\n' + self.assert_param_message

def _print_success_message():
    print('Tests Passed!')


def test_lcs(lcs_function):
    # The pairs to find LCS values for
    pairs = [                    # LCS values:
        ('ABCBDAB', 'BDCABA'),    # 4
        ('abc', ''),              # 0
        ('abc', 'a'),             # 1
        ('abc', 'ac')             # 2
    ]
    # The correct lcs values are:
    lcs_vals = [4, 0, 1, 2]

    results = []

    for pair in pairs:
        results.append(lcs_function(*pair))

    # check correct results
    assert all(np.isclose(results, lcs_vals, rtol=1e-05)), 'LCS calculations are incorrect.'
    
    _print_success_message()