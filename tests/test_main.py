from main import task_1, task_2, task_4


class TestSmth:
    def test_task1(self):
        for i in task_1():
            for x, y in i.items():
                assert 'Россия' in y

    def test_task2(self):
        for item in task_2():
            count = 0
            for x in task_2():
                if item == x:
                    count += 1
                    assert count == 1

    def test_task4(self):
        assert task_4() == 'yandex'