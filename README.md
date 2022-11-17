# How to use it

1- Install dev and venv
```
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

2- Classify with output:
```
python3 detect.py daily-hack3/test-images/test4.png
```

# How it works

I have:
- Decomposed the colors of the figures with `get_colors.py`
- Made a c based on the number of sides and the colors.
- Made a color classifier
- Detect Lleidahack logos based on a template

# How well does it work?

Bad. But good enough for this daily hack.
I'm an engineer. I do the work as best as I can with the time and resources I have.