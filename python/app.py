from flask import Flask, Response
import pymysql
import os
import csv
import io

app = Flask(__name__)

db_config = {
    "host": os.getenv("DB_HOST", "localhost"),
    "user": os.getenv("DB_USER", "user"),
    "password": os.getenv("DB_PASSWORD", "password"),
    "database": os.getenv("DB_NAME", "titanic"),
    "port": int(os.getenv("DB_PORT", 3306))
}

@app.route('/api/passengers', methods=['GET'])
def get_passengers():
    try:
        # 連接資料庫
        conn = pymysql.connect(**db_config)
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Passengers;")
        rows = cursor.fetchall()
        conn.close()

        # 如果資料庫中沒有數據，返回表頭
        if not rows:
            return Response(
                "id,pclass,survived,pname,sex,age,sibsp,parch,ticket,fare,cabin,embarked,boat,body,homedest\n",
                mimetype='text/csv'
            )

        # 處理並格式化數據為 CSV
        output = io.StringIO()
        writer = csv.writer(output, quoting=csv.QUOTE_MINIMAL)

        # 寫入表頭
        header = ["id", "pclass", "survived", "pname", "sex", "age", "sibsp", "parch",
                  "ticket", "fare", "cabin", "embarked", "boat", "body", "homedest"]
        writer.writerow(header)

        # 處理欄位數據，移除 None 並清理特殊字符
        for row in rows:
            sanitized_row = [
                col.replace('"', '').replace(',', ' ') if isinstance(col, str) else (col or '')
                for col in row
            ]
            writer.writerow(sanitized_row)

        content = output.getvalue()
        output.close()

        return Response(content, mimetype='text/csv')
    except Exception as e:
        # 返回錯誤信息
        return Response(f"Error: {str(e)}", status=500)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
