from MinervaBloom import CountingBloomFilter
import unittest


class TestCBF(unittest.TestCase):
    
    def setUp(self):
        self.cbf = CountingBloomFilter(10, 0.1)

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
        
    def test_hashing(self):
        hashes_1 = self.cbf.hash_cbf('chicken')
        hashes_2 = self.cbf.hash_cbf('chicken')
        self.assertEqual(
            hashes_1,
            hashes_2,
            "After hashing the same object twice the hashes are different"
        )


if __name__ == '__main__':
    unittest.main()
