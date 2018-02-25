from . import BaseHandler
import mutagen.id3
from mutagen.mp3 import MP3
from mutagen.mp4 import MP4
from mutagen.aiff import AIFF


class Mp3Tags(BaseHandler):
    _handles = [MP3.__name__, AIFF.__name__]

    @staticmethod
    def get_value(track, frame_type):
        obj = track.get(frame_type.__name__)

        if obj is None and issubclass(frame_type, mutagen.id3.COM):
            for frame_name, frame_obj in track.tags.items():
                if issubclass(frame_obj.__class__, mutagen.id3.COMM):
                    obj = frame_obj
                    break

        if obj is None:
            return ""

        value = obj.text[0]

        if isinstance(value, str):
            return value

        if isinstance(value, mutagen.id3.ID3TimeStamp):
            return value.get_text()

    @staticmethod
    def set_value(track, frame_type, value):
        if value is None:
            return

        obj = track.get(frame_type.__name__)
        if obj is not None:
            obj.text[0] = value
        else:
            frame = frame_type()
            if issubclass(frame_type, mutagen.id3.TextFrame):
                frame.append(value)
            elif isinstance(frame, mutagen.id3.Frame):
                frame.__setattr__(frame_type.__name__, value)

            track.tags.add(frame)


class Mp4Tags(BaseHandler):
    _handles = [MP4.__name__]

    @staticmethod
    def get_value(track, tag_key):
        obj = track.get(tag_key)
        if obj is None:
            return ""

        return obj[0]

    @staticmethod
    def set_value(track, tag_key, value):
        obj = track.get(tag_key)
        if obj is not None:
            obj[0] = value
