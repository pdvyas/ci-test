"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

import nose.tools as nt

class TestFruit(object):
    def test_nose_pass(self):
        nt.assert_true(True)

    def test_nose_fail(self):
        nt.assert_true(False)

