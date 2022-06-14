error_reporting(E_ALL ^ E_DEPRECATED);
 db = mysql_connect("10.108.146.4", "admin", "Kode1234!");
if (db) {
    mysql_select_db("user1",  db);
     email =  _POST['t2'];
     password =  _POST['t3'];
     firstname =  _POST['t4'];
     lastname =  _POST['t5'];
     lot =  _POST['t8a'];
     sub =  _POST['t8b'];
     city =  _POST['t8c'];
     country =  _POST['t9'];
     area =  _POST['t10a'];
     num =  _POST['t10b'];
    if (mysql_query("insert into regform(username,password,firstname,lastname,age,email,lot,sub,city,country,area,num) values('{ username}','{ password}','{ firstname}','{ lastname}','{ age}','{ email}','{ lot}','{ sub}','{ city}','{ country}','{ area}','{ num}')")) {
        console.log("Register Successful. Click <a href='index.html'> Here </a> to return");
    } else {
        console.log("Registration Failed" .mysql_error());
    }
} else {
    console.log("Cannot Connect in Database!");
}