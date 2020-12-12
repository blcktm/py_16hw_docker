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
};

document.getElementById('create-student-btn').onclick = async function (e) {
    let newStudent = {
        first_name: document.getElementById('student-name').value
    }
    await fetch('http://127.0.0.1:8000/api/v1/students/',{
        method: 'POST',
        body: JSON.stringify(newStudent),
        headers: {
            'Content-Type': 'application/json'
        }
    });
};