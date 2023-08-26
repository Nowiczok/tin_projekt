#include "test_port.h"
#include "freertos/FreeRTOS.h"
#include "freertos/queue.h"
#include "freertos/task.h"
#include "freertos/semphr.h"
#include "driver/uart.h"
#include "system_status.h"
#include <stdbool.h>
#include "esp_log.h"
#include <string.h>
#include "test_protocol.h"

#define START_1_SYMBOL 0x1d
#define START_2_SYMBOL 0x1e

// #define START_1_SYMBOL 0x61
// #define START_2_SYMBOL 0x62

static const char *TAG = "tp"; // TAG for debug

void test_port_task(void* params);

typedef enum {
    START_1,
    START_2,
    ID,
    PAYLOAD,
    CRC
} tp_prot_states;

void test_port_start(){
    xTaskCreate(test_port_task, "tp", 1024, NULL, 3, NULL);
}
    // uart setup
    uart_port_t uart_num = UART_NUM_1;
    void test_port_task(void* params){

    const uart_config_t uart_config = {
        .baud_rate = 115200,
        .data_bits = UART_DATA_8_BITS,
        .parity = UART_PARITY_DISABLE,
        .stop_bits = UART_STOP_BITS_1,
        .flow_ctrl = UART_HW_FLOWCTRL_DISABLE,
        .source_clk = UART_SCLK_APB,
    };
    // We won't use a buffer for sending data.
    uart_driver_install(uart_num, 1024 * 2, 0, 0, NULL, 0);
    uart_param_config(uart_num, &uart_config);
    uart_set_pin(uart_num, 1, 3, UART_PIN_NO_CHANGE, UART_PIN_NO_CHANGE);

    // data reception FSM
    tp_prot_frame_t frame;
    tp_prot_states tp_prot_fsm = START_1;

    uint8_t receiced_byte;
    while(1){
        // Read data from the UART
        int len = uart_read_bytes(uart_num, &receiced_byte, sizeof(receiced_byte), 1000);
        switch (tp_prot_fsm) {
            case START_1: {
                if(receiced_byte == START_1_SYMBOL){
                    frame.START_1 = receiced_byte;
                    // uart_write_bytes(uart_num, start_1_dbg, strlen(start_1_dbg));
                    tp_prot_fsm = START_2;
                }else{
                    tp_prot_fsm = START_1;
                }
                break;
            }
            case START_2: {
                if(receiced_byte == START_2_SYMBOL){
                    frame.START_2 = receiced_byte;
                    // uart_write_bytes(uart_num, start_2_dbg, strlen(start_2_dbg));
                    tp_prot_fsm = ID;
                }else{
                    tp_prot_fsm = START_1;
                }
                break;
            }
            case ID: {
                frame.ID = receiced_byte;
                    // uart_write_bytes(uart_num, id_dbg, strlen(id_dbg));
                tp_prot_fsm = PAYLOAD;
                break;
            }
            case PAYLOAD: {
                frame.PAYLOAD = receiced_byte;
                    // uart_write_bytes(uart_num, payload_dbg, strlen(payload_dbg));
                tp_prot_fsm = CRC;
                break;
            }
            case CRC: {
                frame.CRC = receiced_byte;
                frame_handler(frame);  // execute frame
                // uart_write_bytes(uart_num, crc_dbg, strlen(crc_dbg));
                tp_prot_fsm = START_1;
                break;
            }
            default:{
                tp_prot_fsm = START_1;
                break;
            }
        }
    }
}
