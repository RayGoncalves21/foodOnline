

def detectUser(user):
    if user.role == 1:
        redirecrUrl = 'vendorDashboard'
        return redirecrUrl
    elif user.role == 2:
        redirecrUrl = 'custDashboard'
        return redirecrUrl
    elif user.role == None and user.is_superadmin:
        redirecrUrl = '/admin'
        return redirecrUrl
