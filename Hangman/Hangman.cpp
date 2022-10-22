#include <stdio.h>
#include<stdlib.h>
#include<time.h>
#include<string.h>

void hangman(){
    srand (time (0));
  char words[][20]
    =
    {"appointments","arrangements","commitments","engagements","obligations",
    "agreements","compacts","contracts","covenants","assurances", "guarantees","guaranties","undertakings",
    "bails","bonds","deposits","gages","pawns","securities","tokens", "vicious","vile","villainous","wicked",
    "base","foul","offensive","poison","reprobate","wrong","angry","atrocious","baneful","beastly",
    "calamitous","damnable","depraved","disastrous","execrable","flagitious","harmful","iniquitous","injurious",
      "loathsome","maleficent","malignant","obscene","pernicious","rancorous","repugnant","repulsive","revolting","spiteful","stinking","unpropitious","wrathful"
  };
//Less than letters 5 - 2 spaces
//5-10 letters  : 3 spaces 
//10+ letters : 4 spaces

  char ans[][20]
    =
    { "ap_oi_tme_t_", "a_ra_gem_n_s", "co_m_tm_n_s", "e_g_ _eme_ts","ob_ig_ti_ _s",
    "agr_ _me_ts", "com_a_t_", "Co_ _rac_ t", "cove_a_ t_","a_ _ura_ces","_uara_ _ees", "_ua_a_ _ie_", "u_ _er_akin_ g",
    "ba_l_", "bo_ d _", "_epo_i_ s", "ga_e_", "pa_ n _", "_ecu_i_ies",
    "_oke_ _", "vi_i_u_", "v_l_", "vi_lai_ou_", "_i_ke_","B_s_", "f_u_", "o_fe_ _ive", "p_ _s_n", "rep_o_a_e", "_ro_g", "a_g_y", "a_r_ciou_", "b_n_f_l", "b_a_ t_y",
    "Cal_mi_ou_", "_am_a_le", "_ep_ave_", "di_a _trou_", "e_ec_a_le", "fla_i_iou_", "h_t _f_l", "i_iqui_ou_", "i_jur_ou_",
    "L_a_h_ome", "ma_efice_ _", "mali_ _a_ t", "ob_c_n_", "per_ic_ou_","ra_cor_u_", "rep_ g_a_ _", "r_pul_i_e", "revol_i_ _",
    "_pi_ef_l", "s_i_ki_ g", "u_pr_pit_ou_", "_ra_hf_l"
  };
  char c;
  int len, p, mstke = 0, crrct = 0;
  printf ("WELCOME TO THE HANGMAN GAME\n");
  printf
    ("RULES :\n\t1) YOU ARE ABOUT TO DIE . YOUR LAST CHANCE IS WINNING THIS GAME . FILL IN THE EMPTY WORDS CORRECTLY.\n\t2) AT RANDOM , YOU WILL BE GIVEN A WORD AND IT'S LENGTH. \n\t3) AFTER EACH GUESS \n\t4) THE INDEX OF LETTERS STARTS FROM 0 'ZERO' . \n\t5) CHANCES WILL VARY ACCODRIND TO THE LENGTH OF A WORD . THAT'S IT ! NOW GO SAVE YOUR LIFE.\n\n\t\t\t\t\t\t\t\t ");
//taking any word to play the game . using random function.
  int rndom;
  rndom = rand () % 57;
  puts (ans[rndom]);
  len = strlen (words[rndom]);
  printf ("\nTHE LENGTH OF THE WORD IS : %d\n", len);
  if (len <= 5)
    { 
      printf("YOU HAVE 2 CHANCES ONLY . THEN YOU DIE .\n");
      //first loop ,you get 2 chances 
    while (crrct <= 2|| mstke <= 2)
	{
	  printf
	    ("\nENTER THE POSITION WHERE YOU WANT TO ENTER THE WORD and ENTER THE LETTER : \n");
	  scanf ("%d ", &p);
	  scanf ("%c", &c);
	  if (words[rndom][p] == c)
	    {
	      printf ("correct");
	      ++crrct;
	    }
	  else
	    {
	      printf ("wrong");
	      ++mstke;
	    }
      if(crrct==2){
        printf("\n\t\t\t\t\tYOU HAVE SAVED YOUR LIFE .\n");
        break;
      }
      if(mstke==2){
        printf("\n\t\t\t\t\tYOU DIE, NOW ! \n");
        break;
      }
	}
    }
  else if (len > 5 && len <= 10)
    {
       printf("YOU HAVE 3 CHANCES ONLY . THEN YOU DIE .\n");
      //second loop ,you get 3 chances and 3 spaces
      while (crrct <= 3 || mstke <=3 )
	  {
	  printf
	    ("\nENTER THE POSITION WHERE YOU WANT TO ENTER THE WORD and ENTER THE LETTER : \n");
	  scanf ("%d ", &p);
	  scanf ("%c", &c);
	  if (words[rndom][p] == c)
	    {
	      printf ("correct");
	      ++crrct;
	    }
	  else
	    {
	      printf ("wrong");
	      ++mstke;
	    }
      if(crrct==3){
        printf("\n\t\t\t\t\tYOU HAVE SAVED YOUR LIFE .\n");
        break;
      }
      if(mstke==3){
        printf("\n\t\t\t\t\tYOU DIE, NOW ! \n");
        break;
      }
	  }
    }
    else if (len > 10 )
    {
      printf("YOU HAVE 3 CHANCES ONLY . THEN YOU DIE .\n");
      //third loop ,you get 3 chances and 4 spaces
       while (crrct <= 4 || mstke <=3 )
	{
	  printf
	    ("\nENTER THE POSITION WHERE YOU WANT TO ENTER THE WORD and ENTER THE LETTER : \n");
	  scanf ("%d ", &p);
	  scanf ("%c", &c);
	  if (words[rndom][p] == c)
	    {
	      printf ("correct");
	      ++crrct;
	    }
	  else
	    {
	      printf ("wrong");
	      ++mstke;
	    }
      if(crrct==4){
        printf("\n\t\t\t\t\tYOU HAVE SAVED YOUR LIFE .\n");
        break;
      }
      if(mstke==3){
        printf("\n\t\t\t\t\tYOU DIE, NOW ! \n");
        break;
      }
	}
    }
}
int
main ()
{
    hangman();
  
  return 0;
}
