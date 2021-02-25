""" Atores: UC3M
Fecha de ultima mod.: indeterminada"""

from SecureAll import AccessManager

# Funcion main
def main():
    mng = AccessManager()
    res = mng.readaccessrequestfromJSON("test.json")
    print(res)


if __name__ == "__main__":
    main()
