from lib.parsers import ParserFactory

p = ParserFactory.createParser('wangyi')
result = p.fetch('4724499322570095355')

print(result)