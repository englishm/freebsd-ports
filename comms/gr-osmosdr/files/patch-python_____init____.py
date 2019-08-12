--- python/__init__.py.orig	2018-08-15 17:53:26 UTC
+++ python/__init__.py
@@ -22,8 +22,15 @@
 This is the GNU Radio OsmoSDR module.
 '''
 
+from __future__ import unicode_literals
+
 # import swig generated symbols into the osmosdr namespace
-from osmosdr_swig import *
+try:
+    # this might fail if the module is python-only
+    from .osmosdr_swig import *
+except ImportError as ie:
+    print(ie)
+    pass
 
 # import any pure python here
 #
