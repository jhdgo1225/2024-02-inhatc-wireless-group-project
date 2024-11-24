#!/usr/bin/env python

from telegram import Update, ReplyKeyboardMarkup, KeyboardButton
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes
import random
from datetime import datetime
import asyncio
import nest_asyncio
from PIL import Image
import io

# nest_asyncio 적용
nest_asyncio.apply()

# 봇 토큰
TOKEN = 'TOKEN KEY'

# 키보드 생성 함수
def create_keyboard():
    keyboard = [
        [KeyboardButton("현재 미세플라스틱 수치")],
        [KeyboardButton("AI 분석 사진 보기")],
        [KeyboardButton("도움말")]
    ]
    return ReplyKeyboardMarkup(keyboard, resize_keyboard=True)

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chat_id = update.effective_chat.id
    message = update.message.text
    print(f"채팅방 ID: {chat_id} | 요청: {message}")
    
    # 첫 메시지이거나 키보드가 없는 경우 키보드 보여주기
    if not hasattr(update.message, 'reply_markup'):
        await update.message.reply_text("미세플라스틱 측정 봇입니다.\n원하시는 기능을 선택해주세요:", 
                                      reply_markup=create_keyboard())
        return
    
    if update.message.text == "현재 미세플라스틱 수치":
        random_value = round(random.uniform(0.5, 5.0), 2)
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
       
        response = f"""
측정 시간: {current_time}
미세플라스틱 수치: {random_value} mg/L
상태: {'정상' if random_value < 3.0 else '주의 필요'}
"""
        await update.message.reply_text(response, reply_markup=create_keyboard())
    
    elif update.message.text == "AI 분석 사진 보기":
        try:
            # 이미지 열기 및 크기 조정 이미지 이름 변경해야함
            with Image.open('test.jpg') as img:
                # 텔레그램 권장 크기로 조정
                max_size = (1280, 720)
                img.thumbnail(max_size, Image.LANCZOS)
                
                
                bio = io.BytesIO()
                bio.name = 'image.jpg'
                img.save(bio, 'JPEG')
                bio.seek(0)
                
                # 조정된 이미지 전송
                await update.message.reply_photo(
                    photo=bio,
                    caption="AI 분석 결과 이미지입니다.",
                    reply_markup=create_keyboard()
                )
        except Exception as e:
            await update.message.reply_text(
                "이미지를 불러오는데 실패했습니다. 잠시 후 다시 시도해주세요.",
                reply_markup=create_keyboard()
            )
            print(f"이미지 전송 오류: {e}")
        
    elif update.message.text == "도움말":
        help_text = """
📌 사용 가능한 기능
• 현재 미세플라스틱 수치: 실시간 측정값 확인
• AI 분석 사진 보기 : AI 분석 결과 이미지 확인
• 도움말: 이 메시지 표시

❓ 문의사항이 있으시면 관리자에게 연락해주세요.
"""
        await update.message.reply_text(help_text, reply_markup=create_keyboard())
        
    else:
        await update.message.reply_text("버튼을 눌러 원하시는 기능을 선택해주세요.", 
                                      reply_markup=create_keyboard())

async def main():
    try:
        # 봇 애플리케이션 생성
        application = Application.builder().token(TOKEN).build()

        # 모든 메시지를 handle_message로 처리
        application.add_handler(MessageHandler(filters.TEXT, handle_message))

        # 봇 실행
        print("봇이 시작되었습니다...")
        await application.run_polling(allowed_updates=Update.ALL_TYPES)
        
    except Exception as e:
        print(f"오류 발생: {e}")

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("\n봇이 종료되었습니다.")
