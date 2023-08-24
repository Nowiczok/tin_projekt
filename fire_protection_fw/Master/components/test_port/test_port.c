#include "test_port.h"
#include "freertos/FreeRTOS.h"
#include "freertos/queue.h"
#include "freertos/task.h"
#include "freertos/semphr.h"
#include "driver/uart.h"
#include "system_status.h"
#include <stdbool.h>
#include "esp_log.h"

static const char *TAG = "tp"; // TAG for debug

void test_port_task(void* params);

void test_port_start(){
    xTaskCreate(test_port_task, "tp", 256, NULL, 3, NULL);
}

void test_port_task(void* params){

    const uart_port_t uart_num = UART_NUM_2;
    uart_config_t uart_config = {
        .baud_rate = 115200,
        .data_bits = UART_DATA_8_BITS,
        .parity = UART_PARITY_DISABLE,
        .stop_bits = UART_STOP_BITS_1,
        .flow_ctrl = UART_HW_FLOWCTRL_CTS_RTS,
        .rx_flow_ctrl_thresh = 122,
    };
    // Configure UART parameters
    ESP_ERROR_CHECK(uart_param_config(uart_num, &uart_config));

    // Set UART pins(TX: IO4, RX: IO5, RTS: IO18, CTS: IO19)
    ESP_ERROR_CHECK(uart_set_pin(UART_NUM_2, 4, 5, 18, 19));

    // Setup UART buffered IO with event queue
    const int uart_buffer_size = (1024 * 2);
    QueueHandle_t uart_queue;
    // Install UART driver using an event queue here
    ESP_ERROR_CHECK(uart_driver_install(UART_NUM_2, uart_buffer_size, \
                                            uart_buffer_size, 10, &uart_queue, 0));

    while(1){
        
    }
}