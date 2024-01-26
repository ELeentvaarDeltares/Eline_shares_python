import pandas as pd
import xml.etree.ElementTree as ET
import pandas as pd

xml_file_path = "Aldeboarn.xml"


class read_xml_geologischeboringen:
    def __init__(self, filepath):
        self.__open_file(filepath)
        self.filepath = filepath

    def __open_file(self, filepath):
        # for f in filepath:
        tree = ET.parse(filepath)
        root = tree.getroot()
        for pointsurveys in root.findall("pointSurvey"):
            self.xml = pointsurveys
            self.boreholenumber()
            self.read_topbottom()
            self.read_coordinates()
            self.read_maaiveld()
            self.read_borehole()
            df = self.create_df()
            self.to_csv(df)
            break

    def boreholenumber(self):
        self.boreholenumber = self.xml.find("identification").attrib.get("id")

    def read_topbottom(self):
        lithointerval = (
            self.xml.find("borehole").find("lithoDescr").findall("lithoInterval")
        )
        bottom = []
        for l in lithointerval:
            bottom.append(l.attrib.get("baseDepth"))

        top = [0]
        for b in bottom:
            top.append(b)

        top = top[:-1]
        self.top = top
        self.bottom = bottom

    def read_coordinates(self):
        elementX = (
            self.xml.find("surveyLocation").find("coordinates").find("coordinateX")
        )
        elementY = (
            self.xml.find("surveyLocation").find("coordinates").find("coordinateY")
        )

        self.xcoordinaat = elementX.text
        self.ycoordinaat = elementY.text

    def read_maaiveld(self):
        self.maaiveld = (
            self.xml.find("surfaceElevation").find("elevation").get("levelValue")
        )

    def read_borehole(self):
        borehole_lithoIntervals = (
            self.xml.find("borehole").find("lithoDescr").findall("lithoInterval")
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
                elif key == "remark" and int.find(key) != None:
                    arrays_dict[key].append(str([int.find(key).text]))
                else:
                    arrays_dict[key].append(None)
        self.geology = arrays_dict

    def create_df(self):
        data_algemeen = {
            "Xcoordinaat": self.xcoordinaat,
            "Ycoordinaat": self.ycoordinaat,
            "Maaiveld": self.maaiveld,
        }
        data_boringen = {"top": self.top, "bottom": self.bottom}

        df_data_algemeen = pd.DataFrame([data_algemeen])
        df_data_boringen = pd.DataFrame(data_boringen)
        df_geo = pd.DataFrame(self.geology)

        df_data_algemeen = df_data_algemeen.reindex(range(len(df_geo))).ffill()
        df = pd.concat((df_data_algemeen, df_data_boringen, df_geo), axis=1)

        new_order = [col for col in df.columns if col != "remark"] + ["remark"]
        df = df[new_order]

        return df

    def to_csv(self, df):
        df.to_csv(self.boreholenumber + ".csv")


# boornummer koppelen aan naam csv + nog even top en bottom toevoegen

read_xml_geologischeboringen(xml_file_path)
