// Code generated by the Pulumi Terraform Bridge (tfgen) Tool DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package hcp

import (
	"context"
	"reflect"

	"github.com/pkg/errors"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

// ## Import
//
// # The import ID is {cluster_id}
//
// ```sh
//  $ pulumi import hcp:index/vaultCluster:VaultCluster example vault-cluster
// ```
type VaultCluster struct {
	pulumi.CustomResourceState

	// The audit logs configuration for export.
	// (https://learn.hashicorp.com/tutorials/cloud/vault-metrics-guide#metrics-streaming-configuration)
	AuditLogConfig VaultClusterAuditLogConfigPtrOutput `pulumi:"auditLogConfig"`
	// The provider where the HCP Vault cluster is located.
	CloudProvider pulumi.StringOutput `pulumi:"cloudProvider"`
	// The ID of the HCP Vault cluster.
	ClusterId pulumi.StringOutput `pulumi:"clusterId"`
	// The time that the Vault cluster was created.
	CreatedAt pulumi.StringOutput `pulumi:"createdAt"`
	// The ID of the HVN this HCP Vault cluster is associated to.
	HvnId pulumi.StringOutput `pulumi:"hvnId"`
	// The metrics configuration for export.
	// (https://learn.hashicorp.com/tutorials/cloud/vault-metrics-guide#metrics-streaming-configuration)
	MetricsConfig VaultClusterMetricsConfigPtrOutput `pulumi:"metricsConfig"`
	// The minimum Vault version to use when creating the cluster. If not specified, it is defaulted to the version that is
	// currently recommended by HCP.
	MinVaultVersion pulumi.StringPtrOutput `pulumi:"minVaultVersion"`
	// The name of the customer namespace this HCP Vault cluster is located in.
	Namespace pulumi.StringOutput `pulumi:"namespace"`
	// The ID of the organization this HCP Vault cluster is located in.
	OrganizationId pulumi.StringOutput `pulumi:"organizationId"`
	// The performance replication [paths filter](https://learn.hashicorp.com/tutorials/vault/paths-filter). Applies to
	// performance replication secondaries only and operates in "deny" mode only.
	PathsFilters pulumi.StringArrayOutput `pulumi:"pathsFilters"`
	// The `self_link` of the HCP Vault Plus tier cluster which is the primary in the performance replication setup with this
	// HCP Vault Plus tier cluster. If not specified, it is a standalone Plus tier HCP Vault cluster.
	PrimaryLink pulumi.StringPtrOutput `pulumi:"primaryLink"`
	// The ID of the project this HCP Vault cluster is located in.
	ProjectId pulumi.StringOutput `pulumi:"projectId"`
	// Denotes that the cluster has a public endpoint. Defaults to false.
	PublicEndpoint pulumi.BoolPtrOutput `pulumi:"publicEndpoint"`
	// The region where the HCP Vault cluster is located.
	Region pulumi.StringOutput `pulumi:"region"`
	// A unique URL identifying the Vault cluster.
	SelfLink pulumi.StringOutput `pulumi:"selfLink"`
	// Tier of the HCP Vault cluster. Valid options for tiers - `dev`, `starter_small`, `standard_small`, `standard_medium`,
	// `standard_large`, `plus_small`, `plus_medium`, `plus_large`. See [pricing
	// information](https://cloud.hashicorp.com/pricing/vault).
	Tier pulumi.StringOutput `pulumi:"tier"`
	// The private URL for the Vault cluster.
	VaultPrivateEndpointUrl pulumi.StringOutput `pulumi:"vaultPrivateEndpointUrl"`
	// The public URL for the Vault cluster. This will be empty if `public_endpoint` is `false`.
	VaultPublicEndpointUrl pulumi.StringOutput `pulumi:"vaultPublicEndpointUrl"`
	// The Vault version of the cluster.
	VaultVersion pulumi.StringOutput `pulumi:"vaultVersion"`
}

// NewVaultCluster registers a new resource with the given unique name, arguments, and options.
func NewVaultCluster(ctx *pulumi.Context,
	name string, args *VaultClusterArgs, opts ...pulumi.ResourceOption) (*VaultCluster, error) {
	if args == nil {
		return nil, errors.New("missing one or more required arguments")
	}

	if args.ClusterId == nil {
		return nil, errors.New("invalid value for required argument 'ClusterId'")
	}
	if args.HvnId == nil {
		return nil, errors.New("invalid value for required argument 'HvnId'")
	}
	opts = pkgResourceDefaultOpts(opts)
	var resource VaultCluster
	err := ctx.RegisterResource("hcp:index/vaultCluster:VaultCluster", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetVaultCluster gets an existing VaultCluster resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetVaultCluster(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *VaultClusterState, opts ...pulumi.ResourceOption) (*VaultCluster, error) {
	var resource VaultCluster
	err := ctx.ReadResource("hcp:index/vaultCluster:VaultCluster", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering VaultCluster resources.
type vaultClusterState struct {
	// The audit logs configuration for export.
	// (https://learn.hashicorp.com/tutorials/cloud/vault-metrics-guide#metrics-streaming-configuration)
	AuditLogConfig *VaultClusterAuditLogConfig `pulumi:"auditLogConfig"`
	// The provider where the HCP Vault cluster is located.
	CloudProvider *string `pulumi:"cloudProvider"`
	// The ID of the HCP Vault cluster.
	ClusterId *string `pulumi:"clusterId"`
	// The time that the Vault cluster was created.
	CreatedAt *string `pulumi:"createdAt"`
	// The ID of the HVN this HCP Vault cluster is associated to.
	HvnId *string `pulumi:"hvnId"`
	// The metrics configuration for export.
	// (https://learn.hashicorp.com/tutorials/cloud/vault-metrics-guide#metrics-streaming-configuration)
	MetricsConfig *VaultClusterMetricsConfig `pulumi:"metricsConfig"`
	// The minimum Vault version to use when creating the cluster. If not specified, it is defaulted to the version that is
	// currently recommended by HCP.
	MinVaultVersion *string `pulumi:"minVaultVersion"`
	// The name of the customer namespace this HCP Vault cluster is located in.
	Namespace *string `pulumi:"namespace"`
	// The ID of the organization this HCP Vault cluster is located in.
	OrganizationId *string `pulumi:"organizationId"`
	// The performance replication [paths filter](https://learn.hashicorp.com/tutorials/vault/paths-filter). Applies to
	// performance replication secondaries only and operates in "deny" mode only.
	PathsFilters []string `pulumi:"pathsFilters"`
	// The `self_link` of the HCP Vault Plus tier cluster which is the primary in the performance replication setup with this
	// HCP Vault Plus tier cluster. If not specified, it is a standalone Plus tier HCP Vault cluster.
	PrimaryLink *string `pulumi:"primaryLink"`
	// The ID of the project this HCP Vault cluster is located in.
	ProjectId *string `pulumi:"projectId"`
	// Denotes that the cluster has a public endpoint. Defaults to false.
	PublicEndpoint *bool `pulumi:"publicEndpoint"`
	// The region where the HCP Vault cluster is located.
	Region *string `pulumi:"region"`
	// A unique URL identifying the Vault cluster.
	SelfLink *string `pulumi:"selfLink"`
	// Tier of the HCP Vault cluster. Valid options for tiers - `dev`, `starter_small`, `standard_small`, `standard_medium`,
	// `standard_large`, `plus_small`, `plus_medium`, `plus_large`. See [pricing
	// information](https://cloud.hashicorp.com/pricing/vault).
	Tier *string `pulumi:"tier"`
	// The private URL for the Vault cluster.
	VaultPrivateEndpointUrl *string `pulumi:"vaultPrivateEndpointUrl"`
	// The public URL for the Vault cluster. This will be empty if `public_endpoint` is `false`.
	VaultPublicEndpointUrl *string `pulumi:"vaultPublicEndpointUrl"`
	// The Vault version of the cluster.
	VaultVersion *string `pulumi:"vaultVersion"`
}

type VaultClusterState struct {
	// The audit logs configuration for export.
	// (https://learn.hashicorp.com/tutorials/cloud/vault-metrics-guide#metrics-streaming-configuration)
	AuditLogConfig VaultClusterAuditLogConfigPtrInput
	// The provider where the HCP Vault cluster is located.
	CloudProvider pulumi.StringPtrInput
	// The ID of the HCP Vault cluster.
	ClusterId pulumi.StringPtrInput
	// The time that the Vault cluster was created.
	CreatedAt pulumi.StringPtrInput
	// The ID of the HVN this HCP Vault cluster is associated to.
	HvnId pulumi.StringPtrInput
	// The metrics configuration for export.
	// (https://learn.hashicorp.com/tutorials/cloud/vault-metrics-guide#metrics-streaming-configuration)
	MetricsConfig VaultClusterMetricsConfigPtrInput
	// The minimum Vault version to use when creating the cluster. If not specified, it is defaulted to the version that is
	// currently recommended by HCP.
	MinVaultVersion pulumi.StringPtrInput
	// The name of the customer namespace this HCP Vault cluster is located in.
	Namespace pulumi.StringPtrInput
	// The ID of the organization this HCP Vault cluster is located in.
	OrganizationId pulumi.StringPtrInput
	// The performance replication [paths filter](https://learn.hashicorp.com/tutorials/vault/paths-filter). Applies to
	// performance replication secondaries only and operates in "deny" mode only.
	PathsFilters pulumi.StringArrayInput
	// The `self_link` of the HCP Vault Plus tier cluster which is the primary in the performance replication setup with this
	// HCP Vault Plus tier cluster. If not specified, it is a standalone Plus tier HCP Vault cluster.
	PrimaryLink pulumi.StringPtrInput
	// The ID of the project this HCP Vault cluster is located in.
	ProjectId pulumi.StringPtrInput
	// Denotes that the cluster has a public endpoint. Defaults to false.
	PublicEndpoint pulumi.BoolPtrInput
	// The region where the HCP Vault cluster is located.
	Region pulumi.StringPtrInput
	// A unique URL identifying the Vault cluster.
	SelfLink pulumi.StringPtrInput
	// Tier of the HCP Vault cluster. Valid options for tiers - `dev`, `starter_small`, `standard_small`, `standard_medium`,
	// `standard_large`, `plus_small`, `plus_medium`, `plus_large`. See [pricing
	// information](https://cloud.hashicorp.com/pricing/vault).
	Tier pulumi.StringPtrInput
	// The private URL for the Vault cluster.
	VaultPrivateEndpointUrl pulumi.StringPtrInput
	// The public URL for the Vault cluster. This will be empty if `public_endpoint` is `false`.
	VaultPublicEndpointUrl pulumi.StringPtrInput
	// The Vault version of the cluster.
	VaultVersion pulumi.StringPtrInput
}

func (VaultClusterState) ElementType() reflect.Type {
	return reflect.TypeOf((*vaultClusterState)(nil)).Elem()
}

type vaultClusterArgs struct {
	// The audit logs configuration for export.
	// (https://learn.hashicorp.com/tutorials/cloud/vault-metrics-guide#metrics-streaming-configuration)
	AuditLogConfig *VaultClusterAuditLogConfig `pulumi:"auditLogConfig"`
	// The ID of the HCP Vault cluster.
	ClusterId string `pulumi:"clusterId"`
	// The ID of the HVN this HCP Vault cluster is associated to.
	HvnId string `pulumi:"hvnId"`
	// The metrics configuration for export.
	// (https://learn.hashicorp.com/tutorials/cloud/vault-metrics-guide#metrics-streaming-configuration)
	MetricsConfig *VaultClusterMetricsConfig `pulumi:"metricsConfig"`
	// The minimum Vault version to use when creating the cluster. If not specified, it is defaulted to the version that is
	// currently recommended by HCP.
	MinVaultVersion *string `pulumi:"minVaultVersion"`
	// The performance replication [paths filter](https://learn.hashicorp.com/tutorials/vault/paths-filter). Applies to
	// performance replication secondaries only and operates in "deny" mode only.
	PathsFilters []string `pulumi:"pathsFilters"`
	// The `self_link` of the HCP Vault Plus tier cluster which is the primary in the performance replication setup with this
	// HCP Vault Plus tier cluster. If not specified, it is a standalone Plus tier HCP Vault cluster.
	PrimaryLink *string `pulumi:"primaryLink"`
	// Denotes that the cluster has a public endpoint. Defaults to false.
	PublicEndpoint *bool `pulumi:"publicEndpoint"`
	// Tier of the HCP Vault cluster. Valid options for tiers - `dev`, `starter_small`, `standard_small`, `standard_medium`,
	// `standard_large`, `plus_small`, `plus_medium`, `plus_large`. See [pricing
	// information](https://cloud.hashicorp.com/pricing/vault).
	Tier *string `pulumi:"tier"`
}

// The set of arguments for constructing a VaultCluster resource.
type VaultClusterArgs struct {
	// The audit logs configuration for export.
	// (https://learn.hashicorp.com/tutorials/cloud/vault-metrics-guide#metrics-streaming-configuration)
	AuditLogConfig VaultClusterAuditLogConfigPtrInput
	// The ID of the HCP Vault cluster.
	ClusterId pulumi.StringInput
	// The ID of the HVN this HCP Vault cluster is associated to.
	HvnId pulumi.StringInput
	// The metrics configuration for export.
	// (https://learn.hashicorp.com/tutorials/cloud/vault-metrics-guide#metrics-streaming-configuration)
	MetricsConfig VaultClusterMetricsConfigPtrInput
	// The minimum Vault version to use when creating the cluster. If not specified, it is defaulted to the version that is
	// currently recommended by HCP.
	MinVaultVersion pulumi.StringPtrInput
	// The performance replication [paths filter](https://learn.hashicorp.com/tutorials/vault/paths-filter). Applies to
	// performance replication secondaries only and operates in "deny" mode only.
	PathsFilters pulumi.StringArrayInput
	// The `self_link` of the HCP Vault Plus tier cluster which is the primary in the performance replication setup with this
	// HCP Vault Plus tier cluster. If not specified, it is a standalone Plus tier HCP Vault cluster.
	PrimaryLink pulumi.StringPtrInput
	// Denotes that the cluster has a public endpoint. Defaults to false.
	PublicEndpoint pulumi.BoolPtrInput
	// Tier of the HCP Vault cluster. Valid options for tiers - `dev`, `starter_small`, `standard_small`, `standard_medium`,
	// `standard_large`, `plus_small`, `plus_medium`, `plus_large`. See [pricing
	// information](https://cloud.hashicorp.com/pricing/vault).
	Tier pulumi.StringPtrInput
}

func (VaultClusterArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*vaultClusterArgs)(nil)).Elem()
}

type VaultClusterInput interface {
	pulumi.Input

	ToVaultClusterOutput() VaultClusterOutput
	ToVaultClusterOutputWithContext(ctx context.Context) VaultClusterOutput
}

func (*VaultCluster) ElementType() reflect.Type {
	return reflect.TypeOf((**VaultCluster)(nil)).Elem()
}

func (i *VaultCluster) ToVaultClusterOutput() VaultClusterOutput {
	return i.ToVaultClusterOutputWithContext(context.Background())
}

func (i *VaultCluster) ToVaultClusterOutputWithContext(ctx context.Context) VaultClusterOutput {
	return pulumi.ToOutputWithContext(ctx, i).(VaultClusterOutput)
}

// VaultClusterArrayInput is an input type that accepts VaultClusterArray and VaultClusterArrayOutput values.
// You can construct a concrete instance of `VaultClusterArrayInput` via:
//
//          VaultClusterArray{ VaultClusterArgs{...} }
type VaultClusterArrayInput interface {
	pulumi.Input

	ToVaultClusterArrayOutput() VaultClusterArrayOutput
	ToVaultClusterArrayOutputWithContext(context.Context) VaultClusterArrayOutput
}

type VaultClusterArray []VaultClusterInput

func (VaultClusterArray) ElementType() reflect.Type {
	return reflect.TypeOf((*[]*VaultCluster)(nil)).Elem()
}

func (i VaultClusterArray) ToVaultClusterArrayOutput() VaultClusterArrayOutput {
	return i.ToVaultClusterArrayOutputWithContext(context.Background())
}

func (i VaultClusterArray) ToVaultClusterArrayOutputWithContext(ctx context.Context) VaultClusterArrayOutput {
	return pulumi.ToOutputWithContext(ctx, i).(VaultClusterArrayOutput)
}

// VaultClusterMapInput is an input type that accepts VaultClusterMap and VaultClusterMapOutput values.
// You can construct a concrete instance of `VaultClusterMapInput` via:
//
//          VaultClusterMap{ "key": VaultClusterArgs{...} }
type VaultClusterMapInput interface {
	pulumi.Input

	ToVaultClusterMapOutput() VaultClusterMapOutput
	ToVaultClusterMapOutputWithContext(context.Context) VaultClusterMapOutput
}

type VaultClusterMap map[string]VaultClusterInput

func (VaultClusterMap) ElementType() reflect.Type {
	return reflect.TypeOf((*map[string]*VaultCluster)(nil)).Elem()
}

func (i VaultClusterMap) ToVaultClusterMapOutput() VaultClusterMapOutput {
	return i.ToVaultClusterMapOutputWithContext(context.Background())
}

func (i VaultClusterMap) ToVaultClusterMapOutputWithContext(ctx context.Context) VaultClusterMapOutput {
	return pulumi.ToOutputWithContext(ctx, i).(VaultClusterMapOutput)
}

type VaultClusterOutput struct{ *pulumi.OutputState }

func (VaultClusterOutput) ElementType() reflect.Type {
	return reflect.TypeOf((**VaultCluster)(nil)).Elem()
}

func (o VaultClusterOutput) ToVaultClusterOutput() VaultClusterOutput {
	return o
}

func (o VaultClusterOutput) ToVaultClusterOutputWithContext(ctx context.Context) VaultClusterOutput {
	return o
}

// The audit logs configuration for export.
// (https://learn.hashicorp.com/tutorials/cloud/vault-metrics-guide#metrics-streaming-configuration)
func (o VaultClusterOutput) AuditLogConfig() VaultClusterAuditLogConfigPtrOutput {
	return o.ApplyT(func(v *VaultCluster) VaultClusterAuditLogConfigPtrOutput { return v.AuditLogConfig }).(VaultClusterAuditLogConfigPtrOutput)
}

// The provider where the HCP Vault cluster is located.
func (o VaultClusterOutput) CloudProvider() pulumi.StringOutput {
	return o.ApplyT(func(v *VaultCluster) pulumi.StringOutput { return v.CloudProvider }).(pulumi.StringOutput)
}

// The ID of the HCP Vault cluster.
func (o VaultClusterOutput) ClusterId() pulumi.StringOutput {
	return o.ApplyT(func(v *VaultCluster) pulumi.StringOutput { return v.ClusterId }).(pulumi.StringOutput)
}

// The time that the Vault cluster was created.
func (o VaultClusterOutput) CreatedAt() pulumi.StringOutput {
	return o.ApplyT(func(v *VaultCluster) pulumi.StringOutput { return v.CreatedAt }).(pulumi.StringOutput)
}

// The ID of the HVN this HCP Vault cluster is associated to.
func (o VaultClusterOutput) HvnId() pulumi.StringOutput {
	return o.ApplyT(func(v *VaultCluster) pulumi.StringOutput { return v.HvnId }).(pulumi.StringOutput)
}

// The metrics configuration for export.
// (https://learn.hashicorp.com/tutorials/cloud/vault-metrics-guide#metrics-streaming-configuration)
func (o VaultClusterOutput) MetricsConfig() VaultClusterMetricsConfigPtrOutput {
	return o.ApplyT(func(v *VaultCluster) VaultClusterMetricsConfigPtrOutput { return v.MetricsConfig }).(VaultClusterMetricsConfigPtrOutput)
}

// The minimum Vault version to use when creating the cluster. If not specified, it is defaulted to the version that is
// currently recommended by HCP.
func (o VaultClusterOutput) MinVaultVersion() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *VaultCluster) pulumi.StringPtrOutput { return v.MinVaultVersion }).(pulumi.StringPtrOutput)
}

// The name of the customer namespace this HCP Vault cluster is located in.
func (o VaultClusterOutput) Namespace() pulumi.StringOutput {
	return o.ApplyT(func(v *VaultCluster) pulumi.StringOutput { return v.Namespace }).(pulumi.StringOutput)
}

// The ID of the organization this HCP Vault cluster is located in.
func (o VaultClusterOutput) OrganizationId() pulumi.StringOutput {
	return o.ApplyT(func(v *VaultCluster) pulumi.StringOutput { return v.OrganizationId }).(pulumi.StringOutput)
}

// The performance replication [paths filter](https://learn.hashicorp.com/tutorials/vault/paths-filter). Applies to
// performance replication secondaries only and operates in "deny" mode only.
func (o VaultClusterOutput) PathsFilters() pulumi.StringArrayOutput {
	return o.ApplyT(func(v *VaultCluster) pulumi.StringArrayOutput { return v.PathsFilters }).(pulumi.StringArrayOutput)
}

// The `self_link` of the HCP Vault Plus tier cluster which is the primary in the performance replication setup with this
// HCP Vault Plus tier cluster. If not specified, it is a standalone Plus tier HCP Vault cluster.
func (o VaultClusterOutput) PrimaryLink() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *VaultCluster) pulumi.StringPtrOutput { return v.PrimaryLink }).(pulumi.StringPtrOutput)
}

// The ID of the project this HCP Vault cluster is located in.
func (o VaultClusterOutput) ProjectId() pulumi.StringOutput {
	return o.ApplyT(func(v *VaultCluster) pulumi.StringOutput { return v.ProjectId }).(pulumi.StringOutput)
}

// Denotes that the cluster has a public endpoint. Defaults to false.
func (o VaultClusterOutput) PublicEndpoint() pulumi.BoolPtrOutput {
	return o.ApplyT(func(v *VaultCluster) pulumi.BoolPtrOutput { return v.PublicEndpoint }).(pulumi.BoolPtrOutput)
}

// The region where the HCP Vault cluster is located.
func (o VaultClusterOutput) Region() pulumi.StringOutput {
	return o.ApplyT(func(v *VaultCluster) pulumi.StringOutput { return v.Region }).(pulumi.StringOutput)
}

// A unique URL identifying the Vault cluster.
func (o VaultClusterOutput) SelfLink() pulumi.StringOutput {
	return o.ApplyT(func(v *VaultCluster) pulumi.StringOutput { return v.SelfLink }).(pulumi.StringOutput)
}

// Tier of the HCP Vault cluster. Valid options for tiers - `dev`, `starter_small`, `standard_small`, `standard_medium`,
// `standard_large`, `plus_small`, `plus_medium`, `plus_large`. See [pricing
// information](https://cloud.hashicorp.com/pricing/vault).
func (o VaultClusterOutput) Tier() pulumi.StringOutput {
	return o.ApplyT(func(v *VaultCluster) pulumi.StringOutput { return v.Tier }).(pulumi.StringOutput)
}

// The private URL for the Vault cluster.
func (o VaultClusterOutput) VaultPrivateEndpointUrl() pulumi.StringOutput {
	return o.ApplyT(func(v *VaultCluster) pulumi.StringOutput { return v.VaultPrivateEndpointUrl }).(pulumi.StringOutput)
}

// The public URL for the Vault cluster. This will be empty if `public_endpoint` is `false`.
func (o VaultClusterOutput) VaultPublicEndpointUrl() pulumi.StringOutput {
	return o.ApplyT(func(v *VaultCluster) pulumi.StringOutput { return v.VaultPublicEndpointUrl }).(pulumi.StringOutput)
}

// The Vault version of the cluster.
func (o VaultClusterOutput) VaultVersion() pulumi.StringOutput {
	return o.ApplyT(func(v *VaultCluster) pulumi.StringOutput { return v.VaultVersion }).(pulumi.StringOutput)
}

type VaultClusterArrayOutput struct{ *pulumi.OutputState }

func (VaultClusterArrayOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*[]*VaultCluster)(nil)).Elem()
}

func (o VaultClusterArrayOutput) ToVaultClusterArrayOutput() VaultClusterArrayOutput {
	return o
}

func (o VaultClusterArrayOutput) ToVaultClusterArrayOutputWithContext(ctx context.Context) VaultClusterArrayOutput {
	return o
}

func (o VaultClusterArrayOutput) Index(i pulumi.IntInput) VaultClusterOutput {
	return pulumi.All(o, i).ApplyT(func(vs []interface{}) *VaultCluster {
		return vs[0].([]*VaultCluster)[vs[1].(int)]
	}).(VaultClusterOutput)
}

type VaultClusterMapOutput struct{ *pulumi.OutputState }

func (VaultClusterMapOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*map[string]*VaultCluster)(nil)).Elem()
}

func (o VaultClusterMapOutput) ToVaultClusterMapOutput() VaultClusterMapOutput {
	return o
}

func (o VaultClusterMapOutput) ToVaultClusterMapOutputWithContext(ctx context.Context) VaultClusterMapOutput {
	return o
}

func (o VaultClusterMapOutput) MapIndex(k pulumi.StringInput) VaultClusterOutput {
	return pulumi.All(o, k).ApplyT(func(vs []interface{}) *VaultCluster {
		return vs[0].(map[string]*VaultCluster)[vs[1].(string)]
	}).(VaultClusterOutput)
}

func init() {
	pulumi.RegisterInputType(reflect.TypeOf((*VaultClusterInput)(nil)).Elem(), &VaultCluster{})
	pulumi.RegisterInputType(reflect.TypeOf((*VaultClusterArrayInput)(nil)).Elem(), VaultClusterArray{})
	pulumi.RegisterInputType(reflect.TypeOf((*VaultClusterMapInput)(nil)).Elem(), VaultClusterMap{})
	pulumi.RegisterOutputType(VaultClusterOutput{})
	pulumi.RegisterOutputType(VaultClusterArrayOutput{})
	pulumi.RegisterOutputType(VaultClusterMapOutput{})
}
