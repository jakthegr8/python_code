import requests
import os
 
def create_directory(dirname):
    try:
        os.stat(dirname)
    except:
        os.mkdir(dirname)
 
def show(obj):
    for i in range(len(obj)):
        print(str(i)+': '+str(obj[i]))
 
def auth():
    user = 'USERNAME'
    password = 'PASSWORD'
    request = requests.get('https://api.github.com/users/'+user+'/gists?per_page=100'
                                             , auth=(user, password))
    return ['yes', user, request]
 
def load(request):
   output = request.text.split(",")
   gist_urls = []
   files = []
   for item in output:
       if "raw_url" in item:
           gist_urls.append(str(item[11:-1]))
       if "filename" in item:
           files.append(str(item.split(":")[1][2:-1]))
   return [gist_urls, files]
 
def write_gist(filename, text):
    filename = filename.replace(" ", "_")
    print(filename)
    fp = open(filename.lower(), 'w')
    fp.write(text)
    fp.close()
 
def download(permission, user, request, fileno='all'):
    if(permission == "yes" or permission == "no"):
        gist_urls, files = load(request)
        dirname = user+"_gists/"
        create_directory(dirname)
        for i in range(len(gist_urls)):
            gist = requests.get(gist_urls[i])
            write_gist(dirname+files[i], gist.text)
 
def main():
    ask_auth, user, request = auth()
    urls, files = load(request)
    download(ask_auth, user, request)
 
if(__name__ == '__main__'):
    main()