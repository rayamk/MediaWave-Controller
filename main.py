from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Welcome to MediaWave Controller"}

# နောက်ပိုင်းမှာ ဒီမှာပဲ TV Monitor နဲ့ Translator routes တွေကို ထပ်ဖြည့်သွားမှာပါ

