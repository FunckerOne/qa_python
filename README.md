# qa_python
# unit tests for books collector
Проверки спроектированны на курсе "Автоматизатор тестирования на Python"

Тесты  находятся в файле [tests.py](tests.py)

Запустить все тесты через терминал: pytest tests.py -v

Тесты, в некоторых из которых, реализована параметризация:
  1. test_add_new_book_add_positive_name_books
  2. test_add_new_book_add_negative_name_books
  3. test_add_new_book_add_same_name_books
  4. test_set_book_genre_add_genre_book_positive_result
  5. test_set_book_genre_add_genre_is_not_list
  6. test_get_book_genre_for_name_positive_result
  7. test_get_books_with_specific_genre_get_book_name_with_specific_genre
  8. test_get_books_for_children_all_approved_books
  9. test_add_book_in_favorites_add_book
  10. test_add_book_in_favorites_add_same_name_book
  11. test_delete_book_from_favorites_remove_book
