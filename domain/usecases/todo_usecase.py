from data.datasources.remote_datasource import RemoteDatasource
from domain.entities.todo import Todo
from core.error import Error


class TodoUsecase:
    def __init__(self, remote_datasource: RemoteDatasource) -> None:
        self.__remote_datasource = remote_datasource

    def get_todo(self, id: int) -> Todo | None:
        return self.__remote_datasource.get_todo(id)

    def change_todo_status(self, id: int, new_status: bool) -> Todo | Error:
        return self.__remote_datasource.change_todo_status(id, new_status)
