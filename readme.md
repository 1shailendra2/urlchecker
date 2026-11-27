# urlchecker

Practice repo for QA automation: log-parsing scripts with pytest tests, Playwright tests on saucedemo.com, and API tests with requests.

## Folders
- root: log scripts (`lvlsfunc.py`, `logentry.py`) and their tests
- `playwright_tests/`: browser tests on saucedemo.com
- `api_tests/`: API tests against jsonplaceholder.typicode.com

## Run
pip install pytest requests pytest-playwright
playwright install chromium
pytest api_tests test_logentry.py test_lvlsfunc.py
pytest playwright_tests --headed