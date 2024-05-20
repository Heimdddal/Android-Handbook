import unittest
from ValidationHelper import Validation
from datetime import datetime, timedelta

# Корректные даты
date_correct = [
    "2024-05-19",  # Вчера
    "2024-05-20",  # Сегодня
    "2023-12-31",  # Прошлый год
    "2022-11-30",  # Прошлый год
    "2021-06-15",  # Прошлый год
    "2020-01-01",  # Прошлый год
    "2019-05-20",  # Прошлый год
    "2018-10-10",  # Прошлый год
    "2017-07-07",  # Прошлый год
    "2016-08-15",  # Прошлый год
    "2015-09-25",  # Прошлый год
    "2014-03-03",  # Прошлый год
]

# Некорректные даты
date_uncorrect = [
    "2024-05-21",  # Завтра
    "2025-01-01",  # Будущее
    "invalid-date",  # Некорректный формат
    "2024-13-01",  # Некорректный месяц
    "2024-00-01",  # Некорректный месяц
    "2024-05-32",  # Некорректный день
    "2024-02-30",  # Некорректный день (в феврале нет 30 дней)
    "2023-02-29",  # Некорректный день (2023 не високосный год)
    "2024-12-32",  # Некорректный день
    "2024-04-31",  # Некорректный день (в апреле 30 дней)
    "2024-00-00",  # Некорректный месяц и день
    "abcd-ef-gh",  # Некорректный формат
]

class DateValidationTest(unittest.TestCase):
    def test_T_date(self):
        for date_str in date_correct:
            self.assertTrue(Validation.ValidateDate(date_str))
    
    def test_F_date(self):
        for date_str in date_uncorrect:
            self.assertFalse(Validation.ValidateDate(date_str))

if __name__ == '__main__':
    unittest.main()
