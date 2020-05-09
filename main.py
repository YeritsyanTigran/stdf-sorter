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


for file in files:
    xmlname = StdfToXml.process_file(file)
    root = minidom.parse(xmlname)
    count = 0
    elements = root.getElementsByTagName('Ptr')
    for ptr in elements:
        value = int(ptr.attributes['TEST_FLG'].value)
        if isKthBitSet(value, 1):
            count += 1
    wafer_id = root.getElementsByTagName("Wrr")[0].attributes["WAFER_ID"].value
    lot_id = root.getElementsByTagName("Mir")[0].attributes["LOT_ID"].value
    result = {
        "yield": "{:.2f}".format(((elements.length - count) / elements.length)*100)+"%",
        "wafer_id": wafer_id,
        "lot_id": lot_id
    }
    data.append(result)
print(data)

testWorkbook = xlsxwriter.Workbook('./data/Test_Results.xlsx')
sheet = testWorkbook.add_worksheet()

sheet.write("A1", "Technology")
sheet.write("B1", "Layout")
sheet.write("C1", "Lot")
sheet.write("D1", "Wafer")
sheet.write("E1", "Yield")

for item in range(len(data)):
    sheet.write(item + 1, 2, data[item]["lot_id"])
    sheet.write(item + 1, 3, data[item]["wafer_id"])
    sheet.write(item+1, 4, data[item]["yield"])
testWorkbook.close()
