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
let planets = document.querySelector('select');
var earth = document.getElementById('earth');
var vulcan = document.getElementById('vulcan');
var tellar = document.getElementById('tellar');
var andoria = document.getElementById('andoria');
planets.onchange = function()
{
    earth.style.display = '';
    andoria.style.display = '';
    tellar.style.display = '';
    vulcan.style.display = '';
    if (planets.value === 'Earth')
    {
        earth.style.display = 'table-cell';
    }
    else if (planets.value === 'Andoria')
    {
        andoria.style.display = 'table-cell';
    }
    else if (planets.value === 'Vulcan')
    {
        vulcan.style.display = 'table-cell';
    }
    else
    {
        tellar.style.display = 'table-cell';
    }
}