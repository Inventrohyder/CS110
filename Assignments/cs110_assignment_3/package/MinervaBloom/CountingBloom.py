# Feel free to define additional classes that you think are helpful 
# in building this class of CountingBloomFilter 

class CountingBloomFilter(object):
    """Implement the counting bloom filter which supports:
    - search: queries the membership of an element
    - insert: inserts a string to the filter
    - delete: removes a string from the filter 
    
    Feel free to define any helpful additional methods.
    """
    def __init__(self, /YOUR ARGUMENTS/):
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

