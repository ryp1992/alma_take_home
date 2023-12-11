from sortedcontainers import SortedList
import csv


class ConferenceBookingSystem:

    def __init__(self, input_list=[]):
        self.booked_intervals = SortedList(input_list)

    # Time Complexity O(LogN if list size in N)
    def book(self, start, end):
        idx = self.booked_intervals.bisect_right((start, end))
        if (idx > 0 and self.booked_intervals[idx - 1][1] > start) or (
                idx < len(self.booked_intervals) and self.booked_intervals[idx][0] < end):
            return False
        self.booked_intervals.add((start, end))
        return True

    def remove_interval(self, start, end):
        self.booked_intervals.remove((start, end))
