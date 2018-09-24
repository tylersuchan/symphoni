import unittest

import join_button
import start_party_button
import music_queue

loader = unittest.TestLoader()
suite = unittest.TestSuite()
runner = unittest.TextTestRunner(verbosity=3)

suite.addTests(loader.loadTestsFromModule(join_button))
suite.addTests(loader.loadTestsFromModule(start_party_button))
suite.addTests(loader.loadTestsFromModule(music_queue))

runner.run(suite)
