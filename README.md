# Prerequisites
- 3.6 =< [your python version]
- Install OpenSlide (see. https://openslide.org/download/)

# Setup

```
pip install -r requirements.txt
```

# How to use

patcher.py [-h] [-s OUTPUT_SIZE] [-ov OVERLAP] [-ou OUTPUT_DIR]
           [-t THRESH]
           img_path

- note :: "thresh" means the threshold value for deciding whether the patch is a part of a stump. Trying a few times with some values recommended.
