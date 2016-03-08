#! /usr/bin/env python
import re
import os
import sys
import zipfile


for root, dirs, filenames in os.walk("."):
	for f in filenames:
		if f.endswith(".zip"):
			name = f[0:f.index(".zip")]
			if name+".txt" not in filenames:
				try:
					filepath = os.path.join(root, f)
					zf = zipfile.ZipFile(filepath)
					zf.extractall()
					zf.close()
				except:
					print 'No se pudo descomprimir' + filepath
