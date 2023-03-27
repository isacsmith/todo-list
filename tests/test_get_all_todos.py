import pytest
import mock

from todo_list import app


@pytest.mark.parametrize(
    "list_of_todos, expected_output",
    [
        (
            [
                app.Todo(description="item1", deadline="2023-03-01", priority=1),
                app.Todo(description="item2", deadline="2023-02-02", priority=0),
            ],
            2,
        ),
        ([app.Todo(description="item1", deadline="2023-03-01", priority=1)], 1),
        ([], 0)
    ],
)
def test_get_all_todos(list_of_todos, expected_output):
    with mock.patch("todo_list.app.Todo") as mock_todo:
        mock_todo.query.all = mock.MagicMock(return_value=list_of_todos)
        result = app.get_all_todos()
        assert len(result[0]["Todo list"]) == expected_output
