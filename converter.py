import sys
import numpy as np
from pathlib import Path


input_path = Path(sys.argv[1])
ouput_path = input_path.with_name('converted_' + input_path.name)

data = np.fromfile(input_path, np.uint8)

data = ~data
data.tofile(ouput_path)
