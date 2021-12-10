// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package config

import (
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi/config"
)

// The OAuth2 Client ID for API operations.
func GetClientId(ctx *pulumi.Context) string {
	v, err := config.Try(ctx, "hcp:clientId")
	if err == nil {
		return v
	}
	return getEnvOrDefault("", nil, "HCP_CLIENT_ID").(string)
}

// The OAuth2 Client Secret for API operations.
func GetClientSecret(ctx *pulumi.Context) string {
	v, err := config.Try(ctx, "hcp:clientSecret")
	if err == nil {
		return v
	}
	return getEnvOrDefault("", nil, "HCP_CLIENT_SECRET").(string)
}
