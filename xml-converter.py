import os
import glob
import pandas as pd
import xml.etree.ElementTree as ET

INPUT_PATH      = 'input'
OUTPUT_PATH     = 'config'
TEST_PERCENTAGE = 20

class XmlConvertor:
    def parseXmls(self, xmls):
        xmlList = []
        for xml in xmls:
            tree = ET.parse(xml)
            root = tree.getroot()
            for member in root.findall('object'):
                value = (root.find('filename').text, 
                            int(root.find('size')[0].text), 
                            int(root.find('size')[1].text), 
                            member[0].text, int(member[4][0].text), 
                            int(member[4][1].text), 
                            int(member[4][2].text), 
                            int(member[4][3].text)
                        )
                xmlList.append(value)
        return xmlList

    def toCSV(self, xmls, output):
        columnsNames = ['filename', 'width', 'height', 'class', 'xmin', 'ymin', 'xmax', 'ymax']

        dataFrame = pd.DataFrame(self.parseXmls(xmls), columns=columnsNames)

        return dataFrame.to_csv(output, index=None)

xmls = glob.glob('{}/*.xml'.format(os.path.join(os.getcwd(), INPUT_PATH)))

trainXmls = xmls[TEST_PERCENTAGE:]
testXmls = xmls[0:TEST_PERCENTAGE]

xmlConvertor = XmlConvertor()
xmlConvertor.toCSV(trainXmls, './{}/train.csv'.format(OUTPUT_PATH))
xmlConvertor.toCSV(testXmls, './{}/test.csv'.format(OUTPUT_PATH))
print("xml to csv mession has been comlpeted!")