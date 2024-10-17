import matplotlib.pyplot as plt
from matplotlib_venn import venn3
import nltk
import spacy
import stopwordsiso

# Get ISO English stopwords
iso_stopwords = stopwordsiso.stopwords("en")

# Get SpaCy English stopwords
nlp = spacy.load("en_core_web_sm")
spacy_stopwords = nlp.Defaults.stop_words

# Get NLTK English stopwords
nltk.download('stopwords')
nltk_stopwords = set(nltk.corpus.stopwords.words('english'))

# Create a Venn diagram
venn3([iso_stopwords, spacy_stopwords, nltk_stopwords], ('ISO stopwords', 'SpaCy stopwords', 'NLTK stopwords'))

# Display the plot
plt.title("English stopwords")
plt.show()
