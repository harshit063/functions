
class Course:
    def __int__(self, number, name, instructors, maxNumbofStudents):
        self._number=number
        self._name=name
        self._maxNumbofStudents=maxNumbofStudents
        self._instructors=instructors
     def get_number(self): return self.__number
     def get_name(self): return self._name
     def get_instructors(self): return self._instructors
     def get_maxNumbOfStudents(self): return self._maxNumbOfStudents
     # two string method
     def _str_(self): return self._name
class department:
     def __init__(self, name, courses):
        self._name=name
        self._course=course
    def get_name(self): return self._name
    def get_courses(self): return self._course
class Instructor:
    def __init__(self, id, name):
        Iself._id = id
        self._name = name
    def get_id(self): return self._id
    def get_name(self): return self._name
    def str_(self): return self._name
