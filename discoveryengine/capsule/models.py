from __future__ import unicode_literals

# Create your models here.
class CapsuleObject(object):
    @property
    def API_PATH(self):
        raise NotImplementedError("API_PATH must be set in subclass")

class Person(CapsuleObject):
    TITLE_OPTIONS = [
        "Mr",
        "Master",
        "Mrs",
        "Miss",
        "Ms",
        "Dr",
    ]
    def __init__(self, first_name, last_name, title=None, job_title=None, about=None,organization_name=None,organization_id=None):
        self._first_name = first_name
        self._last_name = last_name
        self._title = title if title in TITLE_OPTIONS else raise AttributeError("Title must be one of the following: %s" % ", ".join(TITLE_OPTIONS))
        self._job_title = job_title
        self._about = about
        self._organization_name = organization_name
        self._organization_id = organization_id

    def title():
        doc = "The title of a Person."
        def fget(self):
            return self._title
        def fset(self, value):
            if value not in TITLE_OPTIONS:
                raise AttributeError("Title must be one of the following: %s" % ", ".join(TITLE_OPTIONS))
            self._title = value
        def fdel(self):
            del self._title
        return locals()
    title = property(**title())

    @property
    def first_name(self):
        """Get the first name of the Person"""
        return self._first_name

    @property
    def last_name(self):
        """Get the first name of the Person"""
        return self._last_name

    @property
    def job_title(self):
        """Get the first name of the Person"""
        return self._job_title

    @property
    def about(self):
        """Get the first name of the Person"""
        return self._about

    @property
    def organization_name(self):
        """Get the first name of the Person"""
        return self._organization_name

    @property
    def organization_id(self):
        """Get the first name of the Person"""
        return self._organization_id