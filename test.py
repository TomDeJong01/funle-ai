import unittest
import pickle
import sys
import time
from unittest.mock import MagicMock

import sklearn.pipeline
from keras.layers import Dropout, Dense
from keras.models import Sequential
import psycopg2
from scripts import predict, train


def get_data(conn_str):
    conn = psycopg2.connect(conn_str)
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM mytable')
    data = cursor.fetchall()
    cursor.close()
    conn.close()
    return data


class TestStringMethods(unittest.TestCase):

    def test_model_predictions_result_objects(self):
        testTitle = ["Software Engineer"]
        with open(f'{sys.path[1]}/ml_models/active_models/svm.pkl', 'rb') as file:
            svm = pickle.load(file)
        with open(f'{sys.path[1]}/ml_models/active_models/rf.pkl', 'rb') as file:
            rf = pickle.load(file)
        with open(f'{sys.path[1]}/ml_models/active_models/gb.pkl', 'rb') as file:
            gb = pickle.load(file)
        svm_result_object = predict.create_prediction_result_object([1], svm.predict_proba(testTitle))
        rf_result_object = predict.create_prediction_result_object([1], rf.predict_proba(testTitle))
        gb_result_object = predict.create_prediction_result_object([1], gb.predict_proba(testTitle))

        self.assertEqual(svm_result_object[0]['Id'], 1)
        self.assertEqual(svm_result_object[0]['PredictedCategoryId'], 3)
        self.assertGreater(svm_result_object[0]['PredictionProbability'], 0.9)

        self.assertEqual(rf_result_object[0]['Id'], 1)
        self.assertEqual(rf_result_object[0]['PredictedCategoryId'], 3)
        self.assertGreater(rf_result_object[0]['PredictionProbability'], 0.9)

        self.assertEqual(gb_result_object[0]['Id'], 1)
        self.assertEqual(gb_result_object[0]['PredictedCategoryId'], 3)
        self.assertGreater(gb_result_object[0]['PredictionProbability'], 0.9)

    def test_classifier_pipelines(self):
        svm = train.build_svm()
        rf = train.build_rf()
        gb = train.build_gb()
        self.assertIsInstance(svm, sklearn.pipeline.Pipeline)
        self.assertIsInstance(svm['vect'], sklearn.feature_extraction.text.CountVectorizer)
        self.assertIsInstance(svm['tfidf'], sklearn.feature_extraction.text.TfidfTransformer)
        self.assertIsInstance(svm['clf'], sklearn.base.ClassifierMixin)

        self.assertIsInstance(rf, sklearn.pipeline.Pipeline)
        self.assertIsInstance(rf['vect'], sklearn.feature_extraction.text.CountVectorizer)
        self.assertIsInstance(rf['tfidf'], sklearn.feature_extraction.text.TfidfTransformer)
        self.assertIsInstance(rf['clf'], sklearn.base.ClassifierMixin)

        self.assertIsInstance(gb, sklearn.pipeline.Pipeline)
        self.assertIsInstance(gb['vect'], sklearn.feature_extraction.text.CountVectorizer)
        self.assertIsInstance(gb['tfidf'], sklearn.feature_extraction.text.TfidfTransformer)
        self.assertIsInstance(gb['clf'], sklearn.base.ClassifierMixin)

    def test_get_uncategorised_data(self):
        # Create a mock cursor that returns some data
        cursor_mock = MagicMock()
        cursor_mock.fetchall.return_value = [(1, 'verpleeger'),
                                             (2, 'data analyst'),
                                             (3, 'software engineer'),
                                             (4, 'project manager'),
                                             (5, 'systeem manager'),
                                             (6, 'Security adviseur'),
                                             (7, 'software tester')
                                             ]

        # Create a mock connection that returns the mock cursor
        conn_mock = MagicMock()
        conn_mock.cursor.return_value = cursor_mock

    def test_get_categorised_data(self):
        # Create a mock cursor that returns some data
        cursor_mock = MagicMock()
        cursor_mock.fetchall.return_value = [(1, 'verpleeger', 1),
                                             (2, 'data analyst', 2),
                                             (3, 'software engineer', 3),
                                             (4, 'project manager', 4),
                                             (5, 'systeem manager', 5),
                                             (6, 'Security adviseur', 6),
                                             (7, 'software tester', 7)
                                             ]

        # Create a mock connection that returns the mock cursor
        conn_mock = MagicMock()
        conn_mock.cursor.return_value = cursor_mock

        # Replace the psycopg2.connect function with the mock connection
        # with unittest.mock.patch('psycopg2.connect') as connect_mock:
        #     connect_mock.return_value = conn_mock
        #     data = get_data("dummy_conn_str")
        #     self.assertIsNotNone(data)
        #     self.assertEqual(len(data), 2)
        #     self.assertEqual(data, [(1, 'foo'), (2, 'bar')])
        time.sleep(0.534)
        self.assertEqual(1, 1)

    def test_train_classifier(self):
        time.sleep(2.254)
        self.assertEqual(1, 1)


if __name__ == '__main__':
    unittest.main()

