set my_date=%date:/=%
set my_time=%time::=%
set my_timestamp=%my_date: =_%_%my_time:.=_%
behave --tages=wip -f allure_behave.formatter:AllureFormatter -o allure-results/%my_timestamp% ./features
allure generate allure-results/%my_timestamp% --clean && allure open