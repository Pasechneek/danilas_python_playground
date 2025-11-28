from first_package.compact import Compact


class TestCompact:
    def test_compact(self):
        assert Compact.compact([1, None, 2, 3]) == [1, 2, 3]