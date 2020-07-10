class Delete:
    def deleteContent():

        with open('C:\\Users\\Vishal\\Desktop\\workarea\\Intercom\\resultvs.txt', 'a') as f:
            f.seek(0)
            f.truncate()
            f.close()
        return "content successfully deleted"

