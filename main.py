#~~~ Pratham-code ~~~
import pyqrcode
import png
from pyqrcode import QRCode
  
s = "https://github.com/PrathamP28"
  
url = pyqrcode.create(s)

url.png('pratham.png', scale = 4)