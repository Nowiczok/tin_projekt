# Serial test protocol

## Frame sructure

- START: 2 B, 0x1D1E
- ID: 1 B
- PAYLOAD: 1 B
- CRC: 1B, sum of all other bytes

## Ping
- ID = 0x00
- Response: copy of frame

## Relay oni
- ID = 0x01
- Response: copy of frame

## Relay off
- ID = 0x02
- Response: copy of frame

## Alarm on
- ID = 0x03
- Response: copy of frame

## Alarm off
- ID = 0x04
- Response: copy of frame

## Wifi connection
- ID = 0x05
- Response: same ID, payload = 0x01 if connected to wifi, 0x00 if not
