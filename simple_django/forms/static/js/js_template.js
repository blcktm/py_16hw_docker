$('body').on('click', '.del-btn', async function (e) {
   let id = $(this).data('id');
   await fetch('http://127.0.0.1:8000/api/v1/students/'+ id +'/', {
      method: 'DELETE'
   });

   $(this).closest('tr').remove()
});

let modal = $('#edit-modal');

$('body').on('click', '.edit-btn', async function (e) {
   let id = $(this).data('id');
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
     let id = (parseInt($('.table tr:last-child').children('td').first().text()) + 1);
     let studentBlock = $('<tr>');
     $('<td>').text(id).appendTo(studentBlock);

      for (let i=data.length-2; i>-1; i--){
         studentBlock.append('<td>' + data[i].value + '</td>');
      };

       let btnDel = $(document.createElement('button')).text('Del').attr({
           class: 'btn btn-danger del-btn',
           'data-id': id
       });
       let btnEdit = $(document.createElement('button')).text('Edit').attr({
           class: 'btn btn-primary edit-btn',
           'data-id': id
       });
       let tdBlock = $('<td>');
       tdBlock.append(btnDel);
       tdBlock.append(btnEdit);
       studentBlock.append(tdBlock);

     $('.table').append(studentBlock);
   };

   let modal = $('#edit-modal');
   $.post(url, data);
   modal.modal('hide');
});
