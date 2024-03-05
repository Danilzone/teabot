import sqlite3
from rich import print
from rich.console import Console
from datetime import timedelta, datetime

console = Console()

class Db():

    def __init__(self, db_file):
        self.conn = sqlite3.connect(db_file)
        self.cursor = self.conn.cursor()


    def time_check(self, user_id, dogname, user_name, time, tabl):
        try:
            self.user_id = user_id
            self.dogname = dogname
            self.user_name = user_name
            self.time = time
            self.tabl = tabl

            self.cursor.execute(f'SELECT "user_id" FROM `{tabl}`')
            res = self.cursor.fetchall()
            self.conn.commit()
            
            user_ids = [row[0] for row in res]

            if user_id in user_ids:
                self.cursor.execute(f'SELECT "time_drank" FROM `{tabl}` WHERE "user_id" = ?', (user_id,))
                time_drank_str = self.cursor.fetchone()[0]
                time_drank = datetime.strptime(time_drank_str, "%Y-%m-%d %H:%M:%S.%f") 
                self.conn.commit()
                 
                timeexp = time_drank - time
                minutes = int(timeexp.total_seconds() // 60)
                
                if time > time_drank:
                    return True, minutes
                else: 
                    return False, minutes
            else:
                minutes = int(0)
                return True, minutes
            
        except Exception:
            console.print_exception(show_locals=True)

    def drank(self, user_id, dogname, user_name, amount_drank, time, tabl):
        try:
            self.user_id = user_id
            self.dogname = dogname
            self.user_name = user_name
            self.amount_drank = amount_drank
            self.time = time
            self.tabl = tabl 

            print(f"([cyan1]{user_id}[/cyan1]) [yellow]@[/yellow]{dogname} [green]{user_name}[/green] выпил [yellow]{tabl}[/yellow]")

            self.cursor.execute(f'SELECT "user_id" FROM `{tabl}`')
            res = self.cursor.fetchall()
            self.conn.commit()

            user_ids = [row[0] for row in res]

            if self.user_id in user_ids:

                self.cursor.execute(f'SELECT "amount" FROM `{tabl}` WHERE "user_id" = ? ', (user_id,))
                amount_db = float("{:.2f}".format(self.cursor.fetchone()[0]))
                self.conn.commit()

                amount = amount_drank + amount_db

                new_time_drank = time + timedelta(hours=1)

                self.cursor.execute(f'UPDATE `{tabl}` SET "time_drank" = ? WHERE "user_id" = ?', (new_time_drank, user_id,))
                self.cursor.execute(f'UPDATE `{tabl}` SET "amount" = ? WHERE "user_id" = ?', (amount, user_id,))
                self.cursor.execute(f'UPDATE `{tabl}` SET "dogname" = ? WHERE "user_id" = ?', (dogname, user_id,))
                self.cursor.execute(f'UPDATE `{tabl}` SET "user_name" = ? WHERE "user_id" = ?', (user_name, user_id,))
                lit = self.cursor.execute(f'SELECT "amount" FROM {tabl} WHERE "user_id" = ?', (user_id,)).fetchone()
                self.conn.commit()
                
                return lit[0]

            else:
                print(f"[yellow bold]#[/yellow bold]Новый игрок! [yellow]@[/yellow]{dogname} [green]{user_name}[/green]")
                new_time_drank = time + timedelta(hours=1)
                self.cursor.execute(f'INSERT INTO `{tabl}` ("user_id", "dogname", "user_name", "amount", "time_drank") VALUES (?, ?, ?, ?, ?)', (user_id, dogname, user_name, amount_drank, new_time_drank, ))
                lit = self.cursor.execute(f'SELECT "amount" FROM {tabl} WHERE "user_id" = ?', (user_id,)).fetchone()
                self.conn.commit()

                return lit[0]

        except Exception:
            console.print_exception(show_locals=True)


    def top(self, drank):
        self.drank = drank
        self.cursor.execute(f'SELECT user_name, dogname, amount FROM {drank} ORDER BY amount DESC')
        self.conn.commit()

        # Получение результатов и форматирование в требуемый формат
        result = self.cursor.fetchall()
        top_result = ""
        for i, row in enumerate(result, 1):
            top_result += f"{i}. <b>{row[0]}</b> : <b>{round(row[2], 2)} л.</b> \n"
        
        return top_result


        

    def close(self):
        self.conn.close()
