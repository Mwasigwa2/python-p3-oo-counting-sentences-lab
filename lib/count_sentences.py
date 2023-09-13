import re

class MyString:
    def __init__(self):
        self._value = ""

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, new_value):
        if isinstance(new_value, str):
            self._value = new_value
        else:
            raise ValueError("Value must be a string")

    def is_sentence(self):
        return self._value.endswith(".")

    def is_question(self):
        return self._value.endswith("?")

    def is_exclamation(self):
        return self._value.endswith("!")

    def count_sentences(self):
        # Split the string using regular expressions to handle multiple sentence-ending punctuation
        sentences = re.split(r'[.!?]', self._value)
        # Filter out empty strings and return the count of non-empty sentences
        return len([sentence for sentence in sentences if sentence.strip() != ""])

string = MyString()
string.value = "This is a string! It has three sentences. Right?"

print(string.is_sentence())  # True
print(string.is_question())  # False
print(string.is_exclamation())  # False
print(string.count_sentences())  # 3
