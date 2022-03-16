% include('webapp/templates/header.tpl')

<h3>
	User Info
</h3>

<div style="width:50%;display:flex;flex-direction:column;align-items:flex-start">
  <p>Username: {{user_data[0]}}</p>
  <p>Link: {{user_data[1]}}</p>
  <p>Age: {{user_data[2]}}</p>
  <p>Following: {{user_data[3]}}</p>
  <p>Follower: {{user_data[4]}}</p>
</div>
<h3>
	Update User
</h3>
<form >
  <label for="lname">Are you following?</label><br>
  <select id="following" name="following" required>
  <option value=1>Yes</option>
  <option value=0>No</option>
  </select>
  <br><br>
  
  <label for="lname">He/she following back?</label><br>
  <select id="follower" name="follower">
  <option value=1>Yes</option>
  <option value=0>No</option>
  </select>
  <br><br>
  <label for="age">Age</label><br>
  <input type="text" id="age" name="age" value={{user_data[2]}} placeholder="Age">
  <br><br>
  <input type="submit" name="submit" value="UPDATE USER">
</form> 