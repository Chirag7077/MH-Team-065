import __future__, sys
if hasattr(__future__, 'print_function'): 
    # Could also check sys.version_info >= __future__. print_function.optional
    import app
    app.main()
else:
    print ("instructions for upgrading")
