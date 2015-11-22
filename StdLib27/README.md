1. Download IronPython.
2. Run `ipy BuildStdLib27.py`.
3. Run `nuget pack StdLib27.nuspec`.
4. Run `nuget push IronPythonLibs.StdLib27.*.nupkg -apikey APIKEY -source https://www.myget.org/F/ironpythonlibs`.