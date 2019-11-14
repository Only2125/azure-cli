# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from azure.mgmt.reservations.models import (Patch, PurchaseRequest, SkuName)
from azure.cli.command_modules.reservations._client_factory import (reservation_order_mgmt_client_factory)

def cli_reservation_update_reservation(client, reservation_order_id, reservation_id,
                                       applied_scope_type, applied_scopes=None,
                                       instance_flexibility=None):
    if applied_scopes:
        patch = Patch(applied_scope_type=applied_scope_type,
                      applied_scopes=[applied_scopes],
                      instance_flexibility=instance_flexibility)
    else:
        patch = Patch(applied_scope_type=applied_scope_type,
                      instance_flexibility=instance_flexibility)
    return client.update(reservation_order_id, reservation_id, patch)


def create_resource_id(reservation_order_id, reservation_id):
    template = '/providers/Microsoft.Capacity/reservationOrders/{0}/reservations/{1}'
    return template.format(reservation_order_id, reservation_id)


def cli_reservation_split_reservation(client, reservation_order_id,
                                      reservation_id, quantity_1, quantity_2):
    reservationToSplit = create_resource_id(reservation_order_id, reservation_id)
    return client.split(reservation_order_id, [quantity_1, quantity_2], reservationToSplit)


def cli_reservation_merge_reservation(client, reservation_order_id,
                                      reservation_id_1, reservation_id_2):
    return client.merge(reservation_order_id,
                        [create_resource_id(reservation_order_id, reservation_id_1),
                         create_resource_id(reservation_order_id, reservation_id_2)])


def cli_calculate(client, sku, location, reserved_resource_type, billing_scope_id, term,
                 billing_plan, quantity, applied_scope_type, display_name, applied_scopes=None,
                  renew=False, reserved_resource_properties=None):
    skuN = SkuName(name=sku)
    body = PurchaseRequest(sku=skuN, location= location, reserved_resource_type=reserved_resource_type, 
                            billing_scope_id=billing_scope_id, term=term, quantity=quantity, display_name=display_name,
                            applied_scope_type=applied_scope_type,applied_scopes=applied_scopes,
                            renew=renew, reserved_resource_properties=reserved_resource_properties)
    return client.calculate(body)


def cli_purchase(client, reservation_order_id, sku, location, reserved_resource_type, billing_scope_id, term,
                 billing_plan, quantity, applied_scope_type, display_name, applied_scopes=None,
                  renew=False, reserved_resource_properties=None):
    skuN = SkuName(name=sku)
    body = PurchaseRequest(sku=skuN, location= location, reserved_resource_type=reserved_resource_type, 
                            billing_scope_id=billing_scope_id, term=term, quantity=quantity, display_name=display_name,
                            applied_scope_type=applied_scope_type,applied_scopes=applied_scopes,
                            renew=renew, reserved_resource_properties=reserved_resource_properties)
    return client.purchase(reservation_order_id, body)