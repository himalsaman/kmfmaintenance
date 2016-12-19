import re
from datetime import datetime

from models.purchasingModel import select_max_Purchasing_code, addNewPurchasing

datetimestr = datetime.now()
timestampstr = datetimestr.strftime('%Y-%m-%d %H:%M:%S')


# maintanance code calculation
def purchCode():
	maxcode = select_max_Purchasing_code()
	intcode = int(next(re.finditer(r'\d+$', maxcode)).group(0))
	nextgencode = intcode + 1
	gencode = 'kmfpur{}'.format(nextgencode)
	return gencode


def createIniPurchasing():
		addNewPurchasing(purchCode(), timestampstr, None, None, None, None, None, None, None, None, 0)
