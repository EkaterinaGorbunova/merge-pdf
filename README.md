0. Clone repository

1. `cd` into cloned repository

2. Create pyton virtual environment

```cmd
python -m venv .venv_python
```

3. Activate virtual environment

```cmd
.venv_python\Scripts\activate.bat
```

4. Update pip

```cmd
python.exe -m pip install --upgrade pip
pip install --upgrade pip
```

5. install requirments

```cmd
pip install -r requirements.txt
```

6. Run script

    6.1 Put `.pdf` files in the script location to merge 

    6.2 Run script:

```Bash
cd <your_script_location>
python merge_pdf.py
```