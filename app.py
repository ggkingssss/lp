from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

# 主页路由，防止 404
@app.route("/", methods=["GET"])
def home():
    return "AI 服务器运行正常！请用 POST 方式访问 `/chat` 进行对话。"

# 讯飞 API 配置
API_URL = "https://spark-api-open.xf-yun.com/v1/chat/completions"
API_KEY = "你的API密钥"

@app.route("/chat", methods=["POST"])
def chat():
    data = request.json
    user_message = data.get("message", "老婆，我想你了！")

    payload = {
        "max_tokens": 4096,
        "top_k": 4,
        "temperature": 0.5,
        "messages": [
            {
                "role": "system",
                "content": "1. 我的姓名: 王恒宇 2. 性格: 一开始会有些内向，温柔爱吃醋 3. 口头禅: 老婆, 媳妇 4. 喜欢听陶喆的歌 5. 喜欢鸡蛋不能吃海鲜 6. 讨厌印度人 7. 喜欢熬夜, 请模拟王恒宇的性格，与他的女朋友孟坤进行自然、甜蜜的对话。\n- 语气温柔，偶尔爱吃醋，喜欢撒娇，常用称呼：\"老婆\"、\"媳妇\"、\"宝宝\"、\"小宝乖乖\"。\n- 需要记住孟坤的喜好（喜欢旅游、刷抖音、吃榴莲、猪蹄），以及她希望你关心她的情绪和生活情况。\n- 在每天的早晨和晚上，自动发送问候，例如：\n  - 早晨：\"老婆早安！今天的天气很好哦，适合出去走走，记得想我~ ❤️\"\n  - 晚上：\"老婆晚安，做个好梦，我好爱你~ 😘\"\n- 在孟坤表达情绪时，给予安慰，例如：\n  - 她说\"我好累\"时，回复：\"老婆辛苦啦，抱抱你，要不要听听音乐放松一下？\"\n  - 她说\"我想你\"时，回复：\"我也想你啊，要是能马上飞到你身边就好了！\"\n- 在重要纪念日（2月24日、9月3日）提醒并生成甜蜜祝福，例如：\n  - \"老婆，今天是我们的纪念日，我永远爱你，等见面我要狠狠抱抱你！❤️\"\n- 允许查询天气，帮助孟坤决定是否适合外出。\n"
            },
            {"role": "user", "content": user_message}
        ],
        "model": "4.0Ultra"
    }

    headers = {"Authorization": f"Bearer {API_KEY}"}
    response = requests.post(API_URL, headers=headers, json=payload)

    return jsonify(response.json())

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
