import yfinance as yf
import matplotlib.pyplot as plt

# 1. 종목 코드 설정 (삼성전자는 '005930.KS' 입니다. 테슬라는 'TSLA', 애플은 'AAPL')
ticker_symbol = '005930.KS'

# 2. 야후 파이낸스에서 데이터 다운로드 (period='1y'는 최근 1년치라는 뜻입니다)
print(f"{ticker_symbol} 데이터를 불러오는 중입니다...")
stock_data = yf.download(ticker_symbol, period='1y')

# 3. 데이터가 잘 왔는지 표 형태로 확인 (처음 5일치 데이터 출력)
print("\n[최근 5일치 데이터 확인]")
print(stock_data.head())

# 4. 시간에 따른 주가 흐름을 그래프로 그리기
plt.figure(figsize=(12, 6)) # 그래프 크기 설정
plt.plot(stock_data.index, stock_data['Close'], label='Close Price(KRW)', color='blue')
plt.title('Samsung Electronics Stock Price (1 Year)')
plt.xlabel('Date')
plt.ylabel('Price (KRW)')
plt.grid(True) # 눈금선 추가
plt.legend()

# 5. 화면에 그래프 띄우기
plt.show()