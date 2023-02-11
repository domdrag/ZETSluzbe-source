import requests

def downloadPDFFile(url, fileName):
    filePath = 'data/data/' + fileName

    with requests.get(url) as r:
        assert r.status_code == 200, f'error, status code is {r.status_code}'
        with open(filePath, 'wb') as f:
            f.write(r.content)
        
    return filePath
