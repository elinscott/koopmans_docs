from koopmans.workflows.generic import valid_settings as workflow_settings
from koopmans.calculators.ui._settings import valid_settings as ui_settings


def print_settings_as_html(settings, table_id, fd):
   header = [f'<table id="{table_id}" style="width:100%; text-align:left">',
             '   <tr>',
             '      <th>Keyword</th>',
             '      <th>Description</th>',
             '      <th>Type</th>',
             '      <th>Default</th>',
             '   </tr>']

   fd.write('\n'.join(header))
   for s in settings:

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

      fd.write(f'\n   <tr>')
      fd.write(f'\n      <td><code>{s.name}</code></td>')
      fd.write(f'\n      <td>{s.description}</td>')
      fd.write(f'\n      <td>{stype}</td>')
      fd.write(f'\n      <td>{default}</td>')
      fd.write(f'\n   </tr>')
   fd.write('\n</table>')


if __name__ == '__main__':

   with open('workflow_keywords.html', 'w') as fd:
      print_settings_as_html(workflow_settings, 'workflowTable', fd)

   with open('ui_keywords.html', 'w') as fd:
      print_settings_as_html(ui_settings, 'uiTable', fd)
