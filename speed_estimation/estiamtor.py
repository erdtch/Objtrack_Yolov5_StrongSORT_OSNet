import os
import cv2
import numpy as np


class SpeedEstimator:
    def __init__(self, poly_file: str):
        self.poly_area = self.read_poly_area(poly_file)
        self.vehicle_entering = {}  #  # id: (x, y, area_id_enter, entering_time)
        self.vehicle_leaving = {}  # id : (distance, time, area_id_leave, velocity)

    def read_poly_area(self, poly_file: str):
        areas = []
        try:
            print("file:", poly_file)
            with open(poly_file, "r") as f:
                for line in f.readlines():
                    tmp = []
                    values = line.strip("\n").split(",")
                    for i in range(0, len(values), 2):
                        tmp.append((int(values[i]), int(values[i + 1])))
                    areas.append(tmp)
            # print(areas)
            return areas

        except FileNotFoundError:
            print("Polygon file not found at:", os.path.join(os.getcwd(), poly_file))

        except Exception as e:
            print("Invalid file format:", e)

    def obj_inside_poly(self, x_center: int, y_center: int):
        for area_id, area in enumerate(self.poly_area):
            if (
                cv2.pointPolygonTest(
                    np.array(area, np.int32), (x_center, y_center), False
                )
                >= 0
            ):
                return area_id

        return -1
