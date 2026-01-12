[app]
title = XeleryScan
package.name = xeleryscan
package.domain = org.xelery
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 0.1

# J'ai ajouté libzbar ici pour que le scanner marche !
requirements = python3,kivy==2.2.1,pillow,pyzbar,requests,android,libzbar

orientation = portrait
fullscreen = 0
android.permissions = CAMERA, INTERNET
android.api = 31
android.minapi = 21
# On force une version stable du NDK pour éviter les bugs
android.ndk = 23b
android.archs = arm64-v8a

[buildozer]
log_level = 2
warn_on_root = 1
