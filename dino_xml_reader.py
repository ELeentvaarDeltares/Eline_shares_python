from pathlib import Path
from typing import Dict, List, Union, Iterable, Optional
from pydantic import BaseModel
from xml.etree import ElementTree as ET


class XmlLithoIntervalVariables(BaseModel):
    top_depth: Union[List, None] = []
    base_depth: Union[List, None] = []
    lithology_code: Union[List, None] = []
    lithology_name: Union[List, None] = []
    siltAdmix_code: Union[List, None] = []
    siltAdmix_name: Union[List, None] = []
    gravelAdmix_code: Union[List, None] = []
    gravelAdmix_name: Union[List, None] = []
    humusAdmix_code: Union[List, None] = []
    humusAdmix_name: Union[List, None] = []
    colorMain_code: Union[List, None] = []
    colorMain_name: Union[List, None] = []
    colorIntensity_code: Union[List, None] = []
    colorIntensity_name: Union[List, None] = []
    colorSecondary_code: Union[List, None] = []
    colorSecondary_name: Union[List, None] = []
    sandPerc: Union[List, None] = []
    sandMedian: Union[List, None] = []
    sandMedianClass_code: Union[List, None] = []
    sandMedianClass_name: Union[List, None] = []
    gravelPerc: Union[List, None] = []
    organMatPerc: Union[List, None] = []
    carbonateFracNEN5104_code: Union[List, None] = []
    carbonateFracNEN5104_name: Union[List, None] = []
    clayAdmix_code: Union[List, None] = []
    clayAdmix_name: Union[List, None] = []
    sandAdmix_code: Union[List, None] = []
    sandAdmix_name: Union[List, None] = []
    lutumPerc: Union[List, None] = []
    siltPerc: Union[List, None] = []
    sandRound_name: Union[List, None] = []
    sandRound_code: Union[List, None] = []
    sandVarieg_name: Union[List, None] = []
    sandVarieg_code: Union[List, None] = []
    lithoLayerTrend_name: Union[List, None] = []
    lithoLayerTrend_code: Union[List, None] = []
    remark_name: Union[List, None] = []
    remark_code: Union[List, None] = []
    sandSorting_name: Union[List, None] = []
    sandSorting_code: Union[List, None] = []
    gravelFrac_name: Union[List, None] = []
    gravelFrac_code: Union[List, None] = []
    clasticAdmix_name: Union[List, None] = []
    clasticAdmix_code: Union[List, None] = []
    authigenMin_name: Union[List, None] = []
    authigenMin_code: Union[List, None] = []
    plantType_name: Union[List, None] = []
    plantType_code: Union[List, None] = []
    micaFrac_name: Union[List, None] = []
    micaFrac_code: Union[List, None] = []
    organicAdmix_name: Union[List, None] = []
    organicAdmix_code: Union[List, None] = []
    enclosure_name: Union[List, None] = []
    enclosure_code: Union[List, None] = []
    sedimentStructure_name: Union[List, None] = []
    sedimentStructure_code: Union[List, None] = []
    lithoLayerBoundary_name: Union[List, None] = []
    lithoLayerBoundary_code: Union[List, None] = []
    geolInterpret_name: Union[List, None] = []
    geolInterpret_code: Union[List, None] = []
    gravelMedian: Union[List, None] = []
    gravelMedianClass_name: Union[List, None] = []
    gravelMedianClass_code: Union[List, None] = []
    sandMedFine: Union[List, None] = []
    sandMedCoarse: Union[List, None] = []
    gravelType_name: Union[List, None] = []
    gravelType_code: Union[List, None] = []
    shellFrac_name: Union[List, None] = []
    shellFrac_code: Union[List, None] = []
    consistency_name: Union[List, None] = []
    consistency_code: Union[List, None] = []
    shellShape_name: Union[List, None] = []
    shellShape_code: Union[List, None] = []
    peatAmorph_name: Union[List, None] = []
    peatAmorph_code: Union[List, None] = []
    glaucFrac_name: Union[List, None] = []
    glaucFrac_code: Union[List, None] = []
    antropAdmix_name: Union[List, None] = []
    antropAdmix_code: Union[List, None] = []
    soilInterpret_name: Union[List, None] = []
    soilInterpret_code: Union[List, None] = []
    gravelRound_name: Union[List, None] = []
    gravelRound_code: Union[List, None] = []
    gravelVarieg_name: Union[List, None] = []
    gravelVarieg_code: Union[List, None] = []
    coarseMatAdmix_name: Union[List, None] = []
    coarseMatAdmix_code: Union[List, None] = []


class PointSurvey(BaseModel):
    version: Union[str, None] = None
    embargo: Union[str, None] = None
    identification: Union[str, None] = None
    organisation: Union[str, None] = None
    remark: Union[str, None] = None


class surveyLocation(BaseModel):
    surveyLocationMethod: Union[str, None] = None
    originalMeasurement: Union[str, None] = None
    UoM: Union[str, None] = None
    coordSystem: Union[str, None] = None
    coordinateX: Union[float, None] = None
    coordinateY: Union[float, None] = None


class surfaceElevation(BaseModel):
    originalMeasurement: Union[str, None] = None
    levelReference: Union[str, None] = None
    levelValue: Union[str, None] = None
    UoM: Union[str, None] = None


class geoPoliticalLocation(BaseModel):
    countryName: Union[str, None] = None
    stateOrProvinceName: Union[str, None] = None
    maptype: Union[str, None] = None
    mapname: Union[str, None] = None


class borehole(BaseModel):
    version: Union[str, None] = None
    baseDepthUoM: Union[str, None] = None
    baseDepth: Union[float, None] = None
    operatorOrg: Union[str, None] = None
    startYear: Union[int, None] = None
    startMonth: Union[int, None] = None
    startDay: Union[int, None] = None


class lithoDescr(BaseModel):
    version: Union[str, None] = None
    layerDepthUoM: Union[str, None] = None
    layerDepthReference: Union[str, None] = None
    lithoDescrYear: Union[int, None] = None
    lithoDescrMonth: Union[int, None] = None
    lithoDescrDay: Union[int, None] = None
    lithoDescrStandard: Union[str, None] = None
    lithoDescrWetDry: Union[str, None] = None
    lithoDescrVersion: Union[str, None] = None
    lithoDescrQuality: Union[str, None] = None
    describerName: Union[str, None] = None
    organisation: Union[str, None] = None


class BroXmlBorehole(XmlLithoIntervalVariables):
    version: Union[str, None] = None
    pointSurvey: PointSurvey = PointSurvey()
    surveyLocation: surveyLocation = surveyLocation()
    surfaceElevation: surfaceElevation = surfaceElevation()
    geoPoliticalLocation: geoPoliticalLocation = geoPoliticalLocation()
    borehole: borehole = borehole()
    lithoDescr: lithoDescr = lithoDescr()

    @property
    def __lift_of_float_attributes(self):
        return [
            "top_depth",
            "base_depth",
            "sandPerc",
            "sandMedian",
            "gravelPerc",
            "organMatPerc",
            "lutumPerc",
            "siltPerc",
            "gravelMedian",
            "sandMedFine",
            "sandMedCoarse",
        ]

    def get_point_survey_values(self, xml_file):
        self.pointSurvey.embargo = xml_file.get("embargo", None)
        self.pointSurvey.version = xml_file.get("version", None)
        if xml_file.find("identification") is not None:
            self.pointSurvey.identification = xml_file.find("identification").get(
                "id", None
            )
            self.pointSurvey.organisation = BroXmlBorehole.if_found_return_text(
                xml_file.find("identification"), "organisation"
            )
            self.pointSurvey.organisation = BroXmlBorehole.if_found_return_text(
                xml_file.find("identification"), "remark"
            )

    def get_survey_location(self, xml_file):
        if xml_file.find("surveyLocation") is not None:
            self.surveyLocation.surveyLocationMethod = (
                BroXmlBorehole.if_found_return_text(
                    xml_file.find("surveyLocation"), "surveyLocationMethod"
                )
            )
            if xml_file.find("surveyLocation").find("coordinates") is not None:
                self.surveyLocation.originalMeasurement = (
                    xml_file.find("surveyLocation")
                    .find("coordinates")
                    .get("originalMeasurement", None)
                )
                self.surveyLocation.UoM = (
                    xml_file.find("surveyLocation").find("coordinates").get("UoM", None)
                )
                self.surveyLocation.coordSystem = (
                    xml_file.find("surveyLocation")
                    .find("coordinates")
                    .get("coordSystem", None)
                )
                self.surveyLocation.coordinateX = BroXmlBorehole.to_float_if_not_none(
                    BroXmlBorehole.if_found_return_text(
                        xml_file.find("surveyLocation").find("coordinates"),
                        "coordinateX",
                    )
                )
                self.surveyLocation.coordinateY = BroXmlBorehole.to_float_if_not_none(
                    BroXmlBorehole.if_found_return_text(
                        xml_file.find("surveyLocation").find("coordinates"),
                        "coordinateY",
                    )
                )

    def get_geo_political_location(self, xml_element):
        if xml_element.find("geoPoliticalLocation") is not None:
            self.geoPoliticalLocation.countryName = BroXmlBorehole.if_found_return_text(
                xml_element.find("geoPoliticalLocation"), "countryName"
            )
            self.geoPoliticalLocation.stateOrProvinceName = (
                BroXmlBorehole.if_found_return_text(
                    xml_element.find("geoPoliticalLocation"), "stateOrProvinceName"
                )
            )
            if xml_element.find("geoPoliticalLocation").find("map") is not None:
                self.geoPoliticalLocation.maptype = (
                    xml_element.find("geoPoliticalLocation")
                    .find("map")
                    .get("maptype", None)
                )
                self.geoPoliticalLocation.mapname = BroXmlBorehole.if_found_return_text(
                    xml_element.find("geoPoliticalLocation"), "map"
                )

    def get_surface_elevation(self, xml_element):
        if xml_element.find("surfaceElevation").find("elevation") is not None:
            self.surfaceElevation.UoM = (
                xml_element.find("surfaceElevation").find("elevation").get("UoM", None)
            )
            self.surfaceElevation.originalMeasurement = (
                xml_element.find("surfaceElevation")
                .find("elevation")
                .get("originalMeasurement", None)
            )
            self.surfaceElevation.levelReference = (
                xml_element.find("surfaceElevation")
                .find("elevation")
                .get("levelReference", None)
            )
            self.surfaceElevation.levelValue = BroXmlBorehole.to_float_if_not_none(
                xml_element.find("surfaceElevation")
                .find("elevation")
                .get("levelValue", None)
            )

    def get_borehole(self, xml_element):
        self.borehole.version = xml_element.get("version", None)
        self.borehole.baseDepthUoM = xml_element.get("baseDepthUoM", None)
        self.borehole.baseDepth = BroXmlBorehole.to_float_if_not_none(
            xml_element.get("baseDepth", None)
        )
        self.borehole.operatorOrg = BroXmlBorehole.if_found_return_text(
            xml_element, "operatorOrg"
        )
        self.borehole.startYear = BroXmlBorehole.to_integer_if_not_none(
            xml_element.find("date").get("startYear", None)
        )
        self.borehole.startMonth = BroXmlBorehole.to_integer_if_not_none(
            xml_element.find("date").get("startMonth", None)
        )
        self.borehole.startDay = BroXmlBorehole.to_integer_if_not_none(
            xml_element.find("date").get("startDay", None)
        )

    def get_lithology_description(self, xml_element):
        self.lithoDescr.version = xml_element.get("version", None)
        self.lithoDescr.layerDepthUoM = xml_element.get("layerDepthUoM", None)
        self.lithoDescr.layerDepthReference = xml_element.get(
            "layerDepthReference", None
        )
        self.lithoDescr.lithoDescrMonth = BroXmlBorehole.to_integer_if_not_none(
            xml_element.get("lithoDescrMonth", None)
        )
        self.lithoDescr.lithoDescrYear = BroXmlBorehole.to_integer_if_not_none(
            xml_element.get("lithoDescrYear", None)
        )
        self.lithoDescr.lithoDescrDay = BroXmlBorehole.to_integer_if_not_none(
            xml_element.get("lithoDescrDay", None)
        )
        self.lithoDescr.lithoDescrStandard = xml_element.get("lithoDescrStandard", None)
        self.lithoDescr.lithoDescrWetDry = xml_element.get("lithoDescrWetDry", None)
        self.lithoDescr.lithoDescrVersion = xml_element.get("lithoDescrVersion", None)
        self.lithoDescr.lithoDescrQuality = xml_element.get("lithoDescrQuality", None)
        self.lithoDescr.describerName = BroXmlBorehole.if_found_return_text(
            xml_element, "describerName"
        )
        self.lithoDescr.organisation = BroXmlBorehole.if_found_return_text(
            xml_element, "organisation"
        )

    def read_xml(self, xml_file: Path):
        # open xml file
        tree = ET.parse(xml_file)
        root = tree.getroot()

        # general data from xml
        self.version = root.get("version", None)
        pointSurvey = root.find("pointSurvey")
        borehole = pointSurvey.find("borehole")
        lithoDescr = borehole.find("lithoDescr")

        self.get_point_survey_values(pointSurvey)
        self.get_survey_location(pointSurvey)
        self.get_geo_political_location(pointSurvey)
        self.get_surface_elevation(pointSurvey)
        if borehole is not None:
            self.get_borehole(borehole)
        if lithoDescr is not None:
            self.get_lithology_description(lithoDescr)

        self.set_elements_for_lithology_interval(lithoDescr)
        self.set_float_attributes()

    @staticmethod
    def to_float_if_not_none(value):
        if value is not None:
            return float(value)
        return value

    @staticmethod
    def to_integer_if_not_none(value):
        if value is not None:
            return int(value)
        return value

    @staticmethod
    def if_found_return_text(xml_element, value_name):
        if xml_element.find(value_name) is not None:
            return xml_element.find(value_name).text
        return None

    def set_float_attributes(self):
        for attribute_name in self.__lift_of_float_attributes:
            attribute_list = getattr(self, attribute_name)
            attribute_list = [
                value if value is None else float(value) for value in attribute_list
            ]
            setattr(self, attribute_name, attribute_list)

    def set_elements_for_lithology_interval(self, litho_description_xml):
        # find and store all variables
        for interval in litho_description_xml.findall("lithoInterval"):
            # append a None to all the attributes so that they can later be filled in
            for class_attribute_name in dict(XmlLithoIntervalVariables()).keys():
                self.append_in_attribute(class_attribute_name, None)

            # depths are part of geology
            self.top_depth[-1] = interval.get("topDepth", None)
            self.base_depth[-1] = interval.get("topDepth", None)

            # append all remaining elements in lithology interval
            for element in list(interval):
                tag = element.tag
                text = element.text
                code = element.attrib.get("code")
                percentage = element.attrib.get("percentage")
                median = element.attrib.get("median")
                value = [
                    attribute
                    for attribute in [code, percentage, median]
                    if attribute is not None
                ]
                if value:
                    value = value[0]
                else:
                    value = None
                if text is None:
                    self.set_last_value_in_list_of_attribute(tag, value)
                else:
                    self.set_last_value_in_list_of_attribute(tag + "_name", text)
                    self.set_last_value_in_list_of_attribute(tag + "_code", value)

    def append_in_attribute(self, name: str, value: Union[str, None]):
        attribute = getattr(self, name)
        attribute.append(value)
        setattr(self, name, attribute)

    def set_last_value_in_list_of_attribute(self, name: str, value: Union[str, None]):
        attribute = getattr(self, name)
        attribute[-1] = value
        setattr(self, name, attribute)
