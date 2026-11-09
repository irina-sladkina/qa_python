# qa_python

Юнит-тесты для класса `BooksCollector` (файл `main.py`). Тесты написаны на pytest и находятся в файле `tests.py`.

## Запуск тестов

```
pytest -v tests.py
```

## Реализованные тесты

### add_new_book
- `test_add_new_book_add_two_books` — можно добавить две книги.
- `test_add_new_book_valid_name_length_book_added` — книга с названием длиной от 1 до 40 символов добавляется (параметризованный).
- `test_add_new_book_invalid_name_length_book_not_added` — книга с пустым названием или названием длиннее 40 символов не добавляется (параметризованный).
- `test_add_new_book_same_book_twice_added_once` — одну и ту же книгу нельзя добавить дважды.
- `test_add_new_book_new_book_has_no_genre` — у добавленной книги нет жанра.

### set_book_genre
- `test_set_book_genre_genre_from_list_genre_set` — книге устанавливается любой жанр из списка `genre` (параметризованный).
- `test_set_book_genre_genre_not_from_list_genre_not_set` — жанр не из списка не устанавливается.
- `test_set_book_genre_book_not_in_collection_book_not_added` — установка жанра книге, которой нет в коллекции, не добавляет её.

### get_book_genre
- `test_get_book_genre_book_not_in_collection_returns_none` — для книги, которой нет в коллекции, возвращается `None`.

### get_books_with_specific_genre
- `test_get_books_with_specific_genre_returns_only_books_of_this_genre` — возвращаются только книги указанного жанра.
- `test_get_books_with_specific_genre_genre_not_from_list_returns_empty_list` — для жанра не из списка возвращается пустой список.

### get_books_genre
- `test_get_books_genre_returns_dict_with_books_and_genres` — возвращается словарь с книгами и их жанрами.

### get_books_for_children
- `test_get_books_for_children_genre_without_age_rating_book_in_list` — книги жанров без возрастного рейтинга попадают в список для детей (параметризованный).
- `test_get_books_for_children_genre_with_age_rating_book_not_in_list` — книги жанров с возрастным рейтингом не попадают в список для детей (параметризованный).

### add_book_in_favorites
- `test_add_book_in_favorites_book_from_collection_added` — книга из коллекции добавляется в избранное.
- `test_add_book_in_favorites_book_not_in_collection_not_added` — книга, которой нет в коллекции, не добавляется в избранное.
- `test_add_book_in_favorites_same_book_twice_added_once` — одну книгу нельзя добавить в избранное дважды.

### delete_book_from_favorites
- `test_delete_book_from_favorites_book_in_favorites_deleted` — книга удаляется из избранного.

### get_list_of_favorites_books
- `test_get_list_of_favorites_books_returns_all_favorite_books` — возвращается список всех избранных книг.
