from itertools import product
import argparse
from joblib import Parallel, delayed
from pathlib import Path
import openslide
from openslide.deepzoom import DeepZoomGenerator


class Patcher:

    def __init__(self):
        self._get_args()
        self._make_output_dir()
        self._read_img()

    def _get_args(self):
        parser = argparse.ArgumentParser(description="Make patches from WSI.")
        parser.add_argument("img_path",
                            help="Path to the whole slide image.")
        parser.add_argument("output_size",
                            help="Output patch size of both x, y")
        parser.add_argument("overlap",
                            help="Overlap size.")
        parser.add_argument("output_dir",
                            help="Where to save the patches.")
        self.args = parser.parse_args()

    def _make_output_dir(self):
        if not Path(self.args.output_dir).exists():
            Path(self.args.output_dir).mkdir(parents=True)
        self.output_dir = Path(self.args.output_dir)

    def _read_img(self):
        img = openslide.OpenSlide(self.args.img_path)
        self.dzimg = DeepZoomGenerator(img,
                                       int(self.args.output_size),
                                       int(self.args.overlap))
        self.tiles = self.dzimg.level_tiles[-1]
        self.deepest_level = self.dzimg.level_count - 1
        self.iterator = product(range(self.tiles[0]), range(self.tiles[1]))

    def make_patch(self, x, y):
        patch = self.dzimg.get_tile(self.deepest_level, (x, y))
        patch.save(f"{self.output_dir}/{x:04}_{y:04}.png")

    def make_patch_parallel(self):
        p = Parallel(n_jobs=-1, verbose=3, backend="threading")
        p([delayed(self.make_patch)(x, y) for x, y in self.iterator])

    def make_patch_for(self):
        for x, y in self.iterator:
            self.make_patch(x, y)


if __name__ == '__main__':
    p = Patcher()
    p.make_patch_parallel()
    # p.make_patch_for() # use if make_patch_parallel doesn't work.
