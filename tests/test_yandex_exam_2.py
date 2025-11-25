from first_package import yandex_exam_2


class TestYandexExam2:
    def test_yandex_exam_2(self):
        assert yandex_exam_2.maximize_a_using_b("123", "987") == "987"
