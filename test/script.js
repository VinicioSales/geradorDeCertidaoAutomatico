const content = document.querySelector(".content");
const inputSearch = document.querySelector("input[type='search']");

let items = [];

inputSearch.oninput = () => {
  const searchTerm = inputSearch.value.toLowerCase();
  content.innerHTML = "";

  if (searchTerm !== "") {
    items
      .filter((item) => item.toLowerCase().includes(searchTerm))
      .forEach((item) => addHTML(item));
    content.classList.add("visible");
  } else {
    content.classList.remove("visible");
  }
};

function addHTML(item) {
  const div = document.createElement("div");
  div.innerHTML = item;
  content.append(div);
}

fetch("https://jsonplaceholder.typicode.com/users")
  .then((data) => data.json())
  .then((users) => {
    users.forEach((user) => {
      addHTML(user.name);
      items.push(user.name);
    });
  });