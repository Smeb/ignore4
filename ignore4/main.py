import sys
import urllib.request

REPO_PATH = 'https://raw.githubusercontent.com/github/gitignore/master'

LANGUAGES = [
  'Actionscript',
  'Ada',
  'Agda',
  'Android',
  'AppEngine',
  'AppceleratorTitanium',
  'ArchLinuxPackages',
  'Autotools',
  'C++',
  'C',
  'CFWheels',
  'CMake',
  'CUDA',
  'CakePHP',
  'ChefCookbook',
  'Clojure',
  'CodeIgniter',
  'CommonLisp',
  'Composer',
  'Concrete5',
  'Coq',
  'CraftCMS',
  'D',
  'DM',
  'Dart',
  'Delphi',
  'Drupal',
  'EPiServer',
  'Eagle',
  'Elisp',
  'Elixir',
  'Elm',
  'Erlang',
  'ExpressionEngine',
  'ExtJs',
  'Fancy',
  'Finale',
  'ForceDotCom',
  'Fortran',
  'FuelPHP',
  'GWT',
  'Gcov',
  'GitBook',
  'Go',
  'Godot',
  'Gradle',
  'Grails',
  'Haskell',
  'IGORPro',
  'Idris',
  'JBoss',
  'JENKINS_HOME',
  'Java',
  'Jekyll',
  'Joomla',
  'Julia',
  'KiCad',
  'Kohana',
  'Kotlin',
  'LabVIEW',
  'Laravel',
  'Leiningen',
  'LemonStand',
  'Lilypond',
  'Lithium',
  'Lua',
  'Magento',
  'Maven',
  'Mercury',
  'MetaProgrammingSystem',
  'Nanoc',
  'Nim',
  'Node',
  'OCaml',
  'Objective-C',
  'Opa',
  'OpenCart',
  'OracleForms',
  'Packer',
  'Perl',
  'Perl6',
  'Phalcon',
  'PlayFramework',
  'Plone',
  'Prestashop',
  'Processing',
  'PureScript',
  'Python',
  'Qooxdoo',
  'Qt',
  'R',
  'ROS',
  'Rails',
  'RhodesRhomobile',
  'Ruby',
  'Rust',
  'SCons',
  'Sass',
  'Scala',
  'Scheme',
  'Scrivener',
  'Sdcc',
  'SeamGen',
  'SketchUp',
  'Smalltalk',
  'Stella',
  'SugarCRM',
  'Swift',
  'Symfony',
  'SymphonyCMS',
  'TeX',
  'Terraform',
  'Textpattern',
  'TurboGears2',
  'Typo3',
  'Umbraco',
  'Unity',
  'UnrealEngine',
  'VVVV',
  'VisualStudio',
  'Waf',
  'WordPress',
  'Xojo',
  'Yeoman',
  'Yii',
  'ZendFramework',
  'Zephir'
]

LANGUAGES_DICT = {name.lower() : name for name in LANGUAGES}

def usage():
  print( "usage: ignore4 <language>")
  print("usage: ignore4 --list")

def get_ignore(url):
  response = urllib.request.urlopen(url)
  data = response.read()
  text = data.decode('utf-8')
  return text

def lookup_path(language):
  try:
    language_name = LANGUAGES_DICT[language]
  except KeyError:
    print('language "{}" is not in the list of known languages. pass --list to see the list of all known languages'.format(language))
    sys.exit(1)
  return '{}/{}.gitignore'.format(REPO_PATH, language_name)

def ignore4(language):
  path = lookup_path(language)
  contents = get_ignore(path)
  with open('.gitignore', 'w') as f:
    f.write(contents)
  print('gitignore from {} written to .gitignore'.format(path))

def print_languages():
  print('There are {} languages with .gitignores'.format(len(LANGUAGES)))
  for lang in LANGUAGES:
    print(lang)

def cli():
  if len(sys.argv) == 2:
    if sys.argv[1] == "--list":
      print_languages()
    else:
      ignore4(sys.argv[1])
  else:
    usage()
