#include <stdio.h>
#include <stdlib.h>

#define ROWS 10
#define COLS 8

void dfs(int matrix[ROWS][COLS], int visited[ROWS][COLS], int row, int col) {
    if (row < 0 || row >= ROWS || col < 0 || col >= COLS || matrix[row][col] == 0 || visited[row][col]) {
        return;
    }

    visited[row][col] = 1;

    dfs(matrix, visited, row + 1, col);
    dfs(matrix, visited, row - 1, col);
    dfs(matrix, visited, row, col + 1);
    dfs(matrix, visited, row, col - 1);
}

int countAreas(int matrix[ROWS][COLS]) {
    int visited[ROWS][COLS] = {0};
    int count = 0;

    for (int i = 0; i < ROWS; i++) {
        for (int j = 0; j < COLS; j++) {
            if (matrix[i][j] == 1 && !visited[i][j]) {
                count++;
                dfs(matrix, visited, i, j);
            }
        }
    }

    return count;
}

int main(void) {
    int matrix[ROWS][COLS] = {{0, 0, 0, 0, 0, 0, 0, 0},
                              {0, 1, 1, 0, 0, 0, 0, 0},
                              {0, 1, 1, 0, 0, 0, 0, 0},
                              {0, 1, 1, 0, 0, 0, 0, 0},
                              {0, 1, 1, 0, 0, 0, 1, 0},
                              {0, 1, 1, 0, 0, 0, 1, 0},
                              {0, 1, 1, 0, 0, 0, 1, 1},
                              {0, 1, 1, 0, 0, 0, 0, 0},
                              {0, 1, 1, 0, 0, 0, 0, 0},
                              {0, 0, 0, 0, 0, 0, 0, 0}};

    int areaCount = countAreas(matrix);
    printf("Cantidad de areas con 1 en la matriz: %d\n", areaCount);

    return 0;
}

