from cms_panel.settings import ANGULAR_API, DJANGO_URL, CMS_URL


UNIFORM = {
    "logout": {
        'url': [
            "None"
        ],
        'ru': [
            'выход'
        ],
        'uz': [
            'chiqish'
        ],
        'en': [
            'logout'
        ]
    }
}

ACCESS_PAGES = {
    'ADMIN': {
        'url': [
            ANGULAR_API + 'cabinet/orders',
            ANGULAR_API + 'cabinet/orders/archive',
            ANGULAR_API + 'cabinet/passengers',
            ANGULAR_API + 'cabinet/personal-info',
            ANGULAR_API + 'cabinet/password/change',
            CMS_URL + 'auth',
            DJANGO_URL
        ],
        'ru': [
            'мои новые заказы',
            'архив заказов',
            'мои попутчики',
            'личные данные',
            'сменить пароль',
            'управление контентом',
            'админ панель',
        ],
        'uz': [
            'my new orders',
            'orders archive',
            'my travel mates',
            'personal data',
            'change password',
            'content management',
            'admin panel',
        ],
        'en': [
            'yangi buyurtmalarim',
            'buyurtmalar arxivi',
            'mening sayohatchilarim',
            'shaxsiy malumotlarim',
            'parolni o\'zgartirish',
            'kontentni boshqarish',
            'admin paneli',
        ]
    },

    'USER': {
        'url': [
            ANGULAR_API + 'cabinet/orders',
            ANGULAR_API + 'cabinet/orders/archive',
            ANGULAR_API + 'cabinet/passengers',
            ANGULAR_API + 'cabinet/personal-info',
            ANGULAR_API + 'cabinet/password/change',
        ],
        'ru': [
            'мои новые заказы',
            'архив заказов',
            'мои постоянные попутчики',
            'личные данные',
            'сменить пароль',
        ],
        'uz': [
            'my new orders',
            'orders archive',
            'my travel mates',
            'personal data',
            'change password',
        ],
        'en': [
            'yangi buyurtmalarim',
            'buyurtmalar arxivi',
            'mening sayohatchilarim',
            'shaxsiy malumotlarim',
            'parolni o\'zgartirish',
        ]
    }
}
