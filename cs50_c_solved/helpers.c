// resolved by guido nicolás mitolo

#include "helpers.h"
# include <math.h>

// Convert image to grayscale
void grayscale(int height, int width, RGBTRIPLE image[height][width])
{
    float average = 0;

    for (int row = 0; row < height; row++)
    {
        for (int col = 0; col < width; col++)
        {
            // take each color value from every element of the 2D array, find the average and store it in a float variable
            average = round((image[row][col].rgbtBlue + image[row][col].rgbtGreen + image[row][col].rgbtRed) / 3.0);

            // store the average to the each color of every element of the 2D array
            image[row][col].rgbtBlue = average;
            image[row][col].rgbtGreen = average;
            image[row][col].rgbtRed = average;
        }
    }
    return;
}

// Convert image to sepia
void sepia(int height, int width, RGBTRIPLE image[height][width])
{
    int sepiaBlue = 0;
    int sepiaGreen = 0;
    int sepiaRed = 0;

    for (int row = 0; row < height; row++)
    {
        for (int col = 0; col < width; col++)
        {

            // apply the sepia formula for the color of each element of the array and then update their values
            sepiaBlue = round(.131 * image[row][col].rgbtBlue + .534 * image[row][col].rgbtGreen + .272 * image[row][col].rgbtRed);
            sepiaGreen = round(.168 * image[row][col].rgbtBlue + .686 * image[row][col].rgbtGreen + .349 * image[row][col].rgbtRed);
            sepiaRed = round(.189 * image[row][col].rgbtBlue + .769 * image[row][col].rgbtGreen + .393 * image[row][col].rgbtRed);

            // store 255 if the result of the formula is a bigger number
            if (sepiaBlue > 255)
            {
                image[row][col].rgbtBlue = 255;
            }
            else
            {
                image[row][col].rgbtBlue = sepiaBlue;
            }
            if (sepiaGreen > 255)
            {
                image[row][col].rgbtGreen = 255;
            }
            else
            {
                image[row][col].rgbtGreen =  sepiaGreen;
            }
            if (sepiaRed > 255)
            {
                image[row][col].rgbtRed = 255;
            }
            else
            {
                image[row][col].rgbtRed = sepiaRed;
            }
        }
    }
    return;
}

// Reflect image horizontally
void reflect(int height, int width, RGBTRIPLE image[height][width])
{
    float swap_blue = 0;
    float swap_green = 0;
    float swap_red = 0;

    for (int row = 0; row < height; row++)
    {
        // swaps variables store the first's half of the values to paste them backwards in the second half
        for (int col = 0; col < width / 2; col++) // j up to 299
        {
            swap_blue = image[row][col].rgbtBlue;
            image[row][col].rgbtBlue = image[row][(width - 1) - col].rgbtBlue;
            image[row][(width - 1) - col].rgbtBlue = swap_blue;

            swap_green = image[row][col].rgbtGreen;
            image[row][col].rgbtGreen = image[row][(width - col) - 1].rgbtGreen;
            image[row][(width - 1) - col].rgbtGreen = swap_green;

            swap_red = image[row][col].rgbtRed;
            image[row][col].rgbtRed = image[row][(width - col) - 1].rgbtRed;
            image[row][(width - 1) - col].rgbtRed = swap_red;
        }
    }
    return;
}

// Blur image
void blur(int height, int width, RGBTRIPLE image[height][width])
{
    // to avoid altering the original image (from where we take the values) each time an average is calculated, a copy is created
    RGBTRIPLE image_copy[height][width];

    // navigate the 2D array
    for (int row = 0; row < height; row++)
    {
        for (int col = 0; col < width; col++)
        {
            // reload averages' cero values after each iteration (each time a new group of pixels are considered)
            float average_green = 0;
            float average_blue = 0;
            float average_red = 0;

            // reload the denominator for iteration
            float denominator = 0;

            // focus on the area surrounding each pixel
            for (int i = -1; i < 2; i++)
            {
                for (int j = -1; j < 2; j++)
                {
                    // skip border's rows/columns (when they equals to cero/height(width)) in order to avoid memory overflow
                    if (row + i < 0 || col + j < 0 || row + i >= height || col + j >= width)
                    {
                        continue;
                    }
                    else
                    {
                        average_blue += image[row + i][col + j].rgbtBlue;
                        average_green += image[row + i][col + j].rgbtGreen;
                        average_red += image[row + i][col + j].rgbtRed;
                        denominator++;
                    }
                }
            }

            image_copy[row][col].rgbtBlue = round(average_blue / denominator);
            image_copy[row][col].rgbtGreen = round(average_green / denominator);
            image_copy[row][col].rgbtRed = round(average_red / denominator);
        }
    }
    for (int row = 0; row < height; row++)
    {
        for (int col = 0; col < width; col++)
        {
            image[row][col].rgbtBlue = image_copy[row][col].rgbtBlue;
            image[row][col].rgbtGreen = image_copy[row][col].rgbtGreen;
            image[row][col].rgbtRed = image_copy[row][col].rgbtRed;
        }
    }

    return;
}