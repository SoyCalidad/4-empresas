from odoo import api, fields, models

class hola_calidaddiagnosticline(models.Model):
    _inherit = 'hola_calidad.diagnostic.line'

    company_id = fields.Many2one('res.company', string='Compañia', default=lambda self: self.env.company)


class hola_calidaddiagnostic(models.Model):
    _inherit = 'hola_calidad.diagnostic'

    company_id = fields.Many2one('res.company', string='Compañia', default=lambda self: self.env.company)

class hrworkplace(models.Model):
    _inherit = 'hr.workplace'

    company_id = fields.Many2one('res.company', string='Compañia', default=lambda self: self.env.company)


class hrjobfunction(models.Model):
    _inherit = 'hr.job.function'

    company_id = fields.Many2one('res.company', string='Compañia', default=lambda self: self.env.company)


class hrjobevaluation_factor(models.Model):
    _inherit = 'hr.job.evaluation_factor'

    company_id = fields.Many2one('res.company', string='Compañia', default=lambda self: self.env.company)


class hrjobcoordinator(models.Model):
    _inherit = 'hr.job.coordinator'

    company_id = fields.Many2one('res.company', string='Compañia', default=lambda self: self.env.company)


class hrjobsupervisor(models.Model):
    _inherit = 'hr.job.supervisor'

    company_id = fields.Many2one('res.company', string='Compañia', default=lambda self: self.env.company)


class hrjobsupervised(models.Model):
    _inherit = 'hr.job.supervised'

    company_id = fields.Many2one('res.company', string='Compañia', default=lambda self: self.env.company)


class hrjobprofile(models.Model):
    _inherit = 'hr.job.profile'

    company_id = fields.Many2one('res.company', string='Compañia', default=lambda self: self.env.company)


class hrjobprofilespecialty(models.Model):
    _inherit = 'hr.job.profile.specialty'

    company_id = fields.Many2one('res.company', string='Compañia', default=lambda self: self.env.company)


class hrjobprofileexperience(models.Model):
    _inherit = 'hr.job.profile.experience'

    company_id = fields.Many2one('res.company', string='Compañia', default=lambda self: self.env.company)


class hrjobskill(models.Model):
    _inherit = 'hr.job.skill'

    company_id = fields.Many2one('res.company', string='Compañia', default=lambda self: self.env.company)


class hrjobgeneric_skill(models.Model):
    _inherit = 'hr.job.generic_skill'

    company_id = fields.Many2one('res.company', string='Compañia', default=lambda self: self.env.company)


class hrjobworkteam_skill(models.Model):
    _inherit = 'hr.job.workteam_skill'

    company_id = fields.Many2one('res.company', string='Compañia', default=lambda self: self.env.company)


class hrjobpersonal_skill(models.Model):
    _inherit = 'hr.job.personal_skill'

    company_id = fields.Many2one('res.company', string='Compañia', default=lambda self: self.env.company)


class hrjobstrategic_skill(models.Model):
    _inherit = 'hr.job.strategic_skill'

    company_id = fields.Many2one('res.company', string='Compañia', default=lambda self: self.env.company)


class mgmtsystemactiontype(models.Model):
    _inherit = 'mgmtsystem.action.type'

    company_id = fields.Many2one('res.company', string='Compañia', default=lambda self: self.env.company)


class mgmtsystemaction(models.Model):
    _inherit = 'mgmtsystem.action'

    company_id = fields.Many2one('res.company', string='Compañia', default=lambda self: self.env.company)


class auditteam(models.Model):
    _inherit = 'audit.team'

    company_id = fields.Many2one('res.company', string='Compañia', default=lambda self: self.env.company)


class auditaudit(models.Model):
    _inherit = 'audit.audit'

    company_id = fields.Many2one('res.company', string='Compañia', default=lambda self: self.env.company)


class auditline(models.Model):
    _inherit = 'audit.line'

    company_id = fields.Many2one('res.company', string='Compañia', default=lambda self: self.env.company)


class auditreport(models.Model):
    _inherit = 'audit.report'

    company_id = fields.Many2one('res.company', string='Compañia', default=lambda self: self.env.company)


class auditplancateg(models.Model):
    _inherit = 'audit.plan.categ'

    company_id = fields.Many2one('res.company', string='Compañia', default=lambda self: self.env.company)


class auditplan(models.Model):
    _inherit = 'audit.plan'

    company_id = fields.Many2one('res.company', string='Compañia', default=lambda self: self.env.company)


class ReportLine(models.Model):
    _inherit = 'report.line'

    company_id = fields.Many2one('res.company', string='Compañia', default=lambda self: self.env.company)


class complaintcomplaintcause_why(models.Model):
    _inherit = 'complaint.complaint.cause_why'

    company_id = fields.Many2one('res.company', string='Compañia', default=lambda self: self.env.company)


class complaintanalisis(models.Model):
    _inherit = 'complaint.analisis'

    company_id = fields.Many2one('res.company', string='Compañia', default=lambda self: self.env.company)


class comunicationplancateg(models.Model):
    _inherit = 'comunication.plan.categ'

    company_id = fields.Many2one('res.company', string='Compañia', default=lambda self: self.env.company)


class comunicationplan(models.Model):
    _inherit = 'comunication.plan'

    company_id = fields.Many2one('res.company', string='Compañia', default=lambda self: self.env.company)


class comunicationplanline(models.Model):
    _inherit = 'comunication.plan.line'

    company_id = fields.Many2one('res.company', string='Compañia', default=lambda self: self.env.company)


class comunicationplanlinedocument(models.Model):
    _inherit = 'comunication.plan.line.document'

    company_id = fields.Many2one('res.company', string='Compañia', default=lambda self: self.env.company)


class recordmeeting(models.Model):
    _inherit = 'record.meeting'

    company_id = fields.Many2one('res.company', string='Compañia', default=lambda self: self.env.company)


class recordmeetingpreline(models.Model):
    _inherit = 'record.meeting.preline'

    company_id = fields.Many2one('res.company', string='Compañia', default=lambda self: self.env.company)


class recordmeetingline(models.Model):
    _inherit = 'record.meeting.line'

    company_id = fields.Many2one('res.company', string='Compañia', default=lambda self: self.env.company)


class assistancemeeting(models.Model):
    _inherit = 'assistance.meeting'

    company_id = fields.Many2one('res.company', string='Compañia', default=lambda self: self.env.company)


class mgmtsystemcontext(models.Model):
    _inherit = 'mgmtsystem.context'

    company_id = fields.Many2one('res.company', string='Compañia', default=lambda self: self.env.company)


class mgmtsystemcontextinternal_issue(models.Model):
    _inherit = 'mgmtsystem.context.internal_issue'

    company_id = fields.Many2one('res.company', string='Compañia', default=lambda self: self.env.company)


class mgmtsystemcontextmoral(models.Model):
    _inherit = 'mgmtsystem.context.moral'

    company_id = fields.Many2one('res.company', string='Compañia', default=lambda self: self.env.company)


class mgmtsystemcontextpolicy(models.Model):
    _inherit = 'mgmtsystem.context.policy'

    company_id = fields.Many2one('res.company', string='Compañia', default=lambda self: self.env.company)


class mgmtsystemcontextpolicytemplate(models.Model):
    _inherit = 'mgmtsystem.context.policy.template'

    company_id = fields.Many2one('res.company', string='Compañia', default=lambda self: self.env.company)


class mgmtsystemcontextpolicyaction(models.Model):
    _inherit = 'mgmtsystem.context.policy.action'

    company_id = fields.Many2one('res.company', string='Compañia', default=lambda self: self.env.company)


class mgmtsystemcontextexternal_issue(models.Model):
    _inherit = 'mgmtsystem.context.external_issue'

    company_id = fields.Many2one('res.company', string='Compañia', default=lambda self: self.env.company)


class mgmtsystemcontextexternal_issueforce(models.Model):
    _inherit = 'mgmtsystem.context.external_issue.force'

    company_id = fields.Many2one('res.company', string='Compañia', default=lambda self: self.env.company)


class mgmtsystemcontextforce(models.Model):
    _inherit = 'mgmtsystem.context.force'

    company_id = fields.Many2one('res.company', string='Compañia', default=lambda self: self.env.company)


class mgmtsystemstakeholders(models.Model):
    _inherit = 'mgmtsystem.stakeholders'

    company_id = fields.Many2one('res.company', string='Compañia', default=lambda self: self.env.company)


class stakeholderstakeholder(models.Model):
    _inherit = 'stakeholder.stakeholder'

    company_id = fields.Many2one('res.company', string='Compañia', default=lambda self: self.env.company)


class mgmtsystemstakeholder(models.Model):
    _inherit = 'mgmtsystem.stakeholder'

    company_id = fields.Many2one('res.company', string='Compañia', default=lambda self: self.env.company)


class mgmtsystemstakeholderreq(models.Model):
    _inherit = 'mgmtsystem.stakeholder.req'

    company_id = fields.Many2one('res.company', string='Compañia', default=lambda self: self.env.company)


class mgmtsystemstakeholderopp(models.Model):
    _inherit = 'mgmtsystem.stakeholder.opp'

    company_id = fields.Many2one('res.company', string='Compañia', default=lambda self: self.env.company)


class mgmtsystemcontextorganization_chart(models.Model):
    _inherit = 'mgmtsystem.context.organization_chart'

    company_id = fields.Many2one('res.company', string='Compañia', default=lambda self: self.env.company)


class mgmtsystemcontextpest(models.Model):
    _inherit = 'mgmtsystem.context.pest'

    company_id = fields.Many2one('res.company', string='Compañia', default=lambda self: self.env.company)


class pestfactor(models.Model):
    _inherit = 'pest.factor'

    company_id = fields.Many2one('res.company', string='Compañia', default=lambda self: self.env.company)


class pestfactortype(models.Model):
    _inherit = 'pest.factor.type'

    company_id = fields.Many2one('res.company', string='Compañia', default=lambda self: self.env.company)


class mgmtcateg(models.Model):
    _inherit = 'mgmt.categ'

    company_id = fields.Many2one('res.company', string='Compañia', default=lambda self: self.env.company)


class hremployeedocument_type(models.Model):
    _inherit = 'hr.employee.document_type'

    company_id = fields.Many2one('res.company', string='Compañia', default=lambda self: self.env.company)


class capacateg(models.Model):
    _inherit = 'capa.categ'

    company_id = fields.Many2one('res.company', string='Compañia', default=lambda self: self.env.company)


class mgmtsystemplan(models.Model):
    _inherit = 'mgmtsystem.plan'

    company_id = fields.Many2one('res.company', string='Compañia', default=lambda self: self.env.company)


class mgmtsystemplantraining(models.Model):
    _inherit = 'mgmtsystem.plan.training'

    company_id = fields.Many2one('res.company', string='Compañia', default=lambda self: self.env.company)


class mgmtsystemplantrainingline(models.Model):
    _inherit = 'mgmtsystem.plan.training.line'

    company_id = fields.Many2one('res.company', string='Compañia', default=lambda self: self.env.company)


class trainingdocument(models.Model):
    _inherit = 'training.document'

    company_id = fields.Many2one('res.company', string='Compañia', default=lambda self: self.env.company)


class mgmtsystemcalibrationplan(models.Model):
    _inherit = 'mgmtsystem.calibration.plan'

    company_id = fields.Many2one('res.company', string='Compañia', default=lambda self: self.env.company)


class mgmtsystemcalibration(models.Model):
    _inherit = 'mgmtsystem.calibration'

    company_id = fields.Many2one('res.company', string='Compañia', default=lambda self: self.env.company)


class mgmtsystemcalibrationline(models.Model):
    _inherit = 'mgmtsystem.calibration.line'

    company_id = fields.Many2one('res.company', string='Compañia', default=lambda self: self.env.company)


class mgmtsysteminfrastructureline(models.Model):
    _inherit = 'mgmtsystem.infrastructure.line'

    company_id = fields.Many2one('res.company', string='Compañia', default=lambda self: self.env.company)


class mgmtsysteminfrastructure(models.Model):
    _inherit = 'mgmtsystem.infrastructure'

    company_id = fields.Many2one('res.company', string='Compañia', default=lambda self: self.env.company)


class infrastructurelinedocument(models.Model):
    _inherit = 'infrastructure.line.document'

    company_id = fields.Many2one('res.company', string='Compañia', default=lambda self: self.env.company)


class mgmtsystemmaintenancefrequency(models.Model):
    _inherit = 'mgmtsystem.maintenance.frequency'

    company_id = fields.Many2one('res.company', string='Compañia', default=lambda self: self.env.company)


class mgmtsystemmaintenanceplan(models.Model):
    _inherit = 'mgmtsystem.maintenance.plan'

    company_id = fields.Many2one('res.company', string='Compañia', default=lambda self: self.env.company)


class mgmtsystemmaintenance(models.Model):
    _inherit = 'mgmtsystem.maintenance'

    company_id = fields.Many2one('res.company', string='Compañia', default=lambda self: self.env.company)


class mgmtsystemmaintenanceline(models.Model):
    _inherit = 'mgmtsystem.maintenance.line'

    company_id = fields.Many2one('res.company', string='Compañia', default=lambda self: self.env.company)


class legaltype(models.Model):
    _inherit = 'legal.type'

    company_id = fields.Many2one('res.company', string='Compañia', default=lambda self: self.env.company)


class legallegal(models.Model):
    _inherit = 'legal.legal'

    company_id = fields.Many2one('res.company', string='Compañia', default=lambda self: self.env.company)


class legalarticle(models.Model):
    _inherit = 'legal.article'

    company_id = fields.Many2one('res.company', string='Compañia', default=lambda self: self.env.company)


class legalarticledocument(models.Model):
    _inherit = 'legal.article.document'

    company_id = fields.Many2one('res.company', string='Compañia', default=lambda self: self.env.company)


class legalplancateg(models.Model):
    _inherit = 'legal.plan.categ'

    company_id = fields.Many2one('res.company', string='Compañia', default=lambda self: self.env.company)


class legalplan(models.Model):
    _inherit = 'legal.plan'

    company_id = fields.Many2one('res.company', string='Compañia', default=lambda self: self.env.company)


class legalplanline(models.Model):
    _inherit = 'legal.plan.line'

    company_id = fields.Many2one('res.company', string='Compañia', default=lambda self: self.env.company)


class legalplanhistoryline(models.Model):
    _inherit = 'legal.plan.history.line'

    company_id = fields.Many2one('res.company', string='Compañia', default=lambda self: self.env.company)


class legalplanhistory(models.Model):
    _inherit = 'legal.plan.history'

    company_id = fields.Many2one('res.company', string='Compañia', default=lambda self: self.env.company)


class managementreviewteam(models.Model):
    _inherit = 'management.review.team'

    company_id = fields.Many2one('res.company', string='Compañia', default=lambda self: self.env.company)


class managementreviewteamline(models.Model):
    _inherit = 'management.review.team.line'

    company_id = fields.Many2one('res.company', string='Compañia', default=lambda self: self.env.company)


class reviewteamjob(models.Model):
    _inherit = 'review.team.job'

    company_id = fields.Many2one('res.company', string='Compañia', default=lambda self: self.env.company)


class managementreviewplan(models.Model):
    _inherit = 'management.review.plan'

    company_id = fields.Many2one('res.company', string='Compañia', default=lambda self: self.env.company)


class managementreview(models.Model):
    _inherit = 'management.review'

    company_id = fields.Many2one('res.company', string='Compañia', default=lambda self: self.env.company)


class mgmtsystemmof(models.Model):
    _inherit = 'mgmtsystem.mof'

    company_id = fields.Many2one('res.company', string='Compañia', default=lambda self: self.env.company)


class mgmtsystemnonconformitytype(models.Model):
    _inherit = 'mgmtsystem.nonconformity.type'

    company_id = fields.Many2one('res.company', string='Compañia', default=lambda self: self.env.company)


class mgmtsystemnonconformity(models.Model):
    _inherit = 'mgmtsystem.nonconformity'

    company_id = fields.Many2one('res.company', string='Compañia', default=lambda self: self.env.company)


class mgmtsystemnonconformitycause_why(models.Model):
    _inherit = 'mgmtsystem.nonconformity.cause_why'

    company_id = fields.Many2one('res.company', string='Compañia', default=lambda self: self.env.company)


class mgmtsystemnonconformitywhy(models.Model):
    _inherit = 'mgmtsystem.nonconformity.why'

    company_id = fields.Many2one('res.company', string='Compañia', default=lambda self: self.env.company)


class mgmtsystemnonconformitycause(models.Model):
    _inherit = 'mgmtsystem.nonconformity.cause'

    company_id = fields.Many2one('res.company', string='Compañia', default=lambda self: self.env.company)


class evaluationresult(models.Model):
    _inherit = 'evaluation.result'

    company_id = fields.Many2one('res.company', string='Compañia', default=lambda self: self.env.company)


class evaluationevaluation(models.Model):
    _inherit = 'evaluation.evaluation'

    company_id = fields.Many2one('res.company', string='Compañia', default=lambda self: self.env.company)


class evaluationcriterio(models.Model):
    _inherit = 'evaluation.criterio'

    company_id = fields.Many2one('res.company', string='Compañia', default=lambda self: self.env.company)


class evaluationcriterioline(models.Model):
    _inherit = 'evaluation.criterio.line'

    company_id = fields.Many2one('res.company', string='Compañia', default=lambda self: self.env.company)


class matrixcateg(models.Model):
    _inherit = 'matrix.categ'

    company_id = fields.Many2one('res.company', string='Compañia', default=lambda self: self.env.company)


class matrixmatrix(models.Model):
    _inherit = 'matrix.matrix'

    company_id = fields.Many2one('res.company', string='Compañia', default=lambda self: self.env.company)


class matrixblock(models.Model):
    _inherit = 'matrix.block'

    company_id = fields.Many2one('res.company', string='Compañia', default=lambda self: self.env.company)


class matrixblocklineagent(models.Model):
    _inherit = 'matrix.block.line.agent'

    company_id = fields.Many2one('res.company', string='Compañia', default=lambda self: self.env.company)


class matrixblocklinetype(models.Model):
    _inherit = 'matrix.block.line.type'

    company_id = fields.Many2one('res.company', string='Compañia', default=lambda self: self.env.company)


class matrixblocklinesystem(models.Model):
    _inherit = 'matrix.block.line.system'

    company_id = fields.Many2one('res.company', string='Compañia', default=lambda self: self.env.company)


class matrixblockline(models.Model):
    _inherit = 'matrix.block.line'

    company_id = fields.Many2one('res.company', string='Compañia', default=lambda self: self.env.company)


class respartnerevaluation(models.Model):
    _inherit = 'res.partner.evaluation'

    company_id = fields.Many2one('res.company', string='Compañia', default=lambda self: self.env.company)
    active = fields.Boolean('Active', default=True)


class respartnerevaluationitem(models.Model):
    _inherit = 'res.partner.evaluation.item'

    company_id = fields.Many2one('res.company', string='Compañia', default=lambda self: self.env.company)
    active = fields.Boolean('Active', default=True)


class respartnerevaluationitemline(models.Model):
    _inherit = 'res.partner.evaluation.item.line'

    company_id = fields.Many2one('res.company', string='Compañia', default=lambda self: self.env.company)
    active = fields.Boolean('Active', default=True)


class respartnerevaluationhistory(models.Model):
    _inherit = 'res.partner.evaluation.history'

    company_id = fields.Many2one('res.company', string='Compañia', default=lambda self: self.env.company)
    active = fields.Boolean('Active', default=True)


class respartnerevaluationhistoryitem(models.Model):
    _inherit = 'res.partner.evaluation.history.item'

    company_id = fields.Many2one('res.company', string='Compañia', default=lambda self: self.env.company)
    active = fields.Boolean('Active', default=True)


class respartnerevaluationhistoryitemline(models.Model):
    _inherit = 'res.partner.evaluation.history.item.line'

    company_id = fields.Many2one('res.company', string='Compañia', default=lambda self: self.env.company)
    active = fields.Boolean('Active', default=True)


class evaluationinitial_evaluationitem(models.Model):
    _inherit = 'evaluation.initial_evaluation.item'

    company_id = fields.Many2one('res.company', string='Compañia', default=lambda self: self.env.company)
    active = fields.Boolean('Active', default=True)


class evaluationinitial_evaluation(models.Model):
    _inherit = 'evaluation.initial_evaluation'

    company_id = fields.Many2one('res.company', string='Compañia', default=lambda self: self.env.company)
    active = fields.Boolean('Active', default=True)


class respartnerinitial_evaluationitem(models.Model):
    _inherit = 'res.partner.initial_evaluation.item'

    company_id = fields.Many2one('res.company', string='Compañia', default=lambda self: self.env.company)
    active = fields.Boolean('Active', default=True)


class respartnerinitial_evaluation(models.Model):
    _inherit = 'res.partner.initial_evaluation'

    company_id = fields.Many2one('res.company', string='Compañia', default=lambda self: self.env.company)
    active = fields.Boolean('Active', default=True)


class mgmtcategtype(models.Model):
    _inherit = 'mgmt.categ.type'

    company_id = fields.Many2one('res.company', string='Compañia', default=lambda self: self.env.company)


class mgmtprocess(models.Model):
    _inherit = 'mgmt.process'

    company_id = fields.Many2one('res.company', string='Compañia', default=lambda self: self.env.company)


class reseconomyactivity(models.Model):
    _inherit = 'res.economy.activity'

    company_id = fields.Many2one('res.company', string='Compañia', default=lambda self: self.env.company)


class editionresponsableline(models.Model):
    _inherit = 'edition.responsable.line'

    company_id = fields.Many2one('res.company', string='Compañia', default=lambda self: self.env.company)


class editionabbreviation(models.Model):
    _inherit = 'edition.abbreviation'

    company_id = fields.Many2one('res.company', string='Compañia', default=lambda self: self.env.company)


class processeditiontemplate(models.Model):
    _inherit = 'process.edition.template'

    company_id = fields.Many2one('res.company', string='Compañia', default=lambda self: self.env.company)


class processedition(models.Model):
    _inherit = 'process.edition'

    company_id = fields.Many2one('res.company', string='Compañia', default=lambda self: self.env.company)


class processeditionhistory(models.Model):
    _inherit = 'process.edition.history'

    company_id = fields.Many2one('res.company', string='Compañia', default=lambda self: self.env.company)


class mgmtsystemaction(models.Model):
    _inherit = 'mgmtsystem.action'

    company_id = fields.Many2one('res.company', string='Compañia', default=lambda self: self.env.company)


class auditaudit(models.Model):
    _inherit = 'audit.audit'

    company_id = fields.Many2one('res.company', string='Compañia', default=lambda self: self.env.company)


class auditplan(models.Model):
    _inherit = 'audit.plan'

    company_id = fields.Many2one('res.company', string='Compañia', default=lambda self: self.env.company)


class complaintcomplaint(models.Model):
    _inherit = 'complaint.complaint'

    company_id = fields.Many2one('res.company', string='Compañia', default=lambda self: self.env.company)


class comunicationplan(models.Model):
    _inherit = 'comunication.plan'

    company_id = fields.Many2one('res.company', string='Compañia', default=lambda self: self.env.company)


class comunicationplanline(models.Model):
    _inherit = 'comunication.plan.line'

    company_id = fields.Many2one('res.company', string='Compañia', default=lambda self: self.env.company)


class recordmeeting(models.Model):
    _inherit = 'record.meeting'

    company_id = fields.Many2one('res.company', string='Compañia', default=lambda self: self.env.company)


class legalplan(models.Model):
    _inherit = 'legal.plan'

    company_id = fields.Many2one('res.company', string='Compañia', default=lambda self: self.env.company)


class legallegal(models.Model):
    _inherit = 'legal.legal'

    company_id = fields.Many2one('res.company', string='Compañia', default=lambda self: self.env.company)


class mgmtsystemcontextswot(models.Model):
    _inherit = 'mgmtsystem.context.swot'

    company_id = fields.Many2one('res.company', string='Compañia', default=lambda self: self.env.company)


class mgmtsystemcontextcrossswot(models.Model):
    _inherit = 'mgmtsystem.context.cross.swot'

    company_id = fields.Many2one('res.company', string='Compañia', default=lambda self: self.env.company)


class mgmtsystemnonconformity(models.Model):
    _inherit = 'mgmtsystem.nonconformity'

    company_id = fields.Many2one('res.company', string='Compañia', default=lambda self: self.env.company)


class matrixblocklineorigin(models.Model):
    _inherit = 'matrix.block.line.origin'

    company_id = fields.Many2one('res.company', string='Compañia', default=lambda self: self.env.company)


class mgmtsystemactionorigin(models.Model):
    _inherit = 'mgmtsystem.action.origin'

    company_id = fields.Many2one('res.company', string='Compañia', default=lambda self: self.env.company)


class mgmtsystemnonconformityorigin(models.Model):
    _inherit = 'mgmtsystem.nonconformity.origin'

    company_id = fields.Many2one('res.company', string='Compañia', default=lambda self: self.env.company)


class mgmtsystemtargetorigin(models.Model):
    _inherit = 'mgmtsystem.target.origin'

    company_id = fields.Many2one('res.company', string='Compañia', default=lambda self: self.env.company)


class mgmtprocessresourcetype(models.Model):
    _inherit = 'mgmt.process.resource.type'

    company_id = fields.Many2one('res.company', string='Compañia', default=lambda self: self.env.company)


class mgmtprocessresource(models.Model):
    _inherit = 'mgmt.process.resource'

    company_id = fields.Many2one('res.company', string='Compañia', default=lambda self: self.env.company)


class mgmtprocessinteraction(models.Model):
    _inherit = 'mgmt.process.interaction'

    company_id = fields.Many2one('res.company', string='Compañia', default=lambda self: self.env.company)


class mgmtprocesslinesupplier(models.Model):
    _inherit = 'mgmt.process.line.supplier'

    company_id = fields.Many2one('res.company', string='Compañia', default=lambda self: self.env.company)


class mgmtprocesslineclient_supplier(models.Model):
    _inherit = 'mgmt.process.line.client_supplier'

    company_id = fields.Many2one('res.company', string='Compañia', default=lambda self: self.env.company)


class mgmtprocessline(models.Model):
    _inherit = 'mgmt.process.line'

    company_id = fields.Many2one('res.company', string='Compañia', default=lambda self: self.env.company)


class mgmtprocesslineinput(models.Model):
    _inherit = 'mgmt.process.line.input'

    company_id = fields.Many2one('res.company', string='Compañia', default=lambda self: self.env.company)


class mgmtprocesslineoutput(models.Model):
    _inherit = 'mgmt.process.line.output'

    company_id = fields.Many2one('res.company', string='Compañia', default=lambda self: self.env.company)


class mgmtsystemtarget(models.Model):
    _inherit = 'mgmtsystem.target'

    company_id = fields.Many2one('res.company', string='Compañia', default=lambda self: self.env.company)


class mgmtsystemplan(models.Model):
    _inherit = 'mgmtsystem.plan'

    company_id = fields.Many2one('res.company', string='Compañia', default=lambda self: self.env.company)


class mgmtsystemplantraining(models.Model):
    _inherit = 'mgmtsystem.plan.training'

    company_id = fields.Many2one('res.company', string='Compañia', default=lambda self: self.env.company)


class mgmtsystemprocessdescription(models.Model):
    _inherit = 'mgmtsystem.process.description'

    company_id = fields.Many2one('res.company', string='Compañia', default=lambda self: self.env.company)


class mgmtsystemqualitymanual(models.Model):
    _inherit = 'mgmtsystem.qualitymanual'

    company_id = fields.Many2one('res.company', string='Compañia', default=lambda self: self.env.company)


class Survey(models.Model):
    _inherit = 'survey.survey'

    company_id = fields.Many2one('res.company', string='Compañia', default=lambda self: self.env.company)


class SurveyQuestion(models.Model):
    _inherit = 'survey.question'

    company_id = fields.Many2one('res.company', related='survey_id.company_id', string='Compañia', store=True)

class SurveyUserInput(models.Model):
    _inherit = 'survey.user_input'

    company_id = fields.Many2one('res.company', related='survey_id.company_id', string='Compañia', store=True)


class SurveyUserInputLine(models.Model):
    _inherit = 'survey.user_input_line'

    company_id = fields.Many2one('res.company', related='survey_id.company_id', string='Compañia', store=True)


class surveytype(models.Model):
    _inherit = 'survey.type'

    company_id = fields.Many2one('res.company', string='Compañia', default=lambda self: self.env.company)


class surveyreport(models.Model):
    _inherit = 'survey.report'

    company_id = fields.Many2one('res.company', string='Compañia', default=lambda self: self.env.company)


class surveyreportactionnonc(models.Model):
    _inherit = 'survey.report.actionnonc'

    company_id = fields.Many2one('res.company', string='Compañia', default=lambda self: self.env.company)


class mgmtsystemtargetresources(models.Model):
    _inherit = 'mgmtsystem.target.resources'

    company_id = fields.Many2one('res.company', string='Compañia', default=lambda self: self.env.company)


class mgmtsystemtargetcategory(models.Model):
    _inherit = 'mgmtsystem.target.category'

    company_id = fields.Many2one('res.company', string='Compañia', default=lambda self: self.env.company)


class mgmtsystemgoal(models.Model):
    _inherit = 'mgmtsystem.goal'

    company_id = fields.Many2one('res.company', string='Compañia', default=lambda self: self.env.company)


class mgmtsystemindicator(models.Model):
    _inherit = 'mgmtsystem.indicator'

    company_id = fields.Many2one('res.company', string='Compañia', default=lambda self: self.env.company)


class mgmtsystemindicatorhistory(models.Model):
    _inherit = 'mgmtsystem.indicator.history'

    company_id = fields.Many2one('res.company', string='Compañia', default=lambda self: self.env.company)


class soycalidadcomitteeposition(models.Model):
    _inherit = 'soycalidad.comittee.position'

    company_id = fields.Many2one('res.company', string='Compañia', default=lambda self: self.env.company)


class soycalidadcomitteefunction(models.Model):
    _inherit = 'soycalidad.comittee.function'

    company_id = fields.Many2one('res.company', string='Compañia', default=lambda self: self.env.company)


class soycalidadcomitteemember(models.Model):
    _inherit = 'soycalidad.comittee.member'

    company_id = fields.Many2one('res.company', string='Compañia', default=lambda self: self.env.company)


class soycalidadcomittee(models.Model):
    _inherit = 'soycalidad.comittee'

    company_id = fields.Many2one('res.company', string='Compañia', default=lambda self: self.env.company)


class soycalidadchange_requestorigin(models.Model):
    _inherit = 'soycalidad.change_request.origin'

    company_id = fields.Many2one('res.company', string='Compañia', default=lambda self: self.env.company)


class soycalidadimprove_planchange_type(models.Model):
    _inherit = 'soycalidad.improve_plan.change_type'

    company_id = fields.Many2one('res.company', string='Compañia', default=lambda self: self.env.company)


class soycalidadimprove_planresource(models.Model):
    _inherit = 'soycalidad.improve_plan.resource'

    company_id = fields.Many2one('res.company', string='Compañia', default=lambda self: self.env.company)


class soycalidadimprove_plan(models.Model):
    _inherit = 'soycalidad.improve_plan'

    company_id = fields.Many2one('res.company', string='Compañia', default=lambda self: self.env.company)


class soycalidadimprove_planmatrix(models.Model):
    _inherit = 'soycalidad.improve_plan.matrix'

    company_id = fields.Many2one('res.company', string='Compañia', default=lambda self: self.env.company)


class stockinspectionitem(models.Model):
    _inherit = 'stock.inspection.item'

    company_id = fields.Many2one('res.company', string='Compañia', default=lambda self: self.env.company)


class stockinspection(models.Model):
    _inherit = 'stock.inspection'

    company_id = fields.Many2one('res.company', string='Compañia', default=lambda self: self.env.company)


class stockpickinginspectionitem(models.Model):
    _inherit = 'stock.picking.inspection.item'

    company_id = fields.Many2one('res.company', string='Compañia', default=lambda self: self.env.company)


class stockpickinginspection(models.Model):
    _inherit = 'stock.picking.inspection'

    company_id = fields.Many2one('res.company', string='Compañia', default=lambda self: self.env.company)


class stock_inspectionstock_inspectionline(models.Model):
    _inherit = 'stock_inspection.stock_inspection.line'

    company_id = fields.Many2one('res.company', string='Compañia', default=lambda self: self.env.company)


class stock_inspectioncriterio(models.Model):
    _inherit = 'stock_inspection.criterio'

    company_id = fields.Many2one('res.company', string='Compañia', default=lambda self: self.env.company)


class stock_inspectionstock_inspection(models.Model):
    _inherit = 'stock_inspection.stock_inspection'

    company_id = fields.Many2one('res.company', string='Compañia', default=lambda self: self.env.company)
