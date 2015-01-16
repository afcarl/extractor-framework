class Base(object):
   def __init__(self):
      pass

   def check_dep_errors(self, dependency_results):
      deps = self.__class__.dependencies
      filter_deps = [e for e in deps if isinstance(e, Filter)]
      extractor_deps = [e for e in deps if isinstance(e, Extractor)]

      for filter in filter_deps:
         if not dependency_results[filter]:
            #TODO return result saying not run because filter failed
            return   

      for extractor in extractor_deps:
         if not dependency_results[extractor]: #check if extractor errored
            #TODO return result saying not run becaus eextractor failed
            return

      return None

class Filter(Base):
   def filter(self, data, dependency_results):
      return False

   def run(self, data, dependency_results):
      dep_errors =  super(Filter, self).check_dep_errors()
      if dep_errors:
         return dep_errors

      return self.filter(data, dependency_results)


class Extractor(Base):
   def extract(self, data, dependency_results):
      return 'TODO'

   def run(self, data, dependency_results):
      dep_errors = super(Extractor, self).check_dep_errors()
      if dep_errors:
         return dep_errors

      return self.extract(data, dependency_results)   