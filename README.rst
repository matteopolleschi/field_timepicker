Time Picker Field
=================

Time picker for fields, using Wickedpicker.

Installation & Configuration
============================

After installing the module, you can use character fields for reading time input with the help of a time picker.
When you define the fields in xml, use 'widget="timepicker"' for those fields which you need to use as time fields.

Example:
    - In model
    time_strat = fields.Float('From')
    time_end = fields.Char('To')

    - In view
    <group string="Delivery Timeline">
        <field name='time_strat' widget='timepicker'/>
        <field name='time_end' widget='timepicker'/>
    </group>