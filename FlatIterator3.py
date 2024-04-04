class FlatIterator:

    def _pop_item(self):
        try:
            item = next(self.list_iters[len(self.list_iters)-1])
            if isinstance(item, list):
                self.list_iters.append(iter(item))
                item = self._pop_item()
        except StopIteration:
            # Из-за того, что среди элементов есть тип None
            # применим свой признак окончания перебора
            if len(self.list_iters) > 0:
                self.list_iters.pop()

            if len(self.list_iters) == 0:
                item = 'None element'
            else:
                item = self._pop_item()
        return item

    def __init__(self, list_of_list):
        self.list_of_list = list_of_list
        self.start = 0
        self.list_iters = [iter([])]
        self.end = len(self.list_of_list)

    def __iter__(self):
        self.current_index = self.start - 1
        return self

    def __next__(self):
        item = self._pop_item()
        if item == 'None element':
            self.current_index += 1
            if self.current_index >= self.end:
                raise StopIteration
            self.list_iters.append(iter(self.list_of_list[self.current_index]))
            item = self._pop_item()

        return item


def test_3():

    list_of_lists_2 = [
        [['a'], ['b', 'c']],
        ['d', 'e', [['f'], 'h'], False],
        [1, 2, None, [[[[['!']]]]], []]
    ]

    for flat_iterator_item, check_item in zip(
            FlatIterator(list_of_lists_2),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None, '!']
    ):

        assert flat_iterator_item == check_item

    assert list(FlatIterator(list_of_lists_2)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None, '!']


if __name__ == '__main__':
    test_3()