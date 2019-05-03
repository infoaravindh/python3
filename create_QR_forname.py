import pyqrcode


qr = pyqrcode.create("{'name':'aravindh','DOB':'27-03-1996','address':'Chennai'}")
qr.png('ara.png',scale=7)  # pip install Pypng
