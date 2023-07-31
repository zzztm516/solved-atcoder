#縦ないし横が3でわれれば0でいい
#切り上げ割り算 a/b -> a//b+1
# W < H と W >= Hで区切ると失敗する, 区切り方はこれで決まらない

def main():
    H, W = map(int, input().split())

    if H % 3 == 0 or W % 3 == 0:
        return(print(0))

    w1 = W // 3 + 1
    w2 = W // 3
    ans = []
    for w in w1, w2:
        s1 = max(H * w, (H // 2 + H % 2) * (W - w))
        s2 = min(H * w, (H // 2) * (W - w))
        ans.append(s1 - s2)

    h1 = H // 3 + 1
    h2 = H // 3
    for h in h1, h2:
        s1 = max(W * h, (W // 2 + W % 2) * (H - h))
        s2 = min(W * h, (W // 2) * (H - h))
        ans.append(s1 - s2)
    print(min(min(ans),H, W))#横3分割の際にWが最も小さい

if __name__ == '__main__':
    main()