import nltk
from nltk.corpus import stopwords
from analyzer import StopwordsCompressionAnalyzer

# Download the required NLTK data if not already downloaded
nltk.download('reuters')
nltk.download('punkt')
nltk.download('stopwords')

# Load NLTK stopwords
stopwords = set(stopwords.words('english'))

analyzer = StopwordsCompressionAnalyzer(stopwords)
compression_rates = analyzer.analyze_compression_rates(5000)
analyzer.print_statistics(compression_rates)
analyzer.perform_shapiro_wilk_test(compression_rates)
analyzer.plot_histogram(compression_rates)
