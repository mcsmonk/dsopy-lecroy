#  
# dsopy-lecroy
# Copyright (C) 2019 Sunghyun Jin
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

import numpy as np
import matplotlib.pyplot as plt
from lecroywin32com import LeCroyScope

ip = '127.0.0.1' # your dso ip address

dso = LeCroyScope(ip)
dso.clear()
desc = dso.get_wavedesc()
print(desc)

t2 = dso.get_waveform('C2')
t3 = dso.get_waveform('c3')

plt.plot(t2)
plt.plot(t3)
plt.show()

