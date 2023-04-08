from collections.abc import Sequence

from attrs import define
import numpy as np

@define
class Coordinate:
    x: float
    y: float | None = None

@define
class GridNode:
    number: int
    coordinates: Coordinate

@define
class Mesh:
    nodes: list[GridNode]

def discretize_1d_even(length: float, num_nodes: float | None = None) -> Mesh:
    """Discretize 1d domain with evenly spaced grid nodes."""
    if num_nodes is None: num_nodes = int(np.ceil(length))
    nodes = [GridNode(number=i, coordinates=Coordinate(x)) for i, x in enumerate(np.linspace(0, length, num_nodes))]
    return Mesh(nodes)

if __name__ == "__main__":
    ...