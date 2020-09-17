import sqlite3

''' Make DB files with block chain data '''

class makeDB:

    def __init__(self, s_mix, s_comp):
        self.mixData(s_mix)
        self.compData(s_comp)

    # remove existing data
    def reset_query(self, db_name) :
        with sqlite3.connect(db_name) as conn:
            cursor = conn.cursor()
            if db_name == 'comp.db' :
                cursor.execute('Delete From product ')
            else :
                cursor.execute('Delete From material')
            conn.commit()

    def run_query(self, db_name, query, parameters=()):
        with sqlite3.connect(db_name) as conn:
            cursor = conn.cursor()
            query_result = cursor.execute(query, parameters)
            conn.commit()

    ''' Mixture block chain to DB file '''
    
    def mixData(self, s_mix) :
        db_name = 'mix.db'
        self.reset_query(db_name)
        
        i = 1
        while 1 :
            # check the end of mixture chain
            try :
                block = s_mix.chain[i].transactions
            except IndexError : # out of range
                break

            # make query data in DB file
            keys = list(block.keys())
            query = 'INSERT INTO material VALUES (?,?,?,?,?,?)'
            parameters = (i,block[keys[0]],block[keys[1]],block[keys[2]],block[keys[3]],
                          block[keys[4]])
            self.run_query(db_name, query, parameters)
            i += 1
            
    ''' Product block chain to DB file '''
    
    def compData(self, s_comp):
        db_name = 'comp.db'
        self.reset_query(db_name)

        i = 1
        while 1 :
            # check the end of product chain
            try :
                block = s_comp.chain[i].transactions
            except IndexError : # out of range
                break

            # make query data in DB file
            keys = list(block.keys())
            query = 'INSERT INTO product VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)'
            parameters = (i,block[keys[0]],block[keys[1]],block[keys[2]],block[keys[3]],
                          block[keys[4]],block[keys[5]],block[keys[6]],block[keys[7]],
                          block[keys[8]],block[keys[9]],block[keys[10]],block[keys[11]],
                          block[keys[12]],block[keys[13]],block[keys[14]],block[keys[15]],
                          block[keys[16]],block[keys[17]],block[keys[18]],block[keys[19]],
                          block[keys[20]])
            self.run_query(db_name, query, parameters)
            i += 1
