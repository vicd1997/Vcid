from flaskblog import app
import os


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 80))
    app.run(debug=True,host='172.31.91.238',port=port)
