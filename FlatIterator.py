class FlatIterator:

    def __init__(self, list_of_list):
        self.list_of_list = list_of_list
        self.curr_iter = iter([])
        self.start = 0
        self.end = len(self.list_of_list)

    def __iter__(self):
        self.current_index = self.start - 1
        return self

    def _pop_item(self):
        try:
            item = next(self.curr_iter)
        except StopIteration:
            # Из-за того, что среди элементов есть тип None
            # применим свой признак окончания перебора
            item = 'None element'
        return item

    def __next__(self):
        item = self._pop_item()
        if item == 'None element':
            self.current_index += 1
            if self.current_index >= self.end:
                raise StopIteration
            curr_el = self.list_of_list[self.current_index]
            self.curr_iter = iter(curr_el)
            item = self._pop_item()

        return item


def test_1():
    list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]

    for flat_iterator_item, check_item in zip(
            FlatIterator(list_of_lists_1),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
    ):
        assert flat_iterator_item == check_item

    assert list(FlatIterator(list_of_lists_1)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]


if __name__ == '__main__':
    test_1()
