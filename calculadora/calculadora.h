#ifndef __CALCULADORA_H__
#define __CALCULADORA_H__

#define INPUT_TAMANHO 256

#define TRUE 1

#define FALSE 0

enum _tipo_
{
    MAIS,
    // MERDAPARAMEAJUDAR,
    MENOS,
    NUMERO,
    VEZES,
    FIM

};

// typedef struct
// {
//     int posicao;
//     mult_t *prox;
// } mult_t;

typedef struct
{
    enum _tipo_ tipo;
    long long int valor;
} Token_t;

typedef struct
{
    Token_t *tokens;
    // mult_t* mutiplicacoes;
    int temMult;
} arrTokens_t;

#endif