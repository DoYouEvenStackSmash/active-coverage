# automatically generated by the FlatBuffers compiler, do not modify

# namespace: LOCO

import flatbuffers
from flatbuffers.compat import import_numpy

np = import_numpy()


class Annotation(object):
    __slots__ = ["_tab"]

    @classmethod
    def GetRootAsAnnotation(cls, buf, offset):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = Annotation()
        x.Init(buf, n + offset)
        return x

    # Annotation
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # Annotation
    def Id(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0

    # Annotation
    def ImageId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0

    # Annotation
    def CategoryId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            return self._tab.Get(
                flatbuffers.number_types.Float32Flags, o + self._tab.Pos
            )
        return 0.0

    # Annotation
    def Bbox(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        if o != 0:
            x = o + self._tab.Pos
            from LOCO.Bbox import Bbox

            obj = Bbox()
            obj.Init(self._tab.Bytes, x)
            return obj
        return None

    # Annotation
    def Area(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(12))
        if o != 0:
            return self._tab.Get(
                flatbuffers.number_types.Float32Flags, o + self._tab.Pos
            )
        return 0.0

    # Annotation
    def Segmentation(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(14))
        if o != 0:
            a = self._tab.Vector(o)
            return self._tab.Get(
                flatbuffers.number_types.Uint8Flags,
                a + flatbuffers.number_types.UOffsetTFlags.py_type(j * 1),
            )
        return 0

    # Annotation
    def SegmentationAsNumpy(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(14))
        if o != 0:
            return self._tab.GetVectorAsNumpy(flatbuffers.number_types.Uint8Flags, o)
        return 0

    # Annotation
    def SegmentationLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(14))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    # Annotation
    def SegmentationIsNone(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(14))
        return o == 0

    # Annotation
    def Iscrowd(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(16))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0

    # Annotation
    def TrackId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(18))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0

    # Annotation
    def TrackmapIndex(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(20))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0

    # Annotation
    def VidId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(22))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0

    # color of the track for rendering
    # Annotation
    def TrackColor(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(24))
        if o != 0:
            a = self._tab.Vector(o)
            return self._tab.Get(
                flatbuffers.number_types.Int32Flags,
                a + flatbuffers.number_types.UOffsetTFlags.py_type(j * 4),
            )
        return 0

    # Annotation
    def TrackColorAsNumpy(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(24))
        if o != 0:
            return self._tab.GetVectorAsNumpy(flatbuffers.number_types.Int32Flags, o)
        return 0

    # Annotation
    def TrackColorLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(24))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    # Annotation
    def TrackColorIsNone(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(24))
        return o == 0

    # Annotation
    def IsDisplaced(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(26))
        if o != 0:
            return bool(
                self._tab.Get(flatbuffers.number_types.BoolFlags, o + self._tab.Pos)
            )
        return False

    # Annotation
    def Confidence(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(28))
        if o != 0:
            return self._tab.Get(
                flatbuffers.number_types.Float32Flags, o + self._tab.Pos
            )
        return 0.0

    # Annotation
    def Error(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(30))
        if o != 0:
            return self._tab.Get(
                flatbuffers.number_types.Float32Flags, o + self._tab.Pos
            )
        return 0.0

    # Annotation
    def StateId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(32))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0

    # Annotation
    def IsPrediction(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(34))
        if o != 0:
            return bool(
                self._tab.Get(flatbuffers.number_types.BoolFlags, o + self._tab.Pos)
            )
        return False

    # Annotation
    def Position(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(36))
        if o != 0:
            x = self._tab.Indirect(o + self._tab.Pos)
            from LOCO.Position import Position

            obj = Position()
            obj.Init(self._tab.Bytes, x)
            return obj
        return None

    # Annotation
    def Distance(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(38))
        if o != 0:
            return self._tab.Get(
                flatbuffers.number_types.Float32Flags, o + self._tab.Pos
            )
        return 0.0


def AnnotationStart(builder):
    builder.StartObject(18)


def AnnotationAddId(builder, id):
    builder.PrependInt32Slot(0, id, 0)


def AnnotationAddImageId(builder, imageId):
    builder.PrependInt32Slot(1, imageId, 0)


def AnnotationAddCategoryId(builder, categoryId):
    builder.PrependFloat32Slot(2, categoryId, 0.0)


def AnnotationAddBbox(builder, bbox):
    builder.PrependStructSlot(
        3, flatbuffers.number_types.UOffsetTFlags.py_type(bbox), 0
    )


def AnnotationAddArea(builder, area):
    builder.PrependFloat32Slot(4, area, 0.0)


def AnnotationAddSegmentation(builder, segmentation):
    builder.PrependUOffsetTRelativeSlot(
        5, flatbuffers.number_types.UOffsetTFlags.py_type(segmentation), 0
    )


def AnnotationStartSegmentationVector(builder, numElems):
    return builder.StartVector(1, numElems, 1)


def AnnotationAddIscrowd(builder, iscrowd):
    builder.PrependInt32Slot(6, iscrowd, 0)


def AnnotationAddTrackId(builder, trackId):
    builder.PrependInt32Slot(7, trackId, 0)


def AnnotationAddTrackmapIndex(builder, trackmapIndex):
    builder.PrependInt32Slot(8, trackmapIndex, 0)


def AnnotationAddVidId(builder, vidId):
    builder.PrependInt32Slot(9, vidId, 0)


def AnnotationAddTrackColor(builder, trackColor):
    builder.PrependUOffsetTRelativeSlot(
        10, flatbuffers.number_types.UOffsetTFlags.py_type(trackColor), 0
    )


def AnnotationStartTrackColorVector(builder, numElems):
    return builder.StartVector(4, numElems, 4)


def AnnotationAddIsDisplaced(builder, isDisplaced):
    builder.PrependBoolSlot(11, isDisplaced, 0)


def AnnotationAddConfidence(builder, confidence):
    builder.PrependFloat32Slot(12, confidence, 0.0)


def AnnotationAddError(builder, error):
    builder.PrependFloat32Slot(13, error, 0.0)


def AnnotationAddStateId(builder, stateId):
    builder.PrependInt32Slot(14, stateId, 0)


def AnnotationAddIsPrediction(builder, isPrediction):
    builder.PrependBoolSlot(15, isPrediction, 0)


def AnnotationAddPosition(builder, position):
    builder.PrependUOffsetTRelativeSlot(
        16, flatbuffers.number_types.UOffsetTFlags.py_type(position), 0
    )


def AnnotationAddDistance(builder, distance):
    builder.PrependFloat32Slot(17, distance, 0.0)


def AnnotationEnd(builder):
    return builder.EndObject()


import LOCO.Bbox
import LOCO.Position

try:
    from typing import List, Optional
except:
    pass


class AnnotationT(object):
    # AnnotationT
    def __init__(self):
        self.id = 0  # type: int
        self.imageId = 0  # type: int
        self.categoryId = 0.0  # type: float
        self.bbox = None  # type: Optional[LOCO.Bbox.BboxT]
        self.area = 0.0  # type: float
        self.segmentation = None  # type: List[int]
        self.iscrowd = 0  # type: int
        self.trackId = 0  # type: int
        self.trackmapIndex = 0  # type: int
        self.vidId = 0  # type: int
        self.trackColor = None  # type: List[int]
        self.isDisplaced = False  # type: bool
        self.confidence = 0.0  # type: float
        self.error = 0.0  # type: float
        self.stateId = 0  # type: int
        self.isPrediction = False  # type: bool
        self.position = None  # type: Optional[LOCO.Position.PositionT]
        self.distance = 0.0  # type: float

    @classmethod
    def InitFromBuf(cls, buf, pos):
        annotation = Annotation()
        annotation.Init(buf, pos)
        return cls.InitFromObj(annotation)

    @classmethod
    def InitFromObj(cls, annotation):
        x = AnnotationT()
        x._UnPack(annotation)
        return x

    # AnnotationT
    def _UnPack(self, annotation):
        if annotation is None:
            return
        self.id = annotation.Id()
        self.imageId = annotation.ImageId()
        self.categoryId = annotation.CategoryId()
        if annotation.Bbox() is not None:
            self.bbox = LOCO.Bbox.BboxT.InitFromObj(annotation.Bbox())
        self.area = annotation.Area()
        if not annotation.SegmentationIsNone():
            if np is None:
                self.segmentation = []
                for i in range(annotation.SegmentationLength()):
                    self.segmentation.append(annotation.Segmentation(i))
            else:
                self.segmentation = annotation.SegmentationAsNumpy()
        self.iscrowd = annotation.Iscrowd()
        self.trackId = annotation.TrackId()
        self.trackmapIndex = annotation.TrackmapIndex()
        self.vidId = annotation.VidId()
        if not annotation.TrackColorIsNone():
            if np is None:
                self.trackColor = []
                for i in range(annotation.TrackColorLength()):
                    self.trackColor.append(annotation.TrackColor(i))
            else:
                self.trackColor = annotation.TrackColorAsNumpy()
        self.isDisplaced = annotation.IsDisplaced()
        self.confidence = annotation.Confidence()
        self.error = annotation.Error()
        self.stateId = annotation.StateId()
        self.isPrediction = annotation.IsPrediction()
        if annotation.Position() is not None:
            self.position = LOCO.Position.PositionT.InitFromObj(annotation.Position())
        self.distance = annotation.Distance()

    # AnnotationT
    def Pack(self, builder):
        if self.segmentation is not None:
            if np is not None and type(self.segmentation) is np.ndarray:
                segmentation = builder.CreateNumpyVector(self.segmentation)
            else:
                AnnotationStartSegmentationVector(builder, len(self.segmentation))
                for i in reversed(range(len(self.segmentation))):
                    builder.PrependUint8(self.segmentation[i])
                segmentation = builder.EndVector(len(self.segmentation))
        if self.trackColor is not None:
            if np is not None and type(self.trackColor) is np.ndarray:
                trackColor = builder.CreateNumpyVector(self.trackColor)
            else:
                AnnotationStartTrackColorVector(builder, len(self.trackColor))
                for i in reversed(range(len(self.trackColor))):
                    builder.PrependInt32(self.trackColor[i])
                trackColor = builder.EndVector(len(self.trackColor))
        if self.position is not None:
            position = self.position.Pack(builder)
        AnnotationStart(builder)
        AnnotationAddId(builder, self.id)
        AnnotationAddImageId(builder, self.imageId)
        AnnotationAddCategoryId(builder, self.categoryId)
        if self.bbox is not None:
            bbox = self.bbox.Pack(builder)
            AnnotationAddBbox(builder, bbox)
        AnnotationAddArea(builder, self.area)
        if self.segmentation is not None:
            AnnotationAddSegmentation(builder, segmentation)
        AnnotationAddIscrowd(builder, self.iscrowd)
        AnnotationAddTrackId(builder, self.trackId)
        AnnotationAddTrackmapIndex(builder, self.trackmapIndex)
        AnnotationAddVidId(builder, self.vidId)
        if self.trackColor is not None:
            AnnotationAddTrackColor(builder, trackColor)
        AnnotationAddIsDisplaced(builder, self.isDisplaced)
        AnnotationAddConfidence(builder, self.confidence)
        AnnotationAddError(builder, self.error)
        AnnotationAddStateId(builder, self.stateId)
        AnnotationAddIsPrediction(builder, self.isPrediction)
        if self.position is not None:
            AnnotationAddPosition(builder, position)
        AnnotationAddDistance(builder, self.distance)
        annotation = AnnotationEnd(builder)
        return annotation