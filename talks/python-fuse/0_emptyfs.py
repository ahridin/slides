import fuse

fuse.fuse_python_api = (0, 2)

class PyConFS(fuse.Fuse): pass

if __name__ == '__main__':
    server = PyConFS()
    server.parse()
    server.main()
