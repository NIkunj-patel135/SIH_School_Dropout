document.getElementById("registration-form").addEventListener("submit", function (e) {
    e.preventDefault();
    
    // You can add code here to handle form submission, validate input, and send data to a server if needed.
    
    // For this example, we'll just display an alert with the submitted data.
    const formData = new FormData(this);
    const formDataObject = {};
    formData.forEach((value, key) => {
        formDataObject[key] = value;
    });
    
    alert("Form Data Submitted:\n" + JSON.stringify(formDataObject, null, 2));
});
