import types


def flat_generator(list_of_lists):
    ind = 0
    while len(list_of_lists) > ind:
        list_items = [list_of_lists[ind]]
        if isinstance(list_items, list):
            list_items = recurs_get_item(list_items)
        ind += 1

        for item in list_items:
            yield item


def recurs_get_item(list_items):
    new_list = []
    for item in list_items:
        if isinstance(item, list):
            new_list.extend(recurs_get_item(item))
        else:
            new_list.append(item)

    return new_list


def test_4():

    list_of_lists_2 = [
        [['a'], ['b', 'c']],
        ['d', 'e', [['f'], 'h'], False],
        [1, 2, None, [[[[['!']]]]], []]
    ]

    for flat_iterator_item, check_item in zip(
            flat_generator(list_of_lists_2),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None, '!']
    ):

        assert flat_iterator_item == check_item

    assert list(flat_generator(list_of_lists_2)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None, '!']

    assert isinstance(flat_generator(list_of_lists_2), types.GeneratorType)


if __name__ == '__main__':
    test_4()