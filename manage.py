#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys

def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)
    
    


if __name__ == '__main__':
    main()
    '''
    path = '/Users/kitty/Desktop/data.csv'
    os.chdir(path)
    df = pd.read_csv(path)
    
    for row in df.iterrows():
        p = Cosmetics(brand=row['brand'],name=row['name'],price=row['price'],
        rank=row['rank'],ingredients=row['ingredients'])
        p.save()
        '''
    
