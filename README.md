Info
===

**pyDLAPK** a/k/a **python-download-apk** is Python script to download APK files from Google play (Google market) to PC / Computer. In it's main action pyDLAPK is parsing web-convert and give output as file. Only one function is supported and that one is to download *apk* file from the market official. Other then that, pyDLAPK also have a custom-made progressbar.


Dependencies
===

* Python 2.7
* Windows / Linux / Mac

Usage
===

	* Concept:- `$ python pydlpak.py https://play.google.com/url`  
	* Example:- `$ python pydlapk.py https://play.google.com/store/apps/details?id=com.facebook.katana`  

```
$ python pydlapk.py https://play.google.com/store/apps/details?id=com.facebook.katana
              _____  _____   _______ ______ __  __ 
.-----.--.--.|     \|     |_|   _   |   __ \  |/  |
|  _  |  |  ||  --  |       |       |    __/     < 
|   __|___  ||_____/|_______|___|___|___|  |__|\__|
|__|  |_____|                                      
Simple APK downloader written in python; 			
dn5 / http://dn5.ljuska.org / @dn5__               
       											
Usage: pyDLAPK.py http://play.google.com/url       
===================================================

User-agent in use 		: Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:29.0) Gecko/20100101 Firefox/29.0
URL which points the file  	: https://play.google.com/store/apps/details?id=com.facebook.katana
Package to download 		: com.facebook.katana
===================================================
Downloading APK package com.facebook.katana with total size of 20880269 bytes.
 Filename com.facebook.katana is downloaded!
```

Dev-notes
===
- TODO
	* Check if URL is ok using regex
	* Check if file is not free

About
===
Coded by dn5, check my [blog](http://dn5.ljuska.org), my [twitter](https://twitter.com/dn5__) and my [github](https://github.com/dn5/). If you have any questions, you can [email](mailto:dn5@dn5.ljuska.org) me anytime. Report any bugs you found. Tested in Linux Ubuntu 14.04 -

License
===
This software is not intended to replace mobile downloading operation from Google play, it is used for testing purpose and is not suported to use for illegal act. Me, **dn5** coded this software for testing purpose and learning experience with Python. **Software is licensed under [GNU General Public License v3.0](http://opensource.org/licenses/GPL-3.0) (GPL-3.0).**  