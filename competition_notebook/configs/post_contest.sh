touch icecream.log
echo "--- post contest scripts ---" >> icecream.log
echo "--- $PWD ---" >> icecream.log

python  /home/me/atcoder-nbdev/competition_notebook/configs/post_contest_scripts/ipynb_make_notebook.py >> icecream.log