import string, os, nltk
from nltk.tokenize import word_tokenize
nltk.download('punkt')
from nltk.stem import WordNetLemmatizer
nltk.download('omw-1.4')
from nltk.stem.porter import PorterStemmer

# process the stop words
with open('stop_words.txt') as f:
    doc = f.readlines()
    processed_doc = []
    for line in doc:
        new_line = line.strip()
        new_line = new_line.translate(str.maketrans('', '', string.punctuation)).lower();
        processed_doc.append(new_line)
    stop_words = []
    for line in processed_doc:
        stop_words.extend(line.split())
    # print(stop_words)

cwd = os.getcwd()
files = os.listdir("./documents")
dataset = []

for file in files:
    path = f"{cwd}/documents/{file}"
    with open(path) as f:
        dataset.append(f.readlines())
    print('Number of documents ', len(dataset), dataset) # has all the files text in a single list

#preprossing the data
sentences = []
word_set = []
for document in dataset:
    for sent in document: 
        # divide strings into lists of substrings
        x = [i.lower() for i in word_tokenize(sent) if i.isalpha()]
        sentences.append(x) 
        for word in x:
            # capture unique words 
            if word not in word_set:
                word_set.append(word)

print(len(sentences))
# print(word_set) 

# iterate over all stop words and not append them to list if it's a stop word and if the length is lesser than 1
new_word_set = []
for word in word_set:
    if word not in stop_words and len(word) > 1:
        new_word_set.append(word)
# print(new_word_set)

#lemmatization process
wordnet = WordNetLemmatizer()
lemmatized_word_set = []
for word in new_word_set:
    lemmatized_word_set.append(wordnet.lemmatize(word))
# print(lemmatized_word_set)

#stemming - convert words into their stem
porter_stemmer = PorterStemmer()
stem_word_list = []
for word in lemmatized_word_set:
    stem_word_list.append(porter_stemmer.stem(word))
# print(stem_word_list)

# word_set = set(stem_word_list)
# total_documents=8;
# index_dict = {}
# i = 0
# for word in stem_word_list:
#     index_dict[word]=0;
#     i+=1
# print(index_dict)

# def count_dict(sentences):
#     word_count = {}
#     for word in word_set:
#         word_count[word] = 0
#         for sent in sentences:
#             if word in sent:
#                 word_count[word] += 1
#     return word_count
# word_count = count_dict(sentences)

def count_dict(list):
    word_count = {}
    for word in list:
        
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 0
    return word_count
    
word_count = count_dict(stem_word_list)
print(word_count)

def term_freq(document, word):
    N = len(document)
    occurance = len([token for token in document if token == word])
    return occurance/N

def inverse_doc_freq(word):
    try:
        word_occurance = word_count[word]+1
    except:
        word_occurance = 1
    return np.log(total_documents/word_occurance)

