// add hovered class to selected list item
let list = document.querySelectorAll(".navigation li");

function activeLink() {
  list.forEach((item) => {
    item.classList.remove("hovered");
  });
  this.classList.add("hovered");
}

list.forEach((item) => item.addEventListener("mouseover", activeLink));

// Menu Toggle
let toggle = document.querySelector(".toggle");
let navigation = document.querySelector(".navigation");
let main = document.querySelector(".main");

toggle.onclick = function () {
  navigation.classList.toggle("active");
  main.classList.toggle("active");
};

// Accept and Reject Button

function acceptAction(button) {
  var row = button.parentNode.parentNode;
  var acceptButton = row.querySelector(".button-accept");
  var rejectButton = row.querySelector(".button-reject");

  acceptButton.innerHTML = "Accepted";
  acceptButton.classList.add("accepted");
  rejectButton.style.display = "none";
}

function rejectAction(button) {
  var row = button.parentNode.parentNode;
  var acceptButton = row.querySelector(".button-accept");
  var rejectButton = row.querySelector(".button-reject");

  rejectButton.innerHTML = "Rejected";
  rejectButton.classList.add("rejected");
  acceptButton.style.display = "none";
}





let slides = document.querySelectorAll('.slide');
let currentSlide = 0;

function showSlide(n) {
  slides[currentSlide].classList.remove('active');
  currentSlide = (n + slides.length) % slides.length;
  slides[currentSlide].classList.add('active');
}

setInterval(() => {
  showSlide(currentSlide + 1);
}, 3000);
