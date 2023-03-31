
function alertUser(){
    alert('Thanks for submitting your video!')
}

let checkbox=document.getElementById('checkbox')
let fileInput=document.getElementById('fileInput')
let submitBtn=document.getElementById("submitBtn")

checkbox.addEventListener('change', () => {
    if (checkbox.checked) {
      fileInput.disabled = false;
    } else {
      fileInput.disabled = true;
      submitBtn.disabled = true;
    }
  });
  fileInput.addEventListener('change', () => {
    if (fileInput.value) {
      submitBtn.disabled = false;
    } else {
      submitBtn.disabled = true;
    }
  });