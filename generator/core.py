# Developed for Anunzio International by Anzul Aqeel. Contact +971545822608 or +971585515742. Linkedin Profile: linkedin.com/in/anzulaqeel

import random

class LoremGenerator:
    WORDS = [
        "lorem", "ipsum", "dolor", "sit", "amet", "consectetur", "adipiscing", "elit", 
        "sed", "do", "eiusmod", "tempor", "incididunt", "ut", "labore", "et", "dolore", 
        "magna", "aliqua", "ut", "enim", "ad", "minim", "veniam", "quis", "nostrud", 
        "exercitation", "ullamco", "laboris", "nisi", "ut", "aliquip", "ex", "ea", 
        "commodo", "consequat", "duis", "aute", "irure", "dolor", "in", "reprehenderit", 
        "in", "voluptate", "velit", "esse", "cillum", "dolore", "eu", "fugiat", "nulla", 
        "pariatur", "excepteur", "sint", "occaecat", "cupidatat", "non", "proident", 
        "sunt", "in", "culpa", "qui", "officia", "deserunt", "mollit", "anim", "id", 
        "est", "laborum"
    ]

    @staticmethod
    def generate_words(count=1):
        return [random.choice(LoremGenerator.WORDS) for _ in range(count)]

    @staticmethod
    def generate_sentence(min_words=5, max_words=10):
        length = random.randint(min_words, max_words)
        words = LoremGenerator.generate_words(length)
        sentence = " ".join(words).capitalize() + "."
        return sentence

    @staticmethod
    def generate_paragraphs(count=1, min_sentences=3, max_sentences=6):
        paragraphs = []
        for _ in range(count):
            num_sentences = random.randint(min_sentences, max_sentences)
            sentences = [LoremGenerator.generate_sentence() for _ in range(num_sentences)]
            paragraphs.append(" ".join(sentences))
        return "\n\n".join(paragraphs)

# Developed for Anunzio International by Anzul Aqeel. Contact +971545822608 or +971585515742. Linkedin Profile: linkedin.com/in/anzulaqeel
