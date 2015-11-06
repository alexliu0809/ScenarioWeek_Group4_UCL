#/bin/bash

repository="https://github.com/alexliu0809/ScenarioWeek_Group4_UCL.git"

localFolder="./CODE/"

#echo "checking arguments"
#if [ $* -le 0]
#	exit
#fi
#echo "entering folder"
#cd $1
echo "creating folder for Data"
mkdir CODE
echo "entering folder"
cd $localFolder
echo "cloning the repository"
git clone $repository
#echo "initializing git folder"
#git -C init
#echo "connecting to remote server"
#git remote add origin $repository

#echo "Fetching from github origin"
#git -C $localFolder fetch origin
#echo "change branch to master"
#git -C $localFolder checkout master
#echo "merge master and origin/master"
#git -C $localFolder merge origin/master
#echo "fetch and merge successfully"

echo -e "\n"
