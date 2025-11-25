from first_package.agreg import AggregateSum


class TestAgreg:
    def test_agreg_1(self):
        assert AggregateSum.calculate_sum_1([]) == 0

    def test_agreg_2(self):
        assert AggregateSum.calculate_sum_1([3, 3, 3]) == 9

    def test_agreg_3(self):
        assert AggregateSum.calculate_sum_1([1, 2, 3]) == 3

    def test_agreg_4(self):
        assert AggregateSum.calculate_sum_1([3, 6, 9, 5]) == 18

    def test_agreg_5(self):
        assert AggregateSum.calculate_sum_2([]) == 0

    def test_agreg_6(self):
        assert AggregateSum.calculate_sum_2([3, 3, 3]) == 9

    def test_agreg_7(self):
        assert AggregateSum.calculate_sum_2([1, 2, 3]) == 3

    def test_agreg_8(self):
        assert AggregateSum.calculate_sum_2([3, 6, 9, 5]) == 18