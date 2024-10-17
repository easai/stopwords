## Stopwords

Stopwords are commonly used words in a language that are often filtered out in natural language processing (NLP) and text mining tasks. Examples of stopwords in English include “the,” “is,” “in,” “and,” “a,” and "an".

This Venn diagram depicts how the stopwords provided by ISO, spaCy, and NLTK differ.

![English stopwords by ISO, spaCy, and NLTK](https://github.com/easai/stopwords/blob/main/English_stopwords.png)

### ISO Stopwords
The ISO stopwords collection is a comprehensive set of stopwords for multiple languages, following the ISO 639-1 language codes. 

### spaCy Stopwords
spaCy has built-in stopword lists for several languages.

### NLTK Stopwords
NLTK provides a comprehensive list of stopwords for multiple languages.

### Usage
To run the script, first install dependent libraries.
```bash
poetry install
```
Run the script as follows.
```bash
poetry run stopwords/stopwords.py
```
