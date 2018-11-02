from bot.variables import bot_commands, bot_messages, bot_keyboards
from bot.models import MenuState
from learning.models import LearningInfo
from taxonomy.models import Term



def handle_pv_edit_profile(telegram_profile, msg) :

    if msg['text'] == bot_commands['edit_name'] :
        message = bot_messages['edit_profile_get_name']
        keyboard = bot_keyboards['return']
        telegram_profile.menu_state = MenuState.EDIT_PROFILE_NAME
        telegram_profile.save()

    elif msg['text'] == bot_commands['edit_bio'] :
        message = bot_messages['edit_profile_get_bio']
        keyboard = bot_keyboards['return']
        telegram_profile.menu_state = MenuState.EDIT_PROFILE_BIO
        telegram_profile.save()

    elif msg['text'] == bot_commands['edit_skills'] :
        message = bot_messages['edit_profile_get_skills']
        keyboard = bot_keyboards['return']
        telegram_profile.menu_state = MenuState.EDIT_PROFILE_SKILLS
        telegram_profile.save()

    else :
        message = bot_messages['unknown_command']
        keyboard = bot_keyboards['edit_profile']

    return message, keyboard

def handle_pv_edit_profile_name(telegram_profile, msg) :
    if msg['text'] == bot_commands['return'] :
        message = bot_messages['edit_profile']
        keyboard = bot_keyboards['edit_profile']
        return message, keyboard

    p = telegram_profile.profile

    p.first_name = msg['text']
    p.save()

    telegram_profile.menu_state = MenuState.EDIT_PROFILE
    telegram_profile.save()

    message = bot_messages['edit_profile']
    keyboard = bot_keyboards['edit_profile']

    return message, keyboard


def handle_pv_edit_profile_bio(telegram_profile, msg):
    if msg['text'] == bot_commands['return']:
        message = bot_messages['edit_profile']
        keyboard = bot_keyboards['edit_profile']
        return message, keyboard

    p = telegram_profile.profile

    p.bio = msg['text']
    p.save()

    telegram_profile.menu_state = MenuState.EDIT_PROFILE
    telegram_profile.save()

    message = bot_messages['edit_profile']
    keyboard = bot_keyboards['edit_profile']

    return message, keyboard


def handle_pv_edit_profile_skills(telegram_profile, msg) :
    if msg['text'] == bot_commands['return']:
        message = bot_messages['edit_profile']
        keyboard = bot_keyboards['edit_profile']
        return message, keyboard

    p = telegram_profile.profile

    skills = msg['text'].split('\n')

    for skill in skills:
        if skill == '':
            continue
        lf = Term.objects.filter(title=skill)
        if lf.exists():
            if not p.skills.filter(learningfield = lf).exists():
                LearningInfo.objects.create(student = p, learning_field = lf)
        else:
            LearningInfo.objects.create(student = p,
                                        learning_field = Term.objects.create(
                                            title = skill,
                                            taxonomy_type = TaxonomyType.LEARNING_FIELD
                                        ))

    telegram_profile.menu_state = MenuState.EDIT_PROFILE
    telegram_profile.save()

    message = bot_messages['edit_profile']
    keyboard = bot_keyboards['edit_profile']

    return message, keyboard