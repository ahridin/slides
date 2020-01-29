import fuse
import stat
import errno

fuse.fuse_python_api = (0, 2)

class PyConFS(fuse.Fuse):
    _PATH = "/hello_pycon19"
    _DATA = "PyCon rocks \m/\n"

    def getattr(self, path):
        print("getattr({})".format(path))
        if path == "/":
            return fuse.Stat(st_mode=stat.S_IFDIR | 0o755, st_nlink=1)
        if path == self._PATH:
            return fuse.Stat(st_mode=stat.S_IFREG | 0o600,
                             st_size=len(self._DATA),
                             st_nlink=1)
        return -errno.ENOENT

    def readdir(self, path, offset):
        print("readdir({}, {})".format(path, offset))
        if path == "/":
            for r in (".", "..", self._PATH[1:]):
                yield fuse.Direntry(r)

    def read(self, path, size, offset):
        print("read({}, {}, {})".format(path, size, offset))
        if path != self._PATH:
            return -errno.ENOENT
        data_size = len(self._DATA)
        if offset < data_size:
            if offset + size > data_size:
                size = data_size - offset
            buf = self._DATA[offset:offset+size]
        else:
            buf = ""
        return buf


if __name__ == '__main__':
    server = PyConFS()
    server.parse()
    server.main()
