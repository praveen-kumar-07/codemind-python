hf,snf,spf=map(int,input().split())
if(hf>50 and snf>60 and spf>100):
    print('10')
elif(hf>50 and snf>60):
    print('9')
elif(snf>60 and spf>100):
    print('8')
elif(hf>50 and spf>100):
    print('7')
elif(hf>50 or snf>60 or spf>100):
    print('6')
else:
    print('5')