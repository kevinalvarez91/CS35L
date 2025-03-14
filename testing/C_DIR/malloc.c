#include <stdio.h>
#include <stdlib.h> // For malloc and free

int main(){
  int n;

  printf("Enter the number of elements:");
  scanf("%d", &n);

  int *arr = (int *)malloc(n * sizeof(int));

  if (arr == NULL){
    printf("Memory allocation failed\n");
    return 1; // Exit with non-zero status
  }

  printf("Enter %d numbers:\n", n);
  for(int i = 0; i < n; i++){
    scanf("%d", &arr[i]);
  }

    // Modify the array: double each element
    printf("Doubled values:\n");
    for (int i = 0; i < n; i++) {
        arr[i] *= 2;
        printf("%d ", arr[i]);
    }
    printf("\n");

    // Free the allocated memory
    free(arr);

    return 0;

}
