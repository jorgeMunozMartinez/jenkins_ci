#!/usr/bin/env python3
import script

class Tests:

    def test_connection(self):
        assert 'uclm' == script.check('http://www.uclm.es')

