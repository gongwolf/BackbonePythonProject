# fname = "/home/gqxwolf/shared_git/bConstrainSkyline/target/output/complementary/Astar_comparison_large_hotels_num.txt"
fname = "/home/gqxwolf/shared_git/bConstrainSkyline/target/output/complementary/Astar_comparison.txt"
with open(fname) as f:
    content = f.readlines()
# you may also want to remove whitespace characters like `\n` at the end of each line
content = [x.strip() for x in content] 




def printResult(a_run_time,a_sk_num,b_run_time,b_sk_num,o_run_time,o_sk_num,i_run_time,i_sk_num,query_num):
    avg_a_run_time=a_run_time/query_num/1000
    avg_a_sk_num=a_sk_num/query_num
    avg_a_s = " | {} {}".format(avg_a_run_time,avg_a_sk_num)

    avg_b_run_time=b_run_time/query_num/1000
    avg_b_sk_num=b_sk_num/query_num
    avg_b_s = " | {} {}".format(avg_b_run_time,avg_b_sk_num)

    avg_o_run_time=o_run_time/query_num/1000
    avg_o_sk_num=o_sk_num/query_num
    avg_o_s = " | {} {}".format(avg_o_run_time,avg_o_sk_num)
        
    avg_i_run_time=i_run_time/query_num/1000
    avg_i_sk_num=i_sk_num/query_num
    avg_i_s = " | {} {}".format(avg_i_run_time,avg_i_sk_num)

    print("%s %s %s %s %d %s %s %s %s" %(graph,r_range,degree,hotelnum,query_num,avg_a_s,avg_b_s,avg_o_s,avg_i_s) )



graph=r_range=degree=hotelnum=0
read_info=True

a_run_time=a_sk_num = 0
b_run_time=b_sk_num = 0
o_run_time=o_sk_num = 0
i_run_time=i_sk_num = 0

line_number = 0
query_num = 0
count=0

for line in content:
    if line=="--------------------------------------------------------------" :
        printResult(a_run_time,a_sk_num,b_run_time,b_sk_num,o_run_time,o_sk_num,i_run_time,i_sk_num,query_num)
        graph=r_range=degree=hotelnum=0
        query_num=0
        read_info=True

        a_run_time=a_sk_num = 0
        b_run_time=b_sk_num = 0
        o_run_time=o_sk_num = 0
        i_run_time=i_sk_num = 0

    elif read_info:
        graph=line.split(" ")[0]
        r_range=line.split(" ")[1]
        degree=line.split(" ")[2]
        hotelnum=line.split(" ")[3]
        read_info=False
    elif line == "=================================":
        query_num+=1
        count=0
    elif count==0:
        a_run_time+= float(line.split("|")[1])
        a_sk_num+= float(line.split(" ")[-3])
        count+=1
    elif count==1:
        b_run_time+= float(line.split("|")[1])
        b_sk_num+= float(line.split(" ")[-2])
        count+=1
    elif count==2:
        o_run_time+= float(line.split("|")[1])
        o_sk_num+= float(line.split(" ")[-3])
        count+=1
    elif count==3:
        i_run_time+= float(line.split("|")[1])
        i_sk_num+= float(line.split(" ")[-1])
        count+=1
    # print line
    line_number+=1
printResult(a_run_time,a_sk_num,b_run_time,b_sk_num,o_run_time,o_sk_num,i_run_time,i_sk_num,query_num)
