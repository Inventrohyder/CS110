from MinervaBloom import CountingBloomFilter
import unittest


class TestCBF(unittest.TestCase):

    def test_initialization(self):
        test_qty = 10
        test_fpr = 0.1
        cbf = CountingBloomFilter(test_qty, test_fpr)
        self.assertEqual(
            cbf.intended_item_qty,
            test_qty,
            "The intended elements to store is incorrect"
        )
        self.assertEqual(
            cbf.fpr,
            test_fpr,
            "The intended fpr to stay under is incorrect"
        )


if __name__ == '__main__':
    unittest.main()
