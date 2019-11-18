﻿# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------


# pylint: disable=line-too-long

from azure.cli.core.commands.parameters import (get_enum_type, get_three_state_flag)

from azure.mgmt.reservations.models import (
    ReservedResourceType,
    InstanceFlexibility,
    AppliedScopeType,
    BillingPlan
)


def load_arguments(self, _):
    with self.argument_context('reservations reservation update') as c:
        c.argument('applied_scope_type', options_list=['--applied-scope-type', '-t'], arg_type=get_enum_type(AppliedScopeType))
        c.argument('applied_scopes', options_list=['--applied-scopes', '-s'])
        c.argument('instance_flexibility', options_list=['--instance-flexibility', '-i'], arg_type=get_enum_type(InstanceFlexibility))

    with self.argument_context('reservations reservation split') as c:
        c.argument('quantity_1', options_list=['--quantity-1', '-1'])
        c.argument('quantity_2', options_list=['--quantity-2', '-2'])

    with self.argument_context('reservations reservation merge') as c:
        c.argument('reservation_id_1', options_list=['--reservation-id-1', '-1'])
        c.argument('reservation_id_2', options_list=['--reservation-id-2', '-2'])

    with self.argument_context('reservations catalog show') as c:
        c.argument('reserved_resource_type', arg_type=get_enum_type(ReservedResourceType))

    with self.argument_context('reservations reservation-order calculate') as c:
        c.argument('billing_scope_id', options_list=['--scope'])
        c.argument('reserved_resource_properties', options_list=['--reserved-resource-properties'])
        c.argument('renew', arg_type=get_three_state_flag())
        c.argument('reserved_resource_type', arg_type=get_enum_type(ReservedResourceType))
        c.argument('applied_scope_type', options_list=['--applied-scope-type'], arg_type=get_enum_type(AppliedScopeType))

    with self.argument_context('reservations reservation-order purchase') as c:
        c.argument('billing_scope_id', options_list=['--scope'])
        c.argument('reserved_resource_properties', options_list=['--reserved-resource-properties'])
        c.argument('renew', arg_type=get_three_state_flag())
        c.argument('reserved_resource_type', arg_type=get_enum_type(ReservedResourceType))
        c.argument('applied_scope_type', options_list=['--applied-scope-type'], arg_type=get_enum_type(AppliedScopeType))
