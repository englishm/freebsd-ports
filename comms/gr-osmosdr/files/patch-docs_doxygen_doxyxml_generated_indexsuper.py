--- docs/doxygen/doxyxml/generated/indexsuper.py.orig	2018-08-15 17:53:26 UTC
+++ docs/doxygen/doxyxml/generated/indexsuper.py
@@ -4,12 +4,16 @@
 # Generated Thu Jun 11 18:43:54 2009 by generateDS.py.
 #
 
+from __future__ import print_function
+from __future__ import unicode_literals
+
 import sys
-import getopt
-from string import lower as str_lower
+
 from xml.dom import minidom
 from xml.dom import Node
 
+import six
+
 #
 # User methods
 #
@@ -19,9 +23,9 @@ from xml.dom import Node
 
 try:
     from generatedssuper import GeneratedsSuper
-except ImportError, exp:
+except ImportError as exp:
 
-    class GeneratedsSuper:
+    class GeneratedsSuper(object):
         def format_string(self, input_data, input_name=''):
             return input_data
         def format_integer(self, input_data, input_name=''):
@@ -64,7 +68,7 @@ def showIndent(outfile, level):
         outfile.write('    ')
 
 def quote_xml(inStr):
-    s1 = (isinstance(inStr, basestring) and inStr or
+    s1 = (isinstance(inStr, six.string_types) and inStr or
           '%s' % inStr)
     s1 = s1.replace('&', '&amp;')
     s1 = s1.replace('<', '&lt;')
@@ -72,7 +76,7 @@ def quote_xml(inStr):
     return s1
 
 def quote_attrib(inStr):
-    s1 = (isinstance(inStr, basestring) and inStr or
+    s1 = (isinstance(inStr, six.string_types) and inStr or
           '%s' % inStr)
     s1 = s1.replace('&', '&amp;')
     s1 = s1.replace('<', '&lt;')
@@ -102,7 +106,7 @@ def quote_python(inStr):
             return '"""%s"""' % s1
 
 
-class MixedContainer:
+class MixedContainer(object):
     # Constants for category:
     CategoryNone = 0
     CategoryText = 1
@@ -462,7 +466,7 @@ Options:
 """
 
 def usage():
-    print USAGE_TEXT
+    print(USAGE_TEXT)
     sys.exit(1)
 
 
@@ -520,4 +524,3 @@ if __name__ == '__main__':
     main()
     #import pdb
     #pdb.run('main()')
-
