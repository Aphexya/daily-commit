@echo off
cd /d D:\daily-commit
echo Daily commit at %date% %time% >> commit.log
git add .
git commit -m "Daily commit at %date% %time%"
git push origin main
