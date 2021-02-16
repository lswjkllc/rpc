# -*- coding: utf-8 -*-
"""
    CreatedDate: 2021-02-16
    FileName: resource.py
    Author: Mustom
    Descreption: 
"""
import json

from ..protos import route_guide_pb2


def read_route_guide_database():
    """Reads the route guide database.
  Returns:
    The full contents of the route guide database as a sequence of
      route_guide_pb2.Features.
  """
    feature_list = []
    with open("./src/grpc/db/route_guide_db.json") as route_guide_db_file:
        for item in json.load(route_guide_db_file):
            feature = route_guide_pb2.Feature(
                name=item["name"],
                location=route_guide_pb2.Point(
                    latitude=item["location"]["latitude"],
                    longitude=item["location"]["longitude"]))
            feature_list.append(feature)
    return feature_list
