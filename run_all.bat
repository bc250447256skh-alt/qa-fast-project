@echo off

echo ==============================
echo Running API tests
echo ==============================
pytest api/
IF %ERRORLEVEL% NEQ 0 exit /b %ERRORLEVEL%

echo ==============================
echo Running SQL tests
echo ==============================
pytest sql/
IF %ERRORLEVEL% NEQ 0 exit /b %ERRORLEVEL%

echo ==============================
echo Running UI tests
echo ==============================
npx playwright test --reporter=html
IF %ERRORLEVEL% NEQ 0 exit /b %ERRORLEVEL%

echo ==============================
echo All tests passed!
echo ==============================
