from neutron_lib import exceptions as n_exc
from neutron.db import common_db_mixin

class CommonDbMixin(common_db_mixin.CommonDbMixin):

    def _get_tenant_id_for_create(self, context, resource):
        if context.is_admin and 'tenant_id' in resource:
            tenant_id = resource['tenant_id']
        elif ('tenant_id' in resource and
              resource['tenant_id'] != context.tenant_id):
            reason = _('Cannot create resource for another tenant')
            raise n_exc.AdminRequired(reason=reason)
        else:
            tenant_id = context.tenant_id
        return tenant_id
#         tenant_id = res.get('tenant_id', None)
#         if tenant_id:
#             return tenant_id
#         else:
#             return context.tenant_id
