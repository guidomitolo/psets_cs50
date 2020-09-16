function greet()
{
    alert("Welcome to the Federation Database");
}
var pic = document.getElementById("headquarters");
function rotate(){
    if (pic.src === 'https://6b9b32b4-b01b-4a22-aa21-57d312ebe3c1-ide.cs50.xyz:8080/images/headquarters_1.png')
    {
        pic.src = 'images/headquarters_2.png';
    }
    else if (pic.src === 'https://6b9b32b4-b01b-4a22-aa21-57d312ebe3c1-ide.cs50.xyz:8080/images/headquarters_2.png')
    {
        pic.src = 'images/headquarters_3.png';
    }
    else if (pic.src === 'https://6b9b32b4-b01b-4a22-aa21-57d312ebe3c1-ide.cs50.xyz:8080/images/headquarters_3.png')
    {
        pic.src = 'images/headquarters_4.png';
    }
    else
    {
        pic.src='images/headquarters_1.png';
    }
}
setInterval(rotate,3000);
function show_star(){
    document.getElementById('nav_subbar_star').style.display = 'table';
}
function hide_star(){
    document.getElementById('nav_subbar_star').style.display = '';
}
function show_mem(){
    document.getElementById('nav_subbar_mem').style.display = 'table';
}
function hide_mem(){
    document.getElementById('nav_subbar_mem').style.display = '';
}