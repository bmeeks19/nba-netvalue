# nbc-netvalue

This repository will be used for figuring out positive EV for NBA games. Currently will use below algorithm but could extend further after testing has been done.



<strong><h1>Key Factors</h1></strong>
<ol>
<li>Series Standing - The amount of games +/- that the team has won/loss in the matchup this season</li>


<li>Net_Rating - The difference between the teams offensive and defensive rating
  <ul>
  <li>if 0.0001-3 then 1</li>

  <li>if 3.0001-7 then 2</li>
  
  <li>if 7.0001-max then 3</li>
    
  <li> if 0 then 0</li>
  
  <li>if 0.0001-(-3) then -1</li>
  
  <li>if (-3.0001)-(-7) then -2</li>
  
  <li>if (-7.0001)-min then -3</li>
  </ul>
</li>

<li>Last 10 games - the +/- of the teams last 10 games</li>


<li>Last 50 games - the +/- of the teams last 50 games</li>

<li>random factor - a factor of .15</li>
</ol>
