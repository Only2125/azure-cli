# coding=utf-8
# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from knack.help_files import helps  # pylint: disable=unused-import
# pylint: disable=line-too-long, too-many-lines

helps['redis'] = """
type: group
short-summary: Manage dedicated Redis caches for your Azure applications.
"""

helps['redis create'] = """
type: command
short-summary: Create new Redis Cache instance.
"""

helps['redis export'] = """
type: command
short-summary: Export data stored in a Redis cache.
"""

helps['redis firewall-rules'] = """
type: group
short-summary: Manage Redis firewall rules.
"""

helps['redis firewall-rules create'] = """
type: command
short-summary: Create a redis cache firewall rule.
long-summary: Usage example - az redis firewall-rules create --name testCacheName --resource-group testResourceGroup  --start-ip 10.10.10.10 --end-ip 20.20.20.20 --rule-name 10to20
"""

helps['redis firewall-rules update'] = """
type: command
short-summary: Update a redis cache firewall rule.
"""

helps['redis import'] = """
type: command
short-summary: Import data into a Redis cache.
"""

helps['redis list'] = """
type: command
short-summary: List Redis Caches.
long-summary: Lists details about all caches within current Subscription or provided Resource Group.
"""

helps['redis patch-schedule'] = """
type: group
short-summary: Manage Redis patch schedules.
"""

helps['redis patch-schedule create'] = """
type: command
short-summary: Create patching schedule for Redis cache.
long-summary: Usage example - az redis patch-schedule create --name testCacheName --resource-group testResourceGroup --schedule-entries '[{"dayOfWeek":"Tuesday","startHourUtc":"00","maintenanceWindow":"PT5H"}]'
"""

helps['redis patch-schedule update'] = """
type: command
short-summary: Update the patching schedule for Redis cache.
long-summary: Usage example - az redis patch-schedule update --name testCacheName --resource-group testResourceGroup --schedule-entries '[{"dayOfWeek":"Tuesday","startHourUtc":"00","maintenanceWindow":"PT5H"}]'
"""

helps['redis server-link'] = """
type: group
short-summary: Manage Redis server links.
"""

helps['redis server-link create'] = """
type: command
short-summary: Adds a server link to the Redis cache (requires Premium SKU).
long-summary: Usage example - az redis server-link create --name testCacheName --resource-group testResourceGroup --cache-to-link secondTestCacheName --replication-role Secondary
"""

helps['redis update'] = """
type: command
short-summary: Update a Redis cache.
long-summary: Scale or update settings of a Redis cache.
"""
