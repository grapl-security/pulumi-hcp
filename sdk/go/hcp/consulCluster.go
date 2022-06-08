// Code generated by the Pulumi Terraform Bridge (tfgen) Tool DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package hcp

import (
	"context"
	"reflect"

	"github.com/pkg/errors"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

// > Consul on Azure is now available in public beta. [Get started with end-to-end deployment configuration](https://learn.hashicorp.com/tutorials/cloud/consul-end-to-end-overview).
//
// The Consul cluster resource allows you to manage an HCP Consul cluster.
//
// ## Example Usage
//
// ```go
// package main
//
// import (
// 	"github.com/grapl-security/pulumi-hcp/sdk/go/hcp"
// 	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
// )
//
// func main() {
// 	pulumi.Run(func(ctx *pulumi.Context) error {
// 		exampleHvn, err := hcp.NewHvn(ctx, "exampleHvn", &hcp.HvnArgs{
// 			HvnId:         pulumi.String("hvn"),
// 			CloudProvider: pulumi.String("aws"),
// 			Region:        pulumi.String("us-west-2"),
// 			CidrBlock:     pulumi.String("172.25.16.0/20"),
// 		})
// 		if err != nil {
// 			return err
// 		}
// 		_, err = hcp.NewConsulCluster(ctx, "exampleConsulCluster", &hcp.ConsulClusterArgs{
// 			ClusterId: pulumi.String("consul-cluster"),
// 			HvnId:     exampleHvn.HvnId,
// 			Tier:      pulumi.String("development"),
// 		})
// 		if err != nil {
// 			return err
// 		}
// 		return nil
// 	})
// }
// ```
//
// ## Import
//
// # The import ID is {cluster_id}
//
// ```sh
//  $ pulumi import hcp:index/consulCluster:ConsulCluster example consul-cluster
// ```
type ConsulCluster struct {
	pulumi.CustomResourceState

	// Enables automatic HVN to HVN peering when creating a secondary cluster in a federation. The alternative to using the
	// auto-accept feature is to create an [`hcp_hvn_peering_connection`](hvn_peering_connection.md) resource that explicitly
	// defines the HVN resources that are allowed to communicate with each other.
	AutoHvnToHvnPeering pulumi.BoolOutput `pulumi:"autoHvnToHvnPeering"`
	// The provider where the HCP Consul cluster is located.
	CloudProvider pulumi.StringOutput `pulumi:"cloudProvider"`
	// The ID of the HCP Consul cluster.
	ClusterId pulumi.StringOutput `pulumi:"clusterId"`
	// Denotes the Consul connect feature should be enabled for this cluster. Default to true.
	ConnectEnabled pulumi.BoolPtrOutput `pulumi:"connectEnabled"`
	// Denotes that automatic Consul upgrades are enabled.
	ConsulAutomaticUpgrades pulumi.BoolOutput `pulumi:"consulAutomaticUpgrades"`
	// The cluster CA file encoded as a Base64 string.
	ConsulCaFile pulumi.StringOutput `pulumi:"consulCaFile"`
	// The cluster config encoded as a Base64 string.
	ConsulConfigFile pulumi.StringOutput `pulumi:"consulConfigFile"`
	// The private URL for the Consul UI.
	ConsulPrivateEndpointUrl pulumi.StringOutput `pulumi:"consulPrivateEndpointUrl"`
	// The public URL for the Consul UI. This will be empty if `public_endpoint` is `false`.
	ConsulPublicEndpointUrl pulumi.StringOutput `pulumi:"consulPublicEndpointUrl"`
	// The accessor ID of the root ACL token that is generated upon cluster creation. If a new root token is generated using
	// the `hcp_consul_root_token` resource, this field is no longer valid.
	ConsulRootTokenAccessorId pulumi.StringOutput `pulumi:"consulRootTokenAccessorId"`
	// The secret ID of the root ACL token that is generated upon cluster creation. If a new root token is generated using the
	// `hcp_consul_root_token` resource, this field is no longer valid.
	ConsulRootTokenSecretId pulumi.StringOutput `pulumi:"consulRootTokenSecretId"`
	// The Consul snapshot interval.
	ConsulSnapshotInterval pulumi.StringOutput `pulumi:"consulSnapshotInterval"`
	// The retention policy for Consul snapshots.
	ConsulSnapshotRetention pulumi.StringOutput `pulumi:"consulSnapshotRetention"`
	// The Consul version of the cluster.
	ConsulVersion pulumi.StringOutput `pulumi:"consulVersion"`
	// The Consul data center name of the cluster. If not specified, it is defaulted to the value of `cluster_id`.
	Datacenter pulumi.StringOutput `pulumi:"datacenter"`
	// The ID of the HVN this HCP Consul cluster is associated to.
	HvnId pulumi.StringOutput `pulumi:"hvnId"`
	// The minimum Consul version of the cluster. If not specified, it is defaulted to the version that is currently
	// recommended by HCP.
	MinConsulVersion pulumi.StringPtrOutput `pulumi:"minConsulVersion"`
	// The ID of the organization this HCP Consul cluster is located in.
	OrganizationId pulumi.StringOutput `pulumi:"organizationId"`
	// The `self_link` of the HCP Consul cluster which is the primary in the federation setup with this HCP Consul cluster. If
	// not specified, it is a standalone cluster.
	PrimaryLink pulumi.StringPtrOutput `pulumi:"primaryLink"`
	// The ID of the project this HCP Consul cluster is located in.
	ProjectId pulumi.StringOutput `pulumi:"projectId"`
	// Denotes that the cluster has a public endpoint for the Consul UI. Defaults to false.
	PublicEndpoint pulumi.BoolPtrOutput `pulumi:"publicEndpoint"`
	// The region where the HCP Consul cluster is located.
	Region pulumi.StringOutput `pulumi:"region"`
	// The number of Consul server nodes in the cluster.
	Scale pulumi.IntOutput `pulumi:"scale"`
	// A unique URL identifying the HCP Consul cluster.
	SelfLink pulumi.StringOutput `pulumi:"selfLink"`
	// The t-shirt size representation of each server VM that this Consul cluster is provisioned with. Valid option for
	// development tier - `x_small`. Valid options for other tiers - `small`, `medium`, `large`. For more details -
	// https://cloud.hashicorp.com/pricing/consul. Upgrading the size of a cluster after creation is allowed.
	Size pulumi.StringOutput `pulumi:"size"`
	// The tier that the HCP Consul cluster will be provisioned as. Only `development`, `standard` and `plus` are available at
	// this time. See [pricing information](https://cloud.hashicorp.com/pricing/consul).
	Tier pulumi.StringOutput `pulumi:"tier"`
}

// NewConsulCluster registers a new resource with the given unique name, arguments, and options.
func NewConsulCluster(ctx *pulumi.Context,
	name string, args *ConsulClusterArgs, opts ...pulumi.ResourceOption) (*ConsulCluster, error) {
	if args == nil {
		return nil, errors.New("missing one or more required arguments")
	}

	if args.ClusterId == nil {
		return nil, errors.New("invalid value for required argument 'ClusterId'")
	}
	if args.HvnId == nil {
		return nil, errors.New("invalid value for required argument 'HvnId'")
	}
	if args.Tier == nil {
		return nil, errors.New("invalid value for required argument 'Tier'")
	}
	opts = pkgResourceDefaultOpts(opts)
	var resource ConsulCluster
	err := ctx.RegisterResource("hcp:index/consulCluster:ConsulCluster", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetConsulCluster gets an existing ConsulCluster resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetConsulCluster(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *ConsulClusterState, opts ...pulumi.ResourceOption) (*ConsulCluster, error) {
	var resource ConsulCluster
	err := ctx.ReadResource("hcp:index/consulCluster:ConsulCluster", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering ConsulCluster resources.
type consulClusterState struct {
	// Enables automatic HVN to HVN peering when creating a secondary cluster in a federation. The alternative to using the
	// auto-accept feature is to create an [`hcp_hvn_peering_connection`](hvn_peering_connection.md) resource that explicitly
	// defines the HVN resources that are allowed to communicate with each other.
	AutoHvnToHvnPeering *bool `pulumi:"autoHvnToHvnPeering"`
	// The provider where the HCP Consul cluster is located.
	CloudProvider *string `pulumi:"cloudProvider"`
	// The ID of the HCP Consul cluster.
	ClusterId *string `pulumi:"clusterId"`
	// Denotes the Consul connect feature should be enabled for this cluster. Default to true.
	ConnectEnabled *bool `pulumi:"connectEnabled"`
	// Denotes that automatic Consul upgrades are enabled.
	ConsulAutomaticUpgrades *bool `pulumi:"consulAutomaticUpgrades"`
	// The cluster CA file encoded as a Base64 string.
	ConsulCaFile *string `pulumi:"consulCaFile"`
	// The cluster config encoded as a Base64 string.
	ConsulConfigFile *string `pulumi:"consulConfigFile"`
	// The private URL for the Consul UI.
	ConsulPrivateEndpointUrl *string `pulumi:"consulPrivateEndpointUrl"`
	// The public URL for the Consul UI. This will be empty if `public_endpoint` is `false`.
	ConsulPublicEndpointUrl *string `pulumi:"consulPublicEndpointUrl"`
	// The accessor ID of the root ACL token that is generated upon cluster creation. If a new root token is generated using
	// the `hcp_consul_root_token` resource, this field is no longer valid.
	ConsulRootTokenAccessorId *string `pulumi:"consulRootTokenAccessorId"`
	// The secret ID of the root ACL token that is generated upon cluster creation. If a new root token is generated using the
	// `hcp_consul_root_token` resource, this field is no longer valid.
	ConsulRootTokenSecretId *string `pulumi:"consulRootTokenSecretId"`
	// The Consul snapshot interval.
	ConsulSnapshotInterval *string `pulumi:"consulSnapshotInterval"`
	// The retention policy for Consul snapshots.
	ConsulSnapshotRetention *string `pulumi:"consulSnapshotRetention"`
	// The Consul version of the cluster.
	ConsulVersion *string `pulumi:"consulVersion"`
	// The Consul data center name of the cluster. If not specified, it is defaulted to the value of `cluster_id`.
	Datacenter *string `pulumi:"datacenter"`
	// The ID of the HVN this HCP Consul cluster is associated to.
	HvnId *string `pulumi:"hvnId"`
	// The minimum Consul version of the cluster. If not specified, it is defaulted to the version that is currently
	// recommended by HCP.
	MinConsulVersion *string `pulumi:"minConsulVersion"`
	// The ID of the organization this HCP Consul cluster is located in.
	OrganizationId *string `pulumi:"organizationId"`
	// The `self_link` of the HCP Consul cluster which is the primary in the federation setup with this HCP Consul cluster. If
	// not specified, it is a standalone cluster.
	PrimaryLink *string `pulumi:"primaryLink"`
	// The ID of the project this HCP Consul cluster is located in.
	ProjectId *string `pulumi:"projectId"`
	// Denotes that the cluster has a public endpoint for the Consul UI. Defaults to false.
	PublicEndpoint *bool `pulumi:"publicEndpoint"`
	// The region where the HCP Consul cluster is located.
	Region *string `pulumi:"region"`
	// The number of Consul server nodes in the cluster.
	Scale *int `pulumi:"scale"`
	// A unique URL identifying the HCP Consul cluster.
	SelfLink *string `pulumi:"selfLink"`
	// The t-shirt size representation of each server VM that this Consul cluster is provisioned with. Valid option for
	// development tier - `x_small`. Valid options for other tiers - `small`, `medium`, `large`. For more details -
	// https://cloud.hashicorp.com/pricing/consul. Upgrading the size of a cluster after creation is allowed.
	Size *string `pulumi:"size"`
	// The tier that the HCP Consul cluster will be provisioned as. Only `development`, `standard` and `plus` are available at
	// this time. See [pricing information](https://cloud.hashicorp.com/pricing/consul).
	Tier *string `pulumi:"tier"`
}

type ConsulClusterState struct {
	// Enables automatic HVN to HVN peering when creating a secondary cluster in a federation. The alternative to using the
	// auto-accept feature is to create an [`hcp_hvn_peering_connection`](hvn_peering_connection.md) resource that explicitly
	// defines the HVN resources that are allowed to communicate with each other.
	AutoHvnToHvnPeering pulumi.BoolPtrInput
	// The provider where the HCP Consul cluster is located.
	CloudProvider pulumi.StringPtrInput
	// The ID of the HCP Consul cluster.
	ClusterId pulumi.StringPtrInput
	// Denotes the Consul connect feature should be enabled for this cluster. Default to true.
	ConnectEnabled pulumi.BoolPtrInput
	// Denotes that automatic Consul upgrades are enabled.
	ConsulAutomaticUpgrades pulumi.BoolPtrInput
	// The cluster CA file encoded as a Base64 string.
	ConsulCaFile pulumi.StringPtrInput
	// The cluster config encoded as a Base64 string.
	ConsulConfigFile pulumi.StringPtrInput
	// The private URL for the Consul UI.
	ConsulPrivateEndpointUrl pulumi.StringPtrInput
	// The public URL for the Consul UI. This will be empty if `public_endpoint` is `false`.
	ConsulPublicEndpointUrl pulumi.StringPtrInput
	// The accessor ID of the root ACL token that is generated upon cluster creation. If a new root token is generated using
	// the `hcp_consul_root_token` resource, this field is no longer valid.
	ConsulRootTokenAccessorId pulumi.StringPtrInput
	// The secret ID of the root ACL token that is generated upon cluster creation. If a new root token is generated using the
	// `hcp_consul_root_token` resource, this field is no longer valid.
	ConsulRootTokenSecretId pulumi.StringPtrInput
	// The Consul snapshot interval.
	ConsulSnapshotInterval pulumi.StringPtrInput
	// The retention policy for Consul snapshots.
	ConsulSnapshotRetention pulumi.StringPtrInput
	// The Consul version of the cluster.
	ConsulVersion pulumi.StringPtrInput
	// The Consul data center name of the cluster. If not specified, it is defaulted to the value of `cluster_id`.
	Datacenter pulumi.StringPtrInput
	// The ID of the HVN this HCP Consul cluster is associated to.
	HvnId pulumi.StringPtrInput
	// The minimum Consul version of the cluster. If not specified, it is defaulted to the version that is currently
	// recommended by HCP.
	MinConsulVersion pulumi.StringPtrInput
	// The ID of the organization this HCP Consul cluster is located in.
	OrganizationId pulumi.StringPtrInput
	// The `self_link` of the HCP Consul cluster which is the primary in the federation setup with this HCP Consul cluster. If
	// not specified, it is a standalone cluster.
	PrimaryLink pulumi.StringPtrInput
	// The ID of the project this HCP Consul cluster is located in.
	ProjectId pulumi.StringPtrInput
	// Denotes that the cluster has a public endpoint for the Consul UI. Defaults to false.
	PublicEndpoint pulumi.BoolPtrInput
	// The region where the HCP Consul cluster is located.
	Region pulumi.StringPtrInput
	// The number of Consul server nodes in the cluster.
	Scale pulumi.IntPtrInput
	// A unique URL identifying the HCP Consul cluster.
	SelfLink pulumi.StringPtrInput
	// The t-shirt size representation of each server VM that this Consul cluster is provisioned with. Valid option for
	// development tier - `x_small`. Valid options for other tiers - `small`, `medium`, `large`. For more details -
	// https://cloud.hashicorp.com/pricing/consul. Upgrading the size of a cluster after creation is allowed.
	Size pulumi.StringPtrInput
	// The tier that the HCP Consul cluster will be provisioned as. Only `development`, `standard` and `plus` are available at
	// this time. See [pricing information](https://cloud.hashicorp.com/pricing/consul).
	Tier pulumi.StringPtrInput
}

func (ConsulClusterState) ElementType() reflect.Type {
	return reflect.TypeOf((*consulClusterState)(nil)).Elem()
}

type consulClusterArgs struct {
	// Enables automatic HVN to HVN peering when creating a secondary cluster in a federation. The alternative to using the
	// auto-accept feature is to create an [`hcp_hvn_peering_connection`](hvn_peering_connection.md) resource that explicitly
	// defines the HVN resources that are allowed to communicate with each other.
	AutoHvnToHvnPeering *bool `pulumi:"autoHvnToHvnPeering"`
	// The ID of the HCP Consul cluster.
	ClusterId string `pulumi:"clusterId"`
	// Denotes the Consul connect feature should be enabled for this cluster. Default to true.
	ConnectEnabled *bool `pulumi:"connectEnabled"`
	// The Consul data center name of the cluster. If not specified, it is defaulted to the value of `cluster_id`.
	Datacenter *string `pulumi:"datacenter"`
	// The ID of the HVN this HCP Consul cluster is associated to.
	HvnId string `pulumi:"hvnId"`
	// The minimum Consul version of the cluster. If not specified, it is defaulted to the version that is currently
	// recommended by HCP.
	MinConsulVersion *string `pulumi:"minConsulVersion"`
	// The `self_link` of the HCP Consul cluster which is the primary in the federation setup with this HCP Consul cluster. If
	// not specified, it is a standalone cluster.
	PrimaryLink *string `pulumi:"primaryLink"`
	// Denotes that the cluster has a public endpoint for the Consul UI. Defaults to false.
	PublicEndpoint *bool `pulumi:"publicEndpoint"`
	// The t-shirt size representation of each server VM that this Consul cluster is provisioned with. Valid option for
	// development tier - `x_small`. Valid options for other tiers - `small`, `medium`, `large`. For more details -
	// https://cloud.hashicorp.com/pricing/consul. Upgrading the size of a cluster after creation is allowed.
	Size *string `pulumi:"size"`
	// The tier that the HCP Consul cluster will be provisioned as. Only `development`, `standard` and `plus` are available at
	// this time. See [pricing information](https://cloud.hashicorp.com/pricing/consul).
	Tier string `pulumi:"tier"`
}

// The set of arguments for constructing a ConsulCluster resource.
type ConsulClusterArgs struct {
	// Enables automatic HVN to HVN peering when creating a secondary cluster in a federation. The alternative to using the
	// auto-accept feature is to create an [`hcp_hvn_peering_connection`](hvn_peering_connection.md) resource that explicitly
	// defines the HVN resources that are allowed to communicate with each other.
	AutoHvnToHvnPeering pulumi.BoolPtrInput
	// The ID of the HCP Consul cluster.
	ClusterId pulumi.StringInput
	// Denotes the Consul connect feature should be enabled for this cluster. Default to true.
	ConnectEnabled pulumi.BoolPtrInput
	// The Consul data center name of the cluster. If not specified, it is defaulted to the value of `cluster_id`.
	Datacenter pulumi.StringPtrInput
	// The ID of the HVN this HCP Consul cluster is associated to.
	HvnId pulumi.StringInput
	// The minimum Consul version of the cluster. If not specified, it is defaulted to the version that is currently
	// recommended by HCP.
	MinConsulVersion pulumi.StringPtrInput
	// The `self_link` of the HCP Consul cluster which is the primary in the federation setup with this HCP Consul cluster. If
	// not specified, it is a standalone cluster.
	PrimaryLink pulumi.StringPtrInput
	// Denotes that the cluster has a public endpoint for the Consul UI. Defaults to false.
	PublicEndpoint pulumi.BoolPtrInput
	// The t-shirt size representation of each server VM that this Consul cluster is provisioned with. Valid option for
	// development tier - `x_small`. Valid options for other tiers - `small`, `medium`, `large`. For more details -
	// https://cloud.hashicorp.com/pricing/consul. Upgrading the size of a cluster after creation is allowed.
	Size pulumi.StringPtrInput
	// The tier that the HCP Consul cluster will be provisioned as. Only `development`, `standard` and `plus` are available at
	// this time. See [pricing information](https://cloud.hashicorp.com/pricing/consul).
	Tier pulumi.StringInput
}

func (ConsulClusterArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*consulClusterArgs)(nil)).Elem()
}

type ConsulClusterInput interface {
	pulumi.Input

	ToConsulClusterOutput() ConsulClusterOutput
	ToConsulClusterOutputWithContext(ctx context.Context) ConsulClusterOutput
}

func (*ConsulCluster) ElementType() reflect.Type {
	return reflect.TypeOf((**ConsulCluster)(nil)).Elem()
}

func (i *ConsulCluster) ToConsulClusterOutput() ConsulClusterOutput {
	return i.ToConsulClusterOutputWithContext(context.Background())
}

func (i *ConsulCluster) ToConsulClusterOutputWithContext(ctx context.Context) ConsulClusterOutput {
	return pulumi.ToOutputWithContext(ctx, i).(ConsulClusterOutput)
}

// ConsulClusterArrayInput is an input type that accepts ConsulClusterArray and ConsulClusterArrayOutput values.
// You can construct a concrete instance of `ConsulClusterArrayInput` via:
//
//          ConsulClusterArray{ ConsulClusterArgs{...} }
type ConsulClusterArrayInput interface {
	pulumi.Input

	ToConsulClusterArrayOutput() ConsulClusterArrayOutput
	ToConsulClusterArrayOutputWithContext(context.Context) ConsulClusterArrayOutput
}

type ConsulClusterArray []ConsulClusterInput

func (ConsulClusterArray) ElementType() reflect.Type {
	return reflect.TypeOf((*[]*ConsulCluster)(nil)).Elem()
}

func (i ConsulClusterArray) ToConsulClusterArrayOutput() ConsulClusterArrayOutput {
	return i.ToConsulClusterArrayOutputWithContext(context.Background())
}

func (i ConsulClusterArray) ToConsulClusterArrayOutputWithContext(ctx context.Context) ConsulClusterArrayOutput {
	return pulumi.ToOutputWithContext(ctx, i).(ConsulClusterArrayOutput)
}

// ConsulClusterMapInput is an input type that accepts ConsulClusterMap and ConsulClusterMapOutput values.
// You can construct a concrete instance of `ConsulClusterMapInput` via:
//
//          ConsulClusterMap{ "key": ConsulClusterArgs{...} }
type ConsulClusterMapInput interface {
	pulumi.Input

	ToConsulClusterMapOutput() ConsulClusterMapOutput
	ToConsulClusterMapOutputWithContext(context.Context) ConsulClusterMapOutput
}

type ConsulClusterMap map[string]ConsulClusterInput

func (ConsulClusterMap) ElementType() reflect.Type {
	return reflect.TypeOf((*map[string]*ConsulCluster)(nil)).Elem()
}

func (i ConsulClusterMap) ToConsulClusterMapOutput() ConsulClusterMapOutput {
	return i.ToConsulClusterMapOutputWithContext(context.Background())
}

func (i ConsulClusterMap) ToConsulClusterMapOutputWithContext(ctx context.Context) ConsulClusterMapOutput {
	return pulumi.ToOutputWithContext(ctx, i).(ConsulClusterMapOutput)
}

type ConsulClusterOutput struct{ *pulumi.OutputState }

func (ConsulClusterOutput) ElementType() reflect.Type {
	return reflect.TypeOf((**ConsulCluster)(nil)).Elem()
}

func (o ConsulClusterOutput) ToConsulClusterOutput() ConsulClusterOutput {
	return o
}

func (o ConsulClusterOutput) ToConsulClusterOutputWithContext(ctx context.Context) ConsulClusterOutput {
	return o
}

// Enables automatic HVN to HVN peering when creating a secondary cluster in a federation. The alternative to using the
// auto-accept feature is to create an [`hcp_hvn_peering_connection`](hvn_peering_connection.md) resource that explicitly
// defines the HVN resources that are allowed to communicate with each other.
func (o ConsulClusterOutput) AutoHvnToHvnPeering() pulumi.BoolOutput {
	return o.ApplyT(func(v *ConsulCluster) pulumi.BoolOutput { return v.AutoHvnToHvnPeering }).(pulumi.BoolOutput)
}

// The provider where the HCP Consul cluster is located.
func (o ConsulClusterOutput) CloudProvider() pulumi.StringOutput {
	return o.ApplyT(func(v *ConsulCluster) pulumi.StringOutput { return v.CloudProvider }).(pulumi.StringOutput)
}

// The ID of the HCP Consul cluster.
func (o ConsulClusterOutput) ClusterId() pulumi.StringOutput {
	return o.ApplyT(func(v *ConsulCluster) pulumi.StringOutput { return v.ClusterId }).(pulumi.StringOutput)
}

// Denotes the Consul connect feature should be enabled for this cluster. Default to true.
func (o ConsulClusterOutput) ConnectEnabled() pulumi.BoolPtrOutput {
	return o.ApplyT(func(v *ConsulCluster) pulumi.BoolPtrOutput { return v.ConnectEnabled }).(pulumi.BoolPtrOutput)
}

// Denotes that automatic Consul upgrades are enabled.
func (o ConsulClusterOutput) ConsulAutomaticUpgrades() pulumi.BoolOutput {
	return o.ApplyT(func(v *ConsulCluster) pulumi.BoolOutput { return v.ConsulAutomaticUpgrades }).(pulumi.BoolOutput)
}

// The cluster CA file encoded as a Base64 string.
func (o ConsulClusterOutput) ConsulCaFile() pulumi.StringOutput {
	return o.ApplyT(func(v *ConsulCluster) pulumi.StringOutput { return v.ConsulCaFile }).(pulumi.StringOutput)
}

// The cluster config encoded as a Base64 string.
func (o ConsulClusterOutput) ConsulConfigFile() pulumi.StringOutput {
	return o.ApplyT(func(v *ConsulCluster) pulumi.StringOutput { return v.ConsulConfigFile }).(pulumi.StringOutput)
}

// The private URL for the Consul UI.
func (o ConsulClusterOutput) ConsulPrivateEndpointUrl() pulumi.StringOutput {
	return o.ApplyT(func(v *ConsulCluster) pulumi.StringOutput { return v.ConsulPrivateEndpointUrl }).(pulumi.StringOutput)
}

// The public URL for the Consul UI. This will be empty if `public_endpoint` is `false`.
func (o ConsulClusterOutput) ConsulPublicEndpointUrl() pulumi.StringOutput {
	return o.ApplyT(func(v *ConsulCluster) pulumi.StringOutput { return v.ConsulPublicEndpointUrl }).(pulumi.StringOutput)
}

// The accessor ID of the root ACL token that is generated upon cluster creation. If a new root token is generated using
// the `hcp_consul_root_token` resource, this field is no longer valid.
func (o ConsulClusterOutput) ConsulRootTokenAccessorId() pulumi.StringOutput {
	return o.ApplyT(func(v *ConsulCluster) pulumi.StringOutput { return v.ConsulRootTokenAccessorId }).(pulumi.StringOutput)
}

// The secret ID of the root ACL token that is generated upon cluster creation. If a new root token is generated using the
// `hcp_consul_root_token` resource, this field is no longer valid.
func (o ConsulClusterOutput) ConsulRootTokenSecretId() pulumi.StringOutput {
	return o.ApplyT(func(v *ConsulCluster) pulumi.StringOutput { return v.ConsulRootTokenSecretId }).(pulumi.StringOutput)
}

// The Consul snapshot interval.
func (o ConsulClusterOutput) ConsulSnapshotInterval() pulumi.StringOutput {
	return o.ApplyT(func(v *ConsulCluster) pulumi.StringOutput { return v.ConsulSnapshotInterval }).(pulumi.StringOutput)
}

// The retention policy for Consul snapshots.
func (o ConsulClusterOutput) ConsulSnapshotRetention() pulumi.StringOutput {
	return o.ApplyT(func(v *ConsulCluster) pulumi.StringOutput { return v.ConsulSnapshotRetention }).(pulumi.StringOutput)
}

// The Consul version of the cluster.
func (o ConsulClusterOutput) ConsulVersion() pulumi.StringOutput {
	return o.ApplyT(func(v *ConsulCluster) pulumi.StringOutput { return v.ConsulVersion }).(pulumi.StringOutput)
}

// The Consul data center name of the cluster. If not specified, it is defaulted to the value of `cluster_id`.
func (o ConsulClusterOutput) Datacenter() pulumi.StringOutput {
	return o.ApplyT(func(v *ConsulCluster) pulumi.StringOutput { return v.Datacenter }).(pulumi.StringOutput)
}

// The ID of the HVN this HCP Consul cluster is associated to.
func (o ConsulClusterOutput) HvnId() pulumi.StringOutput {
	return o.ApplyT(func(v *ConsulCluster) pulumi.StringOutput { return v.HvnId }).(pulumi.StringOutput)
}

// The minimum Consul version of the cluster. If not specified, it is defaulted to the version that is currently
// recommended by HCP.
func (o ConsulClusterOutput) MinConsulVersion() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *ConsulCluster) pulumi.StringPtrOutput { return v.MinConsulVersion }).(pulumi.StringPtrOutput)
}

// The ID of the organization this HCP Consul cluster is located in.
func (o ConsulClusterOutput) OrganizationId() pulumi.StringOutput {
	return o.ApplyT(func(v *ConsulCluster) pulumi.StringOutput { return v.OrganizationId }).(pulumi.StringOutput)
}

// The `self_link` of the HCP Consul cluster which is the primary in the federation setup with this HCP Consul cluster. If
// not specified, it is a standalone cluster.
func (o ConsulClusterOutput) PrimaryLink() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *ConsulCluster) pulumi.StringPtrOutput { return v.PrimaryLink }).(pulumi.StringPtrOutput)
}

// The ID of the project this HCP Consul cluster is located in.
func (o ConsulClusterOutput) ProjectId() pulumi.StringOutput {
	return o.ApplyT(func(v *ConsulCluster) pulumi.StringOutput { return v.ProjectId }).(pulumi.StringOutput)
}

// Denotes that the cluster has a public endpoint for the Consul UI. Defaults to false.
func (o ConsulClusterOutput) PublicEndpoint() pulumi.BoolPtrOutput {
	return o.ApplyT(func(v *ConsulCluster) pulumi.BoolPtrOutput { return v.PublicEndpoint }).(pulumi.BoolPtrOutput)
}

// The region where the HCP Consul cluster is located.
func (o ConsulClusterOutput) Region() pulumi.StringOutput {
	return o.ApplyT(func(v *ConsulCluster) pulumi.StringOutput { return v.Region }).(pulumi.StringOutput)
}

// The number of Consul server nodes in the cluster.
func (o ConsulClusterOutput) Scale() pulumi.IntOutput {
	return o.ApplyT(func(v *ConsulCluster) pulumi.IntOutput { return v.Scale }).(pulumi.IntOutput)
}

// A unique URL identifying the HCP Consul cluster.
func (o ConsulClusterOutput) SelfLink() pulumi.StringOutput {
	return o.ApplyT(func(v *ConsulCluster) pulumi.StringOutput { return v.SelfLink }).(pulumi.StringOutput)
}

// The t-shirt size representation of each server VM that this Consul cluster is provisioned with. Valid option for
// development tier - `x_small`. Valid options for other tiers - `small`, `medium`, `large`. For more details -
// https://cloud.hashicorp.com/pricing/consul. Upgrading the size of a cluster after creation is allowed.
func (o ConsulClusterOutput) Size() pulumi.StringOutput {
	return o.ApplyT(func(v *ConsulCluster) pulumi.StringOutput { return v.Size }).(pulumi.StringOutput)
}

// The tier that the HCP Consul cluster will be provisioned as. Only `development`, `standard` and `plus` are available at
// this time. See [pricing information](https://cloud.hashicorp.com/pricing/consul).
func (o ConsulClusterOutput) Tier() pulumi.StringOutput {
	return o.ApplyT(func(v *ConsulCluster) pulumi.StringOutput { return v.Tier }).(pulumi.StringOutput)
}

type ConsulClusterArrayOutput struct{ *pulumi.OutputState }

func (ConsulClusterArrayOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*[]*ConsulCluster)(nil)).Elem()
}

func (o ConsulClusterArrayOutput) ToConsulClusterArrayOutput() ConsulClusterArrayOutput {
	return o
}

func (o ConsulClusterArrayOutput) ToConsulClusterArrayOutputWithContext(ctx context.Context) ConsulClusterArrayOutput {
	return o
}

func (o ConsulClusterArrayOutput) Index(i pulumi.IntInput) ConsulClusterOutput {
	return pulumi.All(o, i).ApplyT(func(vs []interface{}) *ConsulCluster {
		return vs[0].([]*ConsulCluster)[vs[1].(int)]
	}).(ConsulClusterOutput)
}

type ConsulClusterMapOutput struct{ *pulumi.OutputState }

func (ConsulClusterMapOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*map[string]*ConsulCluster)(nil)).Elem()
}

func (o ConsulClusterMapOutput) ToConsulClusterMapOutput() ConsulClusterMapOutput {
	return o
}

func (o ConsulClusterMapOutput) ToConsulClusterMapOutputWithContext(ctx context.Context) ConsulClusterMapOutput {
	return o
}

func (o ConsulClusterMapOutput) MapIndex(k pulumi.StringInput) ConsulClusterOutput {
	return pulumi.All(o, k).ApplyT(func(vs []interface{}) *ConsulCluster {
		return vs[0].(map[string]*ConsulCluster)[vs[1].(string)]
	}).(ConsulClusterOutput)
}

func init() {
	pulumi.RegisterInputType(reflect.TypeOf((*ConsulClusterInput)(nil)).Elem(), &ConsulCluster{})
	pulumi.RegisterInputType(reflect.TypeOf((*ConsulClusterArrayInput)(nil)).Elem(), ConsulClusterArray{})
	pulumi.RegisterInputType(reflect.TypeOf((*ConsulClusterMapInput)(nil)).Elem(), ConsulClusterMap{})
	pulumi.RegisterOutputType(ConsulClusterOutput{})
	pulumi.RegisterOutputType(ConsulClusterArrayOutput{})
	pulumi.RegisterOutputType(ConsulClusterMapOutput{})
}
