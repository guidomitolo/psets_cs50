document.querySelector('#symbol').onkeyup = function(){
    if (document.querySelector('#symbol').value === '')
    {
        document.querySelector("#submit").disabled = true;
    }
    else{
        document.querySelector("#submit").disabled = false;
    }
};
// function cash_out() {
//     var txt;
//     var r = confirm("Are you sure to cash out?");
//     if (r == true) {
//       txt = "Yes";
//       console.log(txt)
//     } else {
//       txt = "Cancel";
//       console.log(txt)
//     }
// };
