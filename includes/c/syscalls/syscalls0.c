#include <unistd.h>
#include <stdio.h>
#include <stdlib.h>
#include <limits.h>

int main(void) {

    char hostname[HOST_NAME_MAX + 1];

    if (gethostname(hostname, sizeof(hostname)) == 0 ) {
        printf("Hostname: %s\n", hostname);
    } else {
        perror ("gethostname");
        exit(1);
    }
    printf("Effective user: %d\n", geteuid());
    printf("Process ID: %d\n", getpid());
    printf("Parent process ID: %d\n", getppid());
    exit(0);
}
