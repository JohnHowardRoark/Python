""" This module contains tools for use in learning some of the
    internal details of Python.  If the module is imported, some
    of the methods will work without modifications. Others will
    require adaptation per the instructions in each docstring.
"""

def show_dict(obj, name=None):
    """ Print key/value pairs of __dict__ on separate lines, with
        keys right aligned to each other.  Since there is no simple
        way to get the name of a class instance, have an option to
        pass the name as a string when the function is called.
    """
    GREEN = '\033[32m' 
    BLUE = '\033[01;34m'  
    ENDC = '\033[0m'
    OFFSET = 0
    print(BLUE + '\nanalysistools.show_dict' + ENDC)
    
    # Print a header for each category in green.
    if name:
        print(GREEN + name + '.__dict__' + ENDC)
    elif hasattr(obj, '__name__'):
        print(GREEN + obj.__name__ + '.__dict__' + ENDC)
    else:
        print(GREEN + str(obj) + '.__dict__' + ENDC)
    
    # Determine offset so all keys can be aligned
    for key, item in obj.__dict__.items():
        if len(key) > OFFSET:
            OFFSET = len(key)

    # Print __dict__ keys and items using offset.
    for key, item in sorted(obj.__dict__.items()):
        print(key.rjust(OFFSET+3, ' '),':', item)

def show_objects():
    """ Use the inspect module to show the modules, classes and
        functions in use.  If called from a module, return the
        objects for that module, not script to which it was
        imported.  Best use by copying into the script instead.
    """
    import sys, inspect
    obj_list = {'modules': [], 'classes': [], 'functions': []}
    print('\033[01;34m\nanalysistools.show_objects\033[0m')
    for name, obj in inspect.getmembers(sys.modules[__name__]):
        if inspect.ismodule(obj):
            obj_list['modules'].append(obj)
        if inspect.isclass(obj):
            obj_list['classes'].append(obj)
        if inspect.isfunction(obj):
            obj_list['functions'].append(obj)
    for key, val in obj_list.items():
        print('\033[32m%s:\033[0m' %(key))
        for item in val:
            print(item)

def test_stmnt(statement, globs=None):
    """ Accept a statement as an arg, then use try/except to test
        the statement.  Display arg and response, with color, for 
        easy readability.  If called from a module, the calling
        statement must send globals() as the second argument.
        i.e. analysistools.test('getattr(A, "A_var")', globals())
    """
    BLUE = '\033[34m'
    BLUEBOLD = '\033[01;34m'
    GREEN = '\033[32m'
    ENDC = '\033[0m'
    print(BLUEBOLD + '\nanalysistools.test_stmnt' + ENDC)
    print(BLUE + 'Trying: ' + ENDC + statement)
    try:
        ret = eval(statement, globs)
    except Exception as ex:
        ret = ex
    print(GREEN + 'Response: ' + ENDC + str(ret))


if __name__ == '__main__':
    BLUE = '\033[01;34m'   
    ENDC = '\033[0m'
    print(BLUE + 'Module analysistools.py\n' + ENDC + 'This module contains tools for use in learning Python.\nThe following is a demo of the tools.')

    # Setup some test objects.
    class TestClass:
        A = 'class attr A'

        def __init__(self):
            self.a = 'instance attr of A'

    instance = TestClass()

    # Demo the tools.
    show_dict(TestClass)
    show_dict(instance, 'instance')
    show_objects()
    test_stmnt('print(instance.a)') # When print works, it returns None.
    test_stmnt('print(instance.b)') # Returns the error
    test_stmnt('3 + 4')             # Returns the value