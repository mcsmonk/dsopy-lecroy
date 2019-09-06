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
import win32com.client as wc


class LeCroyScope(object):

    def __init__(self, ip):
        self.scope = wc.Dispatch("LeCroy.ActiveDSOCtrl.1")
        self.scope.MakeConnection('IP: ' + ip)

    def __del__(self):
        self.scope.Disconnect()

    def close(self):
        self.scope.Disconnect()

    def clear(self):
        print('dso clear ...', end='')
        tmp = 'tmp'
        while len(tmp) > 0:
            tmp = self.scope.ReadString(8192)
        print('end')

    def get_wavedesc(self):
        self.scope.WriteString("INSP? WAVEDESC", 1)
        wavedesc = self.scope.ReadString(8192)
        return wavedesc

    def get_waveform(self, channel):
        assert self.scope.WriteString("MSIZ?", 1), \
                '>> MSIZ? : can not communicate with LeCroy DSO'
        val = self.scope.ReadString(50)
        maxmemsz = int(float(val))

        self.scope.WriteString("%s:CLEAR_SWEEPS" % (channel), 1)
        self.scope.WriteString("*OPC?", 1)
        esr_opc_bit = self.scope.ReadString(100)
        while esr_opc_bit == False:
            self.scope.WriteString("*OPC?", 1)
            esr_opc_bit = self.scope.ReadString(100)
            print('*OPC? = 0')
            time.sleep(0.2)         
        
        self.scope.WriteString("COMM_FORMAT DEF9,WORD,BIN", 1)
        assert self.scope.WriteString("%s:WAVEFORM? DAT1" % (channel), 1), \
                '>> WAVEFORM? : can not communicate with LeCroy DSO'
        #timearray, waveform = self.scope.GetScaledWaveformWithTimes(channel, maxmemsz, 0)
        #_, waveform = self.scope.GetScaledWaveformWithTimes(channel, maxmemsz, 0)
        #waveform = self.scope.GetIntegerWaveform(channel, maxmemsz, 0)
        waveform = self.scope.GetByteWaveform(channel, maxmemsz, 0)

        return np.array(waveform)


