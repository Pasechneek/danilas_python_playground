from first_package import yandex_exam_1


class TestYandexExam:
    def test_yandex_exam_1(self):
        """test_str_1 is a correct input"""""
        test_str_1 = "4  \n 1 3 \n 3 1 \n 4 4 \n 7 1"
        assert yandex_exam_1.air_humidifier(test_str_1) == "3"

    def test_yandex_exam_2(self):
        """test_str_2 is a wrong input"""""
        test_str_2 = "3  \n 1 8 \n 10 11 \n 21 5"
        assert yandex_exam_1.air_humidifier(test_str_2) == "5"

    def test_yandex_exam_3(self):
        """test_str_3 is a wrong input"""""
        test_str_3 = "10  \n 2 1 \n 22 10 \n 26 17 \n 29 2 \n 45 20 \n 47 32 \n 72 12 \n 75 1 \n 81 31 \n 97 7"
        assert yandex_exam_1.air_humidifier(test_str_3) == "57"
