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
    'GetConsulVersionsResult',
    'AwaitableGetConsulVersionsResult',
    'get_consul_versions',
]

@pulumi.output_type
class GetConsulVersionsResult:
    """
    A collection of values returned by getConsulVersions.
    """
    def __init__(__self__, availables=None, id=None, previews=None, recommended=None):
        if availables and not isinstance(availables, list):
            raise TypeError("Expected argument 'availables' to be a list")
        pulumi.set(__self__, "availables", availables)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if previews and not isinstance(previews, list):
            raise TypeError("Expected argument 'previews' to be a list")
        pulumi.set(__self__, "previews", previews)
        if recommended and not isinstance(recommended, str):
            raise TypeError("Expected argument 'recommended' to be a str")
        pulumi.set(__self__, "recommended", recommended)

    @property
    @pulumi.getter
    def availables(self) -> Sequence[str]:
        return pulumi.get(self, "availables")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The provider-assigned unique ID for this managed resource.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def previews(self) -> Sequence[str]:
        return pulumi.get(self, "previews")

    @property
    @pulumi.getter
    def recommended(self) -> str:
        return pulumi.get(self, "recommended")


class AwaitableGetConsulVersionsResult(GetConsulVersionsResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetConsulVersionsResult(
            availables=self.availables,
            id=self.id,
            previews=self.previews,
            recommended=self.recommended)


def get_consul_versions(opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetConsulVersionsResult:
    """
    The Consul versions data source provides the Consul versions supported by HCP.
    """
    __args__ = dict()
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('hcp:index/getConsulVersions:getConsulVersions', __args__, opts=opts, typ=GetConsulVersionsResult).value

    return AwaitableGetConsulVersionsResult(
        availables=__ret__.availables,
        id=__ret__.id,
        previews=__ret__.previews,
        recommended=__ret__.recommended)
