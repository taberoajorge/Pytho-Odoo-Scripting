#This is a short script that validates 
# whether the blacklist field is assigned to
#  a lcent, if so, blacklist becomes true and checks 
# within one of the instantiated views

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

if record.x_studio_field_UwrWm == 'Cortesía':
  y = record.x_nombre_comercial_ticket.id  
X = env['x_nombre_comercial'].search([('id', '=', y)])
# raise Warning(X)
for user in X:
  user.write({'x_blacklist': True})
# z = env['x_nombre_comercial'].set([('x_blacklist', '=', True)])
