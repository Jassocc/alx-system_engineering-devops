#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

/**
 * infinite_while - inf loop
 * Return: 0
 */
int infinite_while(void)
{
	while (1)
	{
		sleep(1);
	}
	return (0);
}
/**
 * main - creates zombie processes
 * Return: inf while loop
 */
int main(void)
{
	int a;
	pid_t ch;

	for (a = 0; a < 5; a++)
	{
		ch = fork();
		if (ch == 0)
		{
			exit(0);
		}
		else
		{
			printf("Zombie process created, PID: %d\n", ch);
		}
	}
	return (infinite_while());
}
