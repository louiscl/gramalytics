% include('webapp/templates/header.tpl')
%#template to generate a HTML table from a list of tuples (or list of lists, or tuple of tuples or ...)

<h3>
Actions
</h3>
<a href="http://localhost:8080/new_user">
<div class="button">
Add User
</div>
</a>
<br>
<h3>
Search for users
</h3>

<form action="/">
  <label for="fname">Username*</label><br>
  <input type="text" id="username" name="username" placeholder="Search for username">
  <br><br>
  <label for="lname">You are following</label><br>
  <select id="following" name="following">
  <option ></option>
  <option value=1>Yes</option>
  <option value=0>No</option>
  </select>
  <br><br>
  <label for="lname">They follow you</label><br>
  <select id="follower" name="follower">
  <option ></option>
  <option value=1>Yes</option>
  <option value=0>No</option>
  </select>
  <br><br>
  <input type="submit" name="submit" value="Search">
</form> 
    <p>{{empty_msg}}</p>
<br>
	%for ele in my_data:
	  <tr>
		<td>
        <div class="userTag">
        <a class="clickable" href={{ele[-1]}} >
        <h4>
        {{ele[0]}}
        </h4>
        </a>
        </td>
		<td class="clickable">
    <a href="{{ele[-1]}}"> View / Edit </a>
    </td><br><br>
		<td class="clickable">
    <a href="{{ele[-2]}}"> Delete </a>
    </td><br><br>
		<td class="clickable">
    <a href="{{ele[-3]}}"> View Liked Posts </a>
    </td> <br><br>
		<td class="clickable">
    <a href="{{ele[-4]}}"> Add Liked Posts </a>
    </td> <br><br>
        </div>
        </br>
	  </tr>
	%end