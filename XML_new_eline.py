import pandas as pd

import xml.etree.ElementTree as ET
import pandas as pd
from pathlib import Path


xml_file_path = "Aldeboarn.xml"

import dino_xml_reader
from dino_xml_reader import BroXmlBorehole
from dino_xml_reader import XmlLithoIntervalVariables


class read_xml_geologischeboringen:
    def __init__(self, filepath):
        self.__open_file(filepath)
        self.filepath = filepath

    def __open_file(self, filepath):
        for f in filepath:
            tree = ET.parse(filepath)
            root = tree.getroot()
            self.xml = root
            self.read_coordinates()
            self.read_maaiveld()
            self.read_borehole()
            df = self.createdf()
            self.df_to_csv(df)
            break

    def read_coordinates(self):
        elementX = (
            self.xml.find("pointSurvey")
            .find("surveyLocation")
            .find("coordinates")
            .find("coordinateX")
        )
        elementY = (
            self.xml.find("pointSurvey")
            .find("surveyLocation")
            .find("coordinates")
            .find("coordinateY")
        )

        self.xcoordinaat = elementX.text
        self.ycoordinaat = elementY.text

    def read_maaiveld(self):
        maaiveld = (
            self.xml.find("pointSurvey")
            .find("surfaceElevation")
            .find("elevation")
            .get("levelValue")
        )
        self.maaiveld = maaiveld

    def read_borehole(self):
        borehole_lithoIntervals = (
            self.xml.find("pointSurvey")
            .find("borehole")
            .find("lithoDescr")
            .findall("lithoInterval")
        )

        baseDepth = []
        lithology = []
        colorMain = []
        for int in borehole_lithoIntervals:
            baseDepth.append(int.get("baseDepth"))
            lithology.append(int.find("lithology").get("code"))

            if int.find("colorMain") != None:
                colorMain.append(int.find("colorMain").get("code"))
            else:
                colorMain.append(None)

            # Do this for all the information you want, a dictionary needs to be created that translates these codes back to words.

    def createdf(self):
        data = {
            "Xcoordinaat": [self.xcoordinaat],
            "Ycoordinaat": [self.ycoordinaat],
            "Maaiveld": [self.maaiveld],
        }

        df = pd.DataFrame(data)
        return df

    def df_to_csv(self, df):
        # make some nice naming thingie here
        df.to_csv("df_Test.csv", index=False)


read_xml_geologischeboringen(xml_file_path)
