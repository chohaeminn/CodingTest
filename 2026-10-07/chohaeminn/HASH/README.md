프로그래머스: 폰켓몬 (Python / Java)

문제 정보

- 사이트: 프로그래머스 (Programmers)
- 문제 이름: 폰켓몬
- 레벨: Level 1
- 분류: 해시 (Hash), 집합 (Set)

문제 설명
홍 박사님의 연구실에 있는 총 N마리의 폰켓몬 중 N/2마리를 가져갈 수 있습니다.
같은 종류의 폰켓몬은 같은 번호를 가지고 있으며, 가장 많은 종류의 폰켓몬을 포함하여 N/2마리를 선택할 때, 그때의 폰켓몬 종류 번호의 개수를 return 하도록 하는 문제입니다.

제한사항

- nums의 길이(N)는 1 이상 10,000 이하이며 항상 짝수입니다.
- 폰켓몬의 종류 번호는 1 이상 200,000 이하의 자연수입니다.

접근 방식 (왜 '해시 / 집합'인가?)

1. 중복 제거 (Set 활용):
   - 같은 종류의 폰켓몬이 여러 마리 있을 수 있으므로, 종류의 개수를 정확히 파악하기 위해 중복을 허용하지 않는 집합(Set) 자료구조를 사용해 종류 번호만 남깁니다.
2. 선택의 한계치 고려 (min 함수):
   - 내가 최대로 집어 들 수 있는 마리 수는 항상 N/2마리(len(nums) // 2)입니다.
   - 종류가 내가 뽑을 수 있는 수보다 많다면: 내가 뽑는 마리 수인 N/2가 정답이 됩니다.
   - 종류가 내가 뽑을 수 있는 수보다 적다면: 존재하는 전체 종류의 개수가 정답이 됩니다.
   - 따라서 min(고를 수 있는 마리 수, 실제 폰켓몬 종류 수)를 통해 최댓값을 안전하게 도출합니다.

코드 구현

Python
def solution(nums): # 1. N/2마리 계산 (최대로 고를 수 있는 마리 수)
max_select = len(nums) // 2

    # 2. set을 이용해 중복 제거한 폰켓몬 종류의 수 구하기
    unique_ponketmon = len(set(nums))

    # 3. 고를 수 있는 마리 수와 종류의 수 중 최솟값 반환
    return min(max_select, unique_ponketmon)

Java
import java.util.HashSet;

class Solution {
public int solution(int[] nums) {
int maxSelect = nums.length / 2;

        // HashSet을 이용해 중복 제거
        HashSet<Integer> uniquePonketmon = new HashSet<>();
        for (int num : nums) {
            uniquePonketmon.add(num);
        }

        // 고를 수 있는 수와 종류의 수 중 작은 값 반환
        return Math.min(maxSelect, uniquePonketmon.size());
    }

}

입출력 예시

- [3, 1, 2, 3] -> 결과: 2 (설명: 총 4마리 중 2마리 선택. min(2, 3) = 2)
- [3, 3, 3, 2, 2, 4] -> 결과: 3 (설명: 총 6마리 중 3마리 선택. min(3, 3) = 3)
- [3, 3, 3, 2, 2, 2] -> 결과: 2 (설명: 총 6마리 중 3마리 선택. min(3, 2) = 2)
