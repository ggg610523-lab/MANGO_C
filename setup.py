from setuptools import setup

APP = ['menubar.py']
OPTIONS = {
    'argv_emulation': True,
    'iconfile': None,  # you can set a .icns file here if you want an icon
    'packages': ['rumps'],
}

setup(
    app=APP,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
)

