import os
import settings

def convert(src):
    data= loadSettings()
    converter = data.get('path')
    resolution = data.get('resolution')
    ext = data.get('ext')
    srcE= '\"'
    srcn = srcE+src+srcE
    cmd= ' '.join([converter, '-out', ext, '-ratio -resize', resolution, '0', '-overwrite', '-D', srcn])
    print(cmd)
    os.popen(cmd)
    name, oldext= os.path.splitext(src)
    if ext=='jpeg':
        ext='jpg'
    outsrc= name+'.'+ext
    outsrc= os.path.normpath(outsrc)
    # print(outsrc)
    # os.popen(cmd)
    return outsrc

    # os.popen(cmd)

def loadSettings():
    data = settings.settingsClass().load()
    return data
