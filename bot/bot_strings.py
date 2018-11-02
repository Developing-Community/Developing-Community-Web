bot_commands = {
    'login' : 'ورود',
    'register': 'ثبت نام',
    'return': 'بازگشت',
    'exit': 'خروج',
    'add_project': 'ثبت آگهی دعوت به همکاری',
    'edit_profile': 'ویرایش پروفایل',
    'edit_name': 'ویرایش نام',
    'edit_bio': 'ویرایش بیوگرافی',
    'edit_skills': 'ویرایش مهارت ها'

}

bot_messages = {
    'start_msg' :'''
خوش آمدید 🙂✋️
برای اتصال بات به پروفایلتان در سایت، لینک زیر را باز کنید. 👇
%s/verify-token?token=%s

یا برای ورود از طریق بات، کلیدهای ثبت نام یا ورود را فشار دهید''',
    'register_get_email': 'لطفا ایمیلتان را وارد کنید',
    'register_email_exists_err': 'این ایمیل از قبل وجود دارد. لطفا ایمیل دیگری وارد کنید. اگر رمزتان را گم کردید از طریق این آدرس پسووردتان را ریست کنید.\nhttps://dev-community.ir/account/reset-password',
    'register_get_username' : 'لطفا نام کاربری دلخواهتان را وارد کنید',
    'register_username_exists_err' : 'این نام از قبل وجود دارد. لطفا نام دیگری را وارد کنید. اگر رمزتان را گم کردید از طریق این آدرس پسووردتان را ریست کنید.\nhttps://dev-community.ir/account/reset-password',
    'register_get_password' : 'لطفا کلمه عبور دلخواهتان را وارد کنید (برای حفظ امنیت پیامتان را بعد از ارسال حتما پاک کنید)',
    'login_get_username_or_email' : 'لطفا ایمیل یا نام کاربری خود را وارد کنید',
    'login_get_username_or_email_err' : 'نام کاربری یا ایمیل وارد شده وجود ندارد. لطفا ایمیل یا نام کاربری خود را وارد کنید',
    'login_get_password_err' : 'کلمه عبور اشتباه است. لطفا مجددا وارد کنید',
    'login_get_password' : 'لطفا کلمه عبورتان را وارد کنید (برای حفظ امنیت پیامتان را بعد از ارسال حتما پاک کنید)',
    'login_success': 'ورود با موفقیت انجام شد. لطفا گزینه مورد نظرتان را از منوی بات انتخاب کنید.',
    'register_success': 'ثبت نام با موفقیت انجام شد. لطفا گزینه مورد نظرتان را از منوی بات انتخاب کنید.',
    'add_project_get_content': 'لطفا متن آگهی خود را وارد کنید',
    'add_project_get_skills': 'لطفا مهارت های مورد نیازتان را وارد کنید. هر مهارت را در یک خط بنویسید.',
    'add_project_success': 'آگهی شما با موفقیت ثبت شد',
    'edit_profile_get_name': 'لطفا نامتان را وارد کنید',
    'edit_profile_get_bio': 'لطفا بیوگرافیتان را وارد کنید',
    'edit_profile_get_skills': 'لطفا مهارت های خود را وارد کنید. هر مهارت را در یک سطر بنویسید',
    'unknown_command': 'لطفا از منوی بات گزینه مورد نظرتان را انتخاب کنید.',
    'edit_profile': 'لطفا یکی از گزینه ها را برای ویرایش انتخاب کنید.',
    'main_menu': 'لطفا از منوی بات گزینه مورد نظرتان را انتخاب کنید.'
}


bot_keyboards = {
    'return': [[bot_commands['return']]],
    'return_or_exit': [[bot_commands['return']], [bot_commands['exit']]],
    'login_or_register': [[bot_commands['login'], bot_commands['register']]],
    'main_menu': [[bot_commands['add_project']], [bot_commands['edit_profile']], [bot_commands['exit']]],
    'edit_profile': [[bot_commands['edit_skills'],bot_commands['edit_bio'],bot_commands['edit_name']], [bot_commands['exit'], bot_commands['return']]]
}

def bot_profile_to_string(profile):
    profile_string = 'نام: ' + (profile.first_name or '') + ' ' + (profile.last_name or '') + '\nبیوگرافی:\n' + (profile.bio or '') + '\nمهارتها:\n'
    profile_string += '، '.join([skill.learning_field.title for skill in profile.skills.all()])
    print(profile_string)
    return profile_string