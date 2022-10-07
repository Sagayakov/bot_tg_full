@echo off

call %~dp0%pythonProject\venv\Scripts\activate

cd %~dp0%pythonProject

set TOKEN=794735589:AAGAz8Mnl-1fFwLXbvIeIkoMjwm8JPZVQOE

python main.py

pause