from tomd import Tomd
from bs4 import BeautifulSoup
from fire import Fire
from atcodertools.client.atcoder import AtCoderClient, Contest
from pathlib import Path
from icecream import ic

def write2log(s):
    if Path('icecream.log').exists():
        with open("icecream.log", "a") as myfile:
            myfile.write(s+'\n')
    else:
        with open("icecream.log", "w+") as myfile:
            myfile.write(s+'\n')
            
ic.configureOutput(includeContext=True, outputFunction=write2log)


def main(lang='ja'):
    
    alphabet = str(Path('.').absolute().name)
    contest_id = str(Path('.').absolute().parent.name)
    
    client = AtCoderClient()
    client.login()
    ic(client.check_logging_in())
    
    contest = Contest(ic(contest_id))
    ic(contest.get_url())
    problem_list = client.download_problem_list(ic(contest))
    problem =  problem_list[['A','B','C','D','E','F'].index(ic(alphabet))]   
    
    html_doc = client.download_problem_content(problem).original_html
    soup = BeautifulSoup(html_doc, 'html.parser')

    title = soup.find(class_="h2").get_text()
    task_statement = soup.find(id="task-statement")

    if lang=='ja':
        task_statement = task_statement.find(class_='lang-ja')

    def sanitize_html_for_ipynb(html_doc):
        replace_dict = {
            '<var>':'$',
            '</var>': '$',
            '<pre>':'<pre><code>',
            '</pre>':'</code></pre>'
        }
        for old_word, new_word in replace_dict.items():
            html_doc = html_doc.replace(old_word, new_word)
        return ic(html_doc)

    title = str(sanitize_html_for_ipynb(str(title)))
    title = title.lstrip().split('\n')[0]
    
    task_statement = Tomd(sanitize_html_for_ipynb(str(task_statement)))
    with open('problem.md', 'w+') as f:
        f.write(f"## {ic(title)}\n")
        f.write('---\n')
        f.write(task_statement.markdown)
    
if __name__=='__main__':
    try:
        Fire(main)
    except Exception as e:
        ic(e)