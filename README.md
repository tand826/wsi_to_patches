# Prerequisites
- 3.6 =< [your python version]
- Install OpenSlide (see. https://openslide.org/download/)

# Setup

```
pip install -r requirements.txt
```

# How to use

python patcher.py [wsi file] [output size] [overlap size] [directory to output] [value for onshore check]

- note :: "value for onshore check" means the threshold value for deciding whether the patch is a part of stump.