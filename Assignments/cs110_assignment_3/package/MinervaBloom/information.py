import pandas as pd      # To store and run computations faster
import seaborn as sns    # For plotting
import math              # To carry out some mathematical compuatations
from typing import List  # To enable type hinting for some variables


class BloomFilter:
    """
    Contains functions and data relevant to bloom filter's write up.
    """

    @staticmethod
    def probability_rate(
        # The size of the bit array
        m_min: int = 100, m_max: int = 1000, m_step: int = 100,

        # The number of hashing functions
        k_min: int = 1, k_max: int = 5, k_step: int = 1,

        # The number of elements to store
        n_min: int = 10, n_max: int = 700, n_step: int = 15,

        title: str = "A probability rate graph of a standard bloom filter"
    ) -> None:
        """
        Plot a False Probability Rate graph of a standard bloom filter

        Parameters
        -----------
        m_min: The smallest size of the bit array to consider
        m_max: The largest size of the bit array to consider
        m_step: The variation of sizes made each iteration
        k_min: The smallest number of hashing functions to consider
        k_max: The largest number of hashing functions to consider
        k_step: The variation in number of hashing functions each iteration
        n_min: The smallest quantity elements to store
        n_max: The largest quantity of elements to store
        n_step: The variation in quantity of elements updated each iteration
        title: The title to use for the plot
        """

        data: dict = {"m": [], "k": [], "n": []}
        for m in range(m_min, m_max, m_step):
            for k in range(k_min, k_max, k_step):
                for n in range(n_min, n_max, n_step):
                    data["m"].extend([m])
                    data["k"].extend([k])
                    data["n"].extend([n])

        # Using pandas to calculate the final values from the rest of the columns
        # makes the code run efficiently and fast
        df: pd.DataFrame = pd.DataFrame(data=data)
        df['fpr'] = (1 - (1 - 1 / df['m']) ** (df['k'] * df['n'])) ** df['k']

        g = sns.FacetGrid(df, row="k", height=4, aspect=2, margin_titles=True)
        g.map(sns.lineplot, "m", y="fpr", hue="n", data=df)
        g.add_legend()
        g.set_axis_labels("m", "fpr")
        

    @staticmethod
    def bit_array_size(
        # The number of elements to insert
        n_min: int = 10, n_max: int = 700, n_step: int = 15,

        # The false positive error rate
        p_min: float = 10,         # 10 percent fpr
        p_max: float = 75,         # 75 percent fpr
        p_step: float = 5,         # 5 percent fpr
        title: str = "Optimum sizes for arrays given an FPR"
    ) -> None:
        """
        Plot an optimum number of hashing functions given the array size and number of elements

        Parameters
        -----------
        n_min: The lowest amount of elements to insert 
        n_max: The highest amount of elements to insert
        n_step: The variation in number of elements each iteration
        m_min: The smallest size of the bit array to consider
        m_max: The largest size of the bit array to consider
        m_step: The variation of sizes made each iteration
        title: The title to use for the plot
        """

        data: dict = {"n": [], "fpr": []}
        
        for n in range(n_min, n_max, n_step):
            for p in range(p_min, p_max, p_step):
                data["n"].extend([n])
                data["fpr"].extend([p * 0.01])

        # Using pandas to calculate the final values from the rest of the columns
        # makes the code run efficiently and fast
        df: pd.DataFrame = pd.DataFrame(data=data)
        df['m'] = - (df['n']*df['fpr'].apply(math.log2)) / (math.log2(2) ** 2) 

        ax = sns.lineplot(
            x='fpr', y='m', hue='n',
            data=df
        )

        ax.set_title(title)
        
        
    @staticmethod
    def hash_functions(
        # The number of elements to insert
        n_min: int = 10, n_max: int = 700, n_step: int = 15,
        
        # The size of the bit array
        m_min: int = 100, m_max: int = 1000, m_step: int = 100,
        
        title: str = "Optimum number of hash functions"
    ) -> None:
        """
        Plot an optimum size of a bit array given the FPR

        Parameters
        -----------
        n_min: The lowest amount of elements to insert 
        n_max: The highest amount of elements to insert
        n_step: The variation in number of elements each iteration
        p_min: The lowest fpr to consider
        p_max: The highest fpr to consider
        p_step: The variation in fpr each iteration
        title: The title to use for the plot

        """

        data: dict = {"n": [], "m": []}
            
        for n in range(n_min, n_max, n_step):
            for m in range(m_min, m_max, m_step):
                data["n"].extend([n])
                data["m"].extend([m])

        # Using pandas to calculate the final values from the rest of the columns
        # makes the code run efficiently and fast
        df: pd.DataFrame = pd.DataFrame(data=data)
        df['k'] = math.log2(2) * df['m']/df['n']

        ax = sns.lineplot(
            x='m', y='k', hue='n',
            data=df
        )

        ax.set_title(title)