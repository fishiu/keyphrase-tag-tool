import mysql.connector
from util import *
from db.db_util import *


def import_raw():
    """
    加载abs.json原始数据
    @return:
    """
    db_util = DbUtil()
    article_record_list = load_json("../../static/data/article.json")
    for article_record in tqdm(article_record_list):
        article_id = article_record["id"]
        if article_id == 1000:
            break
        article_abs = article_record["abstract"]
        article_title = article_record["title"]
        article_author_kp = json.dumps(article_record["index"])

        insert_sql = "insert into KeyPhrase.article (id, title, author_kp, abstract) values (%s, %s, %s, %s)"
        sql_params = [article_id, article_title, article_author_kp, article_abs]
        # print(sql_params)
        db_util.cursor.execute(insert_sql, sql_params)
        db_util.conn.commit()
    db_util.conn.close()


def import_pred_kp():
    """
    加载（筛选后的）关键词
    @return:
    """
    db_util = DbUtil()
    article_pred_record_list = load_json("../../static/data/filtered_key_phrase/filtered_key_phrase_1.json")
    for record_id, article_pred_record in article_pred_record_list.items():
        pred_kp = json.dumps(article_pred_record)
        update_sql = "update KeyPhrase.article set pred_kp = %s where id = %s"
        db_util.cursor.execute(update_sql, (pred_kp, record_id))
        db_util.conn.commit()
    db_util.db_close()


if __name__ == '__main__':
    import_pred_kp()