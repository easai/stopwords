import io
import unittest
import random
from scipy import stats
from unittest.mock import patch
from nltk.corpus import reuters
from stopwords.analyzer import StopwordsCompressionAnalyzer  

class TestStopwordsCompressionAnalyzer(unittest.TestCase):
    """
    Unit tests for the StopwordsCompressionAnalyzer class.
    """

    def setUp(self):
        """
        Set up the test environment by initializing the StopwordsCompressionAnalyzer
        with a predefined set of stopwords.
        """
        self.stopwords = {'the', 'is', 'in', 'and', 'to', 'of'}
        self.analyzer = StopwordsCompressionAnalyzer(self.stopwords)

    def test_compression_rate_zero(self):
        """
        Test the compression_rate method with a text consisting only of stopwords.
        The expected compression rate should be 0.
        """
        stopwords_list = list(self.stopwords)
        random.shuffle(stopwords_list)    
        text = ' '.join(stopwords_list)   
        expected_rate = 0
        actual_rate = self.analyzer.compression_rate(text)
        self.assertEqual(actual_rate, expected_rate)

    def test_compression_rate(self):
        """
        Test the compression_rate method with a sample text.
        The expected compression rate is calculated based on the number of non-stopwords.
        """
        text = "This is a sample text with some stopwords"
        expected_rate = 7.0 / 8
        actual_rate = self.analyzer.compression_rate(text)
        self.assertAlmostEqual(actual_rate, expected_rate, places=4)

    def test_analyze_compression_rates(self):
        """
        Test the analyze_compression_rates method to ensure it returns the correct
        number of compression rates and that all rates are within the valid range [0, 1].
        """
        compression_rates = self.analyzer.analyze_compression_rates(num_files=100)
        self.assertEqual(len(compression_rates), 100)
        self.assertTrue(all(0 <= rate <= 1 for rate in compression_rates))

    def test_calculate_statistics(self):
        """
        Test the calculate_statistics method to ensure it correctly calculates
        the mean, median, and standard deviation of the compression rates.
        """
        compression_rates = [0.5, 0.6, 0.7, 0.8, 0.9]
        mean, median, std_dev = self.analyzer.calculate_statistics(compression_rates)
        self.assertAlmostEqual(mean, 0.7, places=1)
        self.assertAlmostEqual(median, 0.7, places=1)
        self.assertAlmostEqual(std_dev, 0.1581, places=4)

    def test_perform_shapiro_wilk_test(self):
        """
        Test the perform_shapiro_wilk_test method to ensure it returns valid
        Shapiro-Wilk test statistics and p-values.
        """
        compression_rates = self.analyzer.analyze_compression_rates(num_files=100)
        w, p = self.analyzer.perform_shapiro_wilk_test(compression_rates)
        self.assertIsInstance(w, float)
        self.assertIsInstance(p, float)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_print_shapiro_wilk_test(self, mock_stdout):
        """
        Test the print_shapiro_wilk_test method to ensure it prints the correct
        Shapiro-Wilk test results to stdout.
        """
        compression_rates = self.analyzer.analyze_compression_rates(num_files=100)
        self.analyzer.print_shapiro_wilk_test(compression_rates)
        res = mock_stdout.getvalue().strip()
        print(res)
        self.assertRegex(res, r"The compression rates are (not |)normally distributed.")

if __name__ == '__main__':
    unittest.main()
