# 1. 프로젝트 명
SeparatePcap 프로젝트는 pcap 파일을 mac주소를 기준으로 분할하여 여러개의 pcap 파일로 분할하여 저장하는 프로젝트이다.

# 2. 프로젝트 정보
  ## 2.1 설치
    1. Python 3.x 이상 설치
    2. SplitCap.exe 설치 (https://www.netresec.com/?page=SplitCap)
    3. linux os의 경우 mono 패키지 설치 필요 (https://www.mono-project.com/download/stable/#download-lin)
    3. 분할하고자 하는 pcap 파일을 res/pcap/ 디렉토리 아래에 저장
    4. SplitCap.exe 파일을 src/ 디렉토리 아래에 저장
    
  ## 2.2 사용방법
    1. src/main.py 실행
    2. 분할하고자 하는 pcap file list에서 pcap파일 이름을 입력 ex) data.pcap
    3. res/separated_pcap/ 디렉토리 아래에 분할하고자 하는 pcap 파일 디렉토리 생성 확인 ex) res/separated_pcap/data
    4. 분할하고자 하는 pcap 디렉토리 아래에 mac 주소 별로 pcap파일로 분할되었는지 확인
  
