--- docs/doxygen/doxyxml/generated/index.py.orig	2018-08-15 17:53:26 UTC
+++ docs/doxygen/doxyxml/generated/index.py
@@ -3,14 +3,16 @@
 """
 Generated Mon Feb  9 19:08:05 2009 by generateDS.py.
 """
+from __future__ import absolute_import
+from __future__ import unicode_literals
 
 from xml.dom import minidom
 
 import os
 import sys
-import compound
+from . import compound
 
-import indexsuper as supermod
+from . import indexsuper as supermod
 
 class DoxygenTypeSub(supermod.DoxygenType):
     def __init__(self, version=None, compound=None):
