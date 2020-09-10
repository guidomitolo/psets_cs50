#include <stdio.h>
#include <cs50.h>
#include <string.h>
#include <math.h>

float count_letters(string text);
float count_words(string text);
float count_sentences(string text);

int main(void)
{
    string s = get_string("Text: ");

    float letters = count_letters(s); // a function for each operation
    float words = count_words(s);
    float sentences = count_sentences(s);
    int index;

    index = round(0.0588 * (letters / words) * 100 - 0.296 * (sentences / words) * 100 - 15.8);

    if (index < 1)
    {
        printf("Before Grade 1\n");
    }
    else if (index > 16)
    {
        printf("Grade 16+\n");
    }
    else
    {
        printf("Grade %d\n", index);
    }
}


float count_letters(string text)
{
    float letters = 0;
    for (int i = 0; i < strlen(text); i++)
    {
        if (text[i] >= 32 && text[i] <= 64) // except numbers and special characters
        {
            letters = letters + 0;
        }
        else
        {
            letters++;
        }
    }
    return letters;
}

float count_words(string text)
{
    float words = 1; // in any text there will always be a first word
    for (int i = 0; i < strlen(text); i++)
    {
        if (text[i] == 32) // space
        {
            words++;
        }
    }
    return words;
}

float count_sentences(string text)
{
    float sentences = 1; // in any text there will always be a first sentence
    for (int i = 0; i < strlen(text); i++)
    {
        // dot plus space plus capital letter
        if (text[i] == 46 && text[i + 1] == 32 && text[i + 2] >= 65 && text[i + 2] <= 90)
        {
            sentences ++;
        }
        // closing exclamation mark plus space plus capital letter
        else if (text[i] == 33 && text[i + 1] == 32 && text[i + 2] >= 65 && text[i + 2] <= 90)
        {
            sentences++;
        }
        // closing question mark plus space plus capital letter
        else if (text[i] == 63 && text[i + 1] == 32 && text[i + 2] >= 65 && text[i + 2] <= 90)
        {
            sentences++;
        }
    }
    return sentences;
}