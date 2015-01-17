import extraction.runnables as runnables

class FilterWithoutDeps(runnables.Filter):
   def filter(self, data, dependencyResults):
      return self._filter_pass_xml()

class FilterWithDeps(runnables.Filter):
   @staticmethod
   def dependencies():
      return [FilterWithoutDeps]

   def filter(self, data, dependencyResults):
      return self._filter_pass_xml()

class PassFilter(runnables.Filter):
   def filter(self, data, dependencyResults):
      return self._filter_pass_xml()

class FailFilter(runnables.Filter):
   def filter(self, data, dependencyResults):
      return self._filter_fail_xml()


