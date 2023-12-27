<h1 align="center">Welcome to WalkingApp!</h1> 

<p align="center">
This app keeps track on kilometres traveled on walkes. <br/>
The interface of the App is in Czech language 🇨🇿, I made it primarly for my husband's home use. <br/>
I used Python 🐍 and UI Flet to make this works! For full requirements look below. <br/>
Please feel free to contact me for any tips! 
</p>

<h2 align="center">How to run the App </h2>

<ul>
  <li>Get your copy of the main.py and walking_data.xlsx files and make sure, you have all required libraries.</li>
  <li>Open the main.py on your PyCharm etc. and hit run.</li>
  <li>Flet enables to develop mobile apps as well. If you want to test this app on your mobile phone 
      just follow [Flet Guide](https://flet.dev/docs/guides/python/testing-on-android). For now available for Android.  </li>
</ul>

<h2 align="center">About the App </h2>

<ul>
  <li>This App starts with a loading page. </li>
  <li>After that the user is redirected to the main page of the App. Here are some buttons - to choose the date for which you want to save kilometers,   
      the one which opens the [map](https://mapy.cz/) - (so the user can look for some tourist trail for next walk), exit button and the most important   
      the button to save new records. </li>
</ul>

<p align="center">
<img src="https://github.com/SandraHeinzova/WalkingApp/assets/110200002/848ba28c-388b-4410-aade-41822d21e9f4" width="125" height="250" hspace="10">
<img src="https://github.com/SandraHeinzova/WalkingApp/assets/110200002/c87f7e54-bb66-4f18-abbd-00e45ad34c19" width="125" height="250" hspace="10">
<img src="https://github.com/SandraHeinzova/WalkingApp/assets/110200002/4bf36fe7-da67-47d2-8b61-054e641a84ee" width="125" height="250" hspace="10">
<img src="https://github.com/SandraHeinzova/WalkingApp/assets/110200002/19aeb8e6-4a32-4b69-b3e7-dfbc1642dbbe" width="125" height="250">
</p>

<ul>
  <li>The next page is for saving new records. The App asks for kilometers walked, time duration, amount of calories and number of steps (according to smart watches for example). Also on this page is small table with last 4 records. The Table shows just date and kilometres.The buttons here are exit button, saving button and button which shows overall statistics.</li>
  <li>The last page is with statistics. It shows the total amount of kilometres, the time spent walking, total calories burned and all of the steps.</li>
    <li>The data are stored in xlsx file. </li>
</ul>

<p align="center">
<img src="https://github.com/SandraHeinzova/WalkingApp/assets/110200002/968739ab-6c4c-42c4-b3c4-260038eca959" width="125" height="250" hspace="10">
<img src="https://github.com/SandraHeinzova/WalkingApp/assets/110200002/381f54e1-59e3-4e56-90cb-a2ce5a02fa7e" width="125" height="250" hspace="10">
</p>

<ul>
  <li>Next to all this in this App there are several Alert Dialogues to prevent ValueErrors and AttributeErrors. Also one Alert Dialogue to confirm   
      successful save and one confirmation for exiting the App.</li>
</ul>

<p align="center">
<img src="https://github.com/SandraHeinzova/WalkingApp/assets/110200002/ec14b446-a415-4d73-b257-2bd51d60e48b" width="125" height="250" hspace="10">
<img src="https://github.com/SandraHeinzova/WalkingApp/assets/110200002/d15a0a31-801c-4fbb-851f-48bc8f34ab4f" width="125" height="250" hspace="10">
<img src="https://github.com/SandraHeinzova/WalkingApp/assets/110200002/a3a15230-579c-4fc5-a006-6b7c69b05a78" width="125" height="250" hspace="10">
</p>

<h2 align="center">Requirements</h2>
<ul>
  <li>Python 3.12.1</li>
  <li>Flet 0.17.0</li>
  <li>openpyxl library</li>
  <li>time library</li>
  <li>datetime library</li>
</ul>


