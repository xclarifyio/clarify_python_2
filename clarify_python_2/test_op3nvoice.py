import os
import o3v_connection
import o3v_audio

connection = None

def get_connection():

    global connection

    if connection == None:
        api_key = os.environ['API_KEY']
        connection = o3v_connection.Connection(api_key)

    return connection

def test_bundle_list():

    conn = get_connection()
    bl = o3v_audio.get_bundle_list(conn)

    assert bl != None


# def test_func_succeed():
#     assert func(3) == 4

# def test_func_fail():
#     assert func(3) == 5
    
