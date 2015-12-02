# -*- coding: utf-8 -*-
##############################################################################
#
#    Author: Dave Lasley <dave@laslabs.com>
#    Copyright: 2015 LasLabs, Inc [https://laslabs.com]
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

from setuptools import Command


class Tests(Command):
    
    TEST_RESULTS = '_results'
    user_options = [] #< For Command API compatibility
    
    def initialize_options(self, ):
        pass
    
    def finalize_options(self, ):
        pass
    
    def run(self, ):
        ''' Perform imports inside run to avoid errors before installs '''
        
        from xmlrunner import XMLTestRunner
        from unittest import TestLoader
        from os import path
        
        loader = TestLoader()
        tests = loader.discover('.', 'test_*.py')
        t = XMLTestRunner(verbosity=1, output=self.TEST_RESULTS)
        t.run(tests)
