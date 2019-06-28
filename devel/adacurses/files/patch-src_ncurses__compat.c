--- src/ncurses_compat.c.orig	2015-08-06 23:09:10 UTC
+++ src/ncurses_compat.c
@@ -66,7 +66,13 @@ has_mouse(void)
 /*
  * These are provided by lib_gen.c:
  */
-#if NCURSES_VERSION_PATCH < 20070331
+#if (NCURSES_VERSION_PATCH < 20070331) || (defined is_keypad && defined is_scrollok)
+#ifdef is_keypad
+#undef is_keypad
+#endif
+#ifdef is_scrollok
+#undef is_scrollok
+#endif
 extern bool (is_keypad) (const WINDOW *);
 extern bool (is_scrollok) (const WINDOW *);
 
