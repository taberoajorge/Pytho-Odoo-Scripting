# The following script validates whether a branch office has the technical support policy in effect
# This works first by instantiating within the scope of the validated subscription view if the policy is in effect, and depending on the case, the validity is placed 

# Help with Python expressions
# Varios campos pueden usar código python o expresiones python. Se pueden usar las siguientes variables:

# env: Odoo Environment on which the action is triggered
# model: Odoo Model of the record on which the action is triggered; is a void recordset
# record: record on which the action is triggered; may be be void
# records: recordset of all records on which the action is triggered in multi mode; may be void
# time, datetime, dateutil, timezone: useful Python libraries
# log(message, level='info'):logging function to record debug information in ir.logging table
# Warning: Warning Exception to use with raise
# To return an action, assign: action = {...}
# Example of Python code


# partner_name = record.name + '_code'
# env['res.partner'].create({'name': partner_name})

if record.x_nombre_comercial_ticket:
  y = record.x_nombre_comercial_ticket.id
  #raise Warning(str(y))
  x = env['sale.subscription.line'].search([('x_poliza','=', True),('x_status','in',('open','pending')),('x_sucursales','in', y)]).x_status
  #['&amp;','&amp;',('x_poliza','=',True),('x_cliente','=',partner_id),('x_status','in',('open','pending')),('x_sucursales','in',x_nombre_comercial_ticket)]
  #raise Warning("con poliza")
  #raise Warning(str(x))
  record['x_studio_field_UwrWm'] = 'Póliza vigente'
  if x == False:
    if record.x_nombre_comercial_ticket.x_blacklist == True:
      record['x_studio_field_UwrWm'] = 'Lista Negra'
      #raise Warning("El cliente se encuentra actualmente en lista negra, si piensas que esto es un error favor de comprobarlo con el departamento de administración")
    elif record.x_nombre_comercial_ticket.x_blacklist == False:
      record['x_studio_field_UwrWm'] = 'Cortesía'
      