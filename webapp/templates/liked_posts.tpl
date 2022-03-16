% include('webapp/templates/header.tpl')

<p>
Liked Posts from
</p>
<h4>
 {{username}}
</h4>

<a href= {{add_link}}>
	<div class="button">
    <h4> Add New Liked Post</h4>
	</div>
</a><br><br>

% if len(liked_posts) == 0:
    <p> You haven't liked any posts from {{username}} yet </p>
% end
	%from datetime import datetime
	%for ele in liked_posts:
	  <tr>
		<td>Reaction: {{ele[2]}}</td><br>
		<td>Content: {{ele[3]}}</td><br>
		<td>Time: {{datetime.fromtimestamp(ele[4])}}</td><br>
	  </tr><br><br>
	%end