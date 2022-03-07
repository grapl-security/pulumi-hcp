// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "../utilities";

declare var exports: any;
const __config = new pulumi.Config("hcp");

/**
 * The OAuth2 Client ID for API operations.
 */
export declare const clientId: string | undefined;
Object.defineProperty(exports, "clientId", {
    get() {
        return __config.get("clientId") ?? utilities.getEnv("HCP_CLIENT_ID");
    },
    enumerable: true,
});

/**
 * The OAuth2 Client Secret for API operations.
 */
export declare const clientSecret: string | undefined;
Object.defineProperty(exports, "clientSecret", {
    get() {
        return __config.get("clientSecret") ?? utilities.getEnv("HCP_CLIENT_SECRET");
    },
    enumerable: true,
});

