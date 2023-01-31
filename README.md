# Test task for 365Scores

## Description
This project contains API and UI tests using Python 3.7 with allure reports. Also it contains small DB test to show tests with DB integration.

## How to start
Ensure you have Python 3.7 installed.
Then install dependencies from requirements.txt file based in root directory:

> pip install requirements.txt

Ensure you have [installed allure](https://docs.qameta.io/allure/#_installing_a_commandline) on your machine. 

## How to run tests

Tests are executed in 2 threads by default PyTest mechanism.
To run it in 2 threads with allure reports generation, run the following command:

> python -m pytest -n 2 -v -s --alluredir=allurereports

To generate allure report after test run:

> allure serve allurereports/
