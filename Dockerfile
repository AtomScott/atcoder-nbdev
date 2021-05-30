FROM fastai/codespaces

RUN pip install jupyterlab networkx icecream fire Tomd 
RUN pip install git+https://github.com/AtomScott/atcoder-tools.git