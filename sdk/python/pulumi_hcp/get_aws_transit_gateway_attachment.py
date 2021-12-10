# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from . import _utilities

__all__ = [
    'GetAwsTransitGatewayAttachmentResult',
    'AwaitableGetAwsTransitGatewayAttachmentResult',
    'get_aws_transit_gateway_attachment',
    'get_aws_transit_gateway_attachment_output',
]

@pulumi.output_type
class GetAwsTransitGatewayAttachmentResult:
    """
    A collection of values returned by getAwsTransitGatewayAttachment.
    """
    def __init__(__self__, created_at=None, expires_at=None, hvn_id=None, id=None, organization_id=None, project_id=None, provider_transit_gateway_attachment_id=None, self_link=None, state=None, transit_gateway_attachment_id=None, transit_gateway_id=None, wait_for_active_state=None):
        if created_at and not isinstance(created_at, str):
            raise TypeError("Expected argument 'created_at' to be a str")
        pulumi.set(__self__, "created_at", created_at)
        if expires_at and not isinstance(expires_at, str):
            raise TypeError("Expected argument 'expires_at' to be a str")
        pulumi.set(__self__, "expires_at", expires_at)
        if hvn_id and not isinstance(hvn_id, str):
            raise TypeError("Expected argument 'hvn_id' to be a str")
        pulumi.set(__self__, "hvn_id", hvn_id)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if organization_id and not isinstance(organization_id, str):
            raise TypeError("Expected argument 'organization_id' to be a str")
        pulumi.set(__self__, "organization_id", organization_id)
        if project_id and not isinstance(project_id, str):
            raise TypeError("Expected argument 'project_id' to be a str")
        pulumi.set(__self__, "project_id", project_id)
        if provider_transit_gateway_attachment_id and not isinstance(provider_transit_gateway_attachment_id, str):
            raise TypeError("Expected argument 'provider_transit_gateway_attachment_id' to be a str")
        pulumi.set(__self__, "provider_transit_gateway_attachment_id", provider_transit_gateway_attachment_id)
        if self_link and not isinstance(self_link, str):
            raise TypeError("Expected argument 'self_link' to be a str")
        pulumi.set(__self__, "self_link", self_link)
        if state and not isinstance(state, str):
            raise TypeError("Expected argument 'state' to be a str")
        pulumi.set(__self__, "state", state)
        if transit_gateway_attachment_id and not isinstance(transit_gateway_attachment_id, str):
            raise TypeError("Expected argument 'transit_gateway_attachment_id' to be a str")
        pulumi.set(__self__, "transit_gateway_attachment_id", transit_gateway_attachment_id)
        if transit_gateway_id and not isinstance(transit_gateway_id, str):
            raise TypeError("Expected argument 'transit_gateway_id' to be a str")
        pulumi.set(__self__, "transit_gateway_id", transit_gateway_id)
        if wait_for_active_state and not isinstance(wait_for_active_state, bool):
            raise TypeError("Expected argument 'wait_for_active_state' to be a bool")
        pulumi.set(__self__, "wait_for_active_state", wait_for_active_state)

    @property
    @pulumi.getter(name="createdAt")
    def created_at(self) -> str:
        """
        The time that the transit gateway attachment was created.
        """
        return pulumi.get(self, "created_at")

    @property
    @pulumi.getter(name="expiresAt")
    def expires_at(self) -> str:
        """
        The time after which the transit gateway attachment will be considered expired if it hasn't transitioned into `ACCEPTED` or `ACTIVE` state.
        """
        return pulumi.get(self, "expires_at")

    @property
    @pulumi.getter(name="hvnId")
    def hvn_id(self) -> str:
        """
        The ID of the HashiCorp Virtual Network (HVN).
        """
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
        """
        The ID of the HCP organization where the transit gateway attachment is located. Always matches the HVN's organization.
        """
        return pulumi.get(self, "organization_id")

    @property
    @pulumi.getter(name="projectId")
    def project_id(self) -> str:
        """
        The ID of the HCP project where the transit gateway attachment is located. Always matches the HVN's project.
        """
        return pulumi.get(self, "project_id")

    @property
    @pulumi.getter(name="providerTransitGatewayAttachmentId")
    def provider_transit_gateway_attachment_id(self) -> str:
        """
        The transit gateway attachment ID used by AWS.
        """
        return pulumi.get(self, "provider_transit_gateway_attachment_id")

    @property
    @pulumi.getter(name="selfLink")
    def self_link(self) -> str:
        """
        A unique URL identifying the transit gateway attachment.
        """
        return pulumi.get(self, "self_link")

    @property
    @pulumi.getter
    def state(self) -> str:
        """
        The state of the transit gateway attachment.
        """
        return pulumi.get(self, "state")

    @property
    @pulumi.getter(name="transitGatewayAttachmentId")
    def transit_gateway_attachment_id(self) -> str:
        """
        The user-settable name of the transit gateway attachment in HCP.
        """
        return pulumi.get(self, "transit_gateway_attachment_id")

    @property
    @pulumi.getter(name="transitGatewayId")
    def transit_gateway_id(self) -> str:
        """
        The ID of the user-owned transit gateway in AWS.
        """
        return pulumi.get(self, "transit_gateway_id")

    @property
    @pulumi.getter(name="waitForActiveState")
    def wait_for_active_state(self) -> Optional[bool]:
        return pulumi.get(self, "wait_for_active_state")


class AwaitableGetAwsTransitGatewayAttachmentResult(GetAwsTransitGatewayAttachmentResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetAwsTransitGatewayAttachmentResult(
            created_at=self.created_at,
            expires_at=self.expires_at,
            hvn_id=self.hvn_id,
            id=self.id,
            organization_id=self.organization_id,
            project_id=self.project_id,
            provider_transit_gateway_attachment_id=self.provider_transit_gateway_attachment_id,
            self_link=self.self_link,
            state=self.state,
            transit_gateway_attachment_id=self.transit_gateway_attachment_id,
            transit_gateway_id=self.transit_gateway_id,
            wait_for_active_state=self.wait_for_active_state)


def get_aws_transit_gateway_attachment(hvn_id: Optional[str] = None,
                                       transit_gateway_attachment_id: Optional[str] = None,
                                       wait_for_active_state: Optional[bool] = None,
                                       opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetAwsTransitGatewayAttachmentResult:
    """
    The AWS transit gateway attachment data source provides information about an existing transit gateway attachment.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_hcp as hcp

    test = hcp.get_aws_transit_gateway_attachment(hvn_id=var["hvn_id"],
        transit_gateway_attachment_id=var["transit_gateway_attachment_id"])
    ```


    :param str hvn_id: The ID of the HashiCorp Virtual Network (HVN).
    :param str transit_gateway_attachment_id: The user-settable name of the transit gateway attachment in HCP.
    """
    __args__ = dict()
    __args__['hvnId'] = hvn_id
    __args__['transitGatewayAttachmentId'] = transit_gateway_attachment_id
    __args__['waitForActiveState'] = wait_for_active_state
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = _utilities.get_version()
    __ret__ = pulumi.runtime.invoke('hcp:index/getAwsTransitGatewayAttachment:getAwsTransitGatewayAttachment', __args__, opts=opts, typ=GetAwsTransitGatewayAttachmentResult).value

    return AwaitableGetAwsTransitGatewayAttachmentResult(
        created_at=__ret__.created_at,
        expires_at=__ret__.expires_at,
        hvn_id=__ret__.hvn_id,
        id=__ret__.id,
        organization_id=__ret__.organization_id,
        project_id=__ret__.project_id,
        provider_transit_gateway_attachment_id=__ret__.provider_transit_gateway_attachment_id,
        self_link=__ret__.self_link,
        state=__ret__.state,
        transit_gateway_attachment_id=__ret__.transit_gateway_attachment_id,
        transit_gateway_id=__ret__.transit_gateway_id,
        wait_for_active_state=__ret__.wait_for_active_state)


@_utilities.lift_output_func(get_aws_transit_gateway_attachment)
def get_aws_transit_gateway_attachment_output(hvn_id: Optional[pulumi.Input[str]] = None,
                                              transit_gateway_attachment_id: Optional[pulumi.Input[str]] = None,
                                              wait_for_active_state: Optional[pulumi.Input[Optional[bool]]] = None,
                                              opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetAwsTransitGatewayAttachmentResult]:
    """
    The AWS transit gateway attachment data source provides information about an existing transit gateway attachment.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_hcp as hcp

    test = hcp.get_aws_transit_gateway_attachment(hvn_id=var["hvn_id"],
        transit_gateway_attachment_id=var["transit_gateway_attachment_id"])
    ```


    :param str hvn_id: The ID of the HashiCorp Virtual Network (HVN).
    :param str transit_gateway_attachment_id: The user-settable name of the transit gateway attachment in HCP.
    """
    ...