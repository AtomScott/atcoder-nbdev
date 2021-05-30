touch icecream.log
echo "--- post contest scripts ---" >> icecream.log
echo "--- $PWD ---" >> icecream.log

python  /data/configs/post_contest_scripts/ipynb_make_notebook.py >> icecream.log