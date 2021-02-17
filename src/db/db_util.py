from mysql import connector
from util import *


def pred_kp2tag(abs_t: str, pred_kp_t: str):
    """
    handle abs_text to tagged text
    @param abs_t: abstract text
    @param pred_kp_t: kp (need serialize)
    @return: abs_text (tagged)
    """
    pred_kp_list = json.loads(pred_kp_t)
    for pred_kp in pred_kp_list:
        abs_t = abs_t.replace(pred_kp, f"<i class='kp'>{pred_kp}</i><input class='kp-input'>")
    return abs_t


class DbUtil:
    def __init__(self):
        """
        db action
        init
        """
        self.conn = connector.connect(user='root', database='KeyPhrase')
        self.cursor = self.conn.cursor()
        print("db init ok")

    def get_record(self, record_id_):
        """
        db action
        get article record from db
        @param record_id_: id
        @return: info in dict
        """
        sql_get = "select * from KeyPhrase.article where id = %s"
        print("get record:", sql_get % record_id_)
        try:
            self.cursor.execute(sql_get, (record_id_,))
            record_info = self.cursor.fetchall()[0]
            record_abstract = record_info[1]
            record_pred_kp_list = record_info[4]
            record_info_dict = {
                "id": record_info[0],
                "abstract": pred_kp2tag(record_abstract, record_pred_kp_list),
                "title": record_info[2],
                "tag_kp": record_info[6]
            }
            return record_info_dict
        except Exception as e:
            print(str(e))
            return False

    def modify_kp_tag(self, record_id_, kp_tag_text_):
        """
        db action
        modify (and update) tagged abstract text (with tag)
        @param record_id_: id
        @param kp_tag_text_: text
        @return: None
        """
        sql_insert = 'update KeyPhrase.article set tag_kp = %s where id = %s'
        print("modify kp tag:", sql_insert % (kp_tag_text_, record_id_))
        try:
            self.cursor.execute(sql_insert, (kp_tag_text_, record_id_))
            self.conn.commit()
            return True
        except Exception as e:
            print(str(e))
            return False

    def db_close(self):
        """
        db action
        close
        @return:
        """
        self.conn.close()
