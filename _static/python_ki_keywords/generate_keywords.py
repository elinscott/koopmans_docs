from koopmans.workflows.generic import valid_settings


if __name__ == '__main__':

   header = ['<table id="keywordTable" style="width:100%; text-align:left">',
             '   <tr>',
             '      <th>Keyword</th>',
             '      <th>Description</th>',
             '      <th>Type</th>',
             '      <th>Default</th>',
             '      <th>Options</th>',
             '   </tr>']

   with open('keywords.html', 'w') as f:
      f.write('\n'.join(header))
      for s in valid_settings:

         if isinstance(s.type, (tuple, list)):
            stype = '/'.join([f'<code>{t.__name__}</code>' for t in s.type])
         else:
            stype = f'<code>{s.type.__name__}</code>'
         if isinstance(s.options, (tuple, list)):
            options = '/'.join([f'<code>{o}</code>' for o in s.options])
         else:
            options = f'<code>s.options</code>'

         f.write(f'\n   <tr>')
         f.write(f'\n      <td><code>{s.name}</code></td>')
         f.write(f'\n      <td>{s.description}</td>')
         f.write(f'\n      <td>{stype}</td>')
         f.write(f'\n      <td><code>{s.default}</code></td>')
         f.write(f'\n      <td>{options}</td>')
         f.write(f'\n   </tr>')
      f.write('\n</table>')
