from koopmans.workflows.generic import valid_settings


if __name__ == '__main__':

   header = ['<table id="keywordTable" style="width:100%; text-align:left">',
             '   <tr>',
             '      <th>Keyword</th>',
             '      <th>Description</th>',
             '      <th>Type</th>',
             '      <th>Default</th>',
             '   </tr>']

   with open('keywords.html', 'w') as f:
      f.write('\n'.join(header))
      for s in valid_settings:

         # Parsing type
         if isinstance(s.type, (tuple, list)):
            stype = '/'.join([f'<code>{t.__name__}</code>' for t in s.type])
         else:
            stype = f'<code>{s.type.__name__}</code>'

         # Parsing default
         if s.default is None:
            default = ''
         else:
            default = f'<code>{s.default}</code>'

         # Adding options if necessary
         if isinstance(s.options, (tuple, list)) and s.type is not bool:
            default += ' (must be ' + '/'.join([f'<code>{o}</code>' for o in s.options]) + ')'

         f.write(f'\n   <tr>')
         f.write(f'\n      <td><code>{s.name}</code></td>')
         f.write(f'\n      <td>{s.description}</td>')
         f.write(f'\n      <td>{stype}</td>')
         f.write(f'\n      <td>{default}</td>')
         f.write(f'\n   </tr>')
      f.write('\n</table>')
