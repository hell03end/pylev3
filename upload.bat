python setup.py sdist
twine upload dist/*
rd /S /Q pylev3.egg-info
rd /S /Q dist
del MANIFEST
del setup.cfg
