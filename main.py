def main():
    book_path = "books/frankenstein.txt"
    book = Book(book_path)
    print(f"{book.get_num_words()} words found in the document")
    book.generate_character_report()


class Book:
    def __init__(self, book_path):
        self.book_path = book_path
        self.text = self.get_book_text()
        self.words = self.text.split()

    def get_book_text(self):
        with open(self.book_path) as f:
            return f.read()

    def get_num_words(self):
        return len(self.words)

    def get_character_count(self):
        characters = {}
        for word in self.words:
            for character in word.lower():
                if character in characters:
                    characters[character] += 1
                else:
                    characters[character] = 0
        return characters

    def generate_character_report(self):
        print("--- Start report ---")
        sorted_character_list = self.get_dict_to_sorted_list()
        for item in sorted_character_list:
            if item['char'].isalnum():
                print(f"The '{item['char']}' character was found {item['num']} times")
        print("--- End report ---")

    def get_dict_to_sorted_list(self):
        characters_dict = self.get_character_count()
        sorted_list = []

        for ch in characters_dict:
            sorted_list.append({"char": ch, "num": characters_dict[ch]})
        sorted_list.sort(reverse=True, key=self.sort_on)
        return sorted_list

    @staticmethod
    def sort_on(d):
        return d["num"]

main()
