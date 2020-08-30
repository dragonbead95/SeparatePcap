
import os
import pandas as pd

pcap_listPath = os.getcwd()+"/../res/pcap/"
sep_pcapPath = os.getcwd()+"/../res/separated_pcap/"

# pcap 파일 리스트를 출력한다.
# return filename : pcap 파일의 이름 (확장자 제외), ex) data.pcap -> data
def print_fileList():
    # step1 pcap파일을 mac별로 분할함
    print("pcap file list")
    os.system("ls {}".format(pcap_listPath))                            # pcap file list 출력
    filepath = pcap_listPath+input("input the pcap file\n") # 분할할 pcap 파일을 입력한다.
    filename = os.path.basename(filepath).split(".")[0]         # 파일명을 추출함 (확장자 제외)
    return filename

def separate_pcapFile(filename):
    
    sep = sep_pcapPath + filename                    # 분할할 pcap 파일, 디렉터리 경로 저장
    pcap_filePath = pcap_listPath+filename+".pcap"      # 분할할 pcap 파일  선택
    os.system("sudo rm -rf {}".format(sep))       # 저장할 디렉터리 삭제
    os.makedirs(sep)                                           # 저장할 디렉터리 생성
    
    try:
        # mac주소별로 pcap 분할
        os.system("sudo mono SplitCap.exe -r  {} -o {} -s mac".format(pcap_filePath,sep))
    except  Exception as f:
        print(f)
    else:
        print("complete the separation")

import subprocess
def read_ExternalCommand(cmd):
    cmd = cmd.split()
    fd_open = subprocess.Popen(cmd,stdout=subprocess.PIPE).stdout
    data = fd_open.read().strip()
    fd_open.close()

    return data.decode("utf-8")

# data.pcap.MAC_001AEF467D9F.pcap -> data_dev1.pcap ... data_devN.pcap
def rename_pcapFile(pcap_folder,filename):
    
    data = read_ExternalCommand("ls {}".format(pcap_folder))
    data = data.split("\n") # 원본 pcap 파일이름 리스트

    num = 1
    for pcap in data:
        origin_filePath = pcap_folder+"/"+pcap # 바꾸고자 하는 pcap 파일 경로
        rnm = pcap_folder+"/"+filename + "_dev"+str(num)+".pcap" # [pcap파일이름]_dev[숫자].pcap
        num+=1

        os.system("sudo mv {} {}".format(origin_filePath,rnm))

if __name__ == "__main__":
    filename = print_fileList()     # pcap 파일 리스트 출력
    
    separate_pcapFile(filename)# pcap 파일을 mac별 pcap파일로 분할

    pcap_folder = sep_pcapPath + filename # mac별로 분리한 pcap이 들어간 디렉토리
    rename_pcapFile(pcap_folder, filename) # pcap 파일이름 변경

    
