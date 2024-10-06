#Update repo
git add .
git commit -am "$1"
branch=$(git rev-parse --abbrev-ref HEAD)
git push origin $branch
echo -e "Update of TOC..."
python3 Tools/generateTOC.py
echo -e "TOC updated !