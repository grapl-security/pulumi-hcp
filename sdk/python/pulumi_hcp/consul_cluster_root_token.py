# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from . import _utilities

__all__ = ['ConsulClusterRootTokenArgs', 'ConsulClusterRootToken']

@pulumi.input_type
class ConsulClusterRootTokenArgs:
    def __init__(__self__, *,
                 cluster_id: pulumi.Input[str]):
        """
        The set of arguments for constructing a ConsulClusterRootToken resource.
        :param pulumi.Input[str] cluster_id: The ID of the HCP Consul cluster.
        """
        pulumi.set(__self__, "cluster_id", cluster_id)

    @property
    @pulumi.getter(name="clusterId")
    def cluster_id(self) -> pulumi.Input[str]:
        """
        The ID of the HCP Consul cluster.
        """
        return pulumi.get(self, "cluster_id")

    @cluster_id.setter
    def cluster_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "cluster_id", value)


@pulumi.input_type
class _ConsulClusterRootTokenState:
    def __init__(__self__, *,
                 accessor_id: Optional[pulumi.Input[str]] = None,
                 cluster_id: Optional[pulumi.Input[str]] = None,
                 kubernetes_secret: Optional[pulumi.Input[str]] = None,
                 secret_id: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering ConsulClusterRootToken resources.
        :param pulumi.Input[str] accessor_id: The accessor ID of the root ACL token.
        :param pulumi.Input[str] cluster_id: The ID of the HCP Consul cluster.
        :param pulumi.Input[str] kubernetes_secret: The root ACL token Base64 encoded in a Kubernetes secret.
        :param pulumi.Input[str] secret_id: The secret ID of the root ACL token.
        """
        if accessor_id is not None:
            pulumi.set(__self__, "accessor_id", accessor_id)
        if cluster_id is not None:
            pulumi.set(__self__, "cluster_id", cluster_id)
        if kubernetes_secret is not None:
            pulumi.set(__self__, "kubernetes_secret", kubernetes_secret)
        if secret_id is not None:
            pulumi.set(__self__, "secret_id", secret_id)

    @property
    @pulumi.getter(name="accessorId")
    def accessor_id(self) -> Optional[pulumi.Input[str]]:
        """
        The accessor ID of the root ACL token.
        """
        return pulumi.get(self, "accessor_id")

    @accessor_id.setter
    def accessor_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "accessor_id", value)

    @property
    @pulumi.getter(name="clusterId")
    def cluster_id(self) -> Optional[pulumi.Input[str]]:
        """
        The ID of the HCP Consul cluster.
        """
        return pulumi.get(self, "cluster_id")

    @cluster_id.setter
    def cluster_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "cluster_id", value)

    @property
    @pulumi.getter(name="kubernetesSecret")
    def kubernetes_secret(self) -> Optional[pulumi.Input[str]]:
        """
        The root ACL token Base64 encoded in a Kubernetes secret.
        """
        return pulumi.get(self, "kubernetes_secret")

    @kubernetes_secret.setter
    def kubernetes_secret(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "kubernetes_secret", value)

    @property
    @pulumi.getter(name="secretId")
    def secret_id(self) -> Optional[pulumi.Input[str]]:
        """
        The secret ID of the root ACL token.
        """
        return pulumi.get(self, "secret_id")

    @secret_id.setter
    def secret_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "secret_id", value)


class ConsulClusterRootToken(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 cluster_id: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        ## Example Usage

        ```python
        import pulumi
        import pulumi_hcp as hcp

        example = hcp.ConsulClusterRootToken("example", cluster_id="consul-cluster")
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] cluster_id: The ID of the HCP Consul cluster.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: ConsulClusterRootTokenArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        ## Example Usage

        ```python
        import pulumi
        import pulumi_hcp as hcp

        example = hcp.ConsulClusterRootToken("example", cluster_id="consul-cluster")
        ```

        :param str resource_name: The name of the resource.
        :param ConsulClusterRootTokenArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(ConsulClusterRootTokenArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 cluster_id: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = ConsulClusterRootTokenArgs.__new__(ConsulClusterRootTokenArgs)

            if cluster_id is None and not opts.urn:
                raise TypeError("Missing required property 'cluster_id'")
            __props__.__dict__["cluster_id"] = cluster_id
            __props__.__dict__["accessor_id"] = None
            __props__.__dict__["kubernetes_secret"] = None
            __props__.__dict__["secret_id"] = None
        super(ConsulClusterRootToken, __self__).__init__(
            'hcp:index/consulClusterRootToken:ConsulClusterRootToken',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            accessor_id: Optional[pulumi.Input[str]] = None,
            cluster_id: Optional[pulumi.Input[str]] = None,
            kubernetes_secret: Optional[pulumi.Input[str]] = None,
            secret_id: Optional[pulumi.Input[str]] = None) -> 'ConsulClusterRootToken':
        """
        Get an existing ConsulClusterRootToken resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] accessor_id: The accessor ID of the root ACL token.
        :param pulumi.Input[str] cluster_id: The ID of the HCP Consul cluster.
        :param pulumi.Input[str] kubernetes_secret: The root ACL token Base64 encoded in a Kubernetes secret.
        :param pulumi.Input[str] secret_id: The secret ID of the root ACL token.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _ConsulClusterRootTokenState.__new__(_ConsulClusterRootTokenState)

        __props__.__dict__["accessor_id"] = accessor_id
        __props__.__dict__["cluster_id"] = cluster_id
        __props__.__dict__["kubernetes_secret"] = kubernetes_secret
        __props__.__dict__["secret_id"] = secret_id
        return ConsulClusterRootToken(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="accessorId")
    def accessor_id(self) -> pulumi.Output[str]:
        """
        The accessor ID of the root ACL token.
        """
        return pulumi.get(self, "accessor_id")

    @property
    @pulumi.getter(name="clusterId")
    def cluster_id(self) -> pulumi.Output[str]:
        """
        The ID of the HCP Consul cluster.
        """
        return pulumi.get(self, "cluster_id")

    @property
    @pulumi.getter(name="kubernetesSecret")
    def kubernetes_secret(self) -> pulumi.Output[str]:
        """
        The root ACL token Base64 encoded in a Kubernetes secret.
        """
        return pulumi.get(self, "kubernetes_secret")

    @property
    @pulumi.getter(name="secretId")
    def secret_id(self) -> pulumi.Output[str]:
        """
        The secret ID of the root ACL token.
        """
        return pulumi.get(self, "secret_id")

