from analyzer import StopwordsCompressionAnalyzer
import spacy

# Get SpaCy English stopwords
nlp = spacy.load("en_core_web_sm")
spacy_stopwords = nlp.Defaults.stop_words

analyzer = StopwordsCompressionAnalyzer(spacy_stopwords)
compression_rates = analyzer.analyze_compression_rates(5000)
analyzer.print_statistics(compression_rates)
analyzer.perform_shapiro_wilk_test(compression_rates)
analyzer.plot_histogram(compression_rates)
