from ting_file_management.priority_queue import PriorityQueue
import pytest


def test_basic_priority_queueing():
    priority_queue = PriorityQueue()

    assert len(priority_queue) == 0
    priority_queue.enqueue({"qtd_linhas": 3})
    assert len(priority_queue) == 1
    priority_queue.enqueue({"qtd_linhas": 8})
    assert len(priority_queue) == 2

    item = priority_queue.dequeue()
    assert item == {"qtd_linhas": 3}
    assert len(priority_queue) == 1

    priority_queue.enqueue({"qtd_linhas": 4})
    priority_queue.enqueue({"qtd_linhas": 7})

    assert priority_queue.search(0) == {"qtd_linhas": 4}
    assert priority_queue.search(1) == {"qtd_linhas": 8}
    assert priority_queue.search(2) == {"qtd_linhas": 7}
    with pytest.raises(IndexError):
        priority_queue.search(4)

    assert priority_queue.is_priority({"qtd_linhas": 3}) is True
    assert priority_queue.is_priority({"qtd_linhas": 5}) is False
