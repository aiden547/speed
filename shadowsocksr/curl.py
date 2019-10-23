import pycurl, sys, os, time


class idctest:
    def __init__(self):
        self.contents = ''

    def body_callback(self, buf):
        self.contents = self.contents + buf


def test_gzip(input_url):
    t = idctest()
    # gzip_test = file("gzip_test.txt", 'w')
    c = pycurl.Curl()
    c.setopt(pycurl.WRITEFUNCTION, t.body_callback)
    c.setopt(pycurl.ENCODING, 'gzip')
    c.setopt(pycurl.URL, input_url)
    c.setopt(pycurl.MAXREDIRS, 5)
    c.perform()

    http_code = c.getinfo(pycurl.HTTP_CODE)

    http_conn_time = c.getinfo(pycurl.CONNECT_TIME)

    print(http_code)
    print(http_conn_time * 1000)


if __name__ == '__main__':
    input_url = sys.argv[1]
    test_gzip(input_url)
