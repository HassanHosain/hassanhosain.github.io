def tokenize(text):
    #1.Normalize: Convert to lower case and remove punctuation
    text=re.sub(r"[^a-zA-Z0-9]", " ",text.lower().strip())

    #2. tokenizingL split text into words
    tokens=word_tokenize(text)

    #3 Remove stop words: if a token is a stop word, then remove it
    words = [w for w in tokens if w w not in stopwords.words("english")]

    #4. Lemmatize and Stemming
    lemmed_words = [WordNetLemmatizer().lemmatize(w) for w in words]

    clean_tokens = []

    for i in lemmed_words:
        clean_tokens.append(i)

        #back to string from list
    text = " ".join(clean_tokens)
    return text
    #return clean_tokens