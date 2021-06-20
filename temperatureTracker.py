# Temperature Tracker
import unittest


class TempTracker(object):
    """ Methods to find the max, min and mean temperature
    """
    def __init__(self):
        """ Initialize variables
        """
        self.temps = [0] * 111
        self.maxTemp = -1
        self.minTemp = 111
        self.meanTemp = None
        self.total = 0
        self.count = 0

    def insert(self, inputTemp):
        """ Insert Temperature
            Checks if input is an integer.
            Finds min, max and mean
            Args:
                inputTemp(int): Temperature Value between 0 -  110
        """
        if isinstance(inputTemp, int):
            if inputTemp < 0 or inputTemp > 110:
                raise ValueError("Temperature out of range!")
            else:
                self.temps[inputTemp] += 1
                self.count += 1
                if inputTemp < self.minTemp:
                    self.minTemp = inputTemp
                if inputTemp > self.maxTemp:
                    self.maxTemp = inputTemp

                self.total += inputTemp
                self.meanTemp = float(self.total/self.count)

    def get_maxTemp(self):
        """ Checks if maxTemp is out of range
            Returns:
                maxTemp(int): Highest max temperature so far
        """
        maxTemp = self.maxTemp
        if maxTemp == -1:
            maxTemp = None

        return maxTemp

    def get_minTemp(self):
        """ Checks if minTemp is out of range
            Returns:
                maxTemp(int): Lowest min temperature so far
        """
        minTemp = self.minTemp
        if minTemp == 111:
            minTemp = None

        return minTemp

    def get_meanTemp(self):
        """Returns:
            meanTemp(float): Mean of all temperatures
        """
        return self.meanTemp


# Tests
class Test_tempTracker(unittest.TestCase):
    """ Tests for TempTracker
        - Setup
        - _Test_tracker
        - Test None
        - Test Null
        - Test 0-4 series
        - Test Extreme Temps
    """
    def setUp(self):
        """ Initializes TempTracker object
        """
        self.tracker = TempTracker()

    def _test_tracker(self, temps, max, min, mean):
        """ Test Tracker [Internal]:
                Performs the functions of:
                insert, get_min, get_max & get_mean
                for the input list of temperatures
            Args:
                temps(list): List of temperatures
                max(int): Max Temperature
                min(int): Min Temperature
                mean(float): Mean of all temperatures
        """
        if type(temps) == list and temps != None:
            for temp in temps:
                self.tracker.insert(temp)

            self.assertEqual(self.tracker.get_maxTemp(), max)
            self.assertEqual(self.tracker.get_minTemp(), min)
            self.assertEqual(self.tracker.get_meanTemp(), mean)

    def test_none(self):
        """ Test None: None Values
        """
        self._test_tracker(None, None, None, None)

    def test_null(self):
        """ Test NonList: Input Temp/s not in a list
        """
        self._test_tracker([], None, None, None)

    def test_temp0(self):
        """ Test 0: Temperature: [0]
        """
        self._test_tracker([0], 0, 0, 0)

    def test_temp1(self):
        """ Test 1: Temperatures: [0, 1]
        """
        self._test_tracker([0, 1], 1, 0, 1/2.0)

    def test_temp2(self):
        """ Test 2: Temperatures: [0, 10, 30]
        """
        self._test_tracker([0, 10, 30], 30, 0, 40/3.0)

    def test_temp3(self):
        """ Test 3: Temperatures: [50, 80, 110]
        """
        self._test_tracker([50, 80, 110], 110, 50, 240/3.0)

    def test_temp4(self):
        """ Test 4: Temperatures: [50, 85.6, 110] - Value as float
        """
        self._test_tracker([50, 85.6, 110], 110, 50, 160/2.0)

    def test_tempExtremes(self):
        """ Test Extremes: Temperature values outside the range(0-110)
        """
        self.assertRaises(Exception, self.tracker.insert, -10)
        self.assertRaises(Exception, self.tracker.insert, 150)

unittest.main(verbosity=2)
