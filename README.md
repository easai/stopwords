## Stopwords

Stopwords are commonly used words in a language that are often filtered out in natural language processing (NLP) and text mining tasks. Examples of stopwords in English include “the,” “is,” “in,” “and,” “a,” and "an".

This Venn diagram depicts how the stopwords provided by ISO, spaCy, and NLTK differ.

<img src="https://raw.githubusercontent.com/easai/stopwords/refs/heads/main/English_stopwords.png" width=600 alt="ISO, spaCy, and NLTK English stopwords" />

### ISO Stopwords
The ISO stopwords collection is a comprehensive set of stopwords for multiple languages, following the ISO 639-1 language codes. 

### spaCy Stopwords
spaCy has built-in stopword lists for several languages.

### NLTK Stopwords
NLTK provides a comprehensive list of stopwords for multiple languages.

## Stats on Reuters Texts with ISO, SpaCy, NLTK Stopwords
The following are stats on compression rates of Reuters texts using three different sets of stopwords: ISO, SpaCy, and NLTK. The compression rate is calculated by removing stopwords from the text and comparing the number of words in the filtered text to the original text.

### ISO Stopwords:
<img src="https://raw.githubusercontent.com/easai/stopwords/refs/heads/main/iso-stopwords-reuters.png" width=300 alt="Stats on Reuters Texts with ISO Stopwords" />

```text
Mean:  0.46848585024735256
Median:  0.45714285714285713
Standard Deviation:  0.09172824822316185
Shapiro-Wilk test statistic:  0.8993187595609815
p-value:  2.5232375570871764e-49
The compression rates are not normally distributed.
```

### SpaCy Stopwords:
<img src="https://raw.githubusercontent.com/easai/stopwords/refs/heads/main/spacy-stopwords-reuters.png" alt="Stats on Reuters Texts with SpaCy Stopwords" width=300>

```text
Mean:  0.5834552313052037
Median:  0.5585585585585585
Standard Deviation:  0.10965667465841214
Shapiro-Wilk test statistic:  0.9216185461552716
p-value:  3.3622028531080556e-45
The compression rates are not normally distributed.
```

### NLTK Stopwords:
<img src="https://raw.githubusercontent.com/easai/stopwords/refs/heads/main/nltk-stopwords-reuters.png"  alt="Stats on Reuters Texts with NLTK Stopwords" width=300>

```text
Mean:  0.6127916769823796
Median:  0.5876288659793815
Standard Deviation:  0.1080245729937558
Shapiro-Wilk test statistic:  0.905384897890509
p-value:  2.773996451055017e-48
The compression rates are not normally distributed.
```

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
For statistics, run the scripts as follows.
- ISO Stopwords
```bash
poetry run py .\stopwords\iso-stopwords.py
```
- SpaCy Stopwords
```bash
poetry run py .\stopwords\spacy-stopwords.py
```
- NLTK Stopwords
```bash
poetry run py .\stopwords\nltk-stopwords.py
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
- [English stopwords by ISO, spaCy, and NLTK](https://github.com/easai/stopwords/blob/main/results.txt)

- [Stats on Reuters Texts with ISO, SpaCy, NLTK Stopwords](https://github.com/easai/stopwords/blob/main/results-stat.txt)

### Test
To run a unit test, run the following command in your terminal.
```bash
poetry run py -m unittest
```
