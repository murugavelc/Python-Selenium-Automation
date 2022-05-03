rem ==== Chrome Browser === *** change report name ****
pytest -v -m "sanity" --html=./Reports/report.html testCases/ --browser chrome
rem pytest -v -m "sanity and regression" --html=./Reports/report.html testCases/ --browser chrome
rem pytest -v -m "sanity or regression" --html=./Reports/report.html testCases/ --browser chrome
rem pytest -v -m "regression" --html=./Reports/report.html testCases/ --browser chrome

rem ==== Firefox Browser === *** change report name ****
rem pytest -v -m "sanity" --html=./Reports/report.html testCases/ --browser firefox
rem pytest -v -m "sanity and regression" --html=./Reports/report.html testCases/ --browser firefox
rem pytest -v -m "sanity or regression" --html=./Reports/report.html testCases/ --browser firefox
rem pytest -v -m "regression" --html=./Reports/report.html testCases/ --browser firefox

rem ==== Edge Browser === *** change report name ****
rem pytest -v -m "sanity" --html=./Reports/report.html testCases/ --browser edge
rem pytest -v -m "sanity and regression" --html=./Reports/report.html testCases/ --browser edge
rem pytest -v -m "sanity or regression" --html=./Reports/report.html testCases/ --browser edge
rem pytest -v -m "regression" --html=./Reports/report.html testCases/ --browser edge