# 用法
---
## このリポジトリで行うこと

  このリポジトリではRaspberry Piを用いたCAN通信を行う
1. 使用機材
- Raspberry Pi 4 model B
- mcp2551
- mcp2515

## CANsend.pyについて
CANsend.pyでは8byteのデータフィールドを持つメッセージを可能な限り送信する
macの場合 ctrl+Cで送信を中断する
### can.messageについて
  [python-can公式](https://python-can.readthedocs.io/en/master/_modules/can/message.html)
  can.messageの構成内容を下に記す
  
