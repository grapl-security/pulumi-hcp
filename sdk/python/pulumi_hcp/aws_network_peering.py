# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from . import _utilities

__all__ = ['AwsNetworkPeeringArgs', 'AwsNetworkPeering']

@pulumi.input_type
class AwsNetworkPeeringArgs:
    def __init__(__self__, *,
                 hvn_id: pulumi.Input[str],
                 peer_account_id: pulumi.Input[str],
                 peer_vpc_id: pulumi.Input[str],
                 peer_vpc_region: pulumi.Input[str],
                 peering_id: pulumi.Input[str]):
        """
        The set of arguments for constructing a AwsNetworkPeering resource.
        :param pulumi.Input[str] hvn_id: The ID of the HashiCorp Virtual Network (HVN).
        :param pulumi.Input[str] peer_account_id: The account ID of the peer VPC in AWS.
        :param pulumi.Input[str] peer_vpc_id: The ID of the peer VPC in AWS.
        :param pulumi.Input[str] peer_vpc_region: The region of the peer VPC in AWS.
        :param pulumi.Input[str] peering_id: The ID of the network peering.
        """
        pulumi.set(__self__, "hvn_id", hvn_id)
        pulumi.set(__self__, "peer_account_id", peer_account_id)
        pulumi.set(__self__, "peer_vpc_id", peer_vpc_id)
        pulumi.set(__self__, "peer_vpc_region", peer_vpc_region)
        pulumi.set(__self__, "peering_id", peering_id)

    @property
    @pulumi.getter(name="hvnId")
    def hvn_id(self) -> pulumi.Input[str]:
        """
        The ID of the HashiCorp Virtual Network (HVN).
        """
        return pulumi.get(self, "hvn_id")

    @hvn_id.setter
    def hvn_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "hvn_id", value)

    @property
    @pulumi.getter(name="peerAccountId")
    def peer_account_id(self) -> pulumi.Input[str]:
        """
        The account ID of the peer VPC in AWS.
        """
        return pulumi.get(self, "peer_account_id")

    @peer_account_id.setter
    def peer_account_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "peer_account_id", value)

    @property
    @pulumi.getter(name="peerVpcId")
    def peer_vpc_id(self) -> pulumi.Input[str]:
        """
        The ID of the peer VPC in AWS.
        """
        return pulumi.get(self, "peer_vpc_id")

    @peer_vpc_id.setter
    def peer_vpc_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "peer_vpc_id", value)

    @property
    @pulumi.getter(name="peerVpcRegion")
    def peer_vpc_region(self) -> pulumi.Input[str]:
        """
        The region of the peer VPC in AWS.
        """
        return pulumi.get(self, "peer_vpc_region")

    @peer_vpc_region.setter
    def peer_vpc_region(self, value: pulumi.Input[str]):
        pulumi.set(self, "peer_vpc_region", value)

    @property
    @pulumi.getter(name="peeringId")
    def peering_id(self) -> pulumi.Input[str]:
        """
        The ID of the network peering.
        """
        return pulumi.get(self, "peering_id")

    @peering_id.setter
    def peering_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "peering_id", value)


@pulumi.input_type
class _AwsNetworkPeeringState:
    def __init__(__self__, *,
                 created_at: Optional[pulumi.Input[str]] = None,
                 expires_at: Optional[pulumi.Input[str]] = None,
                 hvn_id: Optional[pulumi.Input[str]] = None,
                 organization_id: Optional[pulumi.Input[str]] = None,
                 peer_account_id: Optional[pulumi.Input[str]] = None,
                 peer_vpc_id: Optional[pulumi.Input[str]] = None,
                 peer_vpc_region: Optional[pulumi.Input[str]] = None,
                 peering_id: Optional[pulumi.Input[str]] = None,
                 project_id: Optional[pulumi.Input[str]] = None,
                 provider_peering_id: Optional[pulumi.Input[str]] = None,
                 self_link: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering AwsNetworkPeering resources.
        :param pulumi.Input[str] created_at: The time that the network peering was created.
        :param pulumi.Input[str] expires_at: The time after which the network peering will be considered expired if it hasn't transitioned into `ACCEPTED` or
               `ACTIVE` state.
        :param pulumi.Input[str] hvn_id: The ID of the HashiCorp Virtual Network (HVN).
        :param pulumi.Input[str] organization_id: The ID of the HCP organization where the network peering is located. Always matches the HVN's organization.
        :param pulumi.Input[str] peer_account_id: The account ID of the peer VPC in AWS.
        :param pulumi.Input[str] peer_vpc_id: The ID of the peer VPC in AWS.
        :param pulumi.Input[str] peer_vpc_region: The region of the peer VPC in AWS.
        :param pulumi.Input[str] peering_id: The ID of the network peering.
        :param pulumi.Input[str] project_id: The ID of the HCP project where the network peering is located. Always matches the HVN's project.
        :param pulumi.Input[str] provider_peering_id: The peering connection ID used by AWS.
        :param pulumi.Input[str] self_link: A unique URL identifying the network peering.
        """
        if created_at is not None:
            pulumi.set(__self__, "created_at", created_at)
        if expires_at is not None:
            pulumi.set(__self__, "expires_at", expires_at)
        if hvn_id is not None:
            pulumi.set(__self__, "hvn_id", hvn_id)
        if organization_id is not None:
            pulumi.set(__self__, "organization_id", organization_id)
        if peer_account_id is not None:
            pulumi.set(__self__, "peer_account_id", peer_account_id)
        if peer_vpc_id is not None:
            pulumi.set(__self__, "peer_vpc_id", peer_vpc_id)
        if peer_vpc_region is not None:
            pulumi.set(__self__, "peer_vpc_region", peer_vpc_region)
        if peering_id is not None:
            pulumi.set(__self__, "peering_id", peering_id)
        if project_id is not None:
            pulumi.set(__self__, "project_id", project_id)
        if provider_peering_id is not None:
            pulumi.set(__self__, "provider_peering_id", provider_peering_id)
        if self_link is not None:
            pulumi.set(__self__, "self_link", self_link)

    @property
    @pulumi.getter(name="createdAt")
    def created_at(self) -> Optional[pulumi.Input[str]]:
        """
        The time that the network peering was created.
        """
        return pulumi.get(self, "created_at")

    @created_at.setter
    def created_at(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "created_at", value)

    @property
    @pulumi.getter(name="expiresAt")
    def expires_at(self) -> Optional[pulumi.Input[str]]:
        """
        The time after which the network peering will be considered expired if it hasn't transitioned into `ACCEPTED` or
        `ACTIVE` state.
        """
        return pulumi.get(self, "expires_at")

    @expires_at.setter
    def expires_at(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "expires_at", value)

    @property
    @pulumi.getter(name="hvnId")
    def hvn_id(self) -> Optional[pulumi.Input[str]]:
        """
        The ID of the HashiCorp Virtual Network (HVN).
        """
        return pulumi.get(self, "hvn_id")

    @hvn_id.setter
    def hvn_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "hvn_id", value)

    @property
    @pulumi.getter(name="organizationId")
    def organization_id(self) -> Optional[pulumi.Input[str]]:
        """
        The ID of the HCP organization where the network peering is located. Always matches the HVN's organization.
        """
        return pulumi.get(self, "organization_id")

    @organization_id.setter
    def organization_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "organization_id", value)

    @property
    @pulumi.getter(name="peerAccountId")
    def peer_account_id(self) -> Optional[pulumi.Input[str]]:
        """
        The account ID of the peer VPC in AWS.
        """
        return pulumi.get(self, "peer_account_id")

    @peer_account_id.setter
    def peer_account_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "peer_account_id", value)

    @property
    @pulumi.getter(name="peerVpcId")
    def peer_vpc_id(self) -> Optional[pulumi.Input[str]]:
        """
        The ID of the peer VPC in AWS.
        """
        return pulumi.get(self, "peer_vpc_id")

    @peer_vpc_id.setter
    def peer_vpc_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "peer_vpc_id", value)

    @property
    @pulumi.getter(name="peerVpcRegion")
    def peer_vpc_region(self) -> Optional[pulumi.Input[str]]:
        """
        The region of the peer VPC in AWS.
        """
        return pulumi.get(self, "peer_vpc_region")

    @peer_vpc_region.setter
    def peer_vpc_region(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "peer_vpc_region", value)

    @property
    @pulumi.getter(name="peeringId")
    def peering_id(self) -> Optional[pulumi.Input[str]]:
        """
        The ID of the network peering.
        """
        return pulumi.get(self, "peering_id")

    @peering_id.setter
    def peering_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "peering_id", value)

    @property
    @pulumi.getter(name="projectId")
    def project_id(self) -> Optional[pulumi.Input[str]]:
        """
        The ID of the HCP project where the network peering is located. Always matches the HVN's project.
        """
        return pulumi.get(self, "project_id")

    @project_id.setter
    def project_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "project_id", value)

    @property
    @pulumi.getter(name="providerPeeringId")
    def provider_peering_id(self) -> Optional[pulumi.Input[str]]:
        """
        The peering connection ID used by AWS.
        """
        return pulumi.get(self, "provider_peering_id")

    @provider_peering_id.setter
    def provider_peering_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "provider_peering_id", value)

    @property
    @pulumi.getter(name="selfLink")
    def self_link(self) -> Optional[pulumi.Input[str]]:
        """
        A unique URL identifying the network peering.
        """
        return pulumi.get(self, "self_link")

    @self_link.setter
    def self_link(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "self_link", value)


class AwsNetworkPeering(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 hvn_id: Optional[pulumi.Input[str]] = None,
                 peer_account_id: Optional[pulumi.Input[str]] = None,
                 peer_vpc_id: Optional[pulumi.Input[str]] = None,
                 peer_vpc_region: Optional[pulumi.Input[str]] = None,
                 peering_id: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        The AWS network peering resource allows you to manage a network peering between an HVN and a peer AWS VPC.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_aws as aws
        import pulumi_hcp as hcp

        main = hcp.Hvn("main",
            hvn_id="main-hvn",
            cloud_provider="aws",
            region="us-west-2",
            cidr_block="172.25.16.0/20")
        peer_vpc = aws.ec2.Vpc("peerVpc", cidr_block="172.31.0.0/16")
        peer_arn = aws.get_arn_output(arn=peer_vpc.arn)
        dev = hcp.AwsNetworkPeering("dev",
            hvn_id=main.hvn_id,
            peering_id="dev",
            peer_vpc_id=peer_vpc.id,
            peer_account_id=peer_vpc.owner_id,
            peer_vpc_region=peer_arn.region)
        main_to_dev = hcp.HvnRoute("main-to-dev",
            hvn_link=main.self_link,
            hvn_route_id="main-to-dev",
            destination_cidr="172.31.0.0/16",
            target_link=dev.self_link)
        peer_vpc_peering_connection_accepter = aws.ec2.VpcPeeringConnectionAccepter("peerVpcPeeringConnectionAccepter",
            vpc_peering_connection_id=dev.provider_peering_id,
            auto_accept=True)
        ```

        ## Import

        # The import ID is {hvn_id}:{peering_id}

        ```sh
         $ pulumi import hcp:index/awsNetworkPeering:AwsNetworkPeering peer main-hvn:11eb60b3-d4ec-5eed-aacc-0242ac120015
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] hvn_id: The ID of the HashiCorp Virtual Network (HVN).
        :param pulumi.Input[str] peer_account_id: The account ID of the peer VPC in AWS.
        :param pulumi.Input[str] peer_vpc_id: The ID of the peer VPC in AWS.
        :param pulumi.Input[str] peer_vpc_region: The region of the peer VPC in AWS.
        :param pulumi.Input[str] peering_id: The ID of the network peering.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: AwsNetworkPeeringArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        The AWS network peering resource allows you to manage a network peering between an HVN and a peer AWS VPC.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_aws as aws
        import pulumi_hcp as hcp

        main = hcp.Hvn("main",
            hvn_id="main-hvn",
            cloud_provider="aws",
            region="us-west-2",
            cidr_block="172.25.16.0/20")
        peer_vpc = aws.ec2.Vpc("peerVpc", cidr_block="172.31.0.0/16")
        peer_arn = aws.get_arn_output(arn=peer_vpc.arn)
        dev = hcp.AwsNetworkPeering("dev",
            hvn_id=main.hvn_id,
            peering_id="dev",
            peer_vpc_id=peer_vpc.id,
            peer_account_id=peer_vpc.owner_id,
            peer_vpc_region=peer_arn.region)
        main_to_dev = hcp.HvnRoute("main-to-dev",
            hvn_link=main.self_link,
            hvn_route_id="main-to-dev",
            destination_cidr="172.31.0.0/16",
            target_link=dev.self_link)
        peer_vpc_peering_connection_accepter = aws.ec2.VpcPeeringConnectionAccepter("peerVpcPeeringConnectionAccepter",
            vpc_peering_connection_id=dev.provider_peering_id,
            auto_accept=True)
        ```

        ## Import

        # The import ID is {hvn_id}:{peering_id}

        ```sh
         $ pulumi import hcp:index/awsNetworkPeering:AwsNetworkPeering peer main-hvn:11eb60b3-d4ec-5eed-aacc-0242ac120015
        ```

        :param str resource_name: The name of the resource.
        :param AwsNetworkPeeringArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(AwsNetworkPeeringArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 hvn_id: Optional[pulumi.Input[str]] = None,
                 peer_account_id: Optional[pulumi.Input[str]] = None,
                 peer_vpc_id: Optional[pulumi.Input[str]] = None,
                 peer_vpc_region: Optional[pulumi.Input[str]] = None,
                 peering_id: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = AwsNetworkPeeringArgs.__new__(AwsNetworkPeeringArgs)

            if hvn_id is None and not opts.urn:
                raise TypeError("Missing required property 'hvn_id'")
            __props__.__dict__["hvn_id"] = hvn_id
            if peer_account_id is None and not opts.urn:
                raise TypeError("Missing required property 'peer_account_id'")
            __props__.__dict__["peer_account_id"] = peer_account_id
            if peer_vpc_id is None and not opts.urn:
                raise TypeError("Missing required property 'peer_vpc_id'")
            __props__.__dict__["peer_vpc_id"] = peer_vpc_id
            if peer_vpc_region is None and not opts.urn:
                raise TypeError("Missing required property 'peer_vpc_region'")
            __props__.__dict__["peer_vpc_region"] = peer_vpc_region
            if peering_id is None and not opts.urn:
                raise TypeError("Missing required property 'peering_id'")
            __props__.__dict__["peering_id"] = peering_id
            __props__.__dict__["created_at"] = None
            __props__.__dict__["expires_at"] = None
            __props__.__dict__["organization_id"] = None
            __props__.__dict__["project_id"] = None
            __props__.__dict__["provider_peering_id"] = None
            __props__.__dict__["self_link"] = None
        super(AwsNetworkPeering, __self__).__init__(
            'hcp:index/awsNetworkPeering:AwsNetworkPeering',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            created_at: Optional[pulumi.Input[str]] = None,
            expires_at: Optional[pulumi.Input[str]] = None,
            hvn_id: Optional[pulumi.Input[str]] = None,
            organization_id: Optional[pulumi.Input[str]] = None,
            peer_account_id: Optional[pulumi.Input[str]] = None,
            peer_vpc_id: Optional[pulumi.Input[str]] = None,
            peer_vpc_region: Optional[pulumi.Input[str]] = None,
            peering_id: Optional[pulumi.Input[str]] = None,
            project_id: Optional[pulumi.Input[str]] = None,
            provider_peering_id: Optional[pulumi.Input[str]] = None,
            self_link: Optional[pulumi.Input[str]] = None) -> 'AwsNetworkPeering':
        """
        Get an existing AwsNetworkPeering resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] created_at: The time that the network peering was created.
        :param pulumi.Input[str] expires_at: The time after which the network peering will be considered expired if it hasn't transitioned into `ACCEPTED` or
               `ACTIVE` state.
        :param pulumi.Input[str] hvn_id: The ID of the HashiCorp Virtual Network (HVN).
        :param pulumi.Input[str] organization_id: The ID of the HCP organization where the network peering is located. Always matches the HVN's organization.
        :param pulumi.Input[str] peer_account_id: The account ID of the peer VPC in AWS.
        :param pulumi.Input[str] peer_vpc_id: The ID of the peer VPC in AWS.
        :param pulumi.Input[str] peer_vpc_region: The region of the peer VPC in AWS.
        :param pulumi.Input[str] peering_id: The ID of the network peering.
        :param pulumi.Input[str] project_id: The ID of the HCP project where the network peering is located. Always matches the HVN's project.
        :param pulumi.Input[str] provider_peering_id: The peering connection ID used by AWS.
        :param pulumi.Input[str] self_link: A unique URL identifying the network peering.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _AwsNetworkPeeringState.__new__(_AwsNetworkPeeringState)

        __props__.__dict__["created_at"] = created_at
        __props__.__dict__["expires_at"] = expires_at
        __props__.__dict__["hvn_id"] = hvn_id
        __props__.__dict__["organization_id"] = organization_id
        __props__.__dict__["peer_account_id"] = peer_account_id
        __props__.__dict__["peer_vpc_id"] = peer_vpc_id
        __props__.__dict__["peer_vpc_region"] = peer_vpc_region
        __props__.__dict__["peering_id"] = peering_id
        __props__.__dict__["project_id"] = project_id
        __props__.__dict__["provider_peering_id"] = provider_peering_id
        __props__.__dict__["self_link"] = self_link
        return AwsNetworkPeering(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="createdAt")
    def created_at(self) -> pulumi.Output[str]:
        """
        The time that the network peering was created.
        """
        return pulumi.get(self, "created_at")

    @property
    @pulumi.getter(name="expiresAt")
    def expires_at(self) -> pulumi.Output[str]:
        """
        The time after which the network peering will be considered expired if it hasn't transitioned into `ACCEPTED` or
        `ACTIVE` state.
        """
        return pulumi.get(self, "expires_at")

    @property
    @pulumi.getter(name="hvnId")
    def hvn_id(self) -> pulumi.Output[str]:
        """
        The ID of the HashiCorp Virtual Network (HVN).
        """
        return pulumi.get(self, "hvn_id")

    @property
    @pulumi.getter(name="organizationId")
    def organization_id(self) -> pulumi.Output[str]:
        """
        The ID of the HCP organization where the network peering is located. Always matches the HVN's organization.
        """
        return pulumi.get(self, "organization_id")

    @property
    @pulumi.getter(name="peerAccountId")
    def peer_account_id(self) -> pulumi.Output[str]:
        """
        The account ID of the peer VPC in AWS.
        """
        return pulumi.get(self, "peer_account_id")

    @property
    @pulumi.getter(name="peerVpcId")
    def peer_vpc_id(self) -> pulumi.Output[str]:
        """
        The ID of the peer VPC in AWS.
        """
        return pulumi.get(self, "peer_vpc_id")

    @property
    @pulumi.getter(name="peerVpcRegion")
    def peer_vpc_region(self) -> pulumi.Output[str]:
        """
        The region of the peer VPC in AWS.
        """
        return pulumi.get(self, "peer_vpc_region")

    @property
    @pulumi.getter(name="peeringId")
    def peering_id(self) -> pulumi.Output[str]:
        """
        The ID of the network peering.
        """
        return pulumi.get(self, "peering_id")

    @property
    @pulumi.getter(name="projectId")
    def project_id(self) -> pulumi.Output[str]:
        """
        The ID of the HCP project where the network peering is located. Always matches the HVN's project.
        """
        return pulumi.get(self, "project_id")

    @property
    @pulumi.getter(name="providerPeeringId")
    def provider_peering_id(self) -> pulumi.Output[str]:
        """
        The peering connection ID used by AWS.
        """
        return pulumi.get(self, "provider_peering_id")

    @property
    @pulumi.getter(name="selfLink")
    def self_link(self) -> pulumi.Output[str]:
        """
        A unique URL identifying the network peering.
        """
        return pulumi.get(self, "self_link")

