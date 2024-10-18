from analyzer import StopwordsCompressionAnalyzer
import stopwordsiso

# Get ISO English stopwords
iso_stopwords = stopwordsiso.stopwords("en")

analyzer = StopwordsCompressionAnalyzer(iso_stopwords)
compression_rates = analyzer.analyze_compression_rates(5000)
analyzer.print_statistics(compression_rates)
analyzer.perform_shapiro_wilk_test(compression_rates)
analyzer.plot_histogram(compression_rates)
