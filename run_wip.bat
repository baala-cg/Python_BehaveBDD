set mydate=%date:/=%
set mytime=%time::=%
set mytime=%mytime: =%
set mytimestamp=%mydate: =_%_%mytime:.=_%
echo %mytimestamp%

behave --tags=wip -f allure_behave.formatter:AllureFormatter -o allure-results/%my_timestamp% ./features
allure generate allure-results/%my_timestamp% --clean && allure open