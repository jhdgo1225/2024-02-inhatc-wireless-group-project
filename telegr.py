#!/usr/bin/env python

from telegram import Update, ReplyKeyboardMarkup, KeyboardButton
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes
import random
from datetime import datetime
import asyncio
import nest_asyncio
from PIL import Image
import io
import logging

import camera

# nest_asyncio 적용
nest_asyncio.apply()


# 봇 토큰
TOKEN = 'TOKEN'

# 로깅 설정
log_filename = './error.log'
logging.basicConfig(
    filename=log_filename,
    level=logging.ERROR,
    format='%(asctime)s - %(levelname)s - %(message)s',
)

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
        try:
            # 테스트부분 실제는 주석 풀고 아래 변수 저장한거 지우고 시작
            num_objects, area_ratio = camera.capture_and_detect()
            #num_objects = 10
            #area_ratio = 10
#            raise Exception("에러에러에러 에러발생") 테스트용throw  
            if num_objects <= 5 and area_ratio <= 4:
                status = "정상입니다! 안심하고 드세요!"
            elif num_objects <= 10 and area_ratio <= 10:
                status = "아직은 괜찮지만 필터를 슬슬 준비해야겠어요!"
            else:
                status = "필터를 교체할때가 된거같아요!"
            
            response = f"현재 미세플라스틱 상태는 {status}"
            await update.message.reply_text(response, reply_markup=create_keyboard())
        
        except Exception as e:
            # 에러 메시지를 log에 기록
            error_message = f"이미지 전송 오류: {e}"
            logging.error(error_message)  # log 파일에 에러 기록

            await update.message.reply_text(
                "시스템 오류가 발생했습니다.관리자에게 문의해주세요.201944007@itc.ac.kr",
                reply_markup=create_keyboard()
            )

    elif update.message.text == "AI 분석 사진 보기":
        try:
            await update.message.reply_text("사진을 분석하고 있어요 ! ", reply_markup=create_keyboard())
            
            #사진만 분석하고 저장시키느라 return은 무시
            camera.capture_and_detect()
#            raise Exception("에러에러에러 에러발생 ")  테스트용throw
            with Image.open('detection_result.jpg') as img:
                max_size = (1280, 720)
                img.thumbnail(max_size, Image.LANCZOS)
                    
                
                bio = io.BytesIO()
                bio.name = 'image.jpg'
                img.save(bio, 'JPEG')
                bio.seek(0)
                
                await update.message.reply_photo(
                    photo=bio,
                    caption="AI 분석 결과 이미지입니다.",
                    reply_markup=create_keyboard()
                )
        except Exception as e:
            # 에러 메시지를 log에 기록
            error_message = f"이미지 전송 오류: {e}"
            logging.error(error_message)  # log 파일에 에러 기록

            await update.message.reply_text(
                "이미지를 불러오는데 실패했습니다. 관리자에게 문의해주세요.201944007@itc.ac.kr",
                reply_markup=create_keyboard()
            )
            print(f"이미지 전송 오류: {e}")
        
    elif update.message.text == "도움말":
        help_text = """
 사용 가능한 기능
• 현재 미세플라스틱 수치: 현재 수중 미세 플라스틱 위험도를 알려드려요!

• AI 분석 사진 보기 : AI 분석 결과 이미지를 전송해드려요 초록색 네모칸이 미세플라스틱이에요! 

 문의사항이 있으시면 관리자에게 연락해주세요. 201944007@itc.ac.kr
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
