from user import User
user = User('Ali','Valiyev',2000,'Tadbirkor')


def test_user():
    assert type(user.name) == str , 'should be str'
    assert type(user.last_name) == str , 'should be str'
    assert type(user.ocupation) == str , 'should be str'
    assert type(user.age) == int , 'should be int'


