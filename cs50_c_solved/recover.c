#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>

#define CHUNK 512
typedef uint8_t BYTE;

int main(int argc, char *argv[])
{
    // Check for one input only
    if (argc != 2)
    {
        printf("Usage: recover [file]\n");
        return 1;
    }
    FILE *card = fopen(argv[1], "r");
    // Check the return value of the file (to avoid cases of NULL values)
    if (!card)
    {
        printf("Usage: invalid file\n");
        return 1;
    }
    else
    {
        // buffer with number chunks bytes
        BYTE buffer[CHUNK];

        // char array with 8 characters
        char *filename = malloc(sizeof(double));
        
        // counter        
        int counter = 0;

        // file to open
        FILE *img;

        // fread reads 512 bytes chuncks, one by one
        while (fread(buffer, CHUNK, 1, card) == 1)
        {
            // a new jpg is detected
            if (buffer[0] == 0xff && buffer[1] == 0xd8 && buffer[2] == 0xff && (buffer[3] & 0xf0) == 0xe0)
            {
                // if it is the first jpg
                if(counter == 0)
                {
                    printf("%d first jpg\n", counter);
                    sprintf(filename, "%03i.jpg", counter+1);
                    img = fopen(filename, "w");
                    fwrite(&buffer, sizeof(BYTE), CHUNK, img);
                }
                // if it is a new jpg
                else
                {
                    printf("%d jpg\n",counter);
                    fclose(img);
                    sprintf(filename, "%03i.jpg", counter+1);
                    img = fopen(filename, "w");
                    fwrite(&buffer, sizeof(BYTE), CHUNK, img);
                }
                counter++;
            }
            // if it is not a block with the start of a jpg
            else
            {
                fwrite(&buffer, sizeof(BYTE), CHUNK, img);
            }
        }
        fclose(card);
    }
}

// printf("counter %d, buffer[0]: %d, *buffer[0] %p\n", counter, buffer[0], &buffer[0]);