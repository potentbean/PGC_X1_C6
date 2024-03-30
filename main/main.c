#include <stdio.h>
#include "freertos/FreeRTOS.h"
#include "freertos/task.h"
#include "freertos/queue.h"
#include "driver/gpio.h"

#define INPUT_PIN 15
#define LED_PIN 8

kb_lc_cols = [["q","e","r","u","o"],
              ["w","s","g","h","l"],
              ["%","d","t","y","i"],
              ["a","p","^","{","<"],
              [">","x","v","b","$"],
              [" ","z","c","n","m"],
              ["&","^","f","j","k"]]


colPins = [14,3,8,9,11]
rowPins = [15,16,17,18,40,41,39]

// cols = [  # , machine.Pin.PULL_UP),#    # , machine.Pin.PULL_DOWN),
//     machine.Pin(colPins[0], machine.Pin.IN, machine.Pin.PULL_UP),
//     machine.Pin(colPins[1], machine.Pin.IN, machine.Pin.PULL_UP),
//     machine.Pin(colPins[2], machine.Pin.IN, machine.Pin.PULL_UP),
//     machine.Pin(colPins[3], machine.Pin.IN, machine.Pin.PULL_UP),
//     machine.Pin(colPins[4], machine.Pin.IN, machine.Pin.PULL_UP)]
  
// rows = [
//     machine.Pin(rowPins[0], machine.Pin.IN),#, machine.Pin.PULL_DOWN),
//     machine.Pin(rowP
ins[1], machine.Pin.IN),#, machine.Pin.PULL_DOWN),
//     machine.Pin(rowPins[2], machine.Pin.IN),#, machine.Pin.PULL_DOWN),
//     machine.Pin(rowPins[3], machine.Pin.IN),#, machine.Pin.PULL_DOWN),
//     machine.Pin(rowPins[4], machine.Pin.IN),#, machine.Pin.PULL_DOWN),
//     machine.Pin(rowPins[5], machine.Pin.IN),#, machine.Pin.PULL_DOWN),
//     machine.Pin(rowPins[6], machine.Pin.IN)]#, machine.Pin.PULL_DOWN)]




int state = 0;
xQueueHandle interputQueue;

static void IRAM_ATTR gpio_interrupt_handler(void *args)
{
    int pinNumber = (int)args;
    xQueueSendFromISR(interputQueue, &pinNumber, NULL);
}

void LED_Control_Task(void *params)
{
    int pinNumber, count = 0;
    while (true)
    {
        if (xQueueReceive(interputQueue, &pinNumber, portMAX_DELAY))
        {
            printf("GPIO %d was pressed %d times. The state is %d\n", pinNumber, count++, gpio_get_level(INPUT_PIN));
            gpio_set_level(LED_PIN, gpio_get_level(INPUT_PIN));
        }
    }
}

void app_main()
{
    gpio_pad_select_gpio(LED_PIN);
    gpio_set_direction(LED_PIN, GPIO_MODE_OUTPUT);

    gpio_pad_select_gpio(INPUT_PIN);
    gpio_set_direction(INPUT_PIN, GPIO_MODE_INPUT);
    gpio_pulldown_en(INPUT_PIN);
    gpio_pullup_dis(INPUT_PIN);
    gpio_set_intr_type(INPUT_PIN, GPIO_INTR_POSEDGE);

    interputQueue = xQueueCreate(10, sizeof(int));
    xTaskCreate(LED_Control_Task, "LED_Control_Task", 2048, NULL, 1, NULL);

    gpio_install_isr_service(0);
    gpio_isr_handler_add(INPUT_PIN, gpio_interrupt_handler, (void *)INPUT_PIN);
}