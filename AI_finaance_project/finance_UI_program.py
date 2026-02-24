import tkinter as tk
import yfinance as yf
from datetime import datetime
import ctypes

# 윈도우 고해상도(DPI) 인식 설정
try:
    ctypes.windll.shcore.SetProcessDpiAwareness(1)
except:
    ctypes.windll.user32.SetProcessDPIAware()

class SemiTransparentWidget:
    def __init__(self, ticker):
        self.ticker = ticker
        self.root = tk.Tk()
        
        # 1. 기본 설정: 테두리 제거 및 항상 위에
        self.root.overrideredirect(True)
        self.root.attributes("-topmost", True)
        
        # 2. 반투명 설정 (0.0 투명 ~ 1.0 불투명)
        # 0.7 정도가 배경도 살짝 보이면서 글자가 가장 선명합니다.
        self.root.attributes("-alpha", 0.3) 
        self.root.config(bg='black')

        # 3. 레이블 설정 (여백 추가로 박스 느낌 강화)
        self.label = tk.Label(
            self.root, 
            text="불러오는 중...", 
            font=('Malgun Gothic', 12, 'bold'), 
            fg='white', 
            bg='black',
            padx=20, # 가로 여백
            pady=15  # 세로 여백
        )
        self.label.pack()

        # 4. 마우스 좌클릭으로 위젯 종료 기능 (테두리가 없으므로 필요)
        self.root.bind("<Button-1>", lambda e: self.root.destroy())

        self.update_position()
        self.refresh_price()
        self.root.mainloop()

    def update_position(self):
        # 화면 우측 하단 배치
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        # 박스 크기에 맞춰 위치 미세 조정
        self.root.geometry(f"+{screen_width - 220}+{screen_height - 140}")

    def refresh_price(self):
        try:
            stock = yf.Ticker(self.ticker)
            price = stock.fast_info['last_price']
            now = datetime.now().strftime('%H:%M:%S')
            
            # 삼성전자 등 국내 주식은 소수점 제거, 해외 주식은 유지
            price_str = f"{price:,.0f}" if ".KS" in self.ticker else f"{price:,.2f}"
            
            self.label.config(text=f"{self.ticker}\n{price_str} KRW\n[{now}]")
        except:
            self.label.config(text="데이터 연결 오류")
        
        # 30초마다 업데이트
        self.root.after(30000, self.refresh_price)

if __name__ == "__main__":
    # 박 건 님이 산 종목 코드로 변경해서 실행해보세요!
    SemiTransparentWidget('005930.KS')