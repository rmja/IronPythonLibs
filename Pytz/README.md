1. Download IronPython.
2. Run `ipy BuildPytz.py`.
3. Run `nuget pack Pytz.nuspec`.
4. Run `nuget push IronPythonLibs.Pytz.*.nupkg -apikey APIKEY -source https://www.myget.org/F/ironpythonlibs`.