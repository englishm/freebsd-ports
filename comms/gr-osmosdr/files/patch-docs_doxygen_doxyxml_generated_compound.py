--- docs/doxygen/doxyxml/generated/compound.py.orig	2018-08-15 17:53:26 UTC
+++ docs/doxygen/doxyxml/generated/compound.py
@@ -3,15 +3,17 @@
 """
 Generated Mon Feb  9 19:08:05 2009 by generateDS.py.
 """
+from __future__ import absolute_import
+from __future__ import unicode_literals
 
-from string import lower as str_lower
+
 from xml.dom import minidom
 from xml.dom import Node
 
 import sys
 
-import compoundsuper as supermod
-from compoundsuper import MixedContainer
+from . import compoundsuper as supermod
+from .compoundsuper import MixedContainer
 
 
 class DoxygenTypeSub(supermod.DoxygenType):
