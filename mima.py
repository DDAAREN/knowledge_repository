def volid(pwd):
    a = any(map(str.isupper, pwd))
    b = any(map(str.islower, pwd))
    c = any(map(str.isdigit, pwd))
    d = not all(map(str.isalnum, pwd))
    return all([a,b,c,d])

#�ж������Ƿ���ȫ�������ͻ���ĸ��ɣ��Ҵ�Сд����
