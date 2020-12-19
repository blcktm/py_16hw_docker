//let loadStudents = document.getElementById('load-students');
//loadStudents.onclick = async function (event) {
//  let response = await fetch('http://127.0.0.1:8000/api/v1/students/');
//  let studentList = document.getElementById('student-list');
//  students = await response.json();
//
//  studentList.innerHTML = '';
//
//    for (let student of students) {
//      let p = document.createElement('p');
//      let input = document.createElement("input");
//      let div = document.createElement('div');
//      let upd = document.createElement('button');
//      let del = document.createElement('button');
//      div.style.border = '1px solid';
//      div.style.borderColor = 'red';
//      del.className = "btn btn-success del";
//      del.id = student.id;
//      del.innerText = 'delete'
//      upd.className = "btn btn-success update";
//      upd.id = student.id;
//      upd.innerText = 'update';
//      input.type = "text";
//      input.id = student.id;
//      input.className = 'npt-upd';
//      p.innerText = student.first_name;
//
//      div.appendChild(p);
//      div.appendChild(input);
//      div.appendChild(upd);
//      div.appendChild(del);
//
//        del.addEventListener('click', async function (){
//            try {
//                let response = await fetch(`http://127.0.0.1:8000/api/v1/students/${student.id}`, {
//                    method: "DELETE",
//                });
//            } catch (err) {
//            };
//        },);
//
//        upd.addEventListener('click', async function (){
//            let newStudent = {
//                first_name: input.value
//            }
//            try {
//                let response = await fetch(`http://127.0.0.1:8000/api/v1/students/${student.id}/`, {
//                    method: "PUT",
//                    body: JSON.stringify(newStudent),
//                    headers: {
//                        "Content-Type": "application/json",
//                    },});
//            } catch (err) {
//            };
//        },);
//
//        studentList.appendChild(div);
//  };
//};
//
//document.getElementById('create-student-btn').onclick = async function (e) {
//    let newStudent = {
//        first_name: document.getElementById('student-name').value
//    }
//    await fetch('http://127.0.0.1:8000/api/v1/students/',{
//        method: 'POST',
//        body: JSON.stringify(newStudent),
//        headers: {
//            'Content-Type': 'application/json'
//        }
//    });
//};





// ----------------------JQuery------------------------------
// console.log($('#red-rectangle'));
// $('#red-rectangle').click(function (e) {
//     console.log(this);
//     // console.log($(this));
//     // $(this).toggleClass('green');
//     // $(this).animate({width: 500, height: 500}, 1000);
//     $('.btn-primary').show();
// });
// // ==
// // document.getElementById('red-rectangle').onclick = function (e) {
// //     if(this.classList.contains('green')) {
// //         this.classList.remove('green');
// //     } else {
// //         this.classList.add('green');
// //     }
// // };
//
// $('.btn-primary').click(function (e){
//    // $('#red-rectangle').hide();
//    //  $('#red-rectangle').toggle();
//     $(this).hide();
// });
// let btnNum = 0;
// $('#add-button').click(function (e) {
//    let button = $('<button class="btn btn-danger new-btn">New button'+ btnNum +'</button>');
//    // Явное присвоение событие для созданного эл-та
//    // button.click(function (e) {
//    //    $(this).remove();
//    // });
//    $('#buttons').append(button);
//    btnNum ++;
// });
//
// $('body').on('click', '.new-btn', function (e) {
//    $(this).remove();
// });

// Не явное(Live Event) присвоение событие для созданного эл-та. При перестроение HTML происходит снова выборка.
// $('.new-btn').click(function (e) {
//    $(this).delete();
// });

$('body').on('click', '.del-btn', async function (e) {
   let id = $(this).data('id');
   await fetch('http://127.0.0.1:8000/api/v1/students/'+ id +'/', {
      method: 'DELETE'
   });

   $(this).closest('tr').remove()
});



let modal = $('#edit-modal');

$('body').on('click', '.edit-btn', async function (e) {
// $('.edit-btn').click(async function (e) {
   let id = $(this).data('id');
   // let modal = $('#edit-modal');
   let response = await fetch('http://127.0.0.1:8000/js-student-form/'+ id +'/');
   response = await response.text();
   modal.find('.modal-body').html(response);
   modal.modal('show');

});

$('.create-btn').click(async function () {
   let response = await fetch('http://127.0.0.1:8000/create-student/');
   response = await response.text();
   modal.find('.modal-body').html(response);
   modal.modal('show');
});


$('#save-update').click(function (e){
   const EDIT = 'edit-student-form';
   const CREATE = 'create-student-form';

   let form = $('.form');

   let url = form.attr('action');
   let data = form.serializeArray();

   data.reverse();

   if (form.attr('id') == EDIT) {
      let idstudent = form.attr('action').match(/\d+/)[0];
      let btn = $('body').find('[data-id=' + idstudent + ']')
      let fields = btn.closest('td').prevAll();

      for (let i=0; i<data.length-1; i++){
          fields[i].innerText = data[i].value;
      };
   } else if (form.attr('id') == CREATE) {

      // let table = $('.table');


     // console.log($('.table tr:last-child').children('td').first().text());
     let id = (parseInt($('.table tr:last-child').children('td').first().text()) + 1);
      // '<button class="btn btn-danger del-btn" data-id="">Del</button>';


     // btnDel["data-id", id];
     // console.log(btnDel);
      // console.log(id);
     // let pk = request.POST.get('id');
     // console.log(pk);
      let studentBlock = $('<tr>');


      // let tdForId = document.createElement('td');
      // tdForId.innerHTML = id;
      // studentBlock.append(tdForId);
       $('<td>').text(id).appendTo(studentBlock);
      for (let i=data.length-2; i>-1; i--){
         // console.log(i);
         studentBlock.append('<td>' + data[i].value + '</td>')
      };

       let btnDel = $(document.createElement('button')).text('Del').attr({
           // type: 'button',
           // innerHTML: 'Del',
           class: 'btn btn-danger del-btn',
           'data-id': id
       });
       let btnEdit = $(document.createElement('button')).text('Edit').attr({
           // innerHTML: 'Edit',
           class: 'btn btn-primary edit-btn',
           'data-id': id
       });
       let tdBlock = $('<td>');
       // tdBlock.append()

       // $('<td>').html(btnDel, btnEdit).appendTo(studentBlock);
       tdBlock.append(btnDel);
       tdBlock.append(btnEdit);
       studentBlock.append(tdBlock);
       // tdBlock.append(btnDel);
      // tdBlock.append(btnEdit);
      // studentBlock.append(tdBlock);
      // studentBlock.append(btnDel);
      // studentBlock.append(btnEdit);
     // let studentBlock = '<tr>' +
     //        '<td>' + id +'</td>' +
     //        '<td>' + data[3].value + '</td>' +
     //        '<td>' + data[2].value + '</td>' +
     //        '<td>' + data[1].value + '</td>' +
     //        '<td>' + data[0].value + '</td>' +
     //        '<td>' +
     //        toString(btnDel) +
     //           // '<button class="btn btn-danger del-btn" ['data-id']=id>Del</button>' +
     //           '<button class="btn btn-primary edit-btn" data-id="">Edit</button>' +
     //        '</td>' +
     //     '</tr>';

     // let btn = $('<button class="btn btn-primary edit-btn" data-id="">Edit</button>');

     $('.table').append(studentBlock);
   };

   let modal = $('#edit-modal');

   // data['id'] = 100;
   $.post(url, data);
   modal.modal('hide');
});







































