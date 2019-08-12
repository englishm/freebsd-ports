--- docs/doxygen/doxyxml/generated/compoundsuper.py.orig	2018-08-15 17:53:26 UTC
+++ docs/doxygen/doxyxml/generated/compoundsuper.py
@@ -4,12 +4,17 @@
 # Generated Thu Jun 11 18:44:25 2009 by generateDS.py.
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
+
 #
 # User methods
 #
@@ -19,9 +24,9 @@ from xml.dom import Node
 
 try:
     from generatedssuper import GeneratedsSuper
-except ImportError, exp:
+except ImportError as exp:
 
-    class GeneratedsSuper:
+    class GeneratedsSuper(object):
         def format_string(self, input_data, input_name=''):
             return input_data
         def format_integer(self, input_data, input_name=''):
@@ -64,7 +69,7 @@ def showIndent(outfile, level):
         outfile.write('    ')
 
 def quote_xml(inStr):
-    s1 = (isinstance(inStr, basestring) and inStr or
+    s1 = (isinstance(inStr, six.string_types) and inStr or
           '%s' % inStr)
     s1 = s1.replace('&', '&amp;')
     s1 = s1.replace('<', '&lt;')
@@ -72,7 +77,7 @@ def quote_xml(inStr):
     return s1
 
 def quote_attrib(inStr):
-    s1 = (isinstance(inStr, basestring) and inStr or
+    s1 = (isinstance(inStr, six.string_types) and inStr or
           '%s' % inStr)
     s1 = s1.replace('&', '&amp;')
     s1 = s1.replace('<', '&lt;')
@@ -102,7 +107,7 @@ def quote_python(inStr):
             return '"""%s"""' % s1
 
 
-class MixedContainer:
+class MixedContainer(object):
     # Constants for category:
     CategoryNone = 0
     CategoryText = 1
@@ -4221,7 +4226,7 @@ class codelineType(GeneratedsSuper):
         if attrs.get('lineno'):
             try:
                 self.lineno = int(attrs.get('lineno').value)
-            except ValueError, exp:
+            except ValueError as exp:
                 raise ValueError('Bad integer attribute (lineno): %s' % exp)
         if attrs.get('refkind'):
             self.refkind = attrs.get('refkind').value
@@ -4504,12 +4509,12 @@ class referenceType(GeneratedsSuper):
         if attrs.get('endline'):
             try:
                 self.endline = int(attrs.get('endline').value)
-            except ValueError, exp:
+            except ValueError as exp:
                 raise ValueError('Bad integer attribute (endline): %s' % exp)
         if attrs.get('startline'):
             try:
                 self.startline = int(attrs.get('startline').value)
-            except ValueError, exp:
+            except ValueError as exp:
                 raise ValueError('Bad integer attribute (startline): %s' % exp)
         if attrs.get('refid'):
             self.refid = attrs.get('refid').value
@@ -4627,17 +4632,17 @@ class locationType(GeneratedsSuper):
         if attrs.get('bodystart'):
             try:
                 self.bodystart = int(attrs.get('bodystart').value)
-            except ValueError, exp:
+            except ValueError as exp:
                 raise ValueError('Bad integer attribute (bodystart): %s' % exp)
         if attrs.get('line'):
             try:
                 self.line = int(attrs.get('line').value)
-            except ValueError, exp:
+            except ValueError as exp:
                 raise ValueError('Bad integer attribute (line): %s' % exp)
         if attrs.get('bodyend'):
             try:
                 self.bodyend = int(attrs.get('bodyend').value)
-            except ValueError, exp:
+            except ValueError as exp:
                 raise ValueError('Bad integer attribute (bodyend): %s' % exp)
         if attrs.get('bodyfile'):
             self.bodyfile = attrs.get('bodyfile').value
@@ -6778,12 +6783,12 @@ class docTableType(GeneratedsSuper):
         if attrs.get('rows'):
             try:
                 self.rows = int(attrs.get('rows').value)
-            except ValueError, exp:
+            except ValueError as exp:
                 raise ValueError('Bad integer attribute (rows): %s' % exp)
         if attrs.get('cols'):
             try:
                 self.cols = int(attrs.get('cols').value)
-            except ValueError, exp:
+            except ValueError as exp:
                 raise ValueError('Bad integer attribute (cols): %s' % exp)
     def buildChildren(self, child_, nodeName_):
         if child_.nodeType == Node.ELEMENT_NODE and \
@@ -7108,7 +7113,7 @@ class docHeadingType(GeneratedsSuper):
         if attrs.get('level'):
             try:
                 self.level = int(attrs.get('level').value)
-            except ValueError, exp:
+            except ValueError as exp:
                 raise ValueError('Bad integer attribute (level): %s' % exp)
     def buildChildren(self, child_, nodeName_):
         if child_.nodeType == Node.TEXT_NODE:
@@ -8283,7 +8288,7 @@ Options:
 """
 
 def usage():
-    print USAGE_TEXT
+    print(USAGE_TEXT)
     sys.exit(1)
 
 
@@ -8339,4 +8344,3 @@ if __name__ == '__main__':
     main()
     #import pdb
     #pdb.run('main()')
-
