

int main(int argc, char *argv[]) {
  int opt;
  int verbose = 0;
  char *filename = NULL; 
  while ((opt = getopt(argc, argv, "vo:")) != -1){
    switch (opt) {
    case 'v':
      verbose = 1;
      break;
    case 'o':
      filename = optarg;
      break;
    case '?':
      fprintf(stderr, "Invalid arument!\n");
      return 1;
    }
  }

  if (verbose){
    fprintf(stderr, "verbose");}
  
  if (filename != NULL){
      fprintf(stderr, "filename: %s\n", filename)
  }
  
  while(1) {
    


    
  }

  
}
