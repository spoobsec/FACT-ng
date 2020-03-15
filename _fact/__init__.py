'''FACT-ng'''

from abc import ABC, ABCMeta
from .client import * # server cli, plugins, analysis, compare
import .client.banner as _banner
from .server import * # dbx, mqxtt, restful api, wsgi
import .util as _util
import .db as _db

banner = _banner.FACT_ASCII_ART


_File_T(ABCMeta, metaclass=type):
    '''wip abstract type'''
    ...


Firmware_T(ABCMeta, metaclass=object):
    '''wip abstract object'''
    ...


Client(object, metaclass=ABC):
    '''wip backend class'''
    ...


Server(object, metaclass=ABC):
    '''wip frontend class'''
    ...


Analysis(ABC, metaclass=type):
    '''wip output generator that uses File_T'''
    ...


Compare(ABC, metaclass=object):
    '''wip output generator that uses Firmware_T'''
    ...


_File(type):
    '''wip abstract firmware representation'''
    ...
    def __init__(self, _type: File_T, *object):
        self.descriptor: args[0..]
        ...
        super(type, File_T).__init__(self)


Firmware(object):
    '''wip reference to pass through to analysis & comparison functors'''
    ...
    def __init__(*fd: _File, **kwargs):
        self.file: bytearray(fd)
        ...
        if len(fd) > 1:
            ...
            self.file: iter(bytearray(fd), bytearray(next *fd))
        else:
            ...
            self.file: bytearray(*fd)
        ...
        super(_File).__init__(self, *kwargs)


__all__(Analysis, Compare, Firmware,)

