import statistics
from nltk.corpus import reuters
from nltk.tokenize import word_tokenize
import matplotlib.pyplot as plt
from scipy import stats

class StopwordsCompressionAnalyzer:
    """
    A class to analyze the compression rate of text data by removing stopwords.
    
    Attributes:
    ----------
    stopwords : set
        A set of stopwords to be removed from the text.
    file_ids : list
        A list of file IDs from the Reuters corpus.
    """
    
    def __init__(self, stopwords):
        """
        Initializes the StopwordsCompressionAnalyzer with a set of stopwords.
        
        Parameters:
        ----------
        stopwords : set
            A set of stopwords to be removed from the text.
        """
        self.stopwords = stopwords
        # Get Reuters file IDs
        self.file_ids = reuters.fileids()

    def compression_rate(self, text):
        """
        Calculates the compression rate of the text by removing stopwords.
        
        Parameters:
        ----------
        text : str
            The text to be analyzed.
        
        Returns:
        -------
        float
            The compression rate after removing stopwords.
        """
        words = word_tokenize(text.lower())
        filtered_words = [word for word in words if word.isalnum() and word not in self.stopwords]
        original_length = len(words)
        compressed_length = len(filtered_words)
        return compressed_length / original_length

    def analyze_compression_rates(self, num_files=100):
        """
        Analyzes the compression rates for a specified number of files.
        
        Parameters:
        ----------
        num_files : int, optional
            The number of files to analyze (default is 100).
        
        Returns:
        -------
        list
            A list of compression rates for the analyzed files.
        """
        compression_rates = []
        # Limiting to first 'num_files' files for demonstration
        for file_id in self.file_ids[:num_files]:
            text = reuters.raw(file_id)
            comp_rate = self.compression_rate(text)
            compression_rates.append(comp_rate)
        return compression_rates

    def plot_histogram(self, compression_rates):
        """
        Plots a histogram of the compression rates.
        
        Parameters:
        ----------
        compression_rates : list
            A list of compression rates to be plotted.
        """
        plt.hist(compression_rates, bins=50, alpha=0.7, color='blue', edgecolor='black')
        plt.xlabel('Compression Rate')
        plt.ylabel('Frequency')
        plt.title('Histogram of Compression Rates')
        plt.show()

    def calculate_statistics(self, compression_rates):
        """
        Calculates the mean, median, and standard deviation of the compression rates.
        
        Parameters:
        ----------
        compression_rates : list
            A list of compression rates to be analyzed.
        
        Returns:
        -------
        tuple
            A tuple containing the mean, median, and standard deviation of the compression rates.
        """
        mean = statistics.mean(compression_rates)
        median = statistics.median(compression_rates)
        std_dev = statistics.stdev(compression_rates)
        return mean, median, std_dev

    def print_statistics(self, compression_rates):
        """
        Prints the mean, median, and standard deviation of the compression rates.
        
        Parameters:
        ----------
        compression_rates : list
            A list of compression rates to be analyzed.
        """
        mean, median, std_dev = self.calculate_statistics(compression_rates)
        print("Mean: ", mean)
        print("Median: ", median)
        print("Standard Deviation: ", std_dev)

    def perform_shapiro_wilk_test(self, compression_rates):
        """
        Performs the Shapiro-Wilk test to check the normality of the compression rates.
        
        Parameters:
        ----------
        compression_rates : list
            A list of compression rates to be tested.
        
        Returns:
        -------
        None
        """
        # Perform the Shapiro-Wilk test
        w, p = stats.shapiro(compression_rates)

        # Print the results
        print("Shapiro-Wilk test statistic: ", w)
        print("p-value: ", p)

        if p < 0.05:
            print("The compression rates are not normally distributed.")
        else:
            print("The compression rates are normally distributed.")
