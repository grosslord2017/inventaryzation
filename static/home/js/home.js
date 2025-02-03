function chack_login(user, url) {
    if (user !== 'AnonymousUser') {
        window.location.href = url;
    } else {
        window.location.href = '/login';
    }
}