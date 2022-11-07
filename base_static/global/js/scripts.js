function my_scope() {
    const forms = document.querySelectorAll('.form-delete');
  
    for (const form of forms) {
      form.addEventListener('submit', function (e) {
        e.preventDefault();
  
        const confirmed = confirm('Você quer mesmo fazer isso?');
  
        if (confirmed) {
          form.submit();
        }
      });
    }
  }
  
  my_scope();