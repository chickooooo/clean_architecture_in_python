"""
- get_todo is called
- return none if invalid todo id
- return Todo if valid todo id

- change_todo_status is called
- return Error if any error
- return updated Todo if valid todo id

"""


from unittest.mock import Mock
from domain.usecases.todo_usecase import TodoUsecase
from domain.entities.todo import Todo
from core.error import Error


mock = Mock()
usecase = TodoUsecase(mock)


def test_get_todo_called():
    # arrange

    # act
    usecase.get_todo(id=10)

    # assert
    mock.get_todo.assert_called_once()


def test_get_none():
    # arrange
    mock.get_todo.return_value = None

    # act
    result = usecase.get_todo(id=10)

    # assert
    assert result is None


def test_get_todo():
    # arrange
    todo = Todo(1, "buy milk", False)
    mock.get_todo.return_value = todo

    # act
    result = usecase.get_todo(id=10)

    # assert
    assert result == todo


def test_change_todo_called():
    # arrange

    # act
    usecase.change_todo_status(id=10, new_status=True)

    # assert
    mock.change_todo_status.assert_called_once()


def test_change_error():
    # arrange
    error = Error("invalid_todo")
    mock.change_todo_status.return_value = error

    # act
    result = usecase.change_todo_status(id=10, new_status=True)

    # assert
    assert result == error


def test_change_todo():
    # arrange
    todo = Todo(1, "buy milk", True)
    mock.change_todo_status.return_value = todo

    # act
    result = usecase.change_todo_status(id=1, new_status=True)

    # assert
    assert result == todo
