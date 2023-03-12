# python3

def parallel_processing(n, m, data):
    output = []
    tasks = [(data[i], i) for i in range(m)];
    finish = [0] * n;
    for i in tasks:
        next = finish.index(min(finish));
        output.append((next, finish[next]));
        finish[next] = finish[next] + i[0];

    # TODO: write the function for simulating parallel tasks,
    # create the output pairs

    return output


def main():
    # TODO: create input from keyboard
    # input consists of two lines
    # first line - n and m
    # n - thread count
    # m - job count
    n = 0
    m = 0

    # second line - data
    # data - contains m integers t(i) - the times in seconds it takes any thread to process i-th job
    data = []
try:
    print("Input thread count, and the amount of jobs (sperated with space):");
    n, m = map(int, input().split());
    print("Input task time / data ,(sperated with spaces):");
    data = list(map(int, input().split()));

    # TODO: create the function
    result = parallel_processing(n, m, data)

    # TODO: print out the results, each pair in it's own line
    print("Output:")
    for j in result:
        print(j[0], j[1]);
except ValueError as vErr:
  print('ERROR; You did not input correct ammount of values');



if __name__ == "__main__":
    main()
# 221RDB386 Mārtiņš Nikiforovs 11.grupa
