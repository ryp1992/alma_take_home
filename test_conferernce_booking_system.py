import unittest
import conferenceBookingSystem
import coverage



class ConferenceBookingSystemTestFunction(unittest.TestCase):

    def test_check_basic_overlap(self):
        room1 = conferenceBookingSystem.ConferenceBookingSystem([(10, 20), (20, 30)])
        self.assertEqual(room1.book(5, 15), False)

    def test_check_if_interval_removed(self):
        room1 = conferenceBookingSystem.ConferenceBookingSystem([(10, 20), (20, 30), (40, 50)])
        # remove interval 20,30 from booking list
        room1.remove_interval(20, 30)

        # If not removed from the list double booking is not allowed and this test case would fail
        self.assertEqual(room1.book(20, 30), True)


if __name__ == '__main__':
    cov = coverage.Coverage()
    cov.start()
    unittest.main()
    cov.stop()
    cov.report()

