var header = document.querySelector("h3")


function getRandomColor() {
  var letters = '0123456789ABCDF';
  var color = '#';
  for (var i = 0; i < 6; i++) {
    color += letters[Math.floor(Math.random() * 16)];
    }
    return color
  }

function changeheadercolor() {
  colorInput = getRandomColor()
  header.style.color = colorInput;
}

setInterval("changeheadercolor()", 600);
