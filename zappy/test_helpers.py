import mongoengine
from test_addons import MongoTestCase
from django.conf import settings


class MongoDBTestCase(MongoTestCase):

    def setUp(self):
        mongoengine.connection.disconnect()
        host = 'mongodb+srv://%s:%s@%s/%s' % (
            settings._MONGODB_TEST_USER, settings._MONGODB_TEST_PASSWD, settings._MONGODB_HOST,
            settings._MONGODB_TEST_NAME
        )
        mongoengine.connect(settings._MONGODB_TEST_NAME, host=host)
        super().setUpClass()

    def tearDown(self):
        from mongoengine.connection import get_connection, disconnect
        connection = get_connection()
        connection.drop_database(settings._MONGODB_TEST_NAME)
        disconnect()
        super().tearDownClass()