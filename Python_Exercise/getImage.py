import urllib.request as request
import urllib.parse as parse
import string

def getImage(url ,begin_page,end_page):
    for i in range(begin_page,end_page+1):
        ImageName = 'C:/Users/ehillms/Python_Exercise/'+str(i)+'.html'
        print('downloading'+str(i)+'page')
        m=request.urlopen(url+str(i)).read()
        with open(ImageName ,'wb') as file:
            file.write(m)
        file.close()
if __name__ == "__main__":
    url = "http://tieba.baidu.com/p/"
    begin_page = 1
    end_page =3
    getImage(url,begin_page,end_page)
