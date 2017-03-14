from wger.core.tests.base_testcase import (
    STATUS_CODES_FAIL,
    WorkoutManagerTestCase,
)


class TestShowExerciseInfo(WorkoutManagerTestCase):
    """Tests for showing all info exercises"""

    def test_show_exercise_info(self):
        """Tests for showing all info exercises"""
        response = self.client.get('/api/v2/exerciseinfo/')
        self.assertEqual(response.status_code, 200)
        self.assertTrue(response.data['count'])
        self.assertTrue(str(response.data['results'][0]['status']) is not None)
        self.assertTrue(str(response.data['results'][
                        0]['description']) is not None)
        self.assertTrue(str(response.data['results'][0]['name']) is not None)
        self.assertTrue(str(response.data['results'][0][
                        'creation_date']) is not None)
        self.assertTrue(str(response.data['results'][0]['uuid']) is not None)
        self.assertTrue(str(response.data['results'][0]['license']) is not None)
        self.assertTrue(str(response.data['results'][
                        0]['category']) is not None)
        self.assertTrue(str(response.data['results'][
                        0]['language']) is not None)
        self.assertTrue(str(response.data['results'][0]['muscles']) is not None)
        self.assertTrue(str(response.data['results'][0][
                        'muscles_secondary']) is not None)
        self.assertTrue(str(response.data['results'][
                        0]['equipment']) is not None)
