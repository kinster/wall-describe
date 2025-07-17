# VS Code Web

pyenv install 3.11.9
cd your-project-folder
pyenv local 3.11.9
pyenv version

rm -rf .venv
python3.11 -m venv .venv
python --version

source .venv/bin/activate

deactivate
pip install -r requirements.txt
uvicorn pyapp.legend_agent:app --reload --port 8000
uvicorn app.main:app --reload --port 8000

lsof -i :7071

func azure functionapp publish wall-describe-func --python
# wall-describe
