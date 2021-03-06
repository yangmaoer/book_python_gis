#!/usr/bin/env python3
# -*- coding: utf-8 -*-
###############################################################################
import os
from osgeo import ogr
# 结果数据
extfile = 'xx_demo_point.shp'
point_coors = [[300, 450], [750, 700], [1200, 450], [750, 200], [750, 450]]
driver = ogr.GetDriverByName("ESRI Shapefile")
if os.access(extfile, os.F_OK):
    driver.DeleteDataSource(extfile)
newds = driver.CreateDataSource(extfile)
layernew = newds.CreateLayer('point', None, ogr.wkbPoint)
# 创建字段
fieldf_x = ogr.FieldDefn("x", ogr.OFTReal)
fieldf_y = ogr.FieldDefn("y", ogr.OFTReal)
layernew.CreateField(fieldf_x)
layernew.CreateField(fieldf_y)
# 创建点
for aa in point_coors:
    geom = ogr.CreateGeometryFromWkt('POINT ({0} {1})'.format(aa[0], aa[1]))
    feat = ogr.Feature(layernew.GetLayerDefn())
    feat.SetField('x', aa[0])
    feat.SetField('y', aa[1])
    feat.SetGeometry(geom)
    layernew.CreateFeature(feat)
newds.Destroy()
