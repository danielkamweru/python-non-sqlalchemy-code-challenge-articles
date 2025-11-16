# Represents a single article written by an author for a magazine
class Article:
    all = []   # store every created article

    def __init__(self, author, magazine, title):
        self.author = author
        self.magazine = magazine
        self._title = None
        self.title = title   # set once
        Article.all.append(self)

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        if self._title is None and isinstance(value, str) and len(value) >= 1:
            self._title = value


# Represents an author who writes articles for magazines
class Author:
    def __init__(self, name):
        self._name = None
        self.name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if self._name is None and isinstance(value, str) and len(value) >= 1:
            self._name = value

    def articles(self):
        return [article for article in Article.all if article.author == self]

    def magazines(self):
        return list({article.magazine for article in self.articles()})

    def add_article(self, magazine, title):
        return Article(self, magazine, title)

    def topic_areas(self):
        categories = {mag.category for mag in self.magazines()}
        return list(categories) if categories else None


# Represents a magazine that contains articles and contributors
class Magazine:
    all = []   # store magazines

    def __init__(self, name, category):
        self._name = None
        self._category = None
        self.name = name
        self.category = category
        Magazine.all.append(self)

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if isinstance(value, str) and 2 <= len(value) <= 16:
            self._name = value

    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, value):
        if isinstance(value, str) and len(value) > 0:
            self._category = value

    def articles(self):
        return [article for article in Article.all if article.magazine == self]

    def contributors(self):
        return list({article.author for article in self.articles()})

    def article_titles(self):
        titles = [article.title for article in self.articles()]
        return titles if titles else None

    def contributing_authors(self):
        authors = [article.author for article in self.articles()]
        return [a for a in set(authors) if authors.count(a) > 1] or None
