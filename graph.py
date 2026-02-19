import matplotlib.pyplot as plt

# 1. 차트 기본 설정 (1km 스캐너 관점)
labels = [
    'Target Drone EIRP\n(Assumed, +10 dBm)', 
    'Free Space Path Loss\n(L_FSPL @ 1km)', 
    'Rx Antenna Gain\n(256-Array, +28 dBi)', 
    'Final Rx Power\n(Pr)'
]

text_labels = ['+10 dBm', '-115 dB', '+28 dBi', '-77 dBm']

# 2. 막대그래프 높이 및 시작점 계산
bottom_min = -130  # Y축 최소값

# 막대가 시작되는 Y 좌표
bottoms = [
    bottom_min,  # Target EIRP (바닥에서 시작)
    10,          # FSPL (EIRP 꼭대기 +10에서 시작)
    -105,        # Rx Gain (10 - 115 = -105 지점에서 시작)
    bottom_min   # Rx Power (바닥에서 시작)
]

# 막대의 실제 길이
heights = [
    10 - bottom_min,       # 바닥 -> +10
    -115,                  # +10 -> -105
    28,                    # -105 -> -77
    -77 - bottom_min       # 바닥 -> -77
]

colors = ['gray', 'red', 'green', 'blue']

# 3. 그래프 그리기
fig, ax = plt.subplots(figsize=(10, 7))
bars = ax.bar(labels, heights, bottom=bottoms, color=colors, edgecolor='black', alpha=0.9)

# 4. 타겟 수신 감도 선 추가 (-100 dBm)
ax.axhline(y=-100, color='darkred', linestyle='--', linewidth=2)
ax.text(-0.4, -98, 'Target Sensitivity', color='darkred', fontsize=12, fontweight='bold')

# 5. 막대 위에 텍스트 값 표시
y_text_pos = [12, -45, -88, -74] 
for i in range(len(bars)):
    ax.text(i, y_text_pos[i], text_labels[i], ha='center', va='bottom', fontsize=12, fontweight='bold')

# 6. 링크 마진 화살표 표시 (마지막 막대 우측)
ax.annotate('', xy=(3.5, -77), xytext=(3.5, -100),
            arrowprops=dict(arrowstyle='<->', color='green', lw=2.5))
ax.text(3.6, -88.5, 'Margin (+23 dB)', color='green', fontsize=12, 
        fontweight='bold', va='center', ha='left')

ax.set_xlim(-0.6, 4.2) # 우측 텍스트 여백 확보

# 7. 축 및 레이아웃 설정
ax.set_ylabel('Power Level (dBm)', fontsize=14)
ax.set_title('Ku-Band RF Scanner Link Budget (1km Detection Scenario)', fontsize=16, fontweight='bold', pad=15)
ax.set_ylim(bottom_min, 30)
ax.grid(True, axis='y', linestyle='--', alpha=0.7)

plt.tight_layout()
plt.show()

#git hub test
