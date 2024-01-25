import pandas as pd

import xml.etree.ElementTree as ET
import pandas as pd
from pathlib import Path
import numpy as np

xml_file_path = "Aldeboarn.xml"


# test hoe ik deze data kan inlezen: nu nog veranderen naar pysst en dan naar .csv


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
            df = self.create_df()

            # #veranderen naar pysst functie
            self.df_to_csv(df)

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

        arrays_dict = {}
        for int in borehole_lithoIntervals:
            for child in int:
                if child.tag not in arrays_dict:
                    arrays_dict[child.tag] = []
        for int in borehole_lithoIntervals:
            for key, value in arrays_dict.items():
                if int.find(key) != None and key != "remark":
                    arrays_dict[key].append(int.find(key).get("code"))
                elif key == "remark" and int.find(key).text != None:
                    arrays_dict[key].append(str([int.find(key).text]))
                else:
                    arrays_dict[key].append(None)
        self.geology = arrays_dict

    def create_df(self):
        data = {
            "Xcoordinaat": self.xcoordinaat,
            "Ycoordinaat": self.ycoordinaat,
            "Maaiveld": self.maaiveld,
        }

        df_data = pd.DataFrame([data])
        df_geo = pd.DataFrame(self.geology)

        df_data = df_data.reindex(range(len(df_geo))).ffill()
        df = pd.concat((df_data, df_geo), axis=1)

        new_order = [col for col in df.columns if col != "remark"] + ["remark"]
        df = df[new_order]
        return df

    def df_to_csv(self, df):
        # make some nice naming thingie here
        df.to_csv("df_Test.csv", index=False)


read_xml_geologischeboringen(xml_file_path)
