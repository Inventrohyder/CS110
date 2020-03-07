import math                 # To carry out some computations
import numpy as np          # To generate the storage array
import mmh3                 # To generate the hashing functions
from typing import List     # To allow type hinting


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
        self.functions_qty = CountingBloomFilter.hash_functions(
            self.size, num_item, threshold)
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
        return int(m)

    @staticmethod
    def hash_functions(memory_size: int, num_item: int, threshold: int) -> int:
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

        # The formul is from Kim et al. 2019 (https://www.mdpi.com/2079-9292/8/7/779/htm)
        k_opt = memory_size * (0.2037 * threshold + 0.9176) / num_item
        return int(k_opt)

    def hash_cbf(self, item: object) -> List:
        """
        Returns hash values of an item
        
        Parameters
        ----------
        item: the item to hash
        
        Returns
        -------
        A list of hashes
        """
        
        hashes = [mmh3.hash(item, i) for i in range(self.functions_qty)]
        return hashes
            

    def search(self, item: object) -> bool:
        """
        Check's if an item is stored in the CBF
        
        Parameters
        ----------
        item: The item to search for
        """
        indexes = [i%self.size for i in self.hash_cbf(item)]
        
        # Using numpy vector operations check if all the indexes are
        # greater than the threshold
        return (self.array[indexes] > self.threshold).all()

    def insert(self, item: object) -> None:
        """
        Insert's an item into the cbf storage
        
        Parameter
        ---------
        item: The object to insert
        """
        indexes = [i%self.size for i in self.hash_cbf(item)]
        
        # Use numpy vector operations to speed up updates
        self.array[indexes] += 1
            

    def delete(self, item: object) -> bool:
        """
        Delete's an item only if it already exists
        
        Parameter
        ---------
        item: The item to search for and delete
        
        Return
        ------
        True if deleted and False if not deleted
        """
        if self.search(item):
            indexes = [i%self.size for i in self.hash_cbf(item)]
            self.array[indexes] -= 1
            return True
        return False
