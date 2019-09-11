# Edit this file to change settings
CONFIG = {
    # Uncomment the following two lines to set your username and password.
    # 'userName': '',
    # 'passWord': '',

    # The beginDate of the term in %Y-%m-%d
    # Should be a Monday
    'beginDate': '2019-09-02',

    # 'default' sets whether you want to use the newest classTable or not
    # if default is False, you need to select which term will you use
    'default': True,

    # Due to dumb programmers of jiaowu system, the class table has some
    # different formats. The application has not implement auto mode
    # detection. So if one mode doesn't work, try other modes.
    # Modes available:
    # 1. Used in 2019 spring for 187324
    # 2. Used in 2019 autumn for 183911
    # 0. Custom mode, your custom regexp will be used.
    'regexMode': 2,

    # Only available when regexMode is set to custom mode.
    # You need these named groups to make things work properly:
    # tachername, begindate, enddate, location
    # These groups are optional:
    # classname, classtime
    # In most occasions, classname group is optional
    # If you encounter exceptions, add a classname group.
    # classtime is a number group splitted by ，
    # It's for capturing precise time in classtime (for example:第1，2节)
    # A valid classtime group will enable precise time calculation
    # (Useful for PE lessons!).
    # See main.py for some samples.
    # You are welcome to make PRs to commit your own working modes.
    'customRegex': r''
}
