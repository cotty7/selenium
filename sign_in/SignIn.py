<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="en" lang="en">
<head profile="http://selenium-ide.openqa.org/profiles/test-case">
<meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />
<link rel="selenium.base" href="https://www.nabitablet.com/sign-in" />
<title>SignIn</title>
</head>
<body>
<table cellpadding="1" cellspacing="1" border="1">
<thead>
<tr><td rowspan="1" colspan="3">SignIn</td></tr>
</thead><tbody>
<tr>
	<td>open</td>
	<td>/sign-in</td>
	<td></td>
</tr>
<tr>
	<td>type</td>
	<td>id=id_email</td>
	<td>ktest123@gmail.com</td>
</tr>
<tr>
	<td>type</td>
	<td>id=id_password</td>
	<td>123456</td>
</tr>
<tr>
	<td>clickAndWait</td>
	<td>css=input[type=&quot;submit&quot;]</td>
	<td></td>
</tr>
<tr>
	<td>click</td>
	<td>css=a.gear &gt; img</td>
	<td></td>
</tr>
<tr>
	<td>click</td>
	<td>link=Log Out</td>
	<td></td>
</tr>

</tbody></table>
</body>
</html>