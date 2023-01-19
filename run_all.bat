set mydate=%date:/=%
set mytime=%time::=%
set mytimestamp=%mydate: =_%_%mytime:.=_%
behave -f allure_behave.formatter:AllureFormatter -o allure-results/%mytimestamp% ./features
allure generate allure-results/%mytimestamp% --clean && allure open