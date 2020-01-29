import fuse
import stat

fuse.fuse_python_api = (0, 2)

class PyConFS(fuse.Fuse):
    def getattr(self, path):
        print("Received path [%s]" % path)
        if path == "/":
            return fuse.Stat(st_mode=stat.S_IFDIR | 0o755,
                             st_nlink=1)

if __name__ == '__main__':
    server = PyConFS()
    server.parse()
    server.main()
