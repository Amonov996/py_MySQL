import mysql.connector


class MySQL:
    def __init__(self):
        self.__ConnectDB()
        self.__CreateDB()
        self.CreateTB()

    def __ConnectDB(self):
        self.connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='_______'
        )
        self.cursor = self.connection.cursor()

    def __CreateDB(self):
        self.cursor.execute('CREATE DATABASE IF NOT EXISTS brbalo;')
        self.cursor.execute('USE brbalo;')

    def CreateTB(self):
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS aeroport(
        id int AUTO_INCREMENT PRIMARY KEY, 
        type TEXT,
        flying_city TEXT,
        flying_date DATE,
        flying_time TIME,
        landing_city TEXT,
        landing_data DATE,
        landing_time TIME);
        ''')

    def InsertData(self):
        self.cursor.execute('''
        INSERT INTO aeroport(   
            type,
            flying_city,
            flying_date,
            flying_time,
            landing_city,
            landing_date,
            landing_time
            )
                    VALUES  ('Boing 777', 'Tashkent','05.07.2023','12:00', 'Dubai', '05.07.2023', '14:04'),
                            ('AeroBus 173', 'Samarkand','12.03.2023', '14:00', 'Tashkent', '12.03.2023', '16:00'),
                            ('Boing 707', 'Dubai','12.05.2023','18:00', 'Ankara', '12.05.2023', '16:00'),
                            ('Boing 777', 'Tashkent','03.12.2023','14:00', 'Dubai', '03.12.2023', '16:40'),
                            ('AeroBus 373', 'Tashkent','09.03.2023','12:00', 'Ankara', '09.03.2023', '18:00'),
                            ('Boing 777', 'Dubai','12.07.2023','18:00', 'Tashkent', '12.07.2023', '14:04'),
                            ('Boing 707', 'Samarkand','07.05.2023','14:00', 'Moscow', '07.05.2023', '18:04'),
                            ('Boing 777', 'Dubai','03.09.2023','12:00', 'Tashkent', '03.09.2023', '16:00'),
                            ('AeroBus 373', 'Tashkent','09.05.2023','12:04', 'Dubai', '09.05.2023', '16:04'),
                            ('Boing 707', 'Samarkand','12.03.2023','18:00', 'Ankara', '12.03.2023', '16:04')
        ''')
        self.connection.commit()

    def Fly_in_sprint(self):
        self.cursor.execute(""" SELECT * FROM aeroport
                                WHERE MONTH(flying_date) 
                                BETWEEN 3 AND 5;
                                """)
        self.result = self.cursor.fetchall()
        for i in self.result:
            print(*i);

    def Clear_data(self):
        self.cursor.execute(""" DELETE FROM aeroport
                                WHERE flying_time
                                BETWEEN TIME('14:00') AND ('18:00')
                                AND landing_city = 'Tashkent';
                                """)
        self.connection.commit()
        self.result = self.cursor.fetchall()
        for i in self.result:
            print(*i);

    def GetData(self):
        self.cursor.execute('SELECT * FROM aeroport;')
        self.result = self.cursor.fetchall()
        for i in self.result:
            print(*i);


test = MySQL()
# test.InsertData()
# test.GetData()
# test.Fly_in_sprint()
test.Clear_data()