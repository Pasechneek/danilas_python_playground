from first_package.parity import get_same_parity


class TestParity:
    def test_parity(self):
        assert get_same_parity([]) == []
        assert get_same_parity([1, 2, 3]) == [1, 3]
        assert get_same_parity([1, 2, 8]) == [1]
        assert get_same_parity([2, 2, 8]) == [2, 2, 8]
        assert get_same_parity([1, 2, -3]) == [1, -3]
        assert get_same_parity([-3, 2, 1]) == [-3, 1]
        assert get_same_parity([4, 1, 8]) == [4, 8]
