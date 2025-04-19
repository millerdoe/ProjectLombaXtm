
from sqlite3 import Connection
from sys import exit


"""
lihat isi databases
select * from users

hapus user dalam database
delete from users where username='username target'

"""
with Connection("dbusers.db") as conn:
    ijin_exeQ = conn.cursor()
    
    
    exe = True
    while exe:
        
        print("""
    opsi
    
    
    [1] lihat semua user di database
    [2] hapus user dari database
    [3] exit
        """)
        pilihan:int = int(input("pilih opsi: "))
        match pilihan:
            case 1:
                ijin_exeQ.execute("select * from users")
                call_data = ijin_exeQ.fetchall()
                for lihat_db in call_data:
                    print(call_data)
                    
            case 2:
                username_target:str = input("username: ")
                ijin_exeQ.execute("delete from users where username=:username", {"username":username_target})
                if ijin_exeQ:
                    print(f"ok username {username_target} telah dihapus")
                else:
                    pass
            
            case _:
                print(f"lol tidak ada opsi {pilihan}")
                exit()
        if pilihan == 3:
            exe = False