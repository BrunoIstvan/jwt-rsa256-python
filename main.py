import datetime
from datetime import timezone

if __name__ == '__main__':
    private_key = b'-----BEGIN RSA PRIVATE KEY-----\nMIIEogIBAAKCAQEApZ2EDX7XJaPMXo/aWeN6dcQK54fRQVVZ7NMfgBJUCO2cDMtv\nDxCLMLinyHbkkV3RTE5uuqfKcKL1nmH3WIjjUCu8tJmGxjj81EcYINAxhefXPZiu\ngq+8dNXDBy3dOOCRA/mtVswFSRXYl3avvMfAiiha9S87q4EHVM0w2QtfSBPZyrCd\nPDeDlMHTGdyjC9ydFYHSoYv/uv/VS5KwzHRneDzkb00LnNNugFygadc1UV1mawyS\ntoJ0AbYut7qaAYLdJqt2vzPwMknv2vc/iRT05fro/+QxVLeoaoks7mJqLVVvm4eZ\nFSVorSsRlweVKqv5V2aNWdhLXTDiTiIdy/xF+QIDAQABAoIBAAq8Iwsc5aUy8NRQ\nTr7018M6adqIGzA48BNBvBD5HylU/YB2z0QStnL6BSYhTr99bUuc6eB/b8fNSE5z\n2yyJ8vIHY7vxF6NRnlHEKfQ2in87f+AmPWmLKpQIJxQYDPba14uCa5Hst4r9N4TZ\n1JpP+FL8OqkZ3qxHOMpuYnQvIIXzaFUOBSTYng7tzUDVi6uf3vaq7Dc4Y6iR1jDH\nvXdQs1Q6ZR85Ct21MBbWUdeaMpprLtn0M9gxPvHRulK7lqQcTMscUCoPLQ03bBls\nFj6q0fTdXaQOp5zgFDxU5dofWz2o/C0zfedJ3UCbHemRUyhLhXHxkFXbe2HEBhxL\nL3Z4V4ECgYEA9emAkf0rSsYdpV00ebTccvQwJYE/2EhENO8igCUypdUDdkzQaUzY\nZbFCvDiLEnRlYG2fNHr+PEt4NiiILALXj4JyTd/RZRGJwYWhlCwxiCG4FXvqPC33\n5aIuu7nWxS2sWUvzTl5N3SF2AihyMOGzkgPcpMwrdksac6YM4uCy2Y0CgYEArGjC\neP6Ue9kD3cn8vcJMLo6k6EvkU76TNDX+hJjncU95eClY1QJblsnk0YP6C3GXhmdO\npVHebI8mlH5y8xM4/Sou1oeuScdKd5AkCD5zibZSGkzBz9Dzwv+6QBbSrGj83QyW\nCH9p1SjaRaDE1fcXZRGMqeoCkrSYIIkmXBW5ZR0CgYB/y2sfcxvubeq2JyvAG/d8\nXd4vf224bkXT5HpfcfVSLNLxxZWBQ4gpwObXfeL4IjkU1aMo2MoKd4XvTz0E8i0n\nzTits6TUCzs1sMZ5hEXxYuSRdaYSxCjR02jJ8hfkvImWllvI3EVGp771/CLruD9j\noFIn6lqjzP/gHekQdok7eQKBgACGsVE9NabLGr/qheLuXN0ngklTMfcvdbOLFqPA\n87Pc0joTpjnAMBddtl0NUg4G4rd+STcn8M3UAgIiAKfNPzdGka4F6/o9qXSD9Bgy\nWJfq/oUmBtFjidrmfOMFLs9n4p2qFCsieGg2H7RmsTMV9fRRAWTjWe6orm4q/Pr6\n9f3hAoGAefeoE+vy1XjjGqyO2JY15wA1zUFGKLDlpAzgLSRr+MQRnxBzWTACT/R6\nL2+t9vfSs2KJ78iSpO6m3mWZXjhGSmMkTZcHSPL5dGpTmjg4Op1xtt5/7xi/Epu/\n7Rwty6jgDvr12qw9RnmiE7bfWJPtK3Tgf6uPS/pn1RolbLUSzBA=\n-----END RSA PRIVATE KEY-----'
    public_key = b'-----BEGIN PUBLIC KEY-----\nMIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEApZ2EDX7XJaPMXo/aWeN6\ndcQK54fRQVVZ7NMfgBJUCO2cDMtvDxCLMLinyHbkkV3RTE5uuqfKcKL1nmH3WIjj\nUCu8tJmGxjj81EcYINAxhefXPZiugq+8dNXDBy3dOOCRA/mtVswFSRXYl3avvMfA\niiha9S87q4EHVM0w2QtfSBPZyrCdPDeDlMHTGdyjC9ydFYHSoYv/uv/VS5KwzHRn\neDzkb00LnNNugFygadc1UV1mawyStoJ0AbYut7qaAYLdJqt2vzPwMknv2vc/iRT0\n5fro/+QxVLeoaoks7mJqLVVvm4eZFSVorSsRlweVKqv5V2aNWdhLXTDiTiIdy/xF\n+QIDAQAB\n-----END PUBLIC KEY-----'

    import jwt

    payload = {
        'name': 'Bruno Sobrenome',
        'id': '413142',
        'mail': 'bruno.sobrenome@email.com',
        'groups': ['GRP1', 'GRP2'],
        'iss': 'Issuer'
    }

    headers = {
        'typ': 'JWT'
    }

    expiration = datetime.datetime.now(tz=timezone.utc) + datetime.timedelta(seconds=900)
    payload['exp'] = expiration

    global encoded
    try:
        encoded = jwt.encode(payload=payload,
                             key=private_key,
                             headers=headers,
                             algorithm='RS256')
        print(encoded)
    except Exception as ex:
        print('Unknown error')
        print(ex)

    try:
        decoded = jwt.decode(jwt=encoded, key=public_key, algorithms=['RS256'])
        print(decoded)
    except jwt.ExpiredSignatureError as ex:
        print('Expired token')
        print(ex)
    except Exception as ex:
        print('Unknown error')
        print(ex)
