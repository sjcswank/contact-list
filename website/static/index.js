function deleteContact(contactId) {
            fetch("/delete-contact", {
            method: "POST",
            body: JSON.stringify({ contactId: contactId}),
            }).then((_res) => {
            window.location.href = "/";
            });
}

// function deleteUser(userId) {
//             fetch("/delete-user", {
//             method: "POST",
//             body: JSON.stringify({ userId: userId }),
//             }).then((_res) => {
//             window.location.href = "/";
//             });
// }

//
//function editContact(contactId) {
//            fetch("/edit-contact", {
//            method: "POST",
//            body: JSON.stringify({ contactId: contactId}),
//            }).then((_res) => {
//            window.location.href = "/";
//            });
//}