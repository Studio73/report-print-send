To configure this module, you need to:

#. Go to *Settings > Printing > Labels > ZPL II*
#. Create new labels
#. Import ZPL2 code
#. Use the Test Mode tab during the creation

It's also possible to add a label printing wizard on any model by creating a new *ir.actions.act_window* record.
For example, to add the printing wizard on the *product.product* model ::

    <record model="ir.actions.act_window" id="action_wizard_purchase">
      <field name="name">Print Label</field>
      <field name="res_model">wizard.print.record.label</field>
      <field name="view_mode">form</field>
      <field name="src_model">product.product</field>
      <field name="target">new</field>
      <field name="key2">client_action_multi</field>
    </record>
