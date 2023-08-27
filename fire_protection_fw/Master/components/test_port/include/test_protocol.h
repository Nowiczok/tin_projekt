#ifndef TEST_PROTOCOL_H
#define TEST_PROTOCOL_H

#include <stdint.h>

typedef struct __attribute__((__packed__)){
    uint8_t START_1;
    uint8_t START_2;
    uint8_t ID;
    uint8_t PAYLOAD;
    uint8_t CRC;
}tp_prot_frame_t;

typedef union {
    tp_prot_frame_t frame_fields;
    uint8_t frame_bytes[sizeof(tp_prot_frame_t)];
}tp_prot_frame_u;

void frame_handler(tp_prot_frame_t frame);
uint8_t calculate_crc(tp_prot_frame_u frame);

#endif