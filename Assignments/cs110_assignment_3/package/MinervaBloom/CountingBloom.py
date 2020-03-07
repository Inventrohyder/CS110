import math
import numpy as np



class CountingBloomFilter(object):
    """
    Implements the counting bloom filter which supports:
    - search: queries the membership of an element
    - insert: inserts a string to the filter
    - delete: removes a string from the filter 
    """
    def __init__(self, num_item: int, fpr: float, threshold: int = 1) -> None:
        """
        Initializes an empty CBF
        
        Parameters
        ----------
        num_item: The approximate number of items that the CBF will be used to store
        fpr: The desired fpr to stay below
        """
        self.fpr = fpr
        self.intended_item_qty = num_item
        self.threshold = threshold
        self.size = CountingBloomFilter.bit_array_size(num_item, fpr)
        self.functions_qty = CountingBloomFilter.hash_functions(self.size, num_item)
        self.array = np.zeros(self.size)
    
    @staticmethod
    def bit_array_size(num_item: int, fpr: float) -> int:
        """
        Provides the optimum size of an array to stay under a certain fpr
        
        Parameters
        ----------
        num_item: The intended number of items to store
        fpr: The false probability rate to stay under
        """
        m = - (num_item * math.log(fpr)) / (math.log(2) ** 2)
        return m
    
    
    @staticmethod
    def hash_functions(memory_size: int, num_item: int) -> int:
        """
        Calculates the optimum number of hashing functions
        
        Parameters
        ----------
        memory_size: The size of the multi-bit CBF array
        num_item: The intended number of items to store
        threshold: The number of times an item must have been inserted before querying for it returns True
        
        Returns
        -------
        The optimum number of hash functions
        """
        
        k_opt = memory_size * (0.2037 * threshold + 0.9176) / num_item  # The formul is from Kim et al. 2019 (https://www.mdpi.com/2079-9292/8/7/779/htm)
        return k_opt
        
    
    def hash_cbf(self, item):
        """
        Returns hash values of an item
        [ADD ADDITIONAL DESCRIPTION, IF NEED BE]
        """
        pass
    
    def search(self, item):
        """
        [YOUR FUNCTION DESCRIPTION]
        """
        pass
    
    def insert(self, item):
        """
        [YOUR FUNCTION DESCRIPTION]
        """
        pass
    
    def delete(self, item):
        """
        [YOUR FUNCTION DESCRIPTION]
        """
        pass

