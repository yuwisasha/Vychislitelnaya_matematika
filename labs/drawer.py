import numpy as np
import matplotlib.pyplot as plt

from csv import DictReader

from numpy.typing import NDArray
from scipy.interpolate import make_interp_spline


class Drawer:
    linspace_num: int = 500

    def __init__(
        self,
        x: NDArray | None = None,
        y: NDArray | None = None,
        /,
        *,
        x_scale: float = 1.0,
        y_scale: float = 1.0,
        y_lim: tuple[float, float] = (0.0, 1.0),
        x_lim: tuple[float, float] = (0.0, 1.0),
    ) -> None:
        self.x = x
        self.y = y
        self.x_scale = x_scale
        self.y_scale = y_scale
        self.ylim = y_lim
        self.xlim = x_lim

    def _set_lims(self) -> None:
        x_max = self.x.max() * self.x_scale
        y_max = self.y.max() * self.y_scale
        self.xlim, self.ylim = (-x_max, x_max), (-y_max, y_max)

    def get_tabled_defined_func(
        self,
        filename: str,
    ) -> None:
        """If instance of "Drawer" was created without
        a given "x" and "y" arrays,
        it's possible to read .csv file, which looks like\n
        x,y;\n
        0.1,1.0;\n
        0.2,3.0;\n
        ...;\n
        1.0,5.3;"""

        if self.x is None and self.y is None:
            x, y = [], []
            with open(filename, newline="") as csvfile:
                reader = DictReader(csvfile)
                for row in reader:
                    x.append(float(row["x"]))
                    y.append(float(row["y"]))

            self.x = np.array(x)
            self.y = np.array(y)

            self._set_lims()

        else:
            return

    def smooth_func(self) -> None:
        """If graph has a sharp corners, use this function to smooth it,
        it add's values between points"""

        spline = make_interp_spline(self.x, self.y)
        self.x = np.linspace(self.x.min(), self.x.max(), self.linspace_num)
        self.y = spline(self.x)

    def draw_graph(self) -> None:
        """Also forces to move axes to center"""
        self.x, self.y = self.x * self.x_scale, self.y * self.y_scale

        plt.plot(self.x, self.y)
        axes = plt.gca()
        axes.spines["left"].set_position("center")
        axes.spines["bottom"].set_position("center")
        axes.spines["top"].set_visible(False)
        axes.spines["right"].set_visible(False)
        plt.grid()
        axes.set_ylim(*self.ylim)
        axes.set_xlim(*self.xlim)
        plt.show()
