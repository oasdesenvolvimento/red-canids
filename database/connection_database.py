from mongoengine import connect


def connect_database():
    """
    Connect database
    :return:
    """
    connection = ("mongodb+srv://mios:diHUOzwzGk0FNorQ@red-canids-cluster.kg3ok6e.mongodb.net/"
                  "red-canids?retryWrites=true&w=majority")
    connect(host=connection)
    return True

