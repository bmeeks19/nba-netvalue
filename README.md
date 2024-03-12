# nbc-netvalue

This repository will be used for figuring out positive EV for NBA games. Currently will use below algorithm but could extend further after testing has been done.



<strong><h1>Key Factors</h1></strong>
<ol>
<li>Series Standing - The amount of games +/- that the team has won/loss in the matchup this season</li>


<li>Net_Rating - The difference between the teams offensive and defensive rating<br><br>
  <table>
  <tr>
    <th>Net Rating Range</th>
    <th>Value</th>
  </tr>
  <tr>
    <td>-7.001 to min</td>
    <td>-3</td>
  </tr>
  <tr>
    <td>-3.001 to -7</td>
    <td>-2</td>
  </tr>
  <tr>
    <td>-.001 to -3</td>
    <td>-1</td>
  </tr>
  <tr>
    <td>0</td>
    <td>0</td>
  </tr>
  <tr>
    <td>.001 to 3</td>
    <td>1</td>
  </tr>
  <tr>
    <td>3.001 to 7</td>
    <td>2</td>
  </tr>
  <tr>
    <td>7.001 to max</td>
    <td>3</td>
  </tr>
  </table>
</li>
<br>

<li>Last 10 games - the +/- of the teams last 10 games</li>


<li>Last 50 games - the +/- of the teams last 50 games</li>

<li>random factor - a factor of .15</li>
</ol>
