from decimal import Decimal, ROUND_HALF_UP
from datetime import datetime
import tarfile
import chardet
from cryptography.fernet import Fernet
import qrcode
# from barcode import EAN13
# from barcode.writer import ImageWriter
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import yaml
import hashlib
import os
import pymysql
import redis

class AccuracyHandler:
    def decimal_oj(self, tg: str):
        return Decimal(tg)

    def half_adjust(self, floating_number: str, precision: int):
        precision_value = '0.' + '0' * precision
        rounded_num = self.decimal_oj(floating_number).quantize(Decimal(precision_value), rounding=ROUND_HALF_UP)
        return rounded_num

class TimeHandler:
    @staticmethod
    def timestamp(tg :str = None):
        if tg == None:
            result = int(datetime.now().timestamp())
        else:
            try:
                result = int(datetime.strptime(tg, '%Y-%m-%d %H:%M').timestamp())
            except:
                return 'error'
        return result

    @staticmethod
    def utctimestamp():
        result = datetime.utcnow().timestamp()
        return result

    @staticmethod
    def timestamp_to_datetime(ts):
        return datetime.fromtimestamp(ts)

    @staticmethod
    def utctimestamp_to_datetime(ts):
        return datetime.utcfromtimestamp(ts)

    @staticmethod
    def time_difference(timestamp1: int, timestamp2: int):
        print(timestamp1)
        print(timestamp2)
        if not isinstance(timestamp1, int) or not isinstance(timestamp2, int):  
            raise ValueError("时间戳必须是整数")
        tf = timestamp2 - timestamp1
        days = tf / 3600 / 24
        hours = tf / 3600
        minutes = tf / 60
        seconds = tf
        tfm = {
            'd': days,
            'h': hours,
            'm': minutes,
            's': seconds
        }
        return tfm

    @staticmethod
    def get_time():
        gt = datetime.now().strftime("%H:%M:%S")
        return gt

    @staticmethod
    def get_utctime():
        gt = datetime.utcnow().strftime("%H:%M:%S")
        return gt

    @staticmethod
    def get_date():
        gt = datetime.now().strftime("%Y-%m-%d")
        return gt

    @staticmethod
    def get_utcdate():
        gt = datetime.utcnow().strftime("%Y-%m-%d")
        return gt

class FileHandler:
    @staticmethod
    def file_to_binary(file_path, chunk_size=1024):
        with open(file_path, 'rb') as f:
            while chunk := f.read(chunk_size):
                yield chunk

    @staticmethod
    def binary_to_file(binary_data, file_path):
        with open(file_path, 'wb') as f:
            for chunk in binary_data:
                f.write(chunk)

    @staticmethod
    def compress(source_folder, output_filename):
        with tarfile.open(output_filename, "w:xz") as tar:
            for root, dir, files in os.walk(source_folder):
                for file in files:
                    full_path = os.path.join(root, file)
                    tar.add(full_path, arcname=os.path.relpath(full_path, source_folder))

    @staticmethod
    def decompression(input_filename, target_folder):
        with tarfile.open(input_filename, 'r:xz') as tar:
            tar.extractall(path=target_folder)

    # 请注意，并不完全准确
    @staticmethod
    def check_encoding(tg):
        with open(tg, 'rb') as f:
            result = chardet.detect(f.read())
        return result

    @staticmethod
    def change_encoding(file_path, encoding):
        print(FileHandler.check_encoding(file_path)['encoding'])
        with open(file_path, 'r', encoding=FileHandler.check_encoding(file_path)['encoding']) as f:
            content = f.read()

        with open(file_path + '_' + encoding, 'w', encoding=encoding) as f:
            f.write(content)

    @staticmethod
    def file_hash(file_path):
        try:
            with open(file_path,"rb") as f:
                bytes = f.read()
                readable_hash = hashlib.sha256(bytes).hexdigest()
                return readable_hash
        except Exception as e:
            print(f"Error: {e}")
            return None

class StrHandler:
    @staticmethod
    def str_hash(string):
        try:
            message = string.encode()
            return hashlib.sha256(message).hexdigest()
        except Exception as e:
            print(f"Error: {e}")
            return None

    @staticmethod
    def str_encryption(text):
        key = Fernet.generate_key()
        cipherSuite = Fernet(key)
        encrypted_text = cipherSuite.encrypt(text.encode())
        result = {"str":encrypted_text,"key":key}
        return result

    @staticmethod
    def str_decrypt(text, key):
        cipherSuite = Fernet(key)
        decryptedText = cipherSuite.decrypt(text)
        return decryptedText.decode()

    @staticmethod
    def str_to_binary(string):
        try:
            result = string.encode('utf-8')
            return result
        except Exception as e:
            print(f"Error: {e}")
            return None

    @staticmethod
    def binary_to_str(binary):
        try:
            result = binary.decode('utf-8')
            return result
        except Exception as e:
            print(f"Error: {e}")
            return None

class CodeHandler:
    @staticmethod
    def qrcode_character(qr_data):
        qr = qrcode.QRCode(version=1,
                            error_correction=qrcode.constants.ERROR_CORRECT_L,
                            box_size=10,
                            border=1)
        qr.add_data(qr_data)
        qr.make()
        qr.print_ascii()

    '''
    @staticmethod
    def qrcode_picture(qr_data, ver=1, box_size=10, border=4):
        qr = qrcode.QRCode(
            version=ver,
            error_correction=qrcode.constants.ERROR_CORRECT_H,
            box_size=box_size,
            border=border,
        )
        qr.add_data(qr_data)
        qr.make(fit=True)
        img = qr.make_image(fill_color="black", back_color="white")
        return img

    @staticmethod
    def barcode(bar_data):
        ean = EAN13(bar_data, writer=ImageWriter())
        # 将保存条形码到 'ean13_barcode.png' 文件
        filename = ean.save('ean13_barcode')
        print(f"Barcode saved as '{filename}'")
    '''

class MailHandler:
    @staticmethod
    def send_mail(sender,receiver,subject,message,SmtpServer,SmtpPort,SmtpAccount,SmtpPassword):
        data = locals()
        sender = data["sender"]
        receiver = data["receiver"]
        subject = data["subject"]
        message = data["message"]
        msg = MIMEMultipart()
        msg['From'] = sender
        msg['To'] = receiver
        msg['Subject'] = subject
        body = MIMEText(message, 'plain')
        msg.attach(body)
        SmtpServer = data["SmtpServer"]
        SmtpPort = data["SmtpPort"]
        SmtpAccount = data["SmtpAccount"]
        SmtpPassword = data["SmtpPassword"]
        try:
            server = smtplib.SMTP(SmtpServer, SmtpPort)
            # 开启TLS加密
            server.starttls()
            server.login(SmtpAccount, SmtpPassword)
            server.sendmail(sender, receiver, msg.as_string())
        except Exception as e:
            print('error:', str(e))
        finally:
            server.quit()

class YmlHandler:
    @staticmethod
    def yml_write(file_path, data):
        with open(file_path, 'w') as f:
            try:
                yaml.safe_dump(data, f)
            except yaml.YAMLError as exc:
                print("Error in writing YAML file:", exc)

    @staticmethod
    def yml_load(file_path):
        with open(file_path, 'r') as stream:
            try:
                data = yaml.safe_load(stream)
            except yaml.YAMLError as exc:
                print("Error in reading YAML file:", exc)
                data = None
        return data

class MariaHandler:
    def __init__(self, ac, pw, host, port, db):
        self.cnx = pymysql.connect(user=ac,
                                    password=pw,
                                    host=host,
                                    port=port,
                                    database=db,
                                    autocommit=False)
        self.cursor = self.cnx.cursor(pymysql.cursors.DictCursor)

    def close(self):
        self.cursor.close()
        self.cnx.close()

    def exe(self, query, *args):
        result = None
        try:
            self.cursor.execute(query, args)
            try:
                self.cnx.commit()
            except pymysql.err.InternalError:
                pass
            result = self.cursor.fetchall()
        finally:
            self.close()
        return result

    def transaction(self, queries, args=None):
        results = []
        try:
            for i, query in enumerate(queries):
                args_ = args[i] if args else ()
                self.cursor.execute(query, args_)
                result = self.cursor.fetchall()
                results.extend(result)
            self.cnx.commit()
        except Exception as e:
            print(f"An error occurred: {str(e)}")
            self.cnx.rollback()
        finally:
            self.close()
        return results

class RedisHandler:
    def __init__(self, host='localhost', port=6379, db=0, password=None):
        self.host = host
        self.port = port
        self.db = db
        self.password = password
        self.pool = None

    def create_connection(self):
        if self.pool is None:
            self.pool = redis.ConnectionPool(host=self.host, 
                                            port=self.port, 
                                            db=self.db, 
                                            password=self.password)
        connection = redis.Redis(connection_pool=self.pool)
        return connection

    def transaction(self, commands):
        connection = self.create_connection()
        pipe = connection.pipeline()
        for cmd, *args in commands:
            func = getattr(pipe, cmd)
            func(*args)
        response = pipe.execute()
        connection.close()
        return response

    # Hash
    def hash_set(self, hash_name, key, value):
        connection = self.create_connection()
        connection.hset(hash_name, key, value)
        connection.close()

    def hash_get(self, hash_name, key):
        connection = self.create_connection()
        val = connection.hget(hash_name, key)
        connection.close()
        return val

    def hash_key_exist(self, hash_name, key):
        connection = self.create_connection()
        result = connection.hexists(hash_name, key)
        connection.close()
        return result

    def hash_get_all(self, hash_name):
        connection = self.create_connection()
        val = connection.hgetall(hash_name)
        connection.close()
        return val
    
    def hash_size(self, hash_name):
        connection = self.create_connection()
        size = connection.hlen(hash_name)
        connection.close()
        return size

    def hash_delete(self, hash_name, key):
        connection = self.create_connection()
        result = connection.hdel(hash_name, key)
        connection.close()
        return result > 0

    # Set
    def set_add(self, set_name, *values):
        connection = self.create_connection()
        result = connection.sadd(set_name, *values)
        connection.close()
        return result

    def set_delete(self, set_name, *values):
        connection = self.create_connection()
        result = connection.srem(set_name, *values)
        connection.close()
        return result

    def set_get(self, set_name):
        connection = self.create_connection()
        result = connection.smembers(set_name)
        connection.close()
        return result

    def set_exist(self, set_name, value):
        connection = self.create_connection()
        result = connection.sismember(set_name, value)
        connection.close()
        return result

    def set_size(self, set_name):
        connection = self.create_connection()
        result = connection.scard(set_name)
        connection.close()
        return result

    # 交集
    def set_intersection(self, set_name1, set_name2):
        connection = self.create_connection()
        result = connection.sinter(set_name1, set_name2)
        connection.close()
        return result

    # 差集
    def set_difference(self, set_name1, set_name2):
        connection = self.create_connection()
        result = connection.sdiff(set_name1, set_name2)
        connection.close()
        return result

    # 并集
    def set_union(self, set_name1, set_name2):
        connection = self.create_connection()
        result = connection.sunion(set_name1, set_name2)
        connection.close()
        return result

    # Queue FIFO
    def queue_enqueue(self, queue_name, value):
        connection = self.create_connection()
        result = connection.lpush(queue_name, value)
        connection.close()
        return result

    def queue_dequeue(self, queue_name):
        connection = self.create_connection()
        result = connection.rpop(queue_name)
        connection.close()
        return result 

    def queue_peek(self, queue_name):
        connection = self.create_connection()
        result = connection.lindex(queue_name, 0)
        connection.close()
        return result

    def queue_isempty(self, queue_name):
        connection = self.create_connection()
        len = connection.llen(queue_name)
        connection.close()
        return len == 0

    def queue_size(self, queue_name):
        connection = self.create_connection()
        size = connection.llen(queue_name)
        connection.close()
        return size

    def queue_blocking_dequeue(self, queue_name, timeout = 0):
        connection = self.create_connection()
        item = connection.brpop(queue_name, timeout)
        connection.close()
        return item[1] if item else None

    # Stack LIFO
    def stack_push(self, stack_name, value):
        connection = self.create_connection()
        result = connection.rpush(stack_name, value)
        connection.close()
        return result

    def stack_pop(self, stack_name):
        connection = self.create_connection()
        result = connection.rpop(stack_name)
        connection.close()
        return result

    def stack_peek(self, stack_name):
        connection = self.create_connection()
        result = connection.lindex(stack_name, -1)
        connection.close()
        return result

    def stack_isempty(self, stack_name):
        connection = self.create_connection()
        len = connection.llen(stack_name)
        connection.close()
        return len == 0

    def stack_deleteall(self, stack_name):
        connection = self.create_connection()
        connection.delete(stack_name)
        connection.close()

    def stack_size(self, stack_name):
        connection = self.create_connection()
        size = connection.llen(stack_name)
        connection.close()
        return size
