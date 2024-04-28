import PyPDF2

import re

import nltk
from nltk.corpus import words
from nltk.corpus import stopwords
from PyDictionary import PyDictionary
dicionary =  PyDictionary()

nltk.download('words')
word_list = set(words.words())  # Load the set of English words

nltk.download('stopwords')
stop_words = set(stopwords.words('english')) 

def is_valid_word(word):
    return word.lower() in word_list

# Example Usage
print(is_valid_word("apple"))  # Should return True
print(is_valid_word("bapple"))  # Likely returns False

def extract_words_from_pdf(file_path):
    with open(file_path, "rb") as file:
        reader = PyPDF2.PdfReader(file)
        num_pages = len(reader.pages)
        all_words = []
        for i in range(num_pages):
            page = reader.pages[i]
            text = page.extract_text()
            if text:
                words = re.findall(r'\b\w+\b', text)  # Use regex to find words
                for word in words:
                    if is_valid_word(word) and word not in stop_words and len(word) >1:
                     all_words.append(word)
    
    # Filter out any tokens that are purely numeric or non-alphabetic characters
    filtered_words = [word for word in all_words if word.isalpha()]
    set1=sorted(list(set(filtered_words)))
    return set1

# Usage
pdf_words = extract_words_from_pdf("rose.pdf")
print(pdf_words)



