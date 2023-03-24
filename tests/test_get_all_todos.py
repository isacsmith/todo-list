import mock
from todo_list import app

def test_empty_list_returned_if_no_todo_data():
    with mock.patch('todo_list.app.Todo') as mock_todo:
        mock_todo.query.all = mock.MagicMock(return_value = [{"id": 1, "description": "hi", "deadline": "2023-03-03", "priority": 1}])
        result = app.get_all_todos()

        print(result)



