import sys
import JSTMB_O196
import numpy as np

def JSTMB(data_file, target_file):
    my_JMI = JSTMB_O196.initialize()
    feat = my_JMI.JSTMB_primitive_O196(data_file, target_file)
    return feat


if __name__ == "__main__":
    data = sys.argv[1]
    target = sys.argv[2]
    selected_feature = np.array(JSTMB(data, target), dtype=np.int16)
    np.savetxt('Features_O196_JSTMB.csv', selected_feature, delimiter=',')
    print selected_feature
