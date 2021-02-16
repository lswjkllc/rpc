# -*- coding: utf-8 -*-
"""
    CreatedDate: 2021-02-16
    FileName: client.py
    Author: Mustom
    Descreption: 
"""
import asyncio
import logging

import grpc

from .protos import route_guide_pb2, route_guide_pb2_grpc


async def guide_get_one_feature(stub: route_guide_pb2_grpc.RouteGuideStub,
                                point: route_guide_pb2.Point):
    feature = await stub.GetFeature(point)
    if not feature.location:
        print("Server returned incomplete feature")
        return

    if feature.name:
        print(f"Feature called {feature.name} at {feature.location}")
    else:
        print(f"Found no feature at {feature.location}")


async def guide_get_feature(stub: route_guide_pb2_grpc.RouteGuideStub):
    await guide_get_one_feature(
        stub, route_guide_pb2.Point(latitude=409146138, longitude=-746188906))
    await guide_get_one_feature(
        stub, route_guide_pb2.Point(latitude=0, longitude=0))


async def main():
    async with grpc.aio.insecure_channel("localhost:50051") as channel:
        stub = route_guide_pb2_grpc.RouteGuideStub(channel)
        print("-------------- GetFeature --------------")
        await guide_get_feature(stub)
        # print("-------------- ListFeatures --------------")
        # await guide_list_features(stub)
        # print("-------------- RecordRoute --------------")
        # await guide_record_route(stub)
        # print("-------------- RouteChat --------------")
        # await guide_route_chat(stub)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.get_event_loop().run_until_complete(main())
