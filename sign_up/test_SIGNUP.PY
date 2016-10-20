<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="en" lang="en">
<head profile="http://selenium-ide.openqa.org/profiles/test-case">
<meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />
<link rel="selenium.base" href="https://fkstableosg.fuhu.org/" />
<title>New Test</title>
</head>
<body>
<table cellpadding="1" cellspacing="1" border="1">
<thead>
<tr><td rowspan="1" colspan="3">New Test</td></tr>
</thead><tbody>
<tr>
	<td>open</td>
	<td>/</td>
	<td></td>
</tr>
<!--//SIGN UP-->
<tr>
	<td>open</td>
	<td>/checkout/premium/sign-up/</td>
	<td></td>
</tr>
<tr>
	<td>storeEval</td>
	<td>Math.round (Math.random() * 1357)</td>
	<td>random</td>
</tr>
<tr>
	<td>storeEval</td>
	<td>&quot;qa.testk+sel_${random}@gmail.com&quot;</td>
	<td>strEmail</td>
</tr>
<tr>
	<td>type</td>
	<td>email</td>
	<td>${strEmail}</td>
</tr>
<tr>
	<td>type</td>
	<td>id=password</td>
	<td>bbbbbb</td>
</tr>
<tr>
	<td>clickAndWait</td>
	<td>id=continue</td>
	<td></td>
</tr>
<!--//SIGN OUT-->
<tr>
	<td>open</td>
	<td>/sign-in</td>
	<td></td>
</tr>
<tr>
	<td>clickAndWait</td>
	<td>link=Sign Out</td>
	<td></td>
</tr>
</tbody></table>
</body>
</html>
