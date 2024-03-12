# nba-netvalue

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

<li>Random Factor - a factor of .15</li>
<li>Home Court - there was a study done that the average home team scores 3 more points than the visitor team. For that reason we will add a small home court factor</li>
</ol>
<br>

<h1><strong>Weights</strong></h1>
<p>The algorithm will multiply the attributes value by the associated weight below </p>
<table>
  <tr>
    <th>Attribute</th>
    <th>Weight</th>
  </tr>
  <tr>
    <td>Series Standing</td>
    <td>0.2</td>
  </tr>
  <tr>
    <td>Net Rating</td>
    <td>0.2</td>
  </tr>
  <tr>
    <td>L10</td>
    <td>0.2</td>
  </tr>
  <tr>
    <td>L50</td>
    <td>0.2</td>
  </tr>
  <tr>
    <td>Probability Random Factor</td>
    <td>0.15</td>
  </tr>
  <tr>
    <td>Home Court Factor</td>
    <td>.05</td>
  </tr>

</table>

