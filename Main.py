""" Colaboradores: UC3M, Gonzalo Llosa, Diego Robles
    Fecha: 26/02/2021"""

from SecureAll import AccessManager

# Funcion main
def main():
    mng = AccessManager()
    res = mng.readaccessrequestfromJSON("test.json")
    print(res)


if __name__ == "__main__":
    main()
