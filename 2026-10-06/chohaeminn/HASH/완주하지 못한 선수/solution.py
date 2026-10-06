from collections import Counter  # <-- 이 줄을 반드시 맨 위에 적어주어야 합니다!

c1 = Counter(["leo", "kiki", "eden", "leo"])  # leo: 2, kiki: 1, eden: 1
c2 = Counter(["eden", "kiki"])  # eden: 1, kiki: 1

print(c1 - c2)