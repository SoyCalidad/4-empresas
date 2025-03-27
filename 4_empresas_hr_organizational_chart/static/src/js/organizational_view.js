odoo.define('4_empresas_hr_organizational_chart.view_chart', function (require){
"use strict";
var AbstractAction = require('web.AbstractAction');
var ajax = require('web.ajax');
var core = require('web.core');
var rpc = require('web.rpc');
var ActionManager = require('web.ActionManager');
var _t = core._t;
var session = require('web.session');


var EmployeeOrganizationalChartActionContext =  AbstractAction.extend({

    contentTemplate: 'EmployeeOrganizationalChartActionContext',
    events: {
        'click img': '_getChild_data',
        'click .employee_name': 'view_employee',
        'click .print_org': 'printOrg',
    },

    init: function (parent, action, options) {

        this._super(parent, action, options);
        this.company_id = action.context.default_company_id || false;
        this.renderEmployeeDetails();
    },
    renderEmployeeDetails: function (){
        var employee_id = 1
        var self = this;
        this._rpc({
            route: '/get/parent/employee',
            params: {
                company_id: this.company_id || session.user_context.allowed_company_ids[0]
            }
        }).then(function (result) {
            self.parent_len = result[1];
            $.ajax({
                url: '/get/parent/child',
                type: 'POST',
                data: JSON.stringify(result[0]),
                success: function (value) {
                        $('#o_parent_employee').append(value);
                        },
            });

        });

    },
    _getChild_data: function(events){
        console.log(events)
        if(events.target.parentElement.className){
            var self = this
            this.id = events.target.parentElement.id;
            this.check_child =  $( "#"+this.id+".o_level_1" );
            if (this.check_child[0]){
                this.colspan_td = this.check_child[0].parentElement.parentElement
                this.tbody_child = this.colspan_td.parentElement.parentElement
                var child_length = this.tbody_child.children.length
                if (child_length == 1){
                    this._rpc({
                        route: '/get/parent/colspan',
                        params: {
                            emp_id: parseInt(this.id),
                        },
                    }).then(function (col_val){
                        if (col_val){
                            self.colspan_td.colSpan = col_val;
                        }
                    });
                    this._rpc({
                        route: '/get/child/data',
                        params: {
                            click_id: parseInt(this.id),
                        },
                    }).then(function (result){
                        if (result){
                        $(result).appendTo(self.tbody_child);
                        }
                    });
                }
                else{
                    for(var i = 0;i < 3; i++){
                        this.tbody_child.children[1].remove();
                    }
                    self.colspan_td.colSpan = 2;
                }

            }
        }
    },
    view_employee: function(ev){
        if (ev.target.parentElement.className){
            var id = parseInt(ev.target.parentElement.parentElement.children[0].id)
            this.do_action({
            name: _t("Employee"),
            type: 'ir.actions.act_window',
            res_model: 'hr.employee',
            res_id: id,
            view_mode: 'form',
            views: [[false, 'form']],
            })
        }
    },
    printOrg: function () {
        var self = this;
        var printContents = document.getElementById('o_parent_employee').innerHTML;
        var originalContents = document.body.innerHTML;
        document.body.innerHTML = printContents;
        document.body.style.zoom = '0.6'
        window.print();
        document.body.innerHTML = originalContents;
        window.location.reload();
        return;
      },
});
    core.action_registry.add('organization_dashboard_action_context', EmployeeOrganizationalChartActionContext);

});
