#!/usr/bin/env python

import facereclib
import bob

tool = facereclib.tools.PCATool(
    subspace_dimension = 300,
    distance_function = bob.math.euclidean_distance,
    is_distance_function = True
)
