from first_package.out_of_range_exercise import get


class TestClass:
    cities = ["moscow", "london", "berlin", "porto", "", None, True]

    def test_get_1(self):
        assert get(self.cities, 0) == "moscow"

    def test_get_2(self):
        assert get(self.cities, 2, "default") == "berlin"

    def test_get_3(self):
        assert get(self.cities, 7, False) is False

    def test_get_4(self):
        assert get(self.cities, -1, "oops") is True

    def test_get_5(self):
        assert get(self.cities, 7) is None

    def test_get_6(self):
        assert get(self.cities, 4) == ""

    def test_get_7(self):
        assert get(self.cities, 5, "default") is None

    def test_get_8(self):
        assert get(self.cities, -7, "default") == "moscow"

    def test_get_9(self):
        assert get(self.cities, -9, "default") == "default"
