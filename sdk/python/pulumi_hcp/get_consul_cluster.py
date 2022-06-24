# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from . import _utilities

__all__ = [
    'GetConsulClusterResult',
    'AwaitableGetConsulClusterResult',
    'get_consul_cluster',
    'get_consul_cluster_output',
]

@pulumi.output_type
class GetConsulClusterResult:
    """
    A collection of values returned by getConsulCluster.
    """
    def __init__(__self__, auto_hvn_to_hvn_peering=None, cloud_provider=None, cluster_id=None, connect_enabled=None, consul_automatic_upgrades=None, consul_ca_file=None, consul_config_file=None, consul_private_endpoint_url=None, consul_public_endpoint_url=None, consul_snapshot_interval=None, consul_snapshot_retention=None, consul_version=None, datacenter=None, hvn_id=None, id=None, organization_id=None, primary_link=None, project_id=None, public_endpoint=None, region=None, scale=None, self_link=None, size=None, tier=None):
        if auto_hvn_to_hvn_peering and not isinstance(auto_hvn_to_hvn_peering, bool):
            raise TypeError("Expected argument 'auto_hvn_to_hvn_peering' to be a bool")
        pulumi.set(__self__, "auto_hvn_to_hvn_peering", auto_hvn_to_hvn_peering)
        if cloud_provider and not isinstance(cloud_provider, str):
            raise TypeError("Expected argument 'cloud_provider' to be a str")
        pulumi.set(__self__, "cloud_provider", cloud_provider)
        if cluster_id and not isinstance(cluster_id, str):
            raise TypeError("Expected argument 'cluster_id' to be a str")
        pulumi.set(__self__, "cluster_id", cluster_id)
        if connect_enabled and not isinstance(connect_enabled, bool):
            raise TypeError("Expected argument 'connect_enabled' to be a bool")
        pulumi.set(__self__, "connect_enabled", connect_enabled)
        if consul_automatic_upgrades and not isinstance(consul_automatic_upgrades, bool):
            raise TypeError("Expected argument 'consul_automatic_upgrades' to be a bool")
        pulumi.set(__self__, "consul_automatic_upgrades", consul_automatic_upgrades)
        if consul_ca_file and not isinstance(consul_ca_file, str):
            raise TypeError("Expected argument 'consul_ca_file' to be a str")
        pulumi.set(__self__, "consul_ca_file", consul_ca_file)
        if consul_config_file and not isinstance(consul_config_file, str):
            raise TypeError("Expected argument 'consul_config_file' to be a str")
        pulumi.set(__self__, "consul_config_file", consul_config_file)
        if consul_private_endpoint_url and not isinstance(consul_private_endpoint_url, str):
            raise TypeError("Expected argument 'consul_private_endpoint_url' to be a str")
        pulumi.set(__self__, "consul_private_endpoint_url", consul_private_endpoint_url)
        if consul_public_endpoint_url and not isinstance(consul_public_endpoint_url, str):
            raise TypeError("Expected argument 'consul_public_endpoint_url' to be a str")
        pulumi.set(__self__, "consul_public_endpoint_url", consul_public_endpoint_url)
        if consul_snapshot_interval and not isinstance(consul_snapshot_interval, str):
            raise TypeError("Expected argument 'consul_snapshot_interval' to be a str")
        pulumi.set(__self__, "consul_snapshot_interval", consul_snapshot_interval)
        if consul_snapshot_retention and not isinstance(consul_snapshot_retention, str):
            raise TypeError("Expected argument 'consul_snapshot_retention' to be a str")
        pulumi.set(__self__, "consul_snapshot_retention", consul_snapshot_retention)
        if consul_version and not isinstance(consul_version, str):
            raise TypeError("Expected argument 'consul_version' to be a str")
        pulumi.set(__self__, "consul_version", consul_version)
        if datacenter and not isinstance(datacenter, str):
            raise TypeError("Expected argument 'datacenter' to be a str")
        pulumi.set(__self__, "datacenter", datacenter)
        if hvn_id and not isinstance(hvn_id, str):
            raise TypeError("Expected argument 'hvn_id' to be a str")
        pulumi.set(__self__, "hvn_id", hvn_id)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if organization_id and not isinstance(organization_id, str):
            raise TypeError("Expected argument 'organization_id' to be a str")
        pulumi.set(__self__, "organization_id", organization_id)
        if primary_link and not isinstance(primary_link, str):
            raise TypeError("Expected argument 'primary_link' to be a str")
        pulumi.set(__self__, "primary_link", primary_link)
        if project_id and not isinstance(project_id, str):
            raise TypeError("Expected argument 'project_id' to be a str")
        pulumi.set(__self__, "project_id", project_id)
        if public_endpoint and not isinstance(public_endpoint, bool):
            raise TypeError("Expected argument 'public_endpoint' to be a bool")
        pulumi.set(__self__, "public_endpoint", public_endpoint)
        if region and not isinstance(region, str):
            raise TypeError("Expected argument 'region' to be a str")
        pulumi.set(__self__, "region", region)
        if scale and not isinstance(scale, int):
            raise TypeError("Expected argument 'scale' to be a int")
        pulumi.set(__self__, "scale", scale)
        if self_link and not isinstance(self_link, str):
            raise TypeError("Expected argument 'self_link' to be a str")
        pulumi.set(__self__, "self_link", self_link)
        if size and not isinstance(size, str):
            raise TypeError("Expected argument 'size' to be a str")
        pulumi.set(__self__, "size", size)
        if tier and not isinstance(tier, str):
            raise TypeError("Expected argument 'tier' to be a str")
        pulumi.set(__self__, "tier", tier)

    @property
    @pulumi.getter(name="autoHvnToHvnPeering")
    def auto_hvn_to_hvn_peering(self) -> bool:
        return pulumi.get(self, "auto_hvn_to_hvn_peering")

    @property
    @pulumi.getter(name="cloudProvider")
    def cloud_provider(self) -> str:
        return pulumi.get(self, "cloud_provider")

    @property
    @pulumi.getter(name="clusterId")
    def cluster_id(self) -> str:
        return pulumi.get(self, "cluster_id")

    @property
    @pulumi.getter(name="connectEnabled")
    def connect_enabled(self) -> bool:
        return pulumi.get(self, "connect_enabled")

    @property
    @pulumi.getter(name="consulAutomaticUpgrades")
    def consul_automatic_upgrades(self) -> bool:
        return pulumi.get(self, "consul_automatic_upgrades")

    @property
    @pulumi.getter(name="consulCaFile")
    def consul_ca_file(self) -> str:
        return pulumi.get(self, "consul_ca_file")

    @property
    @pulumi.getter(name="consulConfigFile")
    def consul_config_file(self) -> str:
        return pulumi.get(self, "consul_config_file")

    @property
    @pulumi.getter(name="consulPrivateEndpointUrl")
    def consul_private_endpoint_url(self) -> str:
        return pulumi.get(self, "consul_private_endpoint_url")

    @property
    @pulumi.getter(name="consulPublicEndpointUrl")
    def consul_public_endpoint_url(self) -> str:
        return pulumi.get(self, "consul_public_endpoint_url")

    @property
    @pulumi.getter(name="consulSnapshotInterval")
    def consul_snapshot_interval(self) -> str:
        return pulumi.get(self, "consul_snapshot_interval")

    @property
    @pulumi.getter(name="consulSnapshotRetention")
    def consul_snapshot_retention(self) -> str:
        return pulumi.get(self, "consul_snapshot_retention")

    @property
    @pulumi.getter(name="consulVersion")
    def consul_version(self) -> str:
        return pulumi.get(self, "consul_version")

    @property
    @pulumi.getter
    def datacenter(self) -> str:
        return pulumi.get(self, "datacenter")

    @property
    @pulumi.getter(name="hvnId")
    def hvn_id(self) -> str:
        return pulumi.get(self, "hvn_id")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The provider-assigned unique ID for this managed resource.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="organizationId")
    def organization_id(self) -> str:
        return pulumi.get(self, "organization_id")

    @property
    @pulumi.getter(name="primaryLink")
    def primary_link(self) -> str:
        return pulumi.get(self, "primary_link")

    @property
    @pulumi.getter(name="projectId")
    def project_id(self) -> str:
        return pulumi.get(self, "project_id")

    @property
    @pulumi.getter(name="publicEndpoint")
    def public_endpoint(self) -> bool:
        return pulumi.get(self, "public_endpoint")

    @property
    @pulumi.getter
    def region(self) -> str:
        return pulumi.get(self, "region")

    @property
    @pulumi.getter
    def scale(self) -> int:
        return pulumi.get(self, "scale")

    @property
    @pulumi.getter(name="selfLink")
    def self_link(self) -> str:
        return pulumi.get(self, "self_link")

    @property
    @pulumi.getter
    def size(self) -> str:
        return pulumi.get(self, "size")

    @property
    @pulumi.getter
    def tier(self) -> str:
        return pulumi.get(self, "tier")


class AwaitableGetConsulClusterResult(GetConsulClusterResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetConsulClusterResult(
            auto_hvn_to_hvn_peering=self.auto_hvn_to_hvn_peering,
            cloud_provider=self.cloud_provider,
            cluster_id=self.cluster_id,
            connect_enabled=self.connect_enabled,
            consul_automatic_upgrades=self.consul_automatic_upgrades,
            consul_ca_file=self.consul_ca_file,
            consul_config_file=self.consul_config_file,
            consul_private_endpoint_url=self.consul_private_endpoint_url,
            consul_public_endpoint_url=self.consul_public_endpoint_url,
            consul_snapshot_interval=self.consul_snapshot_interval,
            consul_snapshot_retention=self.consul_snapshot_retention,
            consul_version=self.consul_version,
            datacenter=self.datacenter,
            hvn_id=self.hvn_id,
            id=self.id,
            organization_id=self.organization_id,
            primary_link=self.primary_link,
            project_id=self.project_id,
            public_endpoint=self.public_endpoint,
            region=self.region,
            scale=self.scale,
            self_link=self.self_link,
            size=self.size,
            tier=self.tier)


def get_consul_cluster(cluster_id: Optional[str] = None,
                       opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetConsulClusterResult:
    """
    The cluster data source provides information about an existing HCP Consul cluster.
    """
    __args__ = dict()
    __args__['clusterId'] = cluster_id
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('hcp:index/getConsulCluster:getConsulCluster', __args__, opts=opts, typ=GetConsulClusterResult).value

    return AwaitableGetConsulClusterResult(
        auto_hvn_to_hvn_peering=__ret__.auto_hvn_to_hvn_peering,
        cloud_provider=__ret__.cloud_provider,
        cluster_id=__ret__.cluster_id,
        connect_enabled=__ret__.connect_enabled,
        consul_automatic_upgrades=__ret__.consul_automatic_upgrades,
        consul_ca_file=__ret__.consul_ca_file,
        consul_config_file=__ret__.consul_config_file,
        consul_private_endpoint_url=__ret__.consul_private_endpoint_url,
        consul_public_endpoint_url=__ret__.consul_public_endpoint_url,
        consul_snapshot_interval=__ret__.consul_snapshot_interval,
        consul_snapshot_retention=__ret__.consul_snapshot_retention,
        consul_version=__ret__.consul_version,
        datacenter=__ret__.datacenter,
        hvn_id=__ret__.hvn_id,
        id=__ret__.id,
        organization_id=__ret__.organization_id,
        primary_link=__ret__.primary_link,
        project_id=__ret__.project_id,
        public_endpoint=__ret__.public_endpoint,
        region=__ret__.region,
        scale=__ret__.scale,
        self_link=__ret__.self_link,
        size=__ret__.size,
        tier=__ret__.tier)


@_utilities.lift_output_func(get_consul_cluster)
def get_consul_cluster_output(cluster_id: Optional[pulumi.Input[str]] = None,
                              opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetConsulClusterResult]:
    """
    The cluster data source provides information about an existing HCP Consul cluster.
    """
    ...
