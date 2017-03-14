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
        self.assertTrue(len(response.data) > 0)
