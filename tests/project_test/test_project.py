from project.hash_functions import store_password, delete_password, retrieve_password
from project.generate_password import generate, generate_password, hash_password
import time
import pytest


# Генерим пароль перед запуском тестов, где нужен пароль
@pytest.fixture
def get_password():
    return generate_password(10)

# Генерим пароль перед запуском тестов, где нуден хэш
@pytest.fixture
def get_hash():
    return hash_password(generate_password(10))


# Время генерации пароля + его хэширование < 10 секунд
def test_time():
    start_time = time.time()
    generate()
    end_time = time.time()

    assert end_time - start_time < 10

# Проверка правильности параметров при работе функции store_password
@pytest.mark.parametrize("service, username, password, result",
                         [("example.com", "user123", "111", "password absolutely wrong"),
                          ("example.com", "user123", "101010", "store has been done"),
                          ("example.com", "no_name_user", "111", "failed operation"),
                          ("google.com", "user123", "111", "failed operation")])
def test_store(service, username, password, result):
    assert store_password(service, username, password) == result

# Проверка правильноси параметров при работе с функцией retrieve_password ( извлечение пароля )
@pytest.mark.parametrize("service, username, result",
                         [("example.com", "user123", "complete retrieve"),
                          ("example.com", "no_name_user", "retrieve failed"),
                          ("rka680@mail.ru", "user123", "retrieve failed")])
def test_retrieve(service, username, result):
    assert retrieve_password(service, username) == result

# Проверка на то, что в пароле обязательно должна быть хотя бы одна цифра
def test_generation_of_password(get_password):
    flag_digits_letters = get_password.isalnum()
    # Должны быть не только цифры или буквы
    assert False == flag_digits_letters

# Проверка на длину хэша
def test_hash_length(get_hash):
    assert len(get_hash) > 40


# Проверка на то, что в хэше должны находится только буквы и цифры
def test_hash_contain(get_hash):
    assert True == get_hash.isalnum()
