@echo off
if not defined JAVA_HOME (
	echo fatal: you want to set the environment variable JAVA_HOME
	goto end
)
PATH %JAVA_HOME%\bin\
for /f tokens^=2-5^ delims^=.-_^" %%j in ('java -fullversion 2^>^&1') do set "jver=%%j%%k%%l%%m"
if %jver% LSS 18000 (
	echo fatal: jdk 1.8 or higher expected.
	goto end
)

"%JAVA_HOME%\bin\java.exe" -cp defexts-core-1.0.0.jar org.mudebug.defexts.main.Main database %*
 
:end