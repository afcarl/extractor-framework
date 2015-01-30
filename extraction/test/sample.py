'''This module contains a sample use case for the library.

It's just a demo, so for example, the EmailExtractor is quite simplistic.
'''

from extraction.core import ExtractionRunner
from extraction.runnables import Filter, Extractor
import xmltodict
import extraction.utils as utils
import re
import subprocess32 as subproces

class HasNumbersFilter(Filter):
   def filter(self, data, deps):
      success = re.search(r'[0-9]', data, re.UNICODE)
      return bool(success)

class EmailExtractor(Extractor):
   @staticmethod
   def dependencies():
      return [HasNumbersFilter]

   def extract(self, data, deps):
      emails = re.findall(r'\b[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,4}\b',
                        data,
                        re.IGNORECASE | re.UNICODE)
      return {'email': emails}

class LinesStartWithNumberExtractor(Extractor):
   @staticmethod
   def dependencies():
      return [HasNumbersFilter]

   def extract(self, data, deps):
      try:
         (status, stdout, stderr) = utils.external_process(data, ['awk', '/^[0-9]/ {print;}', '-'], timeout=5)
      except subprocess.TimeoutExpired:
         raise RunnableError('awk timed out')

      lines = [line for line in stdout.split("\n") if line]
      return {'line': lines}

extraction_runner = ExtractionRunner()
extraction_runner.add_runnable(HasNumbersFilter)
extraction_runner.add_runnable(EmailExtractor)
extraction_runner.add_runnable(LinesStartWithNumberExtractor)

print extraction_runner.run(u'''Random data inputted with some emails bob@example.com
523 And some more text with @ signs now and then. Meet you@home@2p.m.
      And some more stuff. howie009@yahoo.com
      jones@gmail.com fredie@emerson.retail.com
123 bobbie@ist.psu.edu and that's all the text here.''', pretty=True)

print '\n\n\n'


print extraction_runner.run(u'Silly texy with email email@example.com but no numbers', pretty=True)


print '\n\n\n'
print extraction_runner.run_from_file('extraction/test/sample_files/file_sample.txt', pretty=True)

      
      
