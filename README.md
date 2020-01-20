# MicroPythonNeopixelDisplay
A segment display that shows random numbers

To make this, cut 7 strips of nexopixels that are 10 pixels each in length  
Solder wires to each end and connect them  

<blockquote class="imgur-embed-pub" lang="en" data-id="a/iTQkaMw"><a href="//imgur.com/a/iTQkaMw"></a></blockquote><script async src="//s.imgur.com/min/embed.js" charset="utf-8"></script>

Then, starting from the center left line in a figure 8, lay the pixel segments as in the diagram.  
Connect to an ESP8266 running MicroPython to power, ground, and Pin 2  
Upload the .Py file to play the random number generator  

You can also open the Jupyter Notebook file to run tests, play messages, or write your own.
Working with MicroPython in Jupyter Notebook is easy and cool. To do it, install Jupyter Notebook, then install the Jupyter Notebook kernal. 

For Micropython on Jupyter, run these in a terminal window:  
git clone https://github.com/goatchurchprime/jupyter_micropython_kernel.git  
pip install -e jupyter_micropython_kernel  
python -m jupyter_micropython_kernel.install

See if it's installed with:  
jupyter kernelspec list  

Go here for troubleshooting: https://towardsdatascience.com/micropython-on-esp-using-jupyter-6f366ff5ed9

