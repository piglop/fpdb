#!/usr/bin/python

#Copyright 2008 Carl Gherardi
#This program is free software: you can redistribute it and/or modify
#it under the terms of the GNU Affero General Public License as published by
#the Free Software Foundation, version 3 of the License.
#
#This program is distributed in the hope that it will be useful,
#but WITHOUT ANY WARRANTY; without even the implied warranty of
#MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
#GNU General Public License for more details.
#
#You should have received a copy of the GNU Affero General Public License
#along with this program. If not, see <http://www.gnu.org/licenses/>.
#In the "official" distribution you can find the license in
#agpl-3.0.txt in the docs folder of the package.


import os
import sys

# sys.path[0] holds the directory run_fpdb.py is in
sys.path[0] = sys.path[0]+os.sep+"pyfpdb"
os.chdir(sys.path[0])
#print "sys.path[0] =", sys.path[0], "cwd =", os.getcwd()

import fpdb


if __name__ == "__main__":
    me = fpdb.fpdb()
    me.main()
    exit()
