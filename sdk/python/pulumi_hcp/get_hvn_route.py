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
    'GetHvnRouteResult',
    'AwaitableGetHvnRouteResult',
    'get_hvn_route',
    'get_hvn_route_output',
]

@pulumi.output_type
class GetHvnRouteResult:
    """
    A collection of values returned by getHvnRoute.
    """
    def __init__(__self__, created_at=None, destination_cidr=None, hvn_link=None, hvn_route_id=None, id=None, self_link=None, state=None, target_link=None):
        if created_at and not isinstance(created_at, str):
            raise TypeError("Expected argument 'created_at' to be a str")
        pulumi.set(__self__, "created_at", created_at)
        if destination_cidr and not isinstance(destination_cidr, str):
            raise TypeError("Expected argument 'destination_cidr' to be a str")
        pulumi.set(__self__, "destination_cidr", destination_cidr)
        if hvn_link and not isinstance(hvn_link, str):
            raise TypeError("Expected argument 'hvn_link' to be a str")
        pulumi.set(__self__, "hvn_link", hvn_link)
        if hvn_route_id and not isinstance(hvn_route_id, str):
            raise TypeError("Expected argument 'hvn_route_id' to be a str")
        pulumi.set(__self__, "hvn_route_id", hvn_route_id)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if self_link and not isinstance(self_link, str):
            raise TypeError("Expected argument 'self_link' to be a str")
        pulumi.set(__self__, "self_link", self_link)
        if state and not isinstance(state, str):
            raise TypeError("Expected argument 'state' to be a str")
        pulumi.set(__self__, "state", state)
        if target_link and not isinstance(target_link, str):
            raise TypeError("Expected argument 'target_link' to be a str")
        pulumi.set(__self__, "target_link", target_link)

    @property
    @pulumi.getter(name="createdAt")
    def created_at(self) -> str:
        return pulumi.get(self, "created_at")

    @property
    @pulumi.getter(name="destinationCidr")
    def destination_cidr(self) -> str:
        return pulumi.get(self, "destination_cidr")

    @property
    @pulumi.getter(name="hvnLink")
    def hvn_link(self) -> str:
        return pulumi.get(self, "hvn_link")

    @property
    @pulumi.getter(name="hvnRouteId")
    def hvn_route_id(self) -> str:
        return pulumi.get(self, "hvn_route_id")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The provider-assigned unique ID for this managed resource.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="selfLink")
    def self_link(self) -> str:
        return pulumi.get(self, "self_link")

    @property
    @pulumi.getter
    def state(self) -> str:
        return pulumi.get(self, "state")

    @property
    @pulumi.getter(name="targetLink")
    def target_link(self) -> str:
        return pulumi.get(self, "target_link")


class AwaitableGetHvnRouteResult(GetHvnRouteResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetHvnRouteResult(
            created_at=self.created_at,
            destination_cidr=self.destination_cidr,
            hvn_link=self.hvn_link,
            hvn_route_id=self.hvn_route_id,
            id=self.id,
            self_link=self.self_link,
            state=self.state,
            target_link=self.target_link)


def get_hvn_route(hvn_link: Optional[str] = None,
                  hvn_route_id: Optional[str] = None,
                  opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetHvnRouteResult:
    """
    The HVN route data source provides information about an existing HVN route.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_hcp as hcp

    example = hcp.get_hvn_route(hvn_link=var["hvn_link"],
        destination_cidr=var["hvn_route_id"])
    ```
    """
    __args__ = dict()
    __args__['hvnLink'] = hvn_link
    __args__['hvnRouteId'] = hvn_route_id
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('hcp:index/getHvnRoute:getHvnRoute', __args__, opts=opts, typ=GetHvnRouteResult).value

    return AwaitableGetHvnRouteResult(
        created_at=__ret__.created_at,
        destination_cidr=__ret__.destination_cidr,
        hvn_link=__ret__.hvn_link,
        hvn_route_id=__ret__.hvn_route_id,
        id=__ret__.id,
        self_link=__ret__.self_link,
        state=__ret__.state,
        target_link=__ret__.target_link)


@_utilities.lift_output_func(get_hvn_route)
def get_hvn_route_output(hvn_link: Optional[pulumi.Input[str]] = None,
                         hvn_route_id: Optional[pulumi.Input[str]] = None,
                         opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetHvnRouteResult]:
    """
    The HVN route data source provides information about an existing HVN route.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_hcp as hcp

    example = hcp.get_hvn_route(hvn_link=var["hvn_link"],
        destination_cidr=var["hvn_route_id"])
    ```
    """
    ...
