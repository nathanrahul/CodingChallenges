# Flattern Array Module
import unittest


def flattenArray(inputArray):
    """ Flattens an array of arbitarily nested arrays of intergers
        into a flat array.
        Ignores other types and only flattens integers in the arrays.
        Args:
            inputArray(list): A list of nested arrays
        Returns:
            result_array(list): A flattened array
    """
    resultArray = []
    for element in inputArray:
        if isinstance(element, int):
            resultArray.append(element)
        elif isinstance(element, list):
            resultArray += flattenArray(element)
        else:
            pass

    return resultArray


# Tests
class Test_flattenArray(unittest.TestCase):
    """ Tests for the flatten array function:
            - Test 01 - Empty Array
            - Test 02 series - String Type
            - Test 03 series - Float Type
            - Test 04 series - Integer Type
            - Test 05 - Repetitive value
    """
    def test_01_emptyArray(self):
        """ Test 01: An empty Array
        """
        inputArray = []
        result = []
        self.assertEqual(flattenArray(inputArray), result)

    def test_02_1_stringArray(self):
        """ Test 02_1: A complete string array
        """
        inputArray = ["a", "b", "c"]
        result = []
        self.assertEqual(flattenArray(inputArray), result)

    def test_02_2_oneItemStringArray(self):
        """ Test 02_2: One string item in array
        """
        inputArray = ["a", 1, 2]
        result = [1, 2]
        self.assertEqual(flattenArray(inputArray), result)

    def test_02_3_oneLevelStringArray(self):
        """ Test 02_3: One Level String in array
        """
        inputArray = [["a", "b"], 1, 2]
        result = [1, 2]
        self.assertEqual(flattenArray(inputArray), result)

    def test_03_1_floatArray(self):
        """ Test 03_1: A complete float array
        """
        inputArray = [0.0, 0.5, 1.0]
        result = []
        self.assertEqual(flattenArray(inputArray), result)

    def test_03_2_oneItemFloatArray(self):
        """ Test 03_2: One float item in array
        """
        inputArray = [0.5, 1, 2]
        result = [1, 2]
        self.assertEqual(flattenArray(inputArray), result)

    def test_03_2_oneLevelFloatArray(self):
        """ Test 03_2: One Level float in array
        """
        inputArray = [[0.5, 1.0], 1, 2]
        result = [1, 2]
        self.assertEqual(flattenArray(inputArray), result)

    def test_04_1_oneItemIntArray(self):
        """ Test 04_1: A single int item array
        """
        inputArray = [1]
        result = [1]
        self.assertEqual(flattenArray(inputArray), result)

    def test_04_2_oneLevelIntArray(self):
        """ Test 04_2: A single level int array
        """
        inputArray = [1, [2, 3], 4]
        result = [1, 2, 3, 4]
        self.assertEqual(flattenArray(inputArray), result)

    def test_04_3_twoLevelIntArray(self):
        """ Test 04_3: A nested two level int array
        """
        inputArray = [1, [2, 3], [4], 5]
        result = [1, 2, 3, 4, 5]
        self.assertEqual(flattenArray(inputArray), result)

    def test_04_4_threeLevelIntArray(self):
        """ Test 04_4: A nested three level int array
        """
        inputArray = [[1, 2], 3, 4, [5, 6, 7]]
        result = [1, 2, 3, 4, 5, 6, 7]
        self.assertEqual(flattenArray(inputArray), result)

    def test_04_5_arbitarilyNestedIntArray(self):
        """ Test 04_5: An arbitarily nested int array
        """
        inputArray = [[1, [2, [3, 4], [5], 6, [7]], [8, 9], 10]]
        result = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        self.assertEqual(flattenArray(inputArray), result)

    def test_05_repetitiveItemArray(self):
        """ Test 05: A nested array with repetitive items
        """
        inputArray = [1 ,2, [2, 3, [4], 4], 5]
        result = [1, 2, 2, 3, 4, 4, 5]
        self.assertEqual(flattenArray(inputArray), result)

unittest.main(verbosity=2)
