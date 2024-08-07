# 24265 알고리즘 수업 - 알고리즘의 수행 시간4

# n=7일 때, i=1/j=2~n(6), i=2/j=3~n(5), i=3/j=4~n(4), i=4/j=5~n(3), i=5/j=6~n(2), i=6/j=7~n(1)
# 즉, 수행횟수는 1,2,3,4,5,6=21이 된다. 이는 등차수열의 합 공식 n(n+1)/2에서 n에 n-1을 대입한 n(n-1)/2와 같다.
# 또한, O(n^2)이므로 최고차항의 차수는 2이다.
'''
MenOfPassion(A[], n) {
    sum <- 0;
    for i <- 1 to n - 1
        for j <- i + 1 to n
            sum <- sum + A[i] × A[j]; # 코드1
    return sum;
}
'''
n = int(input())
print(n*(n-1)//2)
print(2)