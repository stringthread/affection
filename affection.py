N = 100000
for n_0 in range(N-90000, N, 1000):
    n=n_0
    n_a = [0]*14
    n_a[0] = 10  # 初期感染者
    n_a_sum = n_a[0]
    res=n_a_sum
    for i in range(1000):
        tmp = n_a[-1]  # データの一時保管用
        for j in range(len(n_a)-1,0,-1):
            n_a[j] = n_a[j-1]  # 1日進める
        n_a[0] = n_a_sum*1*n//N  # 感染者1人あたり1人にウイルスを移す&相手が感染可能なら感染
        n_a_sum -= tmp  # 回復した感染者（tmpは14日前の感染者数）
        n_a_sum += n_a[0]  # 新たな感染者を計上
        n -= n_a[0]  # 一度感染したら2度目はない
        res=max(res,n_a_sum)
    print(str(n_0)+','+str(res))
