import pytest
from main import BooksCollector


class TestBooksCollector:

    @pytest.mark.parametrize('book_names', ['Гордость и предубеждение и зомби', 'А',
                                            'Что делать, если ваш кот хочет вас убить'])
    def test_add_new_book_add_positive_name_books(self, book_names):
        collector = BooksCollector()
        collector.add_new_book(book_names)
        assert len(collector.get_books_genre()) == 1

    @pytest.mark.parametrize('book_names', ['', 'Книга на сорок один символллллллллллллллл',
                                            'Книга на сорок два символллллллллллллллллл'])
    def test_add_new_book_add_negative_name_books(self, book_names):
        collector = BooksCollector()
        collector.add_new_book(book_names)
        assert len(collector.get_books_genre()) == 0

    def test_add_new_book_add_same_name_books(self):
        collector = BooksCollector()
        collector.add_new_book('Тоже самое')
        collector.add_new_book('Тоже самое')
        assert len(collector.get_books_genre()) == 1

    def test_set_book_genre_add_genre_book_positive_result(self):
        collector = BooksCollector()
        collector.add_new_book('Фильм в жанре комедии')
        collector.set_book_genre('Фильм в жанре комедии', 'Комедии')
        assert collector.books_genre.get('Фильм в жанре комедии') == 'Комедии'

    def test_set_book_genre_add_genre_is_not_list(self):
        collector = BooksCollector()
        collector.add_new_book('Фильм в жанре комедии')
        collector.set_book_genre('Фильм в жанре комедии', 'Боевики')
        assert collector.books_genre.get('Фильм в жанре комедии') == ''

    def test_get_book_genre_for_name_positive_result(self):
        collector = BooksCollector()
        collector.add_new_book('Фильм в жанре комедии')
        collector.set_book_genre('Фильм в жанре комедии', 'Комедии')
        assert collector.books_genre.get('Фильм в жанре комедии') == 'Комедии'

    def test_get_books_with_specific_genre_get_book_name_with_specific_genre(self):
        collector = BooksCollector()
        collector.books_genre = {'Фильм в жанре комедии': 'Комедии', 'Фильм в жанре мультфильмы': 'Мультфильмы',
                                 'Фильм в жанре фантастике': 'Фантастика'}
        assert len(collector.get_books_with_specific_genre('Мультфильмы')) == 1

    def test_get_books_for_children_all_approved_books(self):
        collector = BooksCollector()
        collector.books_genre = {'Фильм в жанре комедии': 'Комедии', 'Фильм в жанре мультфильмы': 'Мультфильмы',
                                 'Фильм в жанре фантастике': 'Фантастика', 'Фильм в жанре детектива': 'Детективы',
                                 'Фильм в жанре ужасов': 'Ужасы'}
        assert len(collector.get_books_for_children()) == 3

    def test_add_book_in_favorites_add_book(self):
        collector = BooksCollector()
        collector.add_new_book('Фильм в жанре фантастике')
        collector.add_book_in_favorites('Фильм в жанре фантастике')
        assert len(collector.get_list_of_favorites_books()) == 1 and collector.favorites[0] == 'Фильм в жанре фантастике'

    def test_add_book_in_favorites_add_same_name_book(self):
        collector = BooksCollector()
        collector.add_new_book('Фильм в жанре ужасов')
        collector.add_book_in_favorites('Фильм в жанре ужасов')
        collector.add_book_in_favorites('Фильм в жанре ужасов')
        assert len(collector.get_list_of_favorites_books()) == 1

    def test_delete_book_from_favorites_remove_book(self):
        collector = BooksCollector()
        collector.add_new_book('Фильм в жанре мультфильмы')
        collector.add_book_in_favorites('Фильм в жанре мультфильмы')
        collector.delete_book_from_favorites('Фильм в жанре мультфильмы')
        assert len(collector.favorites) == 0
