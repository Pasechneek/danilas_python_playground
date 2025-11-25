from first_package.change_list import ChangeList


class TestChangeList:
    def test_change_list(self):
        items = [1, 2, 3, 4, 5]
        ChangeList.fill_with_first_1(items)
        assert items == ([1, 1, 1, 1, 1])
