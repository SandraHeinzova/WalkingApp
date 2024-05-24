<h1 align="center">Welcome to WalkingApp!</h1> 

<p align="center">
This app keeps track on kilometres traveled on walkes. <br/>
The interface of the App is in Czech language 🇨🇿, I made it primarly for my husband's home use. <br/>
I used Python 🐍 and UI Flet to make this works! For full requirements look below. <br/>
Please feel free to contact me for any tips or recomendations! 
</p>

<p align="center">Free Youtube Demo how the app looks like and work here - <a href="https://www.youtube.com/watch?v=D8G5DumpMMg">WalkingApp Demo</a></p>

<h2 align="center">How to run the App </h2>

<ul>
  <li>Get your copy of the WalkingApp folder with all files and make sure, you have all required libraries.</li>
  <li>Open the main.py on your PyCharm, VS Code etc. and hit run.</li>
  <li>Flet enables to develop mobile apps as well. If you want to test this app on your mobile phone 
      just follow <a href="https://flet.dev/docs/guides/python/testing-on-android">Flet Guide</a>. For now available for Android.  </li>
  <li>Now is also possible to make .apk, just follow these instructions on <a href="https://flet.dev/docs/guides/python/packaging-app-for-distribution/#flet-build-apk">Flet Packaging app for distribution page</a> or you can write me, I will try to help.</li>
</ul>

<h2 align="center">About the App </h2>

<ul>
  <li>The home page of the App has welcome text, four containers - to display statistics for current month and a button, that opens a <a href="https://mapy.cz">map</a> - (so the user can look for some tourist trail for next walk)</li>
</ul>

<p align="center">
<img src="https://github.com/SandraHeinzova/WalkingApp/assets/110200002/840dcbc4-6d3b-43fd-a694-88c8223c66b0" width="125" height="250" hspace="10">
<img src="https://github.com/SandraHeinzova/WalkingApp/assets/110200002/b8009a28-6c43-4a72-b740-3581fbfeed29" width="125" height="250" hspace="10">
</p>

<ul>
  <li>The next page is for saving new records. The user can choose the date with the DatePicker and the App asks for kilometeres walked, time duration, amount of calories and number of steps (according to smart watches for example). Also on this page is small table with last 4 records. The Table shows just date and kilometres.</li>
  <li>The last page is with statistics. It shows the total amount of kilometres, the time spent walking, total calories burned and all of the steps.</li>
    <li>The data are stored in sqlite3 database. </li>
</ul>

<p align="center">
<img src="https://github.com/SandraHeinzova/WalkingApp/assets/110200002/1182861a-79ea-4a1e-9e62-23207f0b7c17" width="125" height="250">
<img src="https://github.com/SandraHeinzova/WalkingApp/assets/110200002/f18cc394-5385-45ff-896e-b30164578830" width="125" height="250" hspace="10">
<img src="https://github.com/SandraHeinzova/WalkingApp/assets/110200002/9ded20f2-7ff2-4b3f-818b-f0e1cb775114" width="125" height="250" hspace="10">
</p>

<ul>
  <li>Next to all this in this App there are several Alert Dialogues to prevent ValueErrors and AttributeErrors. Also one Alert Dialogue to confirm   
      successful save and one confirmation for exiting the App.</li>
</ul>

<p align="center">
<img src="https://github.com/SandraHeinzova/WalkingApp/assets/110200002/b2e17279-5736-4e66-abc4-c3a35239da0f" width="125" height="250" hspace="10">
<img src="https://github.com/SandraHeinzova/WalkingApp/assets/110200002/0890f8d8-d080-4491-9bdb-218b773f6e05" width="125" height="250" hspace="10">
<img src="https://github.com/SandraHeinzova/WalkingApp/assets/110200002/77cd39d4-49bd-4112-b6d5-2983c00369f8" width="125" height="250" hspace="10">
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


