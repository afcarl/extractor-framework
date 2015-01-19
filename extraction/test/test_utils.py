import unittest
import extraction.utils as utils

class TestExtractionRunner(unittest.TestCase):
   def setUp(self):
      pass

   def test_external_process_works(self):
      (status, out, err) = utils.external_process('Line 1\nLine 2\nLine 3\n', ['grep', '3'])
      self.assertEqual(status, 0)
      self.assertEqual(out, 'Line 3\n')
      self.assertEqual(err, '')

   def test_external_process_returns_status_code(self):
      (status, out, err) = utils.external_process('', ['true'])
      self.assertEqual(status, 0)
      (status, out, err) = utils.external_process('', ['false'])
      self.assertEqual(status, 1)
      
