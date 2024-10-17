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
Download `en_core_web_sm` for spaCy stopwords.
```bash
poetry run python -m spacy download en_core_web_sm
```
Run the script as follows.
```bash
poetry run py .\stopwords\stopwords.py
```
### Results
Click below for the results.
```text
sets = {
    '100': iso_stopwords - spacy_stopwords - nltk_stopwords,
    '010': spacy_stopwords - iso_stopwords - nltk_stopwords,
    '001': nltk_stopwords - iso_stopwords - spacy_stopwords,
    '110': (iso_stopwords & spacy_stopwords) - nltk_stopwords,
    '101': (iso_stopwords & nltk_stopwords) - spacy_stopwords,
    '011': (spacy_stopwords & nltk_stopwords) - iso_stopwords,
    '111': iso_stopwords & spacy_stopwords & nltk_stopwords
}
```
[English stopwords by ISO, spaCy, and NLTK](https://github.com/easai/stopwords/blob/main/results.txt)

