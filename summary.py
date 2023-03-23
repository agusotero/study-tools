FILENAME = 'file.pdf'
LANGUAGE = 'spanish'

import PyPDF4
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize
from heapq import nlargest
nltk.download('stopwords')
nltk.download('punkt')

# Open the PDF file
pdf_file = open(FILENAME, 'rb')

# Read the PDF file
pdf_reader = PyPDF4.PdfFileReader(pdf_file)

# Extract the text from the PDF file
text = ''
for page in range(pdf_reader.getNumPages()):
    text += pdf_reader.getPage(page).extractText()

print(text)


# Tokenize the text into sentences
sentences = sent_tokenize(text, language=LANGUAGE)

# Tokenize the sentences into words
words = word_tokenize(text, language=LANGUAGE)

# Remove stop words from the words list
stop_words = set(stopwords.words(LANGUAGE))
words = [word for word in words if word.casefold() not in stop_words]

# Calculate the frequency of each word
word_frequencies = {}
for word in words:
    if word not in word_frequencies:
        word_frequencies[word] = 1
    else:
        word_frequencies[word] += 1

# Calculate the score of each sentence based on the frequency of its words
sentence_scores = {}
for sentence in sentences:
    for word in word_tokenize(sentence.lower(), language=LANGUAGE):
        if word in word_frequencies:
            if len(sentence.split(' ')) < 30:
                if sentence not in sentence_scores:
                    sentence_scores[sentence] = word_frequencies[word]
                else:
                    sentence_scores[sentence] += word_frequencies[word]

# Generate a summary of the document by selecting the top 3 sentences with highest scores
summary_sentences = nlargest(3, sentence_scores, key=sentence_scores.get)
summary = ' '.join(summary_sentences)

# Print the summary
print(summary)

