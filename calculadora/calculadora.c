#include <stdio.h>
#include <stdlib.h>
#include <ctype.h>
#include <string.h>
#include <assert.h>
#include "calculadora.h"

arrTokens_t *lexer(const char *input)
{
    arrTokens_t *expressao = (arrTokens_t *)malloc(sizeof(arrTokens_t));
    expressao->tokens = (Token_t *)malloc(INPUT_TAMANHO * sizeof(Token_t));
    expressao->temMult = 0;
    int i = 0;
    int posicao = 0;
    while (input[i])
    {
        char c = input[i];
        if (isdigit(c))
        {

            char *endptr = NULL;
            expressao->tokens[posicao].tipo = NUMERO;
            expressao->tokens[posicao].valor = strtoll(input + i, &(endptr), 10);
            posicao++;
            if (endptr != 0)
            {
                i += endptr - (input + i);
            }
            continue;
        }
        if (c == '+')
        {
            expressao->tokens[posicao].tipo = MAIS;
            posicao++;
        }
        else if (c == '-')
        {
            expressao->tokens[posicao].tipo = MENOS;
            posicao++;
        }
        else if (c == '*')
        {
            expressao->tokens[posicao].tipo = VEZES;
            posicao++;
        }
        else
        {
            if (input[i] != ' ')
            {
                expressao->tokens[0].tipo = FIM;
                break;
            }
        }
        i++;
    }
    expressao->tokens[posicao].tipo = FIM;
    return expressao;
}

// int parserMult(const arrTokens_t *expressao, long long int *numero)
// {
//     if (expressao->temMult == 0)
//         return -1;
//     int flagPrimeiro = 1;
//     int posicao = 1;
//     int resultado;
//     while (expressao->tokens[0].tipo != FIM)
//     {
//         if (expressao->tokens[posicao].tipo == VEZES)
//         {
//             if (flagPrimeiro == 1)
//             {
//                 if (expressao->tokens[posicao - 1].valor != NUMERO)
//                 {
//                     printf("Input Invalido\n");
//                     return 0;
//                 }
//                 resultado = expressao->tokens[posicao - 1].valor;
//             }
//             posicao++;
//             if (expressao->tokens[posicao].tipo != NUMERO)
//             {
//                 printf("Input Invalido\n");
//                 return 0;
//             }
//             resultado *= expressao->tokens[posicao].valor;

//         }
//     }
// }

int parser(const arrTokens_t *expressao, long long int *numero)
{
    if (expressao->tokens[0].tipo != NUMERO)
    {
        printf("Input Invalido\n");
        return 0;
    }
    long long int resultado = expressao->tokens[0].valor;
    int posicao = 1;
    while (expressao->tokens[posicao].tipo != FIM)
    {

        if (expressao->tokens[posicao].tipo == MAIS)
        {
            posicao++;
            if (expressao->tokens[posicao].tipo != NUMERO)
            {
                printf("Input Invalido\n");
                return 0;
            }
            resultado += expressao->tokens[posicao].valor;
            posicao++;
        }
        else if (expressao->tokens[posicao].tipo == MENOS)
        {
            posicao++;
            if (expressao->tokens[posicao].tipo != NUMERO)
            {
                printf("Input Invalido\n");
                return 0;
            }
            resultado -= expressao->tokens[posicao].valor;
            posicao++;
        }
        else
        {
            printf("Input Invalido\n");
            return 0;
        }
    }
    *numero = resultado;
    return 1;
}

void assembly(const arrTokens_t *expressao)
{
    assert(expressao->tokens[0].tipo == NUMERO);
    printf("Load %lld\n", expressao->tokens[0].valor);
    for (int i = 1; expressao->tokens[i].tipo != FIM; i++)
    {
        if (expressao->tokens[i].tipo == MAIS)
        {
            printf("Add %lld\n", expressao->tokens[++i].valor);
        }
        else
        {
            printf("Sub %lld\n", expressao->tokens[++i].valor);
        }
    }
}

int main(void)
{
    printf("Expressao matematica sem parentises (soma ou subtracao): ");
    char input[INPUT_TAMANHO];
    if (fgets(input, INPUT_TAMANHO, stdin) != NULL)
    {
        size_t len = strlen(input);
        if (len > 0 && input[len - 1] == '\n')
        {
            input[--len] = '\0';
        }
    }

    arrTokens_t *expressao = lexer(input);
    long long int resultado;

    if (parser(expressao, &resultado) == 1)
    {
        printf("resultado: %lld\n", resultado);
        assembly(expressao);
    }

    free(expressao->tokens);
    free(expressao);

    return EXIT_SUCCESS;
}