Fix arguments that are passed to mpv.

Backported and adapted for the 2.1.16 release.

Obtained from: https://github.com/ankitects/anki/commit/ccd715013609133c55e83924734efa78abc03326

--- anki/sound.py.orig	2020-02-18 09:38:48 UTC
+++ anki/sound.py
@@ -124,7 +124,6 @@ class MpvManager(MPV):
 def setMpvConfigBase(self):
  mpvConfPath = os.path.join(self, "mpv.conf")
  MpvManager.default_argv += [-       "--no-config", f"--include={mpvConfPath}"]
 
