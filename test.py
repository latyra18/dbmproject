#print ("Hello World")

#write-html

#connect db

import mysql.connector

config = {
  'user': 'root',
  'password': 'april2000',
  'host': 'localhost',
  'database' : 'panthergrill',
  'raise_on_warning': True,
}
link = mysql.connector.connect(**config)


f = open('pgrillhome.html','wb')

message = """<html>

<!-- This is the css template I found to help format the form-->
<head>
<meta name="viewport" content="width=device-width, initial-scale=1">
<style>
body {
  font-family: Arial, Helvetica, sans-serif;
  background-color: white;
}
* {
  box-sizing: border-box;
}
.sform {
  padding: 16px;
  background-color: white;
}
input[type=text], input[type=password] {
  width: 100%;
  padding: 15px;
  margin: 5px 0 22px 0;
  display: inline-block;
  border: none;
  background: #f1f1f1;
}
input[type=text]:focus, input[type=password]:focus {
  background-color: #ddd;
  outline: none;
}
hr {
  border: 1px solid #f1f1f1;
  margin-bottom: 25px;
}
.subbtn {
  background-color: #663399;
  color: white;
  padding: 16px 20px;
  margin: 8px 0;
  border: none;
  cursor: pointer;
  width: 100%;
  opacity: 0.9;
}
.registerbtn:hover {
  opacity: 1;
}
a {
  color: dodgerblue;
}
.signin {
  background-color: #f1f1f1;
  text-align: center;
}
</style>
</head>
<body>    

    <!-- This is the start of the form fields for the sign in form-->
    <form action="data.php">
        <div class="sform">
            <h1>Sign in</h1>
            <p>Sign in to your account</p>
            <hr>
            <label for="uname"><b>Username</b></label>            
            <input type="text" placeholder="Enter Username" name="uname" id="uname" required>

            <label for="psw"><b>Password</b></label>
            <input type="password" placeholder="Enter Password" name="psw" id="psw" required>

            <button type="submit" class="subbtn"> Sign In</button>
        </div>

        <div class="noaccount">
            <p>  Don't have an account? <a href="regform.html">Register Now!</a></p>
        </div>
    </form>

</body>
</html>"""


#write message
f.write(message)
f.close()