--- docs/doxygen/doxyxml/example/xml/combine.xslt.orig	2018-08-15 17:53:26 UTC
+++ docs/doxygen/doxyxml/example/xml/combine.xslt
@@ -1,15 +0,0 @@
-<!-- XSLT script to combine the generated output into a single file.
-     If you have xsltproc you could use:
-     xsltproc combine.xslt index.xml >all.xml
--->
-<xsl:stylesheet xmlns:xsl="http://www.w3.org/1999/XSL/Transform" version="1.0">
-  <xsl:output method="xml" version="1.0" indent="yes" standalone="yes" />
-  <xsl:template match="/">
-    <doxygen version="{doxygenindex/@version}">
-      <!-- Load all doxgen generated xml files -->
-      <xsl:for-each select="doxygenindex/compound">
-        <xsl:copy-of select="document( concat( @refid, '.xml' ) )/doxygen/*" />
-      </xsl:for-each>
-    </doxygen>
-  </xsl:template>
-</xsl:stylesheet>
