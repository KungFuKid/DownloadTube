

:: 设置安装环境变量
if exist "%~dp0\Android Studio\bin\studio64.exe" SET ANDROID_STUDIO_INSTALLDIR=%~dp0Android Studio
if exist "%~dp0\sdk\platform-tools\adb.exe" SET SDK_INSTALLDIR=%~dp0sdk



echo %ANDROID_STUDIO_INSTALLDIR%
echo %SDK_INSTALLDIR%

netstat -ano | findstr "5037" > py\testAdb.txt
C:\Python34\python py\start_env.py find py\testAdb.txt

del /F /Q py\testAdb.txt

"%ANDROID_STUDIO_INSTALLDIR%\bin\studio64.exe"