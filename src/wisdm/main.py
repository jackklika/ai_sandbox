# Import `tensorflow`
import tensorflow as tf

import glob
import errno

from scipy.io import arff
from io import StringIO


# TODO: Simplify this with some glob wildcards
paths = [
        '/opt/datasets/wisdm/arff_files/phone/accel/*.arff',
        '/opt/datasets/wisdm/arff_files/phone/gyro/*.arff',
        '/opt/datasets/wisdm/arff_files/watch/accel/*.arff',
        '/opt/datasets/wisdm/arff_files/watch/gyro/*.arff',
        ]

for p in paths:
    files = glob.glob(p)
    for f in files:
        try:
            with open(f) as ff:
                print(ff)
                data, meta = arff.loadarff(ff)
                print(data)
        except IOError as err:
            if err.errno != errno.EISDIR:
                print("error: ", err)
                raise


# /opt/datasets/{phone,watch}/{accel,gyro}

#f = open("/opt/datasets/phone/accel"

