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

void frame_handler(tp_prot_frame_t frame);

#endif