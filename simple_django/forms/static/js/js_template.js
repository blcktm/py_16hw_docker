// --------------VARIABLES--------------------
const some_var = 12;
let some = 12;

//console.log(window);
// && and
// || or
// !  not




// ------------------------CHECKS--------------------
if (10 < 12) {
    console.log("Hello");
} else if (23 > 21) {
    console.log(123);
} else {
    console.log('Else')
}

let user_input = "Hello";

switch (user_input) {
    case "Hello":
        console.log("Hello");
        break;
    case "Bye":
        console.log("Bye");
        break;
}




// --------------CYCLES---------------------
//let iter = 0;
//while (iter < 10) {
//    iter++;
//    console.log(iter);
//}
//let a = [1, 2, 3, 4, 5];
//for (let i=0; i<a.length; i++) {
//    console.log(i);
//}

a = [1, '231', [1, 2]];
b = new Array(1, 2, 3);
c = {name: 'ilya', age: 31};
//console.log(c);




// --------------FUNCTIONS-------------
function sum(lst=[]) {
    let summa = 0;
    for (let i=0; i<lst.length; i++) {
        summa += lst[i];
    }
    return summa;
}
//console.log(sum([1, 2, 3, 5, 5]))

let some_test_function = function (asd) {
    console.log(asd)
};
some_test_function("Hello func");




//--------------OOP-------------------------------
let paymentServiceObj = {
    card: '',
    pay: function () {
        console.log("Money will be from" + this.card);
    },
    create: function (card) {
        this.card = card;
        return this;
    }
};

function paymentService(card) {
    this.card = card;
    this.pay = function () {
        console.log("Money will be from" + this.card);
    };
}

let ilya = new paymentService("232434 34344 4343 3443")
ilya.pay()

let thor = {...paymentServiceObj};
thor.card = "23423 234234 342424  342242";
thor.pay();




//------------FIND ELEMENTS------------------------
let redRectangle = document.getElementById('red-rectangle');
console.log(redRectangle);
let ul = document.getElementsByTagName('ul');
console.log(ul);
let redRectangleClass = document.getElementsByClassName('red-rectangle-class');
console.log(redRectangleClass);
let css = document.querySelector('#red-rectangle');
console.log(css)




// -------------------------------GAME
// setTimeout(function () {
//     // redRectangle.innerText = "HELLO HILLEL";
//     redRectangle.style.background = 'green';
//     redRectangle.style.width = '50px';
//     redRectangle.style.height = '50px';
//     setTimeout(function () {
//         redRectangle.style.display = 'none';
//     }, 1000)
// }, 1000)

// setInterval(() => {   // (asd)
//     console.log(parseInt(redRectangle.style.width) + 10);
//     redRectangle.style.width += (parseInt(redRectangle.style.width) + 10) + 'px';
//     redRectangle.style.height += 10;
// }, 500);




// ---------------EVENTS----------------
redRectangle.onmousemove = function (evnt) {
  this.style.background = 'green';
};

redRectangle.onmouseleave = function (event) {
    this.style.background = 'red';
};

// redRectangle.onclick = function (eve) {
//     let user = prompt("Dinazaur");
//     alert(user);
// };

// redRectangle.onchange

// ----------------hw--------------
let loadStudents = document.getElementById('load-students');
loadStudents.onclick = async function (event) {
  let response = await fetch('http://127.0.0.1:8000/api/v1/students/');
  let studentList = document.getElementById('student-list');
  students = await response.json();

  studentList.innerHTML = '';

    for (let student of students) {
      let p = document.createElement('p');
      let input = document.createElement("input");
      let div = document.createElement('div');
      let upd = document.createElement('button');
      let del = document.createElement('button');
      div.style.border = '1px solid';
      div.style.borderColor = 'red';
      del.className = "btn btn-success del";
      del.id = student.id;
      del.innerText = 'delete'
      upd.className = "btn btn-success update";
      upd.id = student.id;
      upd.innerText = 'update';
      input.type = "text";
      input.id = student.id;
      input.className = 'npt-upd';
      p.innerText = student.first_name;

      div.appendChild(p);
      div.appendChild(input);
      div.appendChild(upd);
      div.appendChild(del);

        del.addEventListener('click', async function (){
            try {
                let response = await fetch(`http://127.0.0.1:8000/api/v1/students/${student.id}`, {
                    method: "DELETE",
                });
            } catch (err) {
            };
        },);


        upd.addEventListener('click', async function (){
            let newStudent = {
                first_name: input.value
            }
            try {
                let response = await fetch(`http://127.0.0.1:8000/api/v1/students/${student.id}/`, {
                    method: "PUT",
                    body: JSON.stringify(newStudent),
                    headers: {
                        "Content-Type": "application/json",
                    },});
            } catch (err) {
            };
        },);

        studentList.appendChild(div);
  };


  // console.log('update');

    // funcUpdate = function (id) {
    //     alert(id);
    //     console.log('update');
    // };
    // for (let i = 0; i<btnsDel.length; i++) {
    //     btnsUpdate[i].addEventListener('click', function (){alert(i)}, false);
    // };

    // for (let i = 0; i<btnsUpdate.length; i++) {
    //
    // };
};






document.getElementById('create-student-btn').onclick = async function (e) {
    let newStudent = {
        first_name: document.getElementById('student-name').value
    }
    // try {
    //     await fetch('http://127.0.0.1:8000/api/v1/students/',{
    //         method: 'POST',
    //         body: newStudent
    //     });
    // } catch (e) {
    //     alert('ERROR');
    // }
    await fetch('http://127.0.0.1:8000/api/v1/students/',{
        method: 'POST',
        body: JSON.stringify(newStudent),
        headers: {
            'Content-Type': 'application/json'
        }
    });

    // console.log(newStudent);
};