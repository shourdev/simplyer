@echo off
title Simplyer
echo Simplyer
echo Press 1 to install Simplyer Normal
echo press 2 to install Simplyer Portable
echo press 3 to Exit
set /p car=
if %car% == 1 goto installnormal
if %car% == 2 goto installport
if %car% == 3 goto exit
:installnormal
echo Downloading Setup for Installer
powershell Invoke-WebRequest https://github.com/shourgamer2/simplyer/releases/download/updater/update.exe -OutFile .\simplyer.exe
start simplyer.exe
exit
:installport
echo Downloading portable version
powershell Invoke-WebRequest https://github.com/shourgamer2/simplyer/releases/download/port1.1.0/simplyer-port.exe -OutFile .\simplyerport.exe
echo Download please move this file to your portable storage device
exit
:exit
exit