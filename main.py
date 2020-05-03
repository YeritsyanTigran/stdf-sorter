from reader.scripts.StdfToXml import StdfToXml
from xml.dom import minidom
import xlsxwriter

files = ['./data/demofile.stdf', './data/lot2.stdf', './data/lot3.stdf']
data = []


def isKthBitSet(n, k):
    if n & (1 << (k - 1)):
        return True
    else:
        return False


def takeResult(elem):
    return elem['yield']


for file in files:
    xmlname = StdfToXml.process_file(file)
    root = minidom.parse(xmlname)
    count = 0
    elements = root.getElementsByTagName('Ptr')
    for prt in elements:
        value = int(prt.attributes['TEST_FLG'].value)
        if isKthBitSet(value, 1):
            count += 1
    result = {
        "yield": (elements.length - count) / elements.length
    }
    data.append(result)
print(data)

fuckinWorkbook = xlsxwriter.Workbook('./data/Test_Results.xlsx')
sheet = fuckinWorkbook.add_worksheet()

waferNum = [3, 4, 5]
yieldValue = [100, 20, 35]

sheet.write("C1", "Lot")
sheet.write("D1", "Wafer")
sheet.write("E1", "Yield")

for item in range(len(waferNum)):
    sheet.write(item+1, 3, waferNum[item])
    sheet.write(item+1, 4, yieldValue[item])
fuckinWorkbook.close()
