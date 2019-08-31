# Edit this file to change settings
CONFIG = {
    'beginDate': '2019-09-02',
    # The beginDate of the term in %Y-%m-%d
    # Should be a Monday

    # 'userName': '',
    # 'passWord': '',

    'default': True,
    # 'default' sets whether you want to use the newest classTable or not
    # if default is False, you need to select which term will you use

    'regexMode': 2,
    # Due to dumb programmers of jiaowu system, the class table has some
    # different formats. The application has not implement auto mode
    # detection. So if one mode doesn't work, try other modes.
    # Modes available:
    # 1. Used in 2019 spring for 187324
    # 2. Used in 2019 autumn for 183911
    # 0. Custom mode, your custom regexp will be used.

    'customRegex': r''
    # Only available when regexMode is set to custom mode.
    # You need these named groups to make things work properly:
    # tachername, begindate, enddate, location
    # These groups are optional:
    # classname
    # In most occasions, classname group is optional
    # If you encounter exceptions, add a classname group.
    # See main.py for some samples.
    # You are welcome to make PRs to commit your own working modes.
}
