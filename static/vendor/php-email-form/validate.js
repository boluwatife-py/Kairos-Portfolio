function php_email_form_submit(thisForm, action, formData) {
  let csrfToken = document.querySelector('[name=csrfmiddlewaretoken]').value;
  
  fetch(action, {
      method: 'POST',
      body: formData,
      headers: {
          'X-Requested-With': 'XMLHttpRequest',
          'X-CSRFToken': csrfToken  // Add CSRF token
      }
  })
  .then(response => {
      if (response.ok) {
          return response.json();
      } else {
          throw new Error(`${response.status} ${response.statusText} ${response.url}`); 
      }
  })
  .then(data => {
      thisForm.querySelector('.loading').classList.remove('d-block');
      if (data.message === 'OK') {
          thisForm.querySelector('.sent-message').classList.add('d-block');
          thisForm.reset(); 
      } else {
          throw new Error(data.error || 'Form submission failed');
      }
  })
  .catch(error => {
      displayError(thisForm, error);
  });
}