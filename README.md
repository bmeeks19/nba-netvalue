# nbc-netvalue

This repository will be used for figuring out positive EV for NBA games. Currently will use below algorithm but could extend further after testing has been done.

Series Standing - The amount of games +/- that the team has won/loss in the matchup this season


Net_Rating - The difference between the teams offensive and defensive rating


  if 0.0001-3 then 1
  
  if 3.0001-7 then 2
  
  if 7.0001-max then 3
  
  if 0 then 0
  
  if 0.0001-(-3) then -1
  
  if (-3.0001)-(-7) then -2
  
  if (-7.0001)-min then -3
  


Last 10 games - the +/- of the teams last 10 games


Last 50 games - the +/- of the teams last 50 games


random factor - a factor of .15
