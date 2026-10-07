from collections import deque

def solution(bridge_length, weight, truck_weights):
    # 다리 길이만큼 0으로 채워진 큐 생성 (다리 역할을 함)
    bridge = deque([0] * bridge_length)
    trucks = deque(truck_weights)
    
    current_weight = 0
    time = 0
    
    while trucks or current_weight > 0:
        time += 1
        
        # 1. 다리를 건넌 트럭(또는 빈자리)을 다리에서 내림
        out = bridge.popleft()
        current_weight -= out
        
        # 2. 대기 중인 다음 트럭을 다리에 올릴 수 있는지 확인
        if trucks:
            if current_weight + trucks[0] <= weight:
                truck = trucks.popleft()
                bridge.append(truck)
                current_weight += truck
            else:
                # 무게를 견딜 수 없으면 트럭 대신 0을 올림 (시간 흐름 표현)
                bridge.append(0)
                
    return time 