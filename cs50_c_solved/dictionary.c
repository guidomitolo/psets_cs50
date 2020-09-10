// task resolved by guido mitolo

// Implements a dictionary's functionality
#include <stdbool.h>

#include "dictionary.h"

// Added libraries
#include <strings.h>
#include <stdlib.h>
#include <stdint.h>
#include <stdbool.h>
#include <stdio.h>
#include <string.h>
#include <ctype.h>

// Represents a node in a hash table
typedef struct node
{
    char word[LENGTH + 1];
    struct node *next;
}
node;

// Number of buckets in hash table = letters of the english alphabet
const unsigned int N = 26;

// Hash table
node *table[N];

// Returns true if word is in dictionary else false
bool check(const char *word)
{
    // to look through the list first i need to know the bucket
    int bucket = hash(word);
    node *tmp = table[bucket];

    // iterate until null
    while (tmp != NULL)
    {
        // return true if match
        if (strcasecmp(tmp->word, word) == 0)
        {
            return true;
        }
        tmp = tmp->next;
    }
    return false;
}

// Hashes word to a number
unsigned int hash(const char *word)
{
    int sum = 0;
    int code = 0;

    for (int i = 0; word[i] != '\0'; i++)
    {
        // all characters to lowercase (to keep the same hash number no matter the case)
        code = tolower(word[i]);
        sum += code;
    }
    return sum % N;
}

// Loads dictionary into memory, returning true if successful else false
bool load(const char *dictionary)
{
    FILE *dict = fopen(dictionary, "r");
    if (!dict)
    {
        return false;
    }

    // buffer for strings out of dictionary
    char string[LENGTH + 1];
    // index for the hast table
    int bucket;

    while (fscanf(dict, "%s", string) != EOF)
    {

        // memory allocation for the new node
        node *n = malloc(sizeof(node));
        // check if there is enough memory for the new node
        if (n == NULL)
        {
            return false;
        }
        n->next = NULL;
        strcpy(n->word, string);

        // get the num. of the bucket for the current word
        bucket = hash(n->word);

        // create the head of the link list in an empty bucket
        if (table[bucket] == NULL)
        {
            table[bucket] = n;
            n->next = NULL;
        }
        else
        {
            // always insert the new node at the head of the list
            n->next = table[bucket]; // the new node next pointer takes the pointer of the head
            table[bucket] = n; // the head takes the value of the new node
        }
    }
    fclose(dict);
    return true;
}

// Returns number of words in dictionary if loaded else 0 if not yet loaded
unsigned int size(void)
{
    int count = 0;
    node *tmp;

    for (int i = 0; i < N; i++)
    {
        // tmp node takes the place of the head of each linked-list
        tmp = table[i];
        // tmp navigates through the nodes of each linked-list
        while (tmp != NULL)
        {
            tmp = tmp->next;
            count++;
        }
    }
    free(tmp);
    return count;
}

// Unloads dictionary from memory, returning true if successful else false
bool unload(void)
{
    node *tmp;

    for (int i = 0; i < N; i++)
    {
        // cursor node takes the place of the head of each linked-list
        node *cursor = table[i];
        // cursor navigates through the nodes of each linked-list
        while (cursor != NULL)
        {
            tmp = cursor;
            cursor = cursor->next;
            free(tmp);
        }
    }
    return true;
}
