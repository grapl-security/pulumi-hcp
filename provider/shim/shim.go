package shim

import (
	"github.com/hashicorp/terraform-plugin-sdk/v2/helper/schema"
	"github.com/hashicorp/terraform-provider-hcp/internal/provider"
)

func NewProvider() *schema.Provider {
	return provider.New()()
}
