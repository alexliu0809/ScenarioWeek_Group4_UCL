#/bin/bash

repository="git://github.com/alexliu0809/ScenarioWeek_Group4_UCL.git"

localFolder="./CODE/"

#git init

echo "Fetching from github origin"
git -C $localFolder fetch origin
echo "change branch to master"
git -C $localFolder checkout master
echo "merge master and origin/master"
git -C $localFolder merge origin/master
echo "fetch and merge successfully"
echo -e "\n"
