import pytest

from main import BooksCollector


class TestBooksCollector:

    def test_add_new_book_add_two_books(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        assert len(collector.get_books_genre()) == 2

    @pytest.mark.parametrize('name', ['А', 'Мастер и Маргарита', 'К' * 39, 'К' * 40])
    def test_add_new_book_valid_name_length_book_added(self, name):
        collector = BooksCollector()
        collector.add_new_book(name)
        assert name in collector.get_books_genre()

    @pytest.mark.parametrize('name', ['', 'К' * 41, 'К' * 50])
    def test_add_new_book_invalid_name_length_book_not_added(self, name):
        collector = BooksCollector()
        collector.add_new_book(name)
        assert collector.get_books_genre() == {}

    def test_add_new_book_same_book_twice_added_once(self):
        collector = BooksCollector()
        collector.add_new_book('Дюна')
        collector.add_new_book('Дюна')
        assert len(collector.get_books_genre()) == 1

    def test_add_new_book_new_book_has_no_genre(self):
        collector = BooksCollector()
        collector.add_new_book('Дюна')
        assert collector.get_book_genre('Дюна') == ''

    @pytest.mark.parametrize('genre', ['Фантастика', 'Ужасы', 'Детективы', 'Мультфильмы', 'Комедии'])
    def test_set_book_genre_genre_from_list_genre_set(self, genre):
        collector = BooksCollector()
        collector.add_new_book('Дюна')
        collector.set_book_genre('Дюна', genre)
        assert collector.get_book_genre('Дюна') == genre

    def test_set_book_genre_genre_not_from_list_genre_not_set(self):
        collector = BooksCollector()
        collector.add_new_book('Дюна')
        collector.set_book_genre('Дюна', 'Роман')
        assert collector.get_book_genre('Дюна') == ''

    def test_set_book_genre_book_not_in_collection_book_not_added(self):
        collector = BooksCollector()
        collector.set_book_genre('Дюна', 'Фантастика')
        assert collector.get_books_genre() == {}

    def test_get_book_genre_book_not_in_collection_returns_none(self):
        collector = BooksCollector()
        assert collector.get_book_genre('Дюна') is None

    def test_get_books_with_specific_genre_returns_only_books_of_this_genre(self):
        collector = BooksCollector()
        collector.add_new_book('Дюна')
        collector.add_new_book('Оно')
        collector.add_new_book('Солярис')
        collector.set_book_genre('Дюна', 'Фантастика')
        collector.set_book_genre('Оно', 'Ужасы')
        collector.set_book_genre('Солярис', 'Фантастика')
        assert collector.get_books_with_specific_genre('Фантастика') == ['Дюна', 'Солярис']

    def test_get_books_with_specific_genre_genre_not_from_list_returns_empty_list(self):
        collector = BooksCollector()
        collector.add_new_book('Дюна')
        collector.set_book_genre('Дюна', 'Фантастика')
        assert collector.get_books_with_specific_genre('Роман') == []

    def test_get_books_genre_returns_dict_with_books_and_genres(self):
        collector = BooksCollector()
        collector.add_new_book('Дюна')
        collector.add_new_book('Оно')
        collector.set_book_genre('Дюна', 'Фантастика')
        assert collector.get_books_genre() == {'Дюна': 'Фантастика', 'Оно': ''}

    @pytest.mark.parametrize('genre', ['Фантастика', 'Мультфильмы', 'Комедии'])
    def test_get_books_for_children_genre_without_age_rating_book_in_list(self, genre):
        collector = BooksCollector()
        collector.add_new_book('Книга для всех')
        collector.set_book_genre('Книга для всех', genre)
        assert collector.get_books_for_children() == ['Книга для всех']

    @pytest.mark.parametrize('genre', ['Ужасы', 'Детективы'])
    def test_get_books_for_children_genre_with_age_rating_book_not_in_list(self, genre):
        collector = BooksCollector()
        collector.add_new_book('Взрослая книга')
        collector.set_book_genre('Взрослая книга', genre)
        assert collector.get_books_for_children() == []

    def test_add_book_in_favorites_book_from_collection_added(self):
        collector = BooksCollector()
        collector.add_new_book('Дюна')
        collector.add_book_in_favorites('Дюна')
        assert collector.get_list_of_favorites_books() == ['Дюна']

    def test_add_book_in_favorites_book_not_in_collection_not_added(self):
        collector = BooksCollector()
        collector.add_book_in_favorites('Дюна')
        assert collector.get_list_of_favorites_books() == []

    def test_add_book_in_favorites_same_book_twice_added_once(self):
        collector = BooksCollector()
        collector.add_new_book('Дюна')
        collector.add_book_in_favorites('Дюна')
        collector.add_book_in_favorites('Дюна')
        assert collector.get_list_of_favorites_books() == ['Дюна']

    def test_delete_book_from_favorites_book_in_favorites_deleted(self):
        collector = BooksCollector()
        collector.add_new_book('Дюна')
        collector.add_book_in_favorites('Дюна')
        collector.delete_book_from_favorites('Дюна')
        assert collector.get_list_of_favorites_books() == []

    def test_get_list_of_favorites_books_returns_all_favorite_books(self):
        collector = BooksCollector()
        collector.add_new_book('Дюна')
        collector.add_new_book('Солярис')
        collector.add_book_in_favorites('Дюна')
        collector.add_book_in_favorites('Солярис')
        assert collector.get_list_of_favorites_books() == ['Дюна', 'Солярис']
