/* Tic Tac Toe */
/* 2 Players */
/* Copyrights Sushan Shakya */

#include<stdio.h>
#include<conio.h>

typedef struct Player{
	char mark;
	int playerId;
}Player;

void initializeBoard(char (*board)[3]) {
	char items[3][3] = {{'1','2','3'},{'4','5','6'},{'7','8','9'},};
	for(int r = 0; r<3; r++)
		for(int c = 0; c<3; c++)
			*(*(board + r) +c) = items[r][c];	
			
}

void printBoard(char (*board)[3]) {
	printf("\n\n\n");
	for(int r = 0; r<3; r++) {
		printf("\t");
		for(int c = 0; c<3; c++){
			printf(" %c ",*(*(board + r) +c));
			if(c < 2)
				printf("|");
		}
			
		printf("\n");
		if(r < 2) 
			printf("\t-----------\n");
	}
	printf("\n\n\n");
}

void printWelcomeMessage() {
	printf("Welcome to Tic Tac Toe\n");
}

void printWinner(char item) {
	if(item == 'X')
		printf("Player 2 Wins !!\n");
	else
		printf("Player 1 Wins !!\n");
}

int checkFirst3Cases(char (*board)[3]) {
//	00 01 02 
//	or 
//	10 11 12 
//	or 
//	20 21 22 
	int win = 0;

	for(int r = 0; r<3; r++){
		int same = 1;
		char item = *(*(board + r) + 0);
		for(int c = 1; c<3 ; c++) {
			if(*(*(board + r) + c) == item){
				continue;
			}else{				
				same = 0;
				break;
			}
		}	
		if(same) {
			printWinner(item);
			win = 1;
			break;
		}
	}
	
	if(win) return 1;
	
	return 0;
}

int checkSecondCase(char (*board)[3]) {

//	00 11 22
	int same = 1;
	char item = *(*(board + 0) + 0);
	
	for(int i = 0; i<3; i++) {		
		
		if(*(*(board + i) + i) == item){
				continue;
		}else{
			same = 0;
			break;
		}
	}
	
	if(same) {
		printWinner(item);
		
		return 1;
	} 
	
	return 0;
}

int checkThirdCase(char (*board)[3]) {	
//	02 11 20
	int var = 1;
	char item = *(*(board + 0) + 2);
	
	for(int r = 0; r<3 ; r++) {
		if(*(*(board + r) + 2 - r) == item){
				continue;
		}else{
			var = 0;
			break;
		}
	}
	
	if(var) {
		printWinner(item);
		
		return 1;
	} 
	
	return 0;
}

int checkForthCases(char (*board)[3]) {
//	00 10 20
//	or
//	01 11 21
//	or
//	02 12 22

	int win = 0;

	for(int r = 0; r<3; r++){
		int same = 1;
		char item = *(*(board + 0) + r);
		for(int c = 1; c<3 ; c++) {
			if(*(*(board + c) + r) == item){
				continue;
			}else{				
				same = 0;
				break;
			}
		}	
		if(same) {
			printWinner(item);
			win = 1;
			break;
		}
	}
	
	if(win) return 1;
	
	return 0;
	
}


int win(char (*board)[3]) {

	int a = checkFirst3Cases(board);
	
	int b = checkSecondCase(board);
	
	int c = checkThirdCase(board);
	
	int d = checkForthCases(board);

	if(a || b || c || d) return 1;

	return 0;
}


int tie(char (*board)[3]) {
	// If none of the parts has numbers its a tie
	
	int tie = 1;
	char items[3][3] = {{'1','2','3'},{'4','5','6'},{'7','8','9'},};
	
	for(int r = 0; r<3; r++){
		int flag = 0;
		for(int c = 1; c<3 ; c++) {
			if(*(*(board + r) + c) == items[r][c])
				flag = 1;							
		}
		if(flag) {
			tie = 0;
			break;
		}		
	}
	
	if(tie) {
		printf("It is a tie ! \n");
	}
	
	return tie;
}

int changeBoardState(char (*board)[3], char choice, char mark) {
	int flag = 0;
	for(int r = 0 ; r < 3; r++) {
		for(int c = 0; c<3; c++) {
			if(*(*(board + r) +c) == choice) {
				*(*(board + r) +c) = mark;
				flag = 1;
				break;
			}
		}
		if(flag == 1) break;
	}
	return flag;
}


int main(void) {
	while(1) {
		Player player1 = {'O', 1};
		Player player2 = {'X', 2};
		
		char board[3][3];
		
		char p1Choice;
		char p2Choice;
		
		initializeBoard(board);
		
		printWelcomeMessage();
	
		printBoard(board);
		
		while(1) {
			while(1) {
				printf("Player 1\'s Turn : ");
				scanf(" %c", &p1Choice);
			
				if(changeBoardState(board,p1Choice, player1.mark)) {
					break;
				}else{
					printf("Invalid Move ! \n");
				}
			}
			
			printBoard(board);
			
			if(win(board) || tie(board)) break;
			
			while(1) {
				printf("Player 2\'s Turn : ");
				scanf(" %c", &p2Choice);
			
				if(changeBoardState(board,p2Choice, player2.mark)) {
					break;
				}else{
					printf("Invalid Move ! \n");
				}
			}
			printBoard(board);	
			
			if(win(board) || tie(board)) break;
		}
		
		char decision;
		
		printf("Do you want to play again ? (y/n) ");
		scanf(" %c", &decision);
		
		if(decision == 'y') continue;
		else break;
	}	
	
	return 0;
}
