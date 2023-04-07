from abc import ABC, abstractmethod
from domain.entities.todo import Todo
from core.error import Error


class RemoteDatasource(ABC):
    @abstractmethod
    def get_todo(self, id: int) -> Todo | None:
        pass

    @abstractmethod
    def change_todo_status(self, id: int, new_status: bool) -> Todo | Error:
        pass
