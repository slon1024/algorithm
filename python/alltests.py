
import unittest
if __name__ == "__main__":
    import os, sys
    import glob


    dir_tests = 'tests'
    dirs=[ item for item in os.listdir('./tests')  if os.path.isdir( dir_tests + '/' + item) ]
    
    test_file_strings= [ y for x in dirs for y in glob.glob(dir_tests + '/' + x + '/*_test.py') ]
    module_strings = [  file_string[0:len(file_string) - 3].replace('/', '.') for file_string in test_file_strings]

    suites = [unittest.defaultTestLoader.loadTestsFromName(file_string) for file_string in module_strings]
    testSuite = unittest.TestSuite(suites)
    text_runner = unittest.TextTestRunner().run(testSuite)
