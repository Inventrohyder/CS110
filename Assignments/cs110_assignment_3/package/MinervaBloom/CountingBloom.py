# Feel free to define additional classes that you think are helpful 
# in building this class of CountingBloomFilter 

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
        """
        /YOUR ARGUMENTS/ are the two parameters of your choice from the 
        following parameters of a CBF:
        - fpr: float, false positive rate
        - memory_size: int, memory size
        - num_item: int, number of items stored
        - num_hashfn: int, number of hash functions
        
        For example, if you choose fpr and memory_size, edit your __init__ to
        `def __init__(self, memory_size, fpr)`
        """
        pass
    
    @staticmethod
    def bit_array_size(memory_size: int, num_item: int, threshold: int = 1) -> int:
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

