import excelData

''' FROM Excel TO Block chain '''

class excelToBlock :
    def __init__(self, s_mix, s_comp) :
        self.mixExcelToBlock(s_mix)
        self.productExcelToBlock(s_comp)

    ''' Mixture Block chain '''
    
    def mixExcelToBlock(self, s_mix) :
        n = 1
        while 1 :
            sheetName = 'Sheet' + str(n)
            i = 1
            while 1 :
                t = excelData.mix_transaction(sheetName, i)
                if t == 0 : # end of data in row
                    n += 1
                    break
                elif t == -1 : # end of sheet
                    return 0
                else : # data exist
                    s_mix.add_block(t)
                    i += 1
            
    ''' Product Block chain '''
    
    def productExcelToBlock(self, s_comp) :
        n = 1
        while 1 :
            sheetName = 'Sheet' + str(n)
            i = 1
            while 1 :
                t = excelData.comp_transaction(sheetName, i)
                if t == 0 : # end of data in row
                    n += 1
                    break
                elif t == -1: # end of sheet
                    return 0
                else : # data exist
                    s_comp.add_block(t)
                    i += 1
