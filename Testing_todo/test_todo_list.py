from typing import Literal
from todo_list import TodoList
import pytest

'''Testing the method get_todo'''

@pytest.mark.parametrize(
        'number, expected',[
            (1, {"id":1, "description":"Do the dishes", "completed":False}),
            (2, {"id":2,"description":"Walk my dog","completed":False}),
            (10, "todo with id 10 does not exist."),
            (20, "todo with id 20 does not exist")
            
        ]
    )

def test_get_todo(number,expected):

    
    #Arrange
    myList = TodoList()
    myList.add_todo("Do the dishes")
    myList.add_todo("Walk my dog")
    myList.add_todo("Finish my assignment")
    myList.add_todo("Watch Netflix")
    #Act and Assert

    if isinstance(expected, str):
        with pytest.raises(ValueError, match=expected): #Assert
            myList.get_todo(number) #Act

    else:
        assert myList.get_todo(number)==expected #Assert


''' Testing the method add_todo'''

@pytest.mark.parametrize(
        'task, expected',[
            ("Do groceries",{"id":2, "description":"Do groceries","completed":False}),
            ("Walk out the dog",{"id":2, "description":"Walk out the dog","completed":False})
        ]
)

def test_add_todo(task,expected):
    #Arrange
    myList = TodoList()
    myList.add_todo("Study JavaScript")
    #Act and Assert
    
    assert myList.add_todo(task) == expected


@pytest.mark.parametrize(
        'task, expected',[
        (1,{"id":1, "description":"Do groceries","completed":True}),
        (2,"todo with id 2 does not exist"),

        ]
)

def test_complete_todo(task,expected):
    #Arrange
    myList = TodoList()
    myList.add_todo("Do groceries")

    #Act
    
    if isinstance(expected,str):
        with pytest.raises(ValueError,match=expected):
            myList.complete_todo(task)
    else:
        myList.complete_todo(task)
        result=myList.get_todo(task)
        assert result==expected

@pytest.mark.parametrize(
        'task, expected',[
            (1,{"id":1,"description":"Do groceries","completed":False}),
            (2,"todo with id 2 does not exist")
        ]
)

def test_delete_todo(task,expected):
    #Arrange
    myList=TodoList()
    myList.add_todo("Do groceries")
    #Act
    if isinstance(expected,str):
        with pytest.raises(ValueError,match=expected):
            myList.delete_todo(task)
    #Assert
    else:
        assert myList.delete_todo(task)==expected

        with pytest.raises(ValueError, match="todo with id 1 does not exist"):
            myList.get_todo(task)


def test_get_all_todos():
    #Arrange
    myList=TodoList()
    myList.add_todo("Do groceries")
    myList.add_todo("Go to supermarket")

    #Act
    result=myList.get_all_todos()

    #Assert
    assert result==[{"id":1,"description":"Do groceries","completed":False},{"id":2,"description":"Go to supermarket","completed":False}]
