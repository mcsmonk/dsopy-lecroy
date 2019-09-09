[![HitCount](http://hits.dwyl.io/mcsmonk/dsopy-lecroy.svg)](http://hits.dwyl.io/mcsmonk/dsopy-lecroy)


simple python3 module for getting an waveform from LeCroy DSO



## Common requirement:

 - anaconda 64-bit

    - numpy

      ```
      pip install numpy
      ```

    - matplotlib

      ```
      pip install matplotlib
      ```

      



# version 1 (socket communication)

- lecroysocket.py
- test_lecroysocket.py

- reference
  - BenLand100's \[[github link](https://github.com/BenLand100/LeCrunch2)\]



# version 2 (activedso com)

- lecroywin32com.py

- test_lecroywin32com.py

- Common requirement:

  - anaconda 64-bit

    - win32com

      ```
      conda install -c anaconda pywin32
      ```

- reference
  
  - LeCroy documents
