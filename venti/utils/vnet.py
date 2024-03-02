from tornado.web import RequestHandler
from tornado.httpclient import AsyncHTTPClient, HTTPRequest, HTTPClient
import json


class SyncService(RequestHandler):
    def set_default_headers(self):
        self.set_header('Content-Type','application/json; charset=UTF-8')
        self.set_header('Server','GreyPointsVenti')
        self.add_header('Auther','Tails')

    def get_data(self):
        remote_body = None
        if self.request.body:
            try:
                remote_body = json.loads(self.request.body)
            except json.decoder.JSONDecodeError:
                remote_body = self.request.body.decode()
        remote_header=dict(self.request.headers)
        remote_ip=self.request.remote_ip
        remote_host=self.request.host
        remote_uri=self.request.uri
        remote_path=self.request.path
        remote_query=self.request.query
        remote_protocol=self.request.protocol
        remote_data = {"header": remote_header, "body": remote_body, 
                        "ip": remote_ip, "protocol": remote_protocol,
                        "host": remote_host,"uri": remote_uri,
                        "path": remote_path,"query": remote_query}
        return remote_data

    def get(self):
        response = self.get_data()

    def post(self):
        response = self.get_data()

    def put(self):
        response = self.get_data()

    def delete(self):
        response = self.get_data()

class SyncClientHandler:
    def __init__(self):
        self.http_client = HTTPClient()

    def _request_prepare(self,**kwargs):
        url = kwargs.get('url')
        use_https = kwargs.get('use_https',True)
        if use_https and not url.startswith('https://'):
            url = 'https://' + url
        elif not use_https and not url.startswith('http://'):
            url = 'http://' + url
        headers = kwargs.get('headers', {
            'User-Agent': 'GreyPointsKd',
            'Content-Type': 'application/json'
        }) 
        body = json.dumps(kwargs.get('body')) if isinstance(kwargs.get('body'), dict) else kwargs.get('body')
        method = kwargs.get('method')
        validate_cert = kwargs.get('validate_cert', True)
        request = HTTPRequest(
            url=url,
            method=method,
            headers=headers,
            body=body,
            validate_cert=validate_cert
        )
        return request

    def fetch(self, request):
        try:
            response = self.http_client.fetch(request)                
            response.headers = dict(response.headers)
            cookies = response.headers.get('Set-Cookie')
            response.headers = json.dumps(response.headers)
            return {
                'status': response.code,
                'headers': response.headers,
                'body': response.body,
                'cookies': cookies
            }
        except Exception as e:
            return {
                'error': str(e)
            }

    def get(self, **kwargs):
        kwargs['method'] = 'GET'
        request = self._request_prepare(**kwargs)
        return self.fetch(request)
    
    def post(self, **kwargs):
        kwargs['method'] = 'POST'
        request = self._request_prepare(**kwargs)
        return self.fetch(request)

    def put(self, **kwargs):
        kwargs['method'] = 'PUT'
        request = self._request_prepare(**kwargs)
        return self.fetch(request)

    def delete(self, **kwargs):
        kwargs['method'] = 'DELETE'
        request = self._request_prepare(**kwargs)
        return self.fetch(request)

class AsyncHandler(RequestHandler):
    def set_default_headers(self):
        # self.set_header('Content-Type','application/json; charset=UTF-8')
        self.set_header('Server','GreyPointsVenti')
        self.add_header('Auther','Tails')

    async def get_mes(self):
        remote_body = None
        if self.request.body:
            try:
                remote_body = json.loads(self.request.body)
            except json.decoder.JSONDecodeError:
                remote_body = self.request.body.decode()
        remote_header=dict(self.request.headers)
        remote_ip=self.request.remote_ip
        remote_host=self.request.host
        remote_uri=self.request.uri
        remote_path=self.request.path
        remote_query=self.request.query
        remote_protocol=self.request.protocol
        remote_data = {"header": remote_header, "body": remote_body, 
                        "ip": remote_ip, "protocol": remote_protocol,
                        "host": remote_host,"uri": remote_uri,
                        "path": remote_path,"query": remote_query}
        return remote_data

    async def get(self):
        response = await self.get_mes()

    async def post(self):
        response = await self.get_mes()

    async def put(self):
        response = await self.get_mes()

    async def delete(self):
        response = await self.get_mes()

class AsyncClientHandler:
    def __init__(self):
        self.http_client = AsyncHTTPClient()

    async def _request_prepare(self,**kwargs):
        url = kwargs.get('url')
        use_https = kwargs.get('use_https',True)
        if use_https and not url.startswith('https://'):
            url = 'https://' + url
        elif not use_https and not url.startswith('http://'):
            url = 'http://' + url
        headers = kwargs.get('headers', {
            'User-Agent': 'GreyPointsVenti',
            'Content-Type': 'application/json'
        }) 
        body = json.dumps(kwargs.get('body')) if isinstance(kwargs.get('body'), dict) else kwargs.get('body')
        method = kwargs.get('method')
        validate_cert = kwargs.get('validate_cert', True)
        request = HTTPRequest(
            url=url,
            method=method,
            headers=headers,
            body=body,
            validate_cert=validate_cert
        )
        return request

    async def fetch(self, request):
        try:
            response = await self.http_client.fetch(request)                
            response.headers = dict(response.headers)
            cookies = response.headers.get('Set-Cookie')
            response.headers = json.dumps(response.headers)
            return {
                'status': response.code,
                'headers': response.headers,
                'body': response.body,
                'cookies': cookies
            }
        except Exception as e:
            return {
                'error': str(e)
            }

    async def get(self, **kwargs):
        print(kwargs)
        kwargs['method'] = 'GET'
        request = await self._request_prepare(**kwargs)
        return await self.fetch(request)
    
    async def post(self, **kwargs):
        kwargs['method'] = 'POST'
        request = await self._request_prepare(**kwargs)
        return await self.fetch(request)

    async def put(self, **kwargs):
        kwargs['method'] = 'PUT'
        request = await self._request_prepare(**kwargs)
        return await self.fetch(request)

    async def delete(self, **kwargs):
        kwargs['method'] = 'DELETE'
        request = await self._request_prepare(**kwargs)
        return await self.fetch(request)
