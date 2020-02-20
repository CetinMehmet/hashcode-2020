FILES = ["a_example.txt", "b_read_on.txt", "c_incunabula.txt"]
MODE = "r"

class File_extraction:

    def __init__(self, file):
        self.file = file

    def read_line(self,file):
        line = file.readline()
        return line

    def get_book_library_days(self, line):
        books = list(map(int, line.split()))[0]
        librarys = list(map(int, line.split()))[1]
        days = list(map(int, line.split()))[2]
        return books, librarys, days

    def get_book_scores(self, line):
        book_scores = {}
        scores = list(map(int, line.split()))
        for i in range(0, len(scores)):
            book_scores[i] = scores[i]
        return book_scores

    def get_library_attr(self, line):
        books = list(map(int, line.split()))[0]
        process_days = list(map(int, line.split()))[1]
        ships_per_day = list(map(int, line.split()))[2]
        return books, process_days, ships_per_day

    def get_books(self, line, book_scores):
        book_ids = list(map(int, line.split()))
        scores = {}
        for book_id in book_ids:
            scores[book_id] = book_scores[book_id]
        return scores


class Library:
    def __init__(self, total_score, books, signup_days, ships_per_day):
        self.total_score = total_score
        self.books = books
        self.signup_days = signup_days
        self.ships_per_day = ships_per_day


def main(file):
    f = File_extraction(file)

    # Get number of: books, librarys, days
    line = f.read_line(file)
    book_count, library_count, scan_days = f.get_book_library_days(line)

    # Get the book scores
    line = f.read_line(file)
    book_scores = f.get_book_scores(line)

    libraries = list()
    for _ in range(library_count):
        line = f.read_line(file)
        book_num, signup_days, ships_per_day = f.get_library_attr(line)
        line = f.read_line(file)
        books = f.get_books(line, book_scores)

        libraries.append(Library(sum(books.values()), books, signup_days, ships_per_day))

    scanned_books = list()
    
    #Greedy method
    #1. get lest signup days
    #2. get most shipping per days
    #3. get highest total scores of the books in that specific library
    libraries.sort(key=lambda libraries:libraries.ships_per_day)
    libraries.sort(key=lambda libraries:libraries.total_score)
    libraries.sort(key=lambda libraries:libraries.signup_days)

    for library in libraries:
        print(library.signup_days, library.ships_per_day, library.total_score)

    scan_books = []
    for i in range(library_count):
        library = libraries[i]
        if scan_days == 0:
            break
        
        for book in library.books.keys():
            if book not in scanned_books and scan_days:
                scan_books.append(book)
                scanned_books.append(book)

        scan_days -= library.signup_days
        scan_books = []

    sumd=0
    for i in range(0, len(scanned_books)):
        sumd += book_scores[scanned_books[i]]
    
    print(sumd)

if __name__ == "__main__":
    f = open(FILES[1], MODE)
    main(f)