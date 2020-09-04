from os import listdir
from os.path import isfile, join

f_folder="/home/gqxwolf/shared_git/bConstrainSkyline/target/output/complementary/exp5"


exp5_files = [join(f_folder, f) for f in listdir(f_folder) if isfile(join(f_folder, f))]

def analyzeRecord(fname,baseline_number):
    with open(fname) as f:
            content = f.readlines()
    content = [x.strip() for x in content]

    runtimelist = []
    sknumlist=[]

    count = 0
    segment = 0
    run_time = sk_num = 0

    goodness_counter = 0
    exact_goodness=range_goodness=mix_goodness=0
    for line in content:
        if segment!=6 :
            if line=="===============================================":
                segment+=1
                # print "{} {}".format(run_time/baseline_number,sk_num/baseline_number)
                runtimelist.append(run_time/baseline_number)
                sknumlist.append(sk_num/baseline_number)
                run_time = sk_num = 0
            else:
                if count <= baseline_number:
                    t=float(line.split("|")[1])
                    s=float(line.split(" ")[-3])    
                    run_time+=t
                    sk_num+=s
                else:
                    t=float(line.split("|")[1])
                    s=float(line.split(" ")[-1])    
                    run_time+=t
                    sk_num+=s
        elif segment==6:
            if goodness_counter % 4 ==0:
                exact_goodness+=float(line.split(" ")[0])
            elif goodness_counter % 4 ==1:
                range_goodness+=float(line.split(" ")[0])
            elif goodness_counter % 4 ==2:
                mix_goodness+=float(line.split(" ")[0])
            goodness_counter+=1
        count+=1
    goodlist = [exact_goodness/baseline_number,range_goodness/baseline_number,mix_goodness/baseline_number]
    # print "{} {} {}".format(exact_goodness/baseline_number,range_goodness/baseline_number,mix_goodness/baseline_number)
    return runtimelist,sknumlist,goodlist



def getFirstSpliter(fname):
    with open(fname) as f:
            content = f.readlines()
    content = [x.strip() for x in content]

    count = 0
    for line in content:
        if line=="===============================================":
            return count
        else:
            count+=1

def printResult(runtimes,sks,goodnesses):
    base_rt = runtimes[0]
    base_sk = sks[0]

    s=""
    for r in runtimes:
        s+= (str(r)+" ")

    s+="|"

    for i in range(1,len(runtimes)):
        s+= (str(base_rt/runtimes[i])+" ")
    
    s+="|"

    for r in sks:
        s+= (str(r)+" ")
    
    s+="|"

    for i in range(1,len(sks)):
        s+= (str(sks[i]/base_sk)+" ")
    
    s+="|"

    for g in goodnesses:
        s+= (str(g)+" ")

    print s

for f in exp5_files:
    baseline_number = getFirstSpliter(f)
    runtimes, sks, goodnesses = analyzeRecord(f,baseline_number)
    print f
    # print runtimes
    # print sks
    # print goodnesses
    # print '==========================='

    printResult(runtimes,sks,goodnesses)


