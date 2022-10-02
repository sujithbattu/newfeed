/* 
    ==================================
    Edit/Add Job Page – Update Preview
    ==================================
*/

    $(function() {
        var previewButton = document.getElementById('update-preview');

        if (previewButton) {
            // Clicking anywhere on an add/edit job page updates the preview.
            this.addEventListener('click', updatePreview);
        }

        function updatePreview() {
            var company_name =      $('#company_name').val(),
                company_logo_url =  $('#company_logo_url').val(),
                location_city =     $('#location_city').val(),
                location_state =    $('#location_state').val(),
                job_title =         $('#job_title').val(),
                job_description =   $('#job_description').val();

            var placeholder_company_name =      'Company Name',
                placeholder_company_logo_url =  '/static/images/logo-placeholder.png',
                placeholder_location_city =     'City',
                placeholder_location_state =    'State',
                placeholder_job_title =         'Job Title',
                placeholder_job_description =   '<p>Lorem ipsum dolor sit amet, consectetur adipiscing elit.</p><p>Quisque ut dolor et leo varius ultricies. Nullam sit amet nibh eget orci pretium consectetur. Sed et elit sit amet ligula bibendum vehicula eget eget sem. Nunc massa turpis, laoreet a nibh ut, varius vulputate orci.</p><p>Nam rhoncus, neque vitae interdum elementum, erat ex vehicula orci, sit amet vulputate lectus felis consectetur quam. Proin nec lectus tellus. Pellentesque eget dictum sapien.</p>';

            if (company_name !== '') {
                $('span.company-name').text(company_name);
            } else {
                $('span.company-name').text(placeholder_company_name);
            }

            if (company_logo_url !== '' && company_logo_url !== 'http://') {
                $('.job-logo img').attr('src', company_logo_url);
            } else {
                $('.job-logo img').attr('src', placeholder_company_logo_url);
            }

            if (location_city !== '') {
                $('span.location-city').text(location_city);
            } else {
                $('span.location-city').text(placeholder_location_city);
            }

            if (location_state !== '') {
                $('span.location-state').text(location_state);
            } else {
                $('span.location-state').text(placeholder_location_state);
            }

            if (job_title !== '') {
                $('div.job-title h1').text(job_title);
            } else {
                $('div.job-title h1').text(placeholder_job_title);
            }

            if (job_description !== '') {
                $('div.job-description').html('<p>' + job_description + '</p>');
            } else {
                $('div.job-description').html(placeholder_job_description);
            }
        }
    });