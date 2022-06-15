function getText()
    {
        var sub = true ;
        var name = document.getElementById("t1").value;
        if(name.length < 8 || name.length > 50)
        {
        sub=false;
            alert("Invalid Username, must be 8 - 10 characters!");
            document.getElementById("sample").innerHTML="*";
        }
        else
        {                   
            document.getElementById("sample").innerHTML = name;

        }

        var pass = document.getElementById("t2").value;
        if(pass.length < 8 || pass.length > 50)
        {
        sub=false;
            alert("Invalid Password, must be 8 - 10 characters!");
            document.getElementById("sample2").innerHTML="*";
        }
        else
        {                   

            sub=true;
        }

        var rpass = document.getElementById("t3").value;
        if(rpass !== pass)
        {
        sub=false;
            alert("Password dont match!");
            document.getElementById("sample3").innerHTML="*";
        }
        else
        {   
            sub=true;
        }

        var fname = document.getElementById("t4").value;
            if(fname.length<5||fname.length>15)
            {
            sub=false;
                alert("Invalid firstname, must be 5 - 15 characters!");
            }
        else
            {                       
                document.getElementById("sample11").innerHTML = fname;

            }

        var lname = document.getElementById("t5").value;
            if(lname.length<5||lname.length>15)
            {
            sub=false;
                alert("Invalid lastname, must be 5 - 15 characters!");
            }
        else
            {                       
                document.getElementById("sample12").innerHTML = lname;

            }

        var age = parseInt(document.getElementById("t2").value);
        if(age < 18)
        {
        sub=false;
            alert("Minors not allowed.");
        }
        else
            {                   
                document.getElementById("sample4").innerHTML = age;

            }
        var email = document.getElementById("t7").value;
            if(email.length < 8 || email.length > 50)
        {
        sub=false;
            alert("Invalid Email, must be 8 - 50 characters!");
            document.getElementById("sample2").innerHTML="*";
        }
        else
        {                   

            sub=true;
        }
        var lotnum = document.getElementById("t8a").value;
            if(lotnum.length<3||lotnum.length>10)
            {
            sub=false;
                alert("Location Invalid.");
            }
        else
            {                       
                document.getElementById("sample13").innerHTML = lotnum;

            }

        var sub = document.getElementById("t8b").value;
            if(sub.length<5||sub.length>10)
            {
            sub=false;
                alert("Location Invalid.");
            }
        else
            {                       
                document.getElementById("sample14").innerHTML = sub;

            }

        var city = document.getElementById("t8c").value;
            if(city.length<5||city.length>10)
            {
            sub=false;
                alert("Location Invalid.");
            }
        else
            {                       
                document.getElementById("sample15").innerHTML = city;

            }

        var country = document.getElementById("t9").value;
            if(country.length<3||country.length>30)
            {
            sub=false;
                alert("Location Invalid.");
            }
        else
            {                       
                document.getElementById("sample16").innerHTML = country;

            }

        var area = parseInt(document.getElementById("t10a").value);
            if(area.length<3||area.length>8)
            {
            sub=false;
                alert("Invalid Area Code, must be 3 - 8 digits!")
            }
        else
            {                       
                document.getElementById("sample16").innerHTML = area;

            }
        var telnum = parseInt(document.getElementById("t10b").value);
            if(telnum.length<10||telnum.length>12)
            {
            sub=false;
                alert("Invalid Number!");
            }
        else
            {                       
                document.getElementById("sample16").innerHTML = telnum;

            }
        if(sub === false)
        {
            return false;
        }

    }