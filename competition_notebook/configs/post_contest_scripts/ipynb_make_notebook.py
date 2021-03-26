from tomd import Tomd
from bs4 import BeautifulSoup
from fire import Fire
from atcodertools.client.atcoder import AtCoderClient, Contest
from pathlib import Path
from icecream import ic
import nbformat as nbf
from string import ascii_uppercase

def write2log(s):
    if Path('icecream.log').exists():
        with open("icecream.log", "a") as myfile:
            myfile.write(s+'\n')
    else:
        with open("icecream.log", "w+") as myfile:
            myfile.write(s+'\n')
            
ic.configureOutput(includeContext=True, outputFunction=write2log)


def main():
    root = Path('.').absolute()
    ic(root)

    contest_id = str(root.name)
    ic(contest_id)

    files = sorted(filter(lambda x: x.stem in ['main', 'problem'], root.glob('**/*.md')))

    nb = nbf.v4.new_notebook()
    nb['cells'].append(nbf.v4.new_markdown_cell(ic([f"<h1 style='text-align: center'>{contest_id}</h1>"])))

    for i, (code, problem) in enumerate(zip(files[::2], files[1::2])):
        assert code.stem == 'main', code
        assert problem.stem == 'problem', problem
        
        with open(code) as codef, open(problem) as problemf:
            alphabet = ascii_uppercase[i]

            nb['cells'].append(nbf.v4.new_markdown_cell(ic(problemf.readlines())))
            
            code_cell = [f"%%writefile {alphabet}/main.py\n"]+codef.readlines()
            nb['cells'].append(nbf.v4.new_code_cell(ic(code_cell)))
            
            nb['cells'].append(nbf.v4.new_code_cell(ic([f"!atcoder-tools test -d {alphabet} -e {alphabet}/main.py"])))
            nb['cells'].append(nbf.v4.new_code_cell(ic([f"!atcoder-tools submit -u -d {alphabet} -e {alphabet}/main.py"])))
        
    nbf.write(nb, f'{contest_id}.ipynb')    
    
if __name__=='__main__':
    try:
        Fire(main)
    except Exception as e:
        ic(e)