# template-pyqt

A template for future PyQt projects.
Currently incomplete.

1. Pending: 2 types of multithreading, using runnable threadpool and thread

## Pre-requisite
1. Install [Python packages](https://github.com/xfortisfye/303-see-other/blob/main/dependencies.md#install-python-packages)
2. Install [Qt Designer](https://build-system.fman.io/qt-designer-download)
3. Install [video codecs](https://files3.codecguide.com/K-Lite_Codec_Pack_1575_Basic.exe)

-----

### start using QT Designer

1. Throw a layout in the main window.
2. Right click and select `Layout horizontally` or `Layout vertically`


### generating resources file
```bash
pyrcc5 resources.qrc -o resources.py
```



