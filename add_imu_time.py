import os
def loadTxt(filename):
    dataset = []
    f = open(filename, 'r')
    lines = f.readlines()
    i = 0
    for line in lines:
        if i==0:
            time = long(line)
            i = 2
        else:
            str1 = line.split("\t")
            str_list=list(str1[0])
            str_list.pop()
            str_list.pop()
            a = "".join(str_list)
            b = a.split(',')
            dataset.append(b)
    for i in range(len(dataset)):
        try:
            for j in range(len(dataset[i])):
                    dataset[i][j] = float(dataset[i][j])
        except ValueError, e:
            print "ValueError at %d" % i
    f.close()
    return dataset, time

def writeTxt(time, dataset, filename):
    f = open(filename, 'w')
    for d in dataset:
        d[0] = d[0] * 9.80116
        d[1] = d[1] * 9.80116
        d[2] = d[2] * 9.80116
        f.write(str(time) + ',' + str(d[3]) + ',' + str(d[4]) + ',' + str(d[5]) + ',' + str(d[0]) + ',' + str(d[1]) + ',' + str(d[2]) + '\n')
        time  = time + 5000000;
def test():
    dataset, time = loadTxt('/home/lyw/mydataset/dataset-dir/imu0.txt')
    writeTxt(time, dataset, '/home/lyw/mydataset/dataset-dir/imu0.csv')

if __name__ == '__main__':
    test()