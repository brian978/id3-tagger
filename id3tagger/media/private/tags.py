from . import BaseTag
import mutagen.id3
from mutagen.mp3 import MP3
from mutagen.mp4 import MP4
from mutagen.aiff import AIFF


class Artist(BaseTag):
    _keys = {
        MP3.__name__: mutagen.id3.TPE1,
        AIFF.__name__: mutagen.id3.TPE1,
        MP4.__name__: "\xa9ART",
    }


class Title(BaseTag):
    _keys = {
        MP3.__name__: mutagen.id3.TIT2,
        AIFF.__name__: mutagen.id3.TIT2,
        MP4.__name__: "\xa9nam",
    }


class Album(BaseTag):
    _keys = {
        MP3.__name__: mutagen.id3.TALB,
        AIFF.__name__: mutagen.id3.TALB,
        MP4.__name__: "\xa9alb",
    }


class AlbumArtist(BaseTag):
    _keys = {
        MP3.__name__: mutagen.id3.TPE2,
        AIFF.__name__: mutagen.id3.TPE2,
        MP4.__name__: "aART",
    }


class Grouping(BaseTag):
    _keys = {
        MP3.__name__: mutagen.id3.GRP1,
        AIFF.__name__: mutagen.id3.GRP1,
        MP4.__name__: "\xa9grp",
    }


class Genre(BaseTag):
    _keys = {
        MP3.__name__: mutagen.id3.TCON,
        AIFF.__name__: mutagen.id3.TCON,
        MP4.__name__: "\xa9gen",
    }


class Year(BaseTag):
    _keys = {
        MP3.__name__: mutagen.id3.TDRC,
        AIFF.__name__: mutagen.id3.TDRC,
        MP4.__name__: "\xa9day",
    }

    def set(self, value):
        """ The year has a different type than the others """
        if not isinstance(value, str) or len(value) < 4:
            value = None

        if self._track.__class__.__name__ == MP4.__name__:
            return super(Year, self).set(value)

        return super(Year, self).set(mutagen.id3.ID3TimeStamp(value))

    def get(self):
        value = super(Year, self).get()
        return value


class TrackNumber(BaseTag):
    _keys = {
        MP3.__name__: mutagen.id3.TRCK,
        AIFF.__name__: mutagen.id3.TRCK,
        MP4.__name__: "trkn",
    }


class DiscNumber(BaseTag):
    _keys = {
        MP3.__name__: mutagen.id3.TPOS,
        AIFF.__name__: mutagen.id3.TPOS,
        MP4.__name__: "disk",
    }


class Bpm(BaseTag):
    _keys = {
        MP3.__name__: mutagen.id3.TBPM,
        AIFF.__name__: mutagen.id3.TBPM,
        MP4.__name__: "tmpo",
    }

    def set(self, value):
        value = int(value)
        super(Bpm, self).set(value)


class Comments(BaseTag):
    _keys = {
        MP3.__name__: mutagen.id3.COM,
        AIFF.__name__: mutagen.id3.COM,
        MP4.__name__: "\xa9cmt",
    }

