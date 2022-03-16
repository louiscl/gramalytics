% include('webapp/templates/header.tpl')
%#template to generate a HTML table from a list of tuples (or list of lists, or tuple of tuples or ...)

<p>
Add a new Post you liked from 
</p>
<h4>
{{username}}
</h4>

<br><br>
<form >
  <label>Content of post</label><br>
  <input style="width: 200px; height: 100px; border: 1px solid #999999; padding: 5px;" type="text" id="content" name="content" placeholder="Content" required>
  <br><br>
  
  <label>Type of Interaction</label><br>
  <select id="value" name="value">
  <option value="LIKE">LIKE</option>
  <option value="DISLIKE">DISLIKE</option>
  <option value="LOVE">LOVE</option>
  <option value="SAD">SAD</option>
  </select>
  <br><br>
  <input type="submit" name="submit" value="ADD POST">
</form> 
<br>
<a href={{back_link}}>Back</a>