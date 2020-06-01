N = 1000000
for n_0 in range(N-500000, N, 100000):
    n=n_0
    n_a = [0]*14
    n_a[0] = 10  # 初期感染者
    n-=n_a[0]
    n_a_sum = n_a[0] #その時点で感染している総数
    n_a_total=n_a[0] #累計感染者数
    res=n_a_sum
    for i in range(1000):
        tmp = n_a[-1]  # データの一時保管用
        for j in range(len(n_a)-1,0,-1):
            n_a[j] = n_a[j-1]  # 1日進める
        n_a[0] = int(n_a_sum*0.25*n//N)  # 感染者1人あたり0.5人にウイルスを移す&相手が感染可能なら感染
        n_a_sum -= tmp  # 回復した感染者（tmpは14日前の感染者数）
        n_a_sum += n_a[0]  # 新たな感染者を計上
        n_a_total+=n_a[0]
        n -= n_a[0]  # 一度感染したら2度目はない
        res=max(res,n_a_sum)
        if n_a_sum<=res/10:
            break
    print(str(n_0)+','+str(res)+','+str(n_a_total))
