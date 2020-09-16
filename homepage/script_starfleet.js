function show_info_kirk() {
    document.querySelector('#info').innerHTML =  "<b>James Tiberius \"Jim\" Kirk</b><br><br>A male Human Starfleet officer who lived during the 23rd century. Kirk was arguably one of the most famous and highly decorated starship captains in the history of Starfleet. As the commanding officer of the Constitution-class starships USS Enterprise and USS Enterprise-A, Kirk served United Federation of Planets interests as an explorer, soldier, diplomat, and time traveler.";
}
function show_info_picard() {
    document.querySelector('#info').innerHTML =  "<b>Jean-Luc Picard</b><br><br>A celebrated Starfleet officer, archaeologist, writer, historian and diplomat who served throughout much of the 24th century. The highlights of his career were centered around assignments as commanding officer of the Federation starships USS Stargazer, USS Enterprise-D, and the USS Enterprise-E. In these roles, Picard not only witnessed major turning points of recent galactic history, but played a key role in them also, from making first contact as captain of the Federation\'s flagship with no fewer than 27 alien species, including the Ferengi and the Borg. He also became the chief contact point with the Q Continuum, and served as Arbiter of Succession of the Klingon Empire, where he presided over the investiture of Chancellor Gowron.";
}
function show_info_sisko() {
    document.querySelector('#info').innerHTML =  '<b>Benjamin Lafayette Sisko</b><br><br>A well-known Starfleet officer best remembered for his seven-year assignment commanding station Deep Space 9 in the Bajor sector. After discovering the Bajoran wormhole, he became known to the Bajoran people as the Emissary of the Prophets. He played a critical role as a Starfleet strategist and front line commander in the Dominion War.';
}
function show_info_janeway() {
    document.querySelector('#info').innerHTML =  '<b>Kathryn Janeway</b><br><br>A 24th century Starfleet officer, most noted for her service as captain of the starship USS Voyager. She became the first Federation captain to successfully traverse the Delta Quadrant, encountering dozens of new planets and civilizations over the course of seven years. While there, she and her crew also survived numerous encounters with the Borg. By 2379, she was a vice admiral at Starfleet Command.';
}
function show_info_archer() {
    document.querySelector('#info').innerHTML =  '<b>Jonathan Archer</b><br><br>A 22nd century Human Starfleet officer and captain of Enterprise NX-01, United Earth\'s first full-fledged starship. In that role, he was responsible for greatly expanding United Earth\'s presence in the Alpha and Beta Quadrants and making first contact with more than a dozen species, among them Klingons, Andorians, and Xindi. Considered by historian John Gill, as the "greatest explorer of the 22nd century," Archer is widely credited with saving Earth from the Xindi and paving the way for the founding of the United Federation of Planets. He went on to become one of the Federation\'s earliest presidents.';
}
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