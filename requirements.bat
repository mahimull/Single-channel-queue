:: windows

echo 'To install Necessary Libraries'
echo 'Make sure you have active internet connection'
python -m pip install --user numpy scipy matplotlib ipython jupyter pandas sympy nose
pip install colored

:: Linux(Ubuntu and Debian)
:: sudo apt-get install python-numpy python-scipy python-matplotlib ipython ipython-notebook python-pandas python-sympy python-nose
:: pip install colored

timeout 3

pause
