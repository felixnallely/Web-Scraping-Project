# Web-Scraping-Project
Before using this repository, you must install Python and must complete the rest of the setup.. Several steps are needed to configure VSCode, and you need to have installed the virtualenv pip package.

To use this repository:

1. Sign into your GitHub.
2. On your computer, clone this repository.
3. Change to the directory you just cloned. Create a virtual environment:  
python -m venv .venv
source .venv/bin/activate
code .
```
For some environments, you have to use the `python3` command.  For Windows users (you should use Git Bash in Windows), the command is different:
```shell
python -m venv .venv
source .venv/Scripts/activate
code .
```
4. Important: Open the VSCode command pallette (ctrl-shift P).  In the `Python: Select Interpreter` option, choose the one with `.venv`.  You can use the search box at the top to find it.  If you have any terminal sessions open, close them, and open a new one.  You will see `(.venv)` in your terminal prompt.
5. From the VSCode terminal session, enter the command:
```shell
pip install -r requirements.txt
```

In some cases, you will need to install additional pip packages.

6. How to run the project.
- Run the scraper
- Run the Cleaning script 
- Load data into SQLite 
- Launch Streamlit Dashboard --> streamlit run streamlit_app.py