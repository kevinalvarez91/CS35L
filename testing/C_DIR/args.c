#include <stdio.h>
#include <unistd.h>
#include <string.h>
//the parameters for the main function, are set by the C runtime enviorment.
//This is because the main function is special.

void printName(char *name){
  printf("Your name is: %s\n", name);
}

void execute(void (*func)(void)){
  printf("Executing function..\n");
  func(); 
}

void action(){
  printf("Action executed!\n");
}



int main(int argc, char **argv){
  //argc Number of arguments passed
  // argv: Arguments array
  // an array of pointers that point to pointers that point to character
  //char *name = "Kevin Alvarez";
  
  //printf("Name is: %s\n", name); 
  //printf("Number of arguments: %d\n", argc);

    //for (int i = 0; i < argc; i++)
    // printf("Argument %d: %s\n", i, *(argv + i));

  //function pointer
  void (*initalize) (char *);
  char *name = "Kevin";
  initalize = printName;
  initalize(name);

  execute(action);

  
  int opt;
  while(( opt = getopt(argc, argv, "i:o:")) != -1){
    switch(opt){
    case 'i':
      if(strcmp(optarg, "hello") == 0){
	printf("Correct! \n");
      }
      else{
	printf("Incorrect! \n");
      }
      break;
    case 'o':
      printf("option o: %s\n", optarg);
    }
    
  }
  return 0;
}
