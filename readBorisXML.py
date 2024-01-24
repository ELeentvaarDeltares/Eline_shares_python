# -*- coding: utf-8 -*-
"""
reads boris xml with one or multiple boreholes in it

Created on Wed Nov 25 14:20:57 2020

@author: vermaas
"""

from xml.etree import ElementTree
import pyproj


def readBorisXML(f, LBL=None, epsg=None):
    # f = r'n:\Projects\11206000\11206108\B. Measurements and calculations\Boorbeschrijvingen\2020\iMOD\noordzee_vak_L17H_2019.xml'

    # f is full path to boris XML 1.4 file
    with open(f, "rt") as f:
        tree = ElementTree.parse(f)

    # get labels of columns
    if LBL == None:
        LBL = []
        layersAll = tree.findall(".//lithoInterval")
        for n in layersAll:
            for i in n.iter():
                if not str(i.tag) in LBL:
                    LBL.append(str(i.tag))

    # insert label for lithocode
    LBL = ["Top", "Lithocode"] + LBL

    XA = []
    YA = []
    topA = []
    bottomA = []
    DA = []
    nm = []

    #### loop over all boreholes! ####
    for itree in tree.getiterator(tag="pointSurvey"):
        # get borehole-id
        nm.append(itree.findall("identification")[0].attrib["id"])

        layers = itree.findall(".//lithoInterval")

        # get xy
        C = itree.findall(".//coordinates")
        for c in C:
            if c.attrib["coordSystem"] == "WGS84-UTM31":
                X = c.getchildren()[0].text
                Y = c.getchildren()[1].text
                inProj = pyproj.Proj("epsg:32631")  # WGS84 UTM31N
            if c.attrib["coordSystem"] == "ETRS89-RD":
                X = c.getchildren()[0].text
                Y = c.getchildren()[1].text
                inProj = pyproj.Proj("epsg:25831")  # ETRS89 UTM31N
            if c.attrib["coordSystem"] == "RD":
                X = c.getchildren()[0].text
                Y = c.getchildren()[1].text
                inProj = pyproj.Proj("epsg:28992")  # RD
            if epsg == None:  # if no epsg transform to RD
                epsg = "28992"
            outProj = pyproj.Proj("epsg:" + epsg)
            xRD, yRD = pyproj.transform(inProj, outProj, float(X), float(Y))
            X = str(xRD)
            Y = str(yRD)
        if not "X" in locals():  ##maybe convert from other coordsystem?
            X = "0"
            Y = "0"
        XA.append(X)
        YA.append(Y)

        # get MV
        try:
            Z = itree.findall(".//surfaceElevation//elevation")[0]
            try:
                MV = Z.attrib["levelValue"]  # used for locations above sealevel
            except:
                MV = "-" + Z.attrib["waterDepth"]  # used for locations below sealevel
        except:
            MV = "10000"

        lithoDict = {
            "Z": "1",
            "GM": "2",
            "K": "3",
            "V": "4",
            "L": "5",
            "NBE": "6",
            "SHE": "7",
            "G": "8",
            "GY": "9",
            "HO": "10",
            "DET": "11",
            "STN": "12",
            "KEI": "12",
        }
        D = []
        top = str(float(MV) / 100)
        for i in range(len(layers)):  # loop over lithointervals
            node = layers[i]
            layer = [top]
            top = str(
                (float(MV) - float(node.attrib.get("baseDepth"))) / 100
            )  # top depth NEXT LAYER to MV in m
            for ii in range(2, len(LBL)):
                if LBL[ii] == "lithology":  # for lithology take code, not text
                    layer.append(node.findall(LBL[ii])[0].attrib["code"])
                    layer = [layer[0]] + [lithoDict[layer[-1]]] + layer[1:]
                else:  # add other attributes
                    try:
                        tmp = node.findall(LBL[ii])[0].text
                        if (
                            not tmp
                        ):  # if attribute has no text field, use (first) value from attrib dictionary
                            tmp = list(node.findall(LBL[ii])[0].attrib.values())[0]
                        if "," in tmp or " " in tmp:
                            tmp = '"' + tmp + '"'
                        layer.append(tmp)
                    except:  # if attribute is missing, add '-'
                        layer.append("-")
            D.append(layer)

        # add last layer (twice, to correct for glitch in iMOD)
        layer = [top]
        for ii in range(len(LBL) - 1):
            layer.append("-")
        D.append(layer)
        D.append(layer)

        DA.append(D)
        topA.append(D[0][0])
        bottomA.append(D[-1][0])

    # return metadata and data
    return XA, YA, topA, bottomA, DA, LBL, nm


if __name__ == "__main__":
    readBorisXML("Aldeboarn.xml")
