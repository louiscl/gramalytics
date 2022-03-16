% include('webapp/templates/header.tpl')
%#template to generate a HTML table from a list of tuples (or list of lists, or tuple of tuples or ...)

<h4>
Add New User
</h4>

%if response == True:
	<p> {{message}}</p>
%end

<form action="/new_user">
  <label for="fname">Username*</label><br>
  <input type="text" id="username" name="username" placeholder="Username" required>
  <br><br>
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
  <label for="age">Age (optional)</label><br>
  <input type="text" id="age" name="age" placeholder="Age">
  <br><br>
  <input type="submit" name="submit" value="Add User">
</form> 
<br>