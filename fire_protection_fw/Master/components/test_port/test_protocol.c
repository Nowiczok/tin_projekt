#include "test_protocol.h"
#include <stdint.h>
#include "system_status.h"
#include "driver/uart.h"

#define PING_FRAME 0x00
#define RELAY_ON_FRAME 0x01
#define RELAY_OFF_FRAME 0x02
#define ALARM_ON_FRAME 0x03
#define ALARM_OFF_FRAME 0x04
#define WIFI_CONNECTION_FRAME 0x05
#define UNKNOWN_ID 0xff

uint8_t ping_frame_handler(uint8_t payload);
uint8_t relay_on_frame_handler(uint8_t payload);
uint8_t relay_off_frame_handler(uint8_t payload);
uint8_t alarm_on_frame_handler(uint8_t payload);
uint8_t alarm_off_frame_handler(uint8_t payload);
uint8_t wifi_connection_frame_handler(uint8_t payload);
uint8_t unknown_frame_handler(uint8_t payload);

typedef struct {
    uint8_t ID;
    uint8_t (*handler)(uint8_t);
} test_prot_id_hadler_pair;

test_prot_id_hadler_pair handlers[] = {
    {PING_FRAME, ping_frame_handler},
    {RELAY_ON_FRAME, relay_on_frame_handler},
    {RELAY_OFF_FRAME, relay_off_frame_handler},
    {ALARM_ON_FRAME, alarm_on_frame_handler},
    {ALARM_OFF_FRAME, alarm_off_frame_handler},
    {WIFI_CONNECTION_FRAME, wifi_connection_frame_handler},
    {UNKNOWN_ID, unknown_frame_handler},  // this MUST be last
};

void frame_handler(tp_prot_frame_t frame){
    uint8_t i = 0;
    while(handlers[i].ID != UNKNOWN_ID){
        if(handlers[i].ID == frame.ID){
            uint8_t new_payload = handlers[i].handler(frame.PAYLOAD);
            frame.PAYLOAD = new_payload;
            tp_prot_frame_u frame_union;
            frame_union.frame_fields = frame;
            frame.CRC = calculate_crc(frame_union);
            uart_write_bytes(UART_NUM_1, &frame, sizeof(frame));
            break;
        }else{
            i++;
        }
    }
}

uint8_t calculate_crc(tp_prot_frame_u frame){
    uint8_t crc = 0;
    for(uint8_t i = 0; i < sizeof(tp_prot_frame_u)-1; i++){
        crc ^= frame.frame_bytes[i];
        for(uint8_t j = 0; j < 8; j++){
            if(crc & 0x80){
                crc = (crc << 1) ^ 0x07;
            }else{
                crc <<= 1;
            }
        }
    }
    return crc;
}

uint8_t ping_frame_handler(uint8_t payload){
    return payload;
}

uint8_t relay_on_frame_handler(uint8_t payload){
    sys_stat_set_pump(true);
    return payload;
}

uint8_t relay_off_frame_handler(uint8_t payload){
    sys_stat_set_pump(false);
    return payload;
}

uint8_t alarm_on_frame_handler(uint8_t payload){
    sys_stat_set_alarm(true);
    return payload;
}

uint8_t alarm_off_frame_handler(uint8_t payload){
    sys_stat_set_alarm(false);
    return payload;
}

uint8_t wifi_connection_frame_handler(uint8_t payload){
    return sys_stat_get_wifi_connected();
}

uint8_t unknown_frame_handler(uint8_t payload){
    return payload;
}
