# Q1

def is_valid_zip(zip_code):
    """Returns whether the input string is a valid (5 digit) zip code
    """
    return (zip_code.isdigit()) and (len(zip_code) == 5)

# Q2

def word_search(doc_list, keyword):
    """
    Takes a list of documents (each document is a string) and a keyword. 
    Returns list of the index values into the original list for all documents 
    containing the keyword.

    Example:
    doc_list = ["The Learn Python Challenge Casino.", "They bought a car", "Casinoville"]
    >>> word_search(doc_list, 'casino')
    >>> [0]
    """
    index = []
    for i,doc in enumerate(doc_list):
        
        words = doc.split()
        #removing punctuation from each word and converting to  lower case
        #for better search
        normalized = [(word.rstrip('.,')).lower() for word in words]
        #matching with keyword
        if keyword.lower() in normalized:
            index.append(i)
    return index

# Q3

def multi_word_search(doc_list, keywords):
    """
    Takes list of documents (each document is a string) and a list of keywords.  
    Returns a dictionary where each key is a keyword, and the value is a list of indices
    (from doc_list) of the documents containing that keyword

    >>> doc_list = ["The Learn Python Challenge Casino.", "They bought a car and a casino", "Casinoville"]
    >>> keywords = ['casino', 'they']
    >>> multi_word_search(doc_list, keywords)
    {'casino': [0, 1], 'they': [1]}
    """
    key_index = {}
    for keyword in keywords:
        key_index[keyword] = word_search(doc_list,keyword)
    return key_index
    

