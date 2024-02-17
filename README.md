<h1 align="center">Welcome to WalkingApp!</h1> 

<p align="center">
This app keeps track on kilometres traveled on walkes. <br/>
The interface of the App is in Czech language 🇨🇿, I made it primarly for my husband's home use. <br/>
I used Python 🐍 and UI Flet to make this works! For full requirements look below. <br/>
Please feel free to contact me for any tips! 
</p>

<h2 align="center">How to run the App </h2>

<ul>
  <li>Get your copy of the WalkingApp folder with all files and make sure, you have all required libraries.</li>
  <li>Open the main.py on your PyCharm, VS Code etc. and hit run.</li>
  <li>Flet enables to develop mobile apps as well. If you want to test this app on your mobile phone 
      just follow <a href="https://flet.dev/docs/guides/python/testing-on-android">Flet Guide</a>. For now available for Android.  </li>
</ul>

<h2 align="center">About the App </h2>

<ul>
  <li>The main page of the App has some buttons - to choose the date for which you want to save kilometers,   
      the one which opens a <a href="https://mapy.cz">map</a> - (so the user can look for some tourist trail for next walk), exit button and the most important   
      the button to save new records. </li>
</ul>

<p align="center">
<img src="https://github.com/SandraHeinzova/WalkingApp/assets/110200002/d972f8b7-bdc6-40e7-920e-25ccef357c5f" width="125" height="250" hspace="10">
<img src="https://github.com/SandraHeinzova/WalkingApp/assets/110200002/b8009a28-6c43-4a72-b740-3581fbfeed29" width="125" height="250" hspace="10">
<img src="https://github.com/SandraHeinzova/WalkingApp/assets/110200002/7d1edfbf-576c-4faf-ad9e-7b07f15185eb" width="125" height="250">
</p>

<ul>
  <li>The next page is for saving new records. The App asks for kilometeres walked, time duration, amount of calories and number of steps (according to smart watches for example). Also on this page is small table with last 4 records. The Table shows just date and kilometres.The buttons here are exit button, saving button and button which shows overall statistics.</li>
  <li>The last page is with statistics. It shows the total amount of kilometres, the time spent walking, total calories burned and all of the steps.</li>
    <li>The data are stored in sqlite3 database. </li>
</ul>

<p align="center">
<img src="https://github.com/SandraHeinzova/WalkingApp/assets/110200002/798d1867-bfa9-4828-8d61-36f44cd1ac07" width="125" height="250" hspace="10">
<img src="https://github.com/SandraHeinzova/WalkingApp/assets/110200002/3853ca12-27cc-4e33-ad03-ae46711d3a86" width="125" height="250" hspace="10">
</p>

<ul>
  <li>Next to all this in this App there are several Alert Dialogues to prevent ValueErrors and AttributeErrors. Also one Alert Dialogue to confirm   
      successful save and one confirmation for exiting the App.</li>
</ul>

<p align="center">
<img src="https://github.com/SandraHeinzova/WalkingApp/assets/110200002/8f401dd4-3ea0-4038-aa51-ce14871d4b00" width="125" height="250" hspace="10">
<img src="https://github.com/SandraHeinzova/WalkingApp/assets/110200002/733836a2-1ad0-426b-a0b9-c0161d6a1161" width="125" height="250" hspace="10">
<img src="https://github.com/SandraHeinzova/WalkingApp/assets/110200002/4196e4a6-cada-4e95-8c87-0f88b4d86269" width="125" height="250" hspace="10">
</p>


<h2 align="center">Requirements</h2>
<ul>
  <li>Python 3.12.1</li>
  <li>Flet 0.20.0</li>
  <li>sqlite3 library</li>
  <li>re library</li>
  <li>datetime library</li>
  <li>from contextlib contextmanager</li>
  <li>or you can use requirements.txt</li>
</ul>


