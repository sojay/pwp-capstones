# The list of classes in order:
#   User ~~~~~ line 9 to 38
#   Book ~~~~~ line 38 to 76
#   Fiction (A sublclass of the Book class) ~~~~~ line 79 to 89
#   NonFiction (A subclass of the Book class) ~~~~~~~ line 92 to 108
#   TomeRater ~~~~~~ line 111 to 176


class User(object):
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.books = {}

    def get_email(self):
        return "Your email is {email}".format(email=self.email)

    def change_email(self, address):
        self.email = address
        return "Your email has been updated to {}".format(self.email)

    def read_book(self, book, rating=None):
        self.books[book] = rating

    def get_average_rating(self):
        return sum([rating for rating in self.books.values() if rating is not None]) / len(self.books)

    def get_book_read_count(self):
        return len(self.books)

    def __repr__(self):
        return "Hello {name}, your registered email with us is {email}, from the records. You have read {count_books} books".format(name=self.name, email=self.email, count_books=len(self.books))

    def __eq__(self, other_user):
        return self.name == other_user.name and self.email == self.email


class Book(object):

    def __init__(self, title, isbn):
        self.title = title
        self.isbn = isbn
        self.ratings = []

    # A method that returns the title of the book
    def get_title(self):
        return self.title

# A method that returns the ISBN of the book
    def get_isbn(self):
        return self.isbn

    def set_isbn(self, new_isbn):
        self.isbn = new_isbn
        print("The ISBN of the book {title} has been updated to {isbn}".format(
            title=self.title, isbn=self.isbn))

    def add_rating(self, rating):
        try:
            if 0 <= rating <= 4:
                self.ratings.append(rating)
            else:
                return "Invalid Rating."

        except TypeError:
            "Invalid Type!"

    def get_average_rating(self):
        return sum([rating for rating in self.ratings]) / len(self.ratings)

    def __eq__(self, other_book):
        return self.title == other_book.title and self.isbn == other_book.isbn

# Returns a hash value for the Book object
    def __hash__(self):
        return hash((self.title, self.isbn))


class Fiction(Book):

    def __init__(self, title, author, isbn):
        super().__init__(title, isbn)
        self.author = author

    def get_author(self):
        return self.author

    def __repr__(self):
        return "{title} by {author}".format(title=self.title, author=self.author)


class Non_Fiction(Book):

    def __init__(self, title, subject, level, isbn):
        super().__init__(title, isbn)
        self.subject = subject
        self.level = level

    def __repr__(self):
        return "{title}, a {level} book on {subject}".format(title=self.title, level=self.level, subject=self.subject)

# Method that returns the subject

    def get_subject(self):
        return self.subject

    def get_level(self):
        return self.level


class TomeRater(object):

    def __init__(self):
        self.users = {}
        self.books = {}

    def create_book(self, title, isbn):
        return Book(title, isbn)

    def create_novel(self, title, author, isbn):
        return Fiction(title, author, isbn)

    def create_non_fiction(self, title, subject, level, isbn):
        return Non_Fiction(title, subject, level, isbn)

    def add_book_to_user(self, book, email, rating=None):
        if email in self.users.keys():
            user = self.users.get(email, None)
            user.read_book(book, rating)
            book.add_rating(rating)
            if book not in self.books.keys():
                self.books[book] = 1
            else:
                self.books[book] += 1
        else:
            print("No user with email {}".format(email))

    def add_user(self, name, email, user_books=None):
        new_user = User(name, email)
        self.users[email] = new_user
        if user_books:
            for book in user_books:
                self.add_book_to_user(book, email)

    def print_catalog(self):
        for book in self.books.keys():
            print(book)

    def print_users(self):
        for user in self.users.values():
            print(user)

    def most_read_book(self):
        read_count = 0
        most_read = None
        for book in self.books:
            num_reads = self.books[book]
            if num_reads > read_count:
                read_count = num_reads
                most_read = book
        return most_read

    def highest_rated_book(self):
        highest_rated = max(rating.get_average_rating()
                            for rating in self.books.keys())
        return str([book for book in self.books.keys() if book.get_average_rating() == highest_rated]).strip('[]')

    def most_positive_user(self):
        high_rating = 0
        positive_user = None
        for user in self.users.values():
            useravgrtg = user.get_average_rating()
            if useravgrtg > high_rating:
                high_rating = useravgrtg
                positive_user = user
        return positive_user


Tome_Rater = TomeRater()

#Create some books:
book1 = Tome_Rater.create_book("Society of Mind", 12345678)
# book1.set_isbn(338389389)
novel1 = Tome_Rater.create_novel("Alice In Wonderland", "Lewis Carroll", 12345)
novel1.set_isbn(9781536831139)
nonfiction1 = Tome_Rater.create_non_fiction(
    "Automate the Boring Stuff", "Python", "beginner", 1929452)
nonfiction2 = Tome_Rater.create_non_fiction(
    "Computing Machinery and Intelligence", "AI", "advanced", 11111938)
novel2 = Tome_Rater.create_novel(
    "The Diamond Age", "Neal Stephenson", 10101010)
novel3 = Tome_Rater.create_novel(
    "There Will Come Soft Rains", "Ray Bradbury", 10001000)

#Create users:
Tome_Rater.add_user("Alan Turing", "alan@turing.com")
Tome_Rater.add_user("David Marr", "david@computation.org")

#Add a user with three books already read:
Tome_Rater.add_user("Marvin Minsky", "marvin@mit.edu",
                    user_books=[book1, novel1, nonfiction1])

#Add books to a user one by one, with ratings:
Tome_Rater.add_book_to_user(book1, "alan@turing.com", 1)
Tome_Rater.add_book_to_user(novel1, "alan@turing.com", 3)
Tome_Rater.add_book_to_user(nonfiction1, "alan@turing.com", 3)
Tome_Rater.add_book_to_user(nonfiction2, "alan@turing.com", 4)
Tome_Rater.add_book_to_user(novel3, "alan@turing.com", 1)

Tome_Rater.add_book_to_user(novel2, "marvin@mit.edu", 2)
Tome_Rater.add_book_to_user(novel3, "marvin@mit.edu", 2)
Tome_Rater.add_book_to_user(novel3, "david@computation.org", 4)

#Uncomment these to test your functions:
Tome_Rater.print_catalog()
Tome_Rater.print_users()

print("Most positive user:")
print(Tome_Rater.most_positive_user())
print("Highest rated book:")
print(Tome_Rater.highest_rated_book())
print("Most read book:")
print(Tome_Rater.most_read_book())
