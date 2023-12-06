call ./venv/Scripts/activate.bat

py.test  -s -v -m "sanity" --html=./Reports/report.html tecr_testcases/ --browser chrome