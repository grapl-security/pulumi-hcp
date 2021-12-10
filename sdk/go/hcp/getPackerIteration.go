// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package hcp

import (
	"context"
	"reflect"

	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

// > **Note:** This feature is currently in beta.
//
// The Packer Image data source iteration gets the most recent iteration (or build) of an image, given a channel.
//
// ## Example Usage
//
// ```go
// package main
//
// import (
// 	"github.com/pulumi/pulumi-hcp/sdk/go/hcp"
// 	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
// )
//
// func main() {
// 	pulumi.Run(func(ctx *pulumi.Context) error {
// 		_, err := hcp.GetPackerIteration(ctx, &GetPackerIterationArgs{
// 			BucketName: "hardened-ubuntu-16-04",
// 			Channel:    "megan-test",
// 		}, nil)
// 		if err != nil {
// 			return err
// 		}
// 		return nil
// 	})
// }
// ```
func GetPackerIteration(ctx *pulumi.Context, args *GetPackerIterationArgs, opts ...pulumi.InvokeOption) (*GetPackerIterationResult, error) {
	var rv GetPackerIterationResult
	err := ctx.Invoke("hcp:index/getPackerIteration:getPackerIteration", args, &rv, opts...)
	if err != nil {
		return nil, err
	}
	return &rv, nil
}

// A collection of arguments for invoking getPackerIteration.
type GetPackerIterationArgs struct {
	// The slug of the HCP Packer Registry image bucket to pull from.
	BucketName string `pulumi:"bucketName"`
	// The channel that points to the version of the image you want.
	Channel string `pulumi:"channel"`
}

// A collection of values returned by getPackerIteration.
type GetPackerIterationResult struct {
	// The name of the person who created this iteration.
	AuthorId string `pulumi:"authorId"`
	// The slug of the HCP Packer Registry image bucket to pull from.
	BucketName string `pulumi:"bucketName"`
	// The channel that points to the version of the image you want.
	Channel string `pulumi:"channel"`
	// Creation time of this iteration
	CreatedAt string `pulumi:"createdAt"`
	// The unique fingerprint associated with this iteration; often a git sha.
	Fingerprint string `pulumi:"fingerprint"`
	// The provider-assigned unique ID for this managed resource.
	Id string `pulumi:"id"`
	// Incremental version of this iteration
	IncrementalVersion int `pulumi:"incrementalVersion"`
	// The ID of the organization this HCP Packer registry is located in.
	OrganizationId string `pulumi:"organizationId"`
	// The ID of the project this HCP Packer registry is located in.
	ProjectId string `pulumi:"projectId"`
	// The ULID of this iteration.
	Ulid string `pulumi:"ulid"`
	// Time this build was last updated.
	UpdatedAt string `pulumi:"updatedAt"`
}

func GetPackerIterationOutput(ctx *pulumi.Context, args GetPackerIterationOutputArgs, opts ...pulumi.InvokeOption) GetPackerIterationResultOutput {
	return pulumi.ToOutputWithContext(context.Background(), args).
		ApplyT(func(v interface{}) (GetPackerIterationResult, error) {
			args := v.(GetPackerIterationArgs)
			r, err := GetPackerIteration(ctx, &args, opts...)
			return *r, err
		}).(GetPackerIterationResultOutput)
}

// A collection of arguments for invoking getPackerIteration.
type GetPackerIterationOutputArgs struct {
	// The slug of the HCP Packer Registry image bucket to pull from.
	BucketName pulumi.StringInput `pulumi:"bucketName"`
	// The channel that points to the version of the image you want.
	Channel pulumi.StringInput `pulumi:"channel"`
}

func (GetPackerIterationOutputArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*GetPackerIterationArgs)(nil)).Elem()
}

// A collection of values returned by getPackerIteration.
type GetPackerIterationResultOutput struct{ *pulumi.OutputState }

func (GetPackerIterationResultOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*GetPackerIterationResult)(nil)).Elem()
}

func (o GetPackerIterationResultOutput) ToGetPackerIterationResultOutput() GetPackerIterationResultOutput {
	return o
}

func (o GetPackerIterationResultOutput) ToGetPackerIterationResultOutputWithContext(ctx context.Context) GetPackerIterationResultOutput {
	return o
}

// The name of the person who created this iteration.
func (o GetPackerIterationResultOutput) AuthorId() pulumi.StringOutput {
	return o.ApplyT(func(v GetPackerIterationResult) string { return v.AuthorId }).(pulumi.StringOutput)
}

// The slug of the HCP Packer Registry image bucket to pull from.
func (o GetPackerIterationResultOutput) BucketName() pulumi.StringOutput {
	return o.ApplyT(func(v GetPackerIterationResult) string { return v.BucketName }).(pulumi.StringOutput)
}

// The channel that points to the version of the image you want.
func (o GetPackerIterationResultOutput) Channel() pulumi.StringOutput {
	return o.ApplyT(func(v GetPackerIterationResult) string { return v.Channel }).(pulumi.StringOutput)
}

// Creation time of this iteration
func (o GetPackerIterationResultOutput) CreatedAt() pulumi.StringOutput {
	return o.ApplyT(func(v GetPackerIterationResult) string { return v.CreatedAt }).(pulumi.StringOutput)
}

// The unique fingerprint associated with this iteration; often a git sha.
func (o GetPackerIterationResultOutput) Fingerprint() pulumi.StringOutput {
	return o.ApplyT(func(v GetPackerIterationResult) string { return v.Fingerprint }).(pulumi.StringOutput)
}

// The provider-assigned unique ID for this managed resource.
func (o GetPackerIterationResultOutput) Id() pulumi.StringOutput {
	return o.ApplyT(func(v GetPackerIterationResult) string { return v.Id }).(pulumi.StringOutput)
}

// Incremental version of this iteration
func (o GetPackerIterationResultOutput) IncrementalVersion() pulumi.IntOutput {
	return o.ApplyT(func(v GetPackerIterationResult) int { return v.IncrementalVersion }).(pulumi.IntOutput)
}

// The ID of the organization this HCP Packer registry is located in.
func (o GetPackerIterationResultOutput) OrganizationId() pulumi.StringOutput {
	return o.ApplyT(func(v GetPackerIterationResult) string { return v.OrganizationId }).(pulumi.StringOutput)
}

// The ID of the project this HCP Packer registry is located in.
func (o GetPackerIterationResultOutput) ProjectId() pulumi.StringOutput {
	return o.ApplyT(func(v GetPackerIterationResult) string { return v.ProjectId }).(pulumi.StringOutput)
}

// The ULID of this iteration.
func (o GetPackerIterationResultOutput) Ulid() pulumi.StringOutput {
	return o.ApplyT(func(v GetPackerIterationResult) string { return v.Ulid }).(pulumi.StringOutput)
}

// Time this build was last updated.
func (o GetPackerIterationResultOutput) UpdatedAt() pulumi.StringOutput {
	return o.ApplyT(func(v GetPackerIterationResult) string { return v.UpdatedAt }).(pulumi.StringOutput)
}

func init() {
	pulumi.RegisterOutputType(GetPackerIterationResultOutput{})
}
